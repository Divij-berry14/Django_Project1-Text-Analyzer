from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse("Hello World! This is Home Page!")

def index(request):
    return render(request, 'index.html')
#    file=open("1.txt",'r+')
#    return HttpResponse(file.read())

def navigation(request):
    s="<h1> Navigator Page! <br> </h1> <a href='https://www.linkedin.com/feed/'> Linkdlen </a> <br> <a href='https://docs.djangoproject.com/en/3.0/'> Django Documentation </a>"
    return HttpResponse(s)

def home(request):
    s="<button type='button'> <a href = 'http://127.0.0.1:8000/removepunc/'>Remove Punctuation</a></button> <br> " \
      "<button type='button'> <a href = 'http://127.0.0.1:8000/capitF/'>Capital First</a></button>"
    return HttpResponse(s)

def analyze(request):
    # print(request.GET.get('text','off'))
    djtext=request.POST.get('text', 'default')
    removepunc_check=request.POST.get('removepunc_check','off')
    upper_tick=request.POST.get('upper_tick','off')
    remove_new_line=request.POST.get('remove_new_line','off')
    remove_extra_space=request.POST.get('remove_extra_space')
    char_count=request.POST.get('char_count','off')

    # data={'rp':removepunc,'up':upper_tick,'rnl':remove_new_line,'res':remove_extra_space,'chc':char_count}

    if removepunc_check=='on' and upper_tick=='on' and remove_extra_space=='on' and remove_new_line=='on':
        analyzed = ''
        for char in djtext:
            if char != "\n" and char!='\r':
                analyzed = analyzed + char
        analyzed1=''
        for index,char in enumerate(analyzed):
            if analyzed[index]==' ' and  analyzed[index+1]==' ':
                pass
            else:
                analyzed1=analyzed1+char
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in analyzed1:
            if char not in punctuations:
                analyzed=analyzed+char
        analyzed=analyzed.upper()
        param={'purpose':'Mutiple Checkboxes','analyzed_text':analyzed}
        return render(request,'analyze.html',param)
    #Remove Punctuation
    if removepunc_check =='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        param={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',param)

    #To check UPPER case
    if upper_tick=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        param={'purpose':'To Upper Case','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',param)

    #To Remove New Line
    if remove_new_line=='on':
        analyzed=''
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed=analyzed+char
        param={'purpose':'Removes New Line','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',param)

    # Remove Extra space
    if remove_extra_space=='on':
        analyzed=''
        for i,char in enumerate(djtext):
            if djtext[i]==' ' and djtext[i+1]==' ':
                pass
            else:
                analyzed=analyzed+char
        param={'purpose':'Remove Extra Space','analyzed_text':analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',param)

    # if char_count=='on':
    #     analyzed=len(djtext)
    #     param={'purpose':'Number of characters','analyzed_text':analyzed}
    #     djtext = analyzed
        # return render(request,'analyze.html',param)
    if remove_new_line!='on' and remove_extra_space!='on' and removepunc_check!='on' and upper_tick!='on':
        return HttpResponse("Please select any checkbox and Try Again!")
    else:
        return render(request, 'analyze.html', param)


    # print(djtext)
    # print(removepunc)
    # return HttpResponse("Remove Punctuation")

def capfirst(request):
    return HttpResponse('''<h1>Capitalize First</h1><br>
                            <button type="button"><a href = "http://127.0.0.1:8000/removepunc">Go Back</a></button>''')

