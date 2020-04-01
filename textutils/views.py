 # i have created this website 
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def RemovePuch(text):
    ans = ''
    punctutations = '''(){}[]-_!"'.,/@#$%^&*'''

    for char in text:
        if char in punctutations:
            continue
        ans = ans + char
    return ans

def Charcount(text):
    dict = {}
    for i in range(len(text)):
        if text[i] in dict:
            dict[text[i]] = dict[text[i]] + 1
        else:
            dict[text[i]] = 1
    return dict

def NewlineRemover(text):
    ans = ''
    for char in text:
        if char == '\n' or char=='\r':
            continue
        ans = ans + char
    return ans

def ExtraspaceRemover(text):
    ans = ''
    for index,char in enumerate(text):
        if text[index] == " " and text[index+1] == " ":
            continue
        ans = ans + char
    return ans

def MakeupperCase(text):
    ans = ''
    for char in text:
        ans = ans + char.upper()
    return ans

def analyze(request):
    #first we need to get the text.
    data = request.POST.get('text','')
    removePuch = request.POST.get('removePuch','off')
    newlineRemover = request.POST.get('newlineRemover','off')
    extraspaceRemover = request.POST.get('extraspaceRemover','off')
    makeupperCase = request.POST.get('makeupperCase','off')

    #if data=='':
        #return HttpResponse("<h1 style:' color=red;'>Please enter some text!</h1>")

    Responses = [removePuch,makeupperCase,newlineRemover,extraspaceRemover]
    
    if Responses[0] == 'on':
        data = RemovePuch(data)
    if Responses[1] == 'on':
        data = MakeupperCase(data)
    if Responses[2] == 'on':
        data = NewlineRemover(data)
    if Responses[3] == 'on':
        data = ExtraspaceRemover(data)
    
    dict = Charcount(data)
    # basically there are four function. I want to work all of them independently.
    #removePuch                   
    #charcount
    #newlineRemover
    #extraspaceRemover
    if 'on' not in Responses:
        return HttpResponse("<h1>Please select a valid option</h1>")
    params = {'ans':data , 'dict':dict}
    return render(request,'analyze.html',params)

def about(request):
    return render(request,'about.html')