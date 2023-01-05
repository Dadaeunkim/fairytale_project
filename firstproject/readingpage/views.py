from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.db import connection
import os
import openai
import json
import numpy as np
from summarizer import Summarizer

import sys
import urllib.request
# Create your views here.


#전래동화용 함수
def bookillu_ko(body):
    #문장 요약
    model = Summarizer()
    sen=model(body,1)
    #요약된 문장 번역
    client_id = "****"
    client_secret = "****"
    encText = urllib.parse.quote(sen)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        sen=json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
        #번역된 문장으로 그림 생성
        sen = sen + "Korean, fairy tale illustration, watercolor, pre-historical, Ancient East Asia, light, peaceful, blurr, disney folk tale"
        openai.api_key = "****"
        response = openai.Image.create(prompt=sen,n=1,size='256x256')
        image_url = response['data'][0]['url']
    else:
        print("Error Code:" + rescode)
    return image_url

#외국동화용 함수
def bookillu_for(body):
    #문장 요약
    model = Summarizer() 
    sen=model(body,1)
    #요약문장 번역
    client_id = "****"
    client_secret = "****"
    encText = urllib.parse.quote(sen)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        sen=json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
        #번역된 문장으로 그림 생성
        sen = sen + "fairy tale, watercolor, for children, pencil drawing, fantasy, quite, adorable, light, peaceful, soothing, cosy, tender, blurr, fairy tale illustration, disney"
        openai.api_key = "****"
        response = openai.Image.create(prompt=sen,n=1,size='256x256')
        image_url = response['data'][0]['url']
    else:
        print("Error Code:" + rescode)
    return image_url

class PostList(ListView):
    model=Post
    template_name='readinglist.html'
        
def list_show_0(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=1"
    result = cursor.execute(query)
    datas = cursor.fetchall()
    connection.commit()
    connection.close()
    
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_ko(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    dt={'datas':datas}
    adt={'dt':dt,'books':books}
    

    return render(request,"0.html", adt)

def list_show_1(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=2"
    result = cursor.execute(query)
    datas = cursor.fetchall()
    connection.commit()
    connection.close()
    
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_ko(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    dt={'datas':datas}
    adt={'dt':dt,'books':books}
    

    return render(request,"1.html", adt)
            
def list_show_2(request):

    cursor = connection.cursor()
    query = "select * from readingpage_post where id=3"
    result = cursor.execute(query)
    datas = cursor.fetchall()
    connection.commit()
    connection.close()
    
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_ko(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    dt={'datas':datas}
    adt={'dt':dt,'books':books}
    
    return render(request,"2.html",adt)    

def list_show_3(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=4"
    result = cursor.execute(query)
    datas = cursor.fetchall()
    connection.commit()
    connection.close()
    
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_ko(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    dt={'datas':datas}
    adt={'dt':dt,'books':books}
    

    return render(request,"3.html", adt) 

def list_show_4(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=5"
    result = cursor.execute(query)
    datas = cursor.fetchall()
    connection.commit()
    connection.close()
    
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_ko(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    dt={'datas':datas}
    adt={'dt':dt,'books':books}
    
    return render(request,"4.html",adt)    

def list_show_5(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=6"
    result = cursor.execute(query)
    datas = cursor.fetchall()

    connection.commit()
    connection.close()
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_ko(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    
    dt={'datas':datas}
    adt={'dt':dt}
    return render(request,"5.html",adt)    

def list_show_6(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=7"
    result = cursor.execute(query)
    datas = cursor.fetchall()

    connection.commit()
    connection.close()
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_for(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    
    dt={'datas':datas}
    adt={'dt':dt}
    return render(request,"6.html",adt)    
    
def list_show_7(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=8"
    result = cursor.execute(query)
    datas = cursor.fetchall()
    connection.commit()
    connection.close()
    
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_for(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    dt={'datas':datas}
    adt={'dt':dt,'books':books}
    return render(request,"7.html",adt)    

def list_show_8(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=9"
    result = cursor.execute(query)
    datas = cursor.fetchall()
    connection.commit()
    connection.close()
    
    books = []
    
    for data in datas:
        for i in range(2,9):
            con=bookillu_for(data[i])
            books.append(con)                 
    print(books)
    print("###############################################")
    dt={'datas':datas}
    adt={'dt':dt,'books':books}
    
    return render(request,"8.html",adt)    
            
def list_show_9(request):
    
    cursor = connection.cursor()
    query = "select * from readingpage_post where id=10"
    result = cursor.execute(query)
    stocks = cursor.fetchall()

    connection.commit()
    connection.close()
    
    dt={'stocks':stocks}
    adt={'dt':dt}
    
    return render(request,"9.html",adt)    
    


