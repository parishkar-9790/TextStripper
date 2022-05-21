# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# i have created this file
# ...............................................................
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params2 = {'name': 'parishkar', 'place': 'home'}
    return render(request, 'index.html')
    # return HttpResponse("<h1> Parishkar Singh </h1>")


# function to remove puncs
def rrpunc(text):
    punc = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    for char in text:
        if char in punc:
            analyzed = analyzed + " "
        else:
            analyzed = analyzed + char
    return analyzed


# function to convert the text in all caps
def fcaps(text):
    analyzed = text.upper()
    return analyzed


def nwremover(text):
    analyzed = ""
    for char in text:
        if char != "\n" and char!="\r":
            analyzed = analyzed + char
    return analyzed


def extraspacer(text):
    analyzed = ""
    for index, char in enumerate(text):
        if not (text[index] == " " and text[index + 1] == " "):
            analyzed = analyzed + char
    return analyzed

# def about(request):
def analyze(request):
    analyzed = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc')
    fullcaps = request.POST.get('fullcaps')
    nwremove = request.POST.get('nwremove')
    extraspace = request.POST.get('extraspace')

    pur = "";
    if removepunc == "on":
        analyzed = rrpunc(analyzed)
        pur = pur + " removing puncuations"
    if (fullcaps == "on"):
        analyzed = fcaps(analyzed)
        pur = pur + ", Fullcaps "
    if (nwremove == "on"):
        analyzed = nwremover(analyzed)
        pur = pur + ",removing new line "
    if (extraspace == "on"):
        analyzed = extraspacer(analyzed)
        pur = pur + ", removing extraspaces"
    params = {'purpose': pur, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
# def navigator(request):
#     return HttpResponse('''<h1>Parishkar watches</h1> <a href="https://www.youtube.com/"  >Youtube</a>''')


# def one(request):
#     f = open("D:\\C++\\Django\\PycharmProjects\\TextUtils\\textutils\\textutils\\one.txt", "r")
#     return HttpResponse(f.read())
