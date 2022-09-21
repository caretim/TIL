# Django 개발환경 설정 가이드(bash기준)

1. 가상환경 생성 / 실행 /에러
2. Django LTS 버전 설치
3. Django 프로젝트 생성
4. Django 실행

## 1. 가상환경 생성 / 실행

가상환경에서 장고를 진행하는 이유는 각각의 프로젝트는 사용되는 장고버전이 다를 수 있기 때문에 각 프로젝트에 맞는 라이브러리를 사용해야한다. 가상환경을 통해 각각 다른 버전을 설치하여 이용할 수 있기 때문이다.

(1) 파이썬이 설치되어있는지 확인한다.

```bash
$python --version
```

(2) 가상환경을 설치할 폴더를 생성한다

```bash
$python -m venv {폴더명} 
```

(3) 설치된 폴더의 Scripts/activate를 실행시킨다

```bash
$source {폴더명}/Scripts/activate
```

(4) 가상환경 종료는 `$deactivate`를 입력한다

5) 가상환경에러

* 가상환경 설치시 에러 해결 방법- 가상환경을 설치할 때 여러가지 이유로 에러가 날 수 있다. (경로, 메모리, 기존의 설치된 파일 등등)

그럴 때 해결하기 위해서, 가상환경을 전역적으로 설치해주거나 / 삭제했다가 다시 설치함으로 해결할 수 있다.

## 2.Django LTS 버전 설치

```bash
//장고 인스톨
$pip install django=={버전번호}

//pip 설치 리스트 확인
$pip list
```

## 3. Django 프로젝트 생성

```bash
django-admin startproject {파일명} {시작경로}
```

## 4. Django 실행

```bash
//manage.py 파일 안에 실행 코드가 들어가 있음 
$python  manage.py runserver 

실행 후 자신의 로컬 주소로 접속하여 실행이 되었는지 확인한다.

localhost:8000

입력 후 들어가서 서버가 구축되어있는지 확인한다.
```