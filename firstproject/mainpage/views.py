from django.views.generic.base import TemplateView
from django.shortcuts import render
import os
import openai
import json
import numpy as np
from summarizer import Summarizer
import sys
import urllib.request



class MainpageView(TemplateView):
    template_name = 'mainpage/main.html'
 
 #동화 텍스트 정제하기   
def filtering(x):
    x=x.replace("\n","")
    x=x.replace('.', '.\n')
    x=x.replace('.\n\"',".\"\n")
    x=x.replace(".\n\'",".\'\n")
    x=x.replace("\'\'","")
    x=x.replace("\r","")
    x=x.split('\n')
    return x

#문장 리스트로 바뀐 텍스트를 n개로 나누기
def list_split(lst,page_num):
    return [lst[i:i+page_num] for i in range(0,len(lst),page_num)]

#리스트로 된 문장들을 하나의 string으로 합치기
def listToString(list_split):
    result = ""
    for s in list_split:
        result += s + " "
    return result.strip()

#커스텀동화메뉴 입력 페이지
def custom(request):
    return render(request,"custom.html")

def name_remove(x):
    x= x.replace('[','')
    x= x.replace(']','')
    x= x.replace('\'','')
    return x

#커스텀동화 만드는 함수    
def bookillu_custom(request):
    title=request.GET.get('custom_title')
    text=request.GET.get('custom_text')
    lst=filtering(text)
    page_num = len(lst) //7
    split = list_split(lst,page_num)
    model = Summarizer()
    image_url=[]
    for i in range(0,7):
        result = listToString(split[i])    
        sen = model(result, num_sentences=1)  #1문장으로 요약
        print(sen)
        #papago api - 요약문 번역
        client_id = "****"
        client_secret = "****"
        encText = urllib.parse.quote(sen)
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        re_request = urllib.request.Request(url)
        re_request.add_header("X-Naver-Client-Id",client_id)
        re_request.add_header("X-Naver-Client-Secret",client_secret)
        res = urllib.request.urlopen(re_request, data=data.encode("utf-8"))
        rescode = res.getcode()
        if(rescode==200):
            response_body = res.read()
            sen=json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
            print(sen)
            #dalle api - 요약문으로 그림 생성
            sen = sen + "Korean, fairy tale illustration, watercolor, pre-historical, Ancient East Asia, light, peaceful, blurr, disney folk tale"
            #sen = sen + "fairy tale, for children, fantasy, quite, adorable, watercolor, light, peaceful, soothing, cosy, tender, pencil drawing, blurr, fairy tale illustration, disney"
            openai.api_key = "****"
            res = openai.Image.create(prompt=sen,n=1,size='256x256')
            image_url_str = res['data'][0]['url']
            print(image_url_str)
            image_url.append(image_url_str)
        else:
            print("Error Code:" + rescode)
            
    split1=name_remove(str(split[0]))
    split2=name_remove(str(split[1]))
    split3=name_remove(str(split[2]))
    split4=name_remove(str(split[3]))
    split5=name_remove(str(split[4]))
    split6=name_remove(str(split[5]))
    split7=name_remove(str(split[6]))
    print("###############")
    print(image_url)
    print("###############")
    print(type(image_url),len(image_url))
            
    img1=image_url[0]
    img2=image_url[1]
    img3=image_url[2]
    img4=image_url[3]
    img5=image_url[4]
    img6=image_url[5]
    img7=image_url[6]

                
    dt={'split1':split1,
        'split2':split2,
        'split3':split3,
        'split4':split4,
        'split5':split5,
        'split6':split6,
        'split7':split7,

        'img1':img1,
        'img2':img2,
        'img3':img3,
        'img4':img4,
        'img5':img5,
        'img6':img6,
        'img7':img7,
        
        'title':title
        
        }
    

    return render(request,"custompage.html", dt)
        
    

                
        

    
