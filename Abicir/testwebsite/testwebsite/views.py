
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("""<h1></h1> <a href="https://www.youtube.com/shorts/7eByQfpu4P8"> Study content </a> """)

def about(request):
    return HttpResponse("<h1> About this class</h1> ")

def index(request):
    pars = {'name': 'Abicir' , 'place': 'Earth' } 
    return render(request, 'index.html', pars)

def Analyze(request):
    djangotext=request.POST.get('text', 'default')
    removingpunc=request.POST.get('removingpunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    exspaceremover=request.POST.get('exspaceremover', 'off')``
    
   
    if (removingpunc =="on"):
        analyzed=djangotext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djangotext:
            if char not in punctuations:
                analyzed=analyzed+char
            

        params={'purpose':' Removed the Punctuations', 'analyzed_text':analyzed}
        return render( request,'analyze.html',params)
    
    if(fullcaps=="on"):
        analyzed=djangotext.upper()
        for char in djangotext:
            analyzed=analyzed+char.upper()
        params={'purpose':' Changed to Uppercase', 'analyzed_text':analyzed}
        return render( request,'analyze.html',params)


    if(newlineremover=="on"):
        analyzed=""
        for char in djangotext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':' Removed New Lines', 'analyzed_text':analyzed}
        return render( request,'analyze.html',params)

    if(exspaceremover=="on"):
        analyzed=djangotext
        for index, char in enumerate(djangotext):
            if not(djangotext[index]==" " and djangotext[index+1]==" "):
                analyzed=analyzed+char
        params={'purpose':' Removed Extra Spaces', 'analyzed_text':analyzed}

        return render( request,'analyze.html',params)
    




    else:
        return HttpResponse("Error")
    
def removingpunc(request):
    return HttpResponse("Removing the punctuations.")

def capitalizingfirst(request):
    return HttpResponse(" Capitalizing First Letter ")

def newlineremover(request):
    return HttpResponse(" Removing New Lines")

def thespaceremover(request):
    return HttpResponse(" Removing the Spaces <a href='/'>back</a>")

def charactercount(request):
    return HttpResponse(" Character Count ")
