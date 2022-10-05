
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import chicken
from .forms import testForm

# Create your views here.

def index(request):
    k = chicken.objects.all().order_by('title')

    context={
        'chickens' : k
    }

    
    return render (request,'testapp/index.html',context)



def create(request):
    # if request.method=='GET':
    #     rt = request.GET
    #     context= {
    #         'rt' : rt
    #     }
    #     return render (request,'testapp/create.html',context)
    # else :
        
    #     title = request.POST.get("title")
    #     content = request.POST.get("content")
    #     chicken.objects.create(title=title,content=content)
    #     return render(request,'testapp/create.html')
    if request.method=='POST':
        form= testForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("testapp:index")
    else:
        form =testForm()
        context ={
            'form' : form,
        }
        return render(request,'testapp/create.html',context)

def detail(request,pk):
    pick = chicken.objects.get(pk=pk)
    context={
        'pick': pick
    }
    

    return render (request,'testapp/detail.html',context)

def delete (request,pk):
    pick = chicken.objects.get(pk=pk).delete()
    

    return redirect ('testapp:index')


def update (request,pk):
    rb= chicken.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        form = testForm(request.POST, instance=rb)
        if form.is_valid():
            #유효성 검사 후 통과가 된다면 ,저장 후 인덱스로 리다이렉트
            form.save()
            return redirect('testapp:detail',rb.pk)
    else:
        form = testForm(instance=rb)

    context ={'form':form,
    'rb':rb}

    return render (request,'testapp/update.html',context)



    # if request.method=='GET':
    #     rb= chicken.objects.get(pk=pk)
    #     context={
    #         'rb':rb
    #     }
    #     return render (request,'testapp/update.html',context)

    # else:
    #     ra = chicken.objects.get(pk=pk)
    #     title = request.POST.get('title')
    #     content= request.POST.get('content')
    #     ra.title=title
    #     ra.content=content
    #     ra.save()
    #     return redirect('/')

