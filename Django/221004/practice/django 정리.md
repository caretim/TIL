## 목차

1. 가상환경 생성
2.  프로젝트와 앱생성 
3. 앱 등록과 서버 실행
4. urls와 views, templates
5. 데이터베이스와 Model 설정
6. CRUD (Create,Read,Update,Delete)
7. GET과 POST
8. ModelForm

## 1. 가상환경 생성

각각의 프로젝트는 프로젝트에 따라 사용되는 패키지와 버전이 다르기에 가상환경을 생성하여 

 필요한 패키지로만 구성을 하여 사용 할 수 있다.

```bash
##가상환경 설치

$python --version ## 파이썬이 설치되어있는지 확인한다. 

$python -m venv {가상환경이 설치될 폴더명}

$source{가상환경이 설치된 폴더명}/Scripts/Activate ## 가상환경 설치폴더의 실행파일을 실행시켜 가상환경 실행 

$deactivate #가상환경 종료

$pip list ## 환경에 설치된 패키지목록 확인
$pip install {패키지와 버전} ## 패키지를 인스톨받는다.
$pip install -r requirements.txt ## 기록된 패키지를 한번에 일괄 인스톨한다.
$pip freeze > requirements.txt  ## 저장된 패키지를  requirements.txt에 저장하여 패키지관리를 용이하게한다.
$pip install django==3.3.12  LTS버전(TS(Long Term Support)는 말 그대로 장기 지원되는 버전)

```

## 2.프로젝트와 앱 생성

프로젝트 생성 시에는 되도록 파이썬이나 장고에서 사용하는 키워드는 피해서 만들 것을 권장한다.

‘-’ 하이픈 사용할 수 없음

```bash
django-admin startproject {프로젝트명} {시작경로}   #보통은 프로젝트 명 뒤에 띄어쓰기 .(닷)을 찍는 이유는 현재 폴더를 위치로 지정
# 설치가 되었다면 프로젝트 폴더와 manage.py가 생성됨

python manage.py startapp {앱이름}   # 프로젝트 설치 후 manage.py가 존재해야함
# 설치시 앱이름의 폴더가 생성됨
```

**프로젝트 폴더의 구성 파일**

- __init__.py
    - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시하는 역할을 수행합니다.
- asgi.py
    - Asynchronous Server Gateway Interface의 약자
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 돕습니다.
- [settings.py](http://settings.py) *** 자주 사용**
    - 애플리케이션의 모든 설정을 포함하고 있습니다.
- urls  ***자주 사용**
    - 사이트의 url과 적절한 views의 연결을 지정합니다.
- wsgi.py
    - Web Server Gatewy Interface
    - django 애플리케이션이 웹서봐 연결 및 소통하는 것을 돕습니다.

**앱 폴더의 구성 파일** 

- admin.py
    - 관리자용 페이지를 설정 하는 곳입니다.
- apps.py
    - 앱의 정보가 작성된 곳입니다.
- models.py
    - 앱에서 사용하는 Modle(db)을 정의하는 곳입니다.
- tests.py
    - 프로젝트의 테스트 코드를 작성하는 곳입니다.
- views.py
    - view 함수들이 정의 되는 곳입니다.
    
    ### 프로젝트와 앱의 역활과 관계
    
    ### 3. Project & Application
    
    > Project
    > 
    > - Project(이하 프로젝트)는 Application(이하 앱)의 집합
    > - 프로젝트는 여러 앱이 포함될 수 있음
    > - 앱은 여러 프로젝트에 있을 수 있음
    > 
    > ### Application
    > 
    > - 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할을 담당
    > - 하나의 프로젝트는 여러 앱을 가짐
    > - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함
    > 

## 3. 서버실행과 앱등록

**서버 실행**

```bash
$python manage.py runserver # 서버를 실행시킨 후 localhost 주소로 접속하여 실행이 되었는지 확인한다.

# 정상적으로 서버가 실행되었다면, 로컬주소페이지에서 로켓확인
```

**앱 등록 절차** 

프로젝트에서 앱을 사용하기 위해서는 반드시  setting.py 에서 INSTALLED_APPS 리스트에 앱을 추가해야한다.

`INSTALLED_APPS`는 django installation에 활성화된 모든 앱을 지정하는 문자열 목록

`INSTALLED_APPS` 에 앱을 추가해준다. {’앱이름’}, 

## 4. urls와 views, templates

urls.py → 주문서

[views.py](http://views.py) → 로직구현 

templates(HTML → HTML페이지 구성

주소(누구에게) → https://search.naver.com

주문서(무엇을) → /search.naver?query=아이유

https://search.naver.com/search.naver?

form의 action에 정의한 내용을 주문서로 받고 

query=  아이유

주문받은 내용을 views.py에서 처리한 후 html로 되돌려준다.

### (1)urls

view 메소드를 연결하고 요청 url을 정의하는 파일

```bash
from django.urls import path
from . import views   ##  from . 현재폴더를 참조

app_name = "pair"

# 다른앱의 urls를 참조하기 위해서는 앱네임을 지정해줘야한다.

urlpatterns = [
    path('', views.index, name="index"),
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result")
		path('update/<int:pk>', views.update, name='update'),
# <int:pk>는 파라미터값 views.uadate는 views를 참조하여 데이터를 처리할 곳 , name은 구분을 위한 변수지정

```

### (2)views

데이터를 처리하는 로직인 view 메소드를 정의하는 파일

```bash
from django.shortcuts import render ,redirect  

 # 요청 정보를 받아서 페이지를 render
def index(request): 
    return HttpResponse("Hello world")

def select(request):
    message = "수 하나를 입력해주세요."
    return HttpResponse(message)

def result(request):
    message = "추첨 결과입니다."
    return HttpResponse(message)

```

### (3)templates

•template의 loder로 템플릿 파일을 로드하고, 해당 템플릿에 전달할 데이터를 설정하여 render에 인자로 넘길 수 있다.

HTML로 구성되며 FORM을 통해 전달할 데이터를 설정하여 render에 인자로 보낼 수 있다.

## 5. 데이터베이스와 MODEL

데이터베이스의 들어갈 데이터를 가공하는 법

데이버베이스에 들어갈 내용을 form통해 받고 저장하기 위해서는 

MODELS.py에서 필드를 지정해 줘야 한다.

```bash
test/models.py # 폴더명

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

앱에서 사용되는 데이터를 가공하기 위해선 models.py에서 클래스를 선언한 후 어떤 데이터값으로 가져올지 지정할 수 있다.

데이터를 어떻게 받아올지 정했다면, 

python [manage.py](http://manage.py)  makemigration - > 마이그레이션을 실행함으로써 모델의 변경사항을 django에게 알려준다.

python [manage.py](http://manage.py) migrate  → 마이그레이션을 통해 지정된 모델들을 저장시켜준다.

## 6.CRUD ( Create , Read , Update , Delete)

views에 함수 정의를 통해 저장되는 데이터들을 가공하여 CRUD로 처리한다.

CRUD를 하기 위해서는 미리 MODEL이 되어있어야함

`[**views.py](http://views.py)` 에서 데이터베이스를 참조하기 위해 선행** 

```bash
from django.shortcuts import render, redirect
from .models import tests <- 이부분 from {모델의 위치}model imorts {참조할 데이터 테이블}

```

### (1) Create

HTML의 FORM을 통해 데이터를 전달 받고 받은 데이터를 데이터베이스에 넣어준다.

```bash
def send(request): # FORM을 통해 받은 데이터들을 각각의 변수에 지정해준다.
    title = request.GET.get("title")
    content = request.GET.get("content")
    created_at = request.GET.get("created_at")
    update_ad = request.GET.get("update_ad")

    Review.objects.create(  # 지정된 데이터들을 {model변수}.objects.create()를 통해 데이터베이스에 생성
        title=title,
        content=content,
        created_at=created_at,
        update_ad=update_ad,
    )
	return redirect("pair:index")
```

### (2) Read

데이터베이스에 저장된 데이터를 pk값을 통해 불러온다

```bash

def detail(request, pk):   #pk값을 통해 데이터를 불러온다 pk값은 url파라미터로 가져온다
    pk = Review.objects.get(id=pk)

	  context = {"id": pk} #데이터를 내보내기위해 딕셔너리형식으로 지정해준다.

    return render(request, "detail.html", context) # 렌더의 세번째 인자에 딕셔너리 변수를 넣어 정보를 보낸다.
```

### (3) Update

데이터베이스에 저장된 데이터를 pk값을 통해 가져온 뒤 수정한 후 수정한 내용을 저장한다.

```bash
def update(request, pk):  # pk값으로 수정할 데이터의 url파라미터를 가져온다.
    pk = Review.objects.get(id=pk)

    title = request.GET.get("title")   # 변경할 내용들을 변수에 지정
    content = request.GET.get("content")

    pk.title = title                    #변경된 내용 변수들을 데이터베이스의 값에 넣는다.
    pk.content = content

    pk.save()                           #변경된 데이터베이스를 저장해준다.

    return redirect("pair:detail", pk.pk)
```

### (4) Delete

데이터베이스에 저장된 데이터를 pk값으로 불러온 후 지운다.

```bash
def delete(request, pk):
    pk = Review.objects.get(id=pk)
    pk.delete()    

    return redirect("pair:index")

```

## 7. GET과 POST

GET과 POST의 공통점은 **서버에 Request 요청을 하는 메소드**

GET이 POST의 차이점은 **클라이언트의 요청이 URL 뒤에 추가되어서 요청되는 점**

### (1) GET

1. GET 방식의 특징으로는 SELECT 쿼리문과 유사한 성격을 가지며, POST보다 전송속도가 빠르다.
2. ex) www.xxx.com?id=aaa&bbb=111 의 형식 작성으로 작성된다. (작성된 데이터가 노출되며 타인이 접속가능)
3. URL의 길이가 한정되어 있기에 보내는 양의 한계가 존재한다.

# GET - 쿼리스트링으로 요청이 왔을 시 처리방법

`요청(request)`이 GET 쿼리스트링 형식으로 왔을 때 처리하는 방식에 대해서 알아보고자한다.

### 쿼리스트링

우선 `쿼리스트링` 이란게 뭔지 알아야한다. 쿼리스트링은 **사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 미리 협의된 데이터를 파라미터를 통해 넘기는 것을 말한다.**

### 쿼리스트링 형식

- 정해진 엔드포인트 주소 이후에 `?`를 쓰는 것으로 쿼리스트링의 시작을 알린다.
- parameter=value 로 필요한 파라미터 값을 적는다
- 파라미터가 여러개일 경우 `&` 을 붙여서 구분해준다.

```
엔드포인트주소/엔드포인트주소?파라미터=값&파라미터&값...
```

### (2) POST

1. POST방식의 특징으로는 URL이 아닌 BODY에 데이터를 넣어서 숨겨진 상태로 전송된다.
2. 헤더필드중 BODY의 데이터를 설명하는 `Content-Type`이라는 헤더필드가 들어가고 어떤 데이터 타입인지 명시해야 한다.

## 8.Django ModelForm

모델 스키마들을 정해진 폼을 통해 빠르게 설정하여 불러낼 수 있다.

1.앱 폴더에서 forms.py를 생성 후 폼 생성 틀을 만들어준다.

```
from django import forms
from .models import tests

class test1Form(forms.ModelForm):
    class Meta:
        model = tests
        fields = '__all__'
```

2.views.py에서  forms.py를 참조 한 후  폼을 적용 할 수 있도록 함수를 정의해준다.

```bash
from .models import tests
from .forms import test1Form #<= forms 형태를 참조하여 가져옴

def new(request):
    test_form = test1Form  # 폼을 입력해줄 변수 지정후 내보낼 딕셔녀리에 키값으로 묶어준다.
    context = {
        "test_form": test_form,
    }
    return render(request, "test1/new.html", context=context) #여긴 왜 context=context형태일까?
```

1. html에서 폼을 적용해서 사용할 시 

```bash
<form action="{% url 'test1:create' %}" method="Post">
        {% csrf_token %}
        {{ test_form.as_p }}
        <input type="submit" value="제출 ">
    </form>
```