from django.shortcuts import render,redirect

from .models import blog

def blog(request):
    try:
        data = blog.objects.all()
    except:
        data = ""
    context = {
        'data':data
    }
    return render(request,'blog.html',context=context)

def writeblog(request):
    if request.method =='POST':
        usr = request.user
        data = blog()
        data.by = usr
        data.title = request.POST.get('title')
        data.body = request.POST.get('content')
        data.save()
        return redirect('blog')
