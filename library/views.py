from django.shortcuts import render,HttpResponse

def index(request):
    context = [
        {'title':'harry potter'},
        {'title': 'learn python'},
        {'title': 'learn Django'},
    ]


        
    return render(request, 'library/index.html', {'context':context})
