# Git -분산 버전 관리 시스템

**버전**이란 컴퓨터 소프트웨어의 특정 상태

일반적으로 자료버전이 뭐가 바뀌었는지 차이를 알 수 없다.

버전관리, 소스코드 관리란 동일한 정보에 대한 여러가지 버전을 관리하는 것을 의미한다.

리누스 토르발스가 2005년 리눅스 커널을 위한 도구로 개발했다.

컴퓨터 파일의 변경사항을 추적하고 여러명의 사용자들 간에 해당파일의 작업을 조율

**분산버전관리시스템** (DVCS)

-   중앙집중식버전관리시스템은 중앙에서 버전을 관리하고 파일을 받앗 ㅓ사용
-   분산버전관리시스템은 원격저장소를 통하여 협업하고 모든 히스토리를 클라이언트들이 공유한다.

1.  작업 2) ADD하여 Staging area모아 3)버전으로 남긴다. (commit)

*Staging area를 사용하는 이유: 버전기록을 나누거나 따로 버전을 기록하기 위해 또는 미리테스트하기 위한 임시공간

staging 단계가 있는 이유1. 실질적인 변경 사항을 파악해 최종 저장 용량을 최소화 하기 위해서!2. 실서비스 사용 전에 테스트 보드로서 사용

(master)는 깃이랑 연결되어있음

자주 사용된 기본 명령어

-   pwd(print working directory) :현재 디렉토리 출력
-   cd(change directory): 디렉토리 이동
    -   .:현재 디렉토리, ..:상위 디렉토리
    -   cd + tap을 누르면 리스트가 나온다
-   ls(list) : 목록
-   mkdir(make directory): 디렉토리 생성
-   touch: 파일의 날짜와 시간을 수정 (0바이트 빈파일 생성)
-   rm(remove) :파일을 지운다
    -   rm –r 폴더명 : 폴더 삭제하기
-   clear or 기록 지우기 컨트롤 + L

# 기본명령어 -add

**$ git add <file>**

working drectory상의 변경 내용을 staging area에 추가하기 위해 사용

# 기본명령어 -commit

**$git commit- m [메세지]**

staged 상태의 파일들을 커밋을 통해 버전으로 기록

40자로 고유커밋을 표기한다.

git은 데이터를 파일시스템의 스냅샷으로 관리하고 매우 크기가 작다.


# 기본명령어 -log

-   **$git log [3통 조회]**
-   현재 저장소에 기록된 커밋(commit)을 조회
-   다양한 옵션을 통해 로그를 조회할 수 있음

$git log-1 (최근 커밋조회)

$git log —oneline 한줄로 짧게

$git log -2 —oneline

# 기본명령어 - status

-   **$git status** [깃으로 관리되고 있지 않는 파일] 1통 ,2통 확인


**git 사용시 init을 통해 master가 되어있는지 꼭 확인하기**

깃 저장 이메일 닉네임 확인 - git config --global --list

**1.(master) 있는 곳에서는 git init을 하지 않는다.**

**2.git 명령어를 입력할 때는 항.상. 경로를 잘 보자**

**3.명령어의 결과를 잘 읽자 (모르면 구글링)**

# 파일 라이프사이클


untracked 상태에서 add를 하게되면 스테이지에 들어감

staged 상태의 파일을 commit하게되면 unmodified상태로 들어가게됨

1.  보고서파일을 새로 만들었다 ⇒ untracked
2.  보고서 파일을 add했다 ⇒ staged
3.  commit = unmodified
4.  보고서 수정 ⇒ modified

$git status의 초록색(staged)과 빨간색(untracked, modified)

## 커밋은 의미 있는 저장이 되어야한다.

**사용자 정보 (commit author) : 커밋을 하기 위해 반드시 필요**

-   git config —global [user.name](http://user.name)
    
-   git config —global user.
    

git으로 버전관리 하기 위해서 git init을 사용한다

만일 프로젝트가 각각의 프로젝트라면 각 폴더마다 init을 따로 지정해줘야한다.

빈폴더는 status에 나타나지 않는다. 안에 파일이 있어서 status에 나타남

> 꺽쇠 표시가 나오면 뒤에 마무리가 안되어서 나오는것 마무리를 하거나 or `ctrl+c`를 쓰자

## 원격저장소

-   Github
-   GitLab
-   Bitbucket

## 원격저장소 PUSH & PULL

로컬에서 원격저장소로 **버전 (커밋) 보내기 PUSH**

원격저장소에서 로컬로 **버전을 (커밋) 가져오기 PULL**

## $는 터미널에서 입력하라는 뜻 (로컬)

## 1. 원격저장소 경로 설정

-   원격저장소 정보를 로컬장소에 추가
-   로컬 저장소에는 한번만 설정해주면 된다.

$git remote add origin [http:~]

[](https://github.com/)[https://github.com/](https://github.com/)[gitHub username]/[저장소 이름].git

붙여넣기 단축키 `shift+ ins`

컨트롤 v 가 아님

## 2. 원격저장소에 push로 보내기

$git push origin master

깃 프로젝트 폴더마다 각각의 원격저장소를 만들어줘야한다.

(git 원격저장소 만들고 각각 주소가 달라야함 )

원격저장소 이름을 바꾸면 원격저장소 주소가 바뀐다.

$git push origin -u master *-u는 명령어를 간단하게 만들어 git push만 적어도 푸시가 되게 만듬

깃허브는 분산버전관리시스템이라는걸 꼭 기억

## 3.원격저장소에서 pull로 가져오기

$git push origin origin master

## github파일과 로컬파일이 다르면 발생하는 오류는 pull을 통해 파일을 다시 받고 새로 파일을 커밋하여 보내면 사라짐

이 과정에서 merge라는 커밋이 생김 - 병합된파일


# .Gitignore - 버전관리를 하고 싶지 않은 폴더나 파일을 별도로 관리가능

커밋전에 미리 ignore에 미리 설정해야 편함.

ex) 윈도우와 맥의 파일이 안 겹치게 무시하는것

ignore 사용법 확인해보기

[gitignore.io](http://gitignore.io) - 프로젝트 할 때 불필요한 내용 빼는 코드 설정


wildcard로 .exe 를 제외시킨 모습 (자동으로 exe파일들을 제외한다)