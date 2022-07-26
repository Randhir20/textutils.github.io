#i have created this file-Randhir
from site import removeduppaths
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext  = request.POST.get('text','default')
    print(djtext)
    
    #checkbox--
    removepunc= request.POST.get('removepunc','off') 
    fullcaps= request.POST.get('fullcaps','off') 
    newlineremover= request.POST.get('newlineremover','off') 
    extraspaceremover= request.POST.get('extraspaceremover','off') 
    charcount= request.POST.get('charcount','off') 
    
  
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
        djtext=analyzed
 
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose':'Changed to Uppercase','analyzed_text': analyzed}
        djtext=analyzed
        
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char  
        params = {'purpose':'Remove New line','analyzed_text': analyzed}
        djtext=analyzed
       
    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
                
        params = {'purpose':'Remove Extra line','analyzed_text': analyzed}
        djtext=analyzed
     
    if(charcount=="on"):
        analyzed=('No. of characters given in the text are : '+str(len(djtext)))
        params = {'purpose':'Character Count','analyzed_text': analyzed}
        djtext=analyzed

    if(removepunc != 'on' and fullcaps != "on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on"):
        return HttpResponse("Please select any operation and try again")
        
    
    return render(request, 'analyze.html', params)       
     
 




