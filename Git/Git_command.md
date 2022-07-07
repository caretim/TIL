# 🔑Git 명령어 모음 



### 1.기본 CLI 명령어

---

- pwd(print working directory) :현재 디렉토리 출력

- cd(change directory): 디렉토리 이동

  -   .:현재 디렉토리, ..:상위 디렉토리
  -   cd + tap을 누르면 리스트가 나온다

- ls(list) : 목록

- mkdir(make directory): 디렉토리 생성

- touch: 파일의 날짜와 시간을 수정 (0바이트 빈파일 생성)

- rm(remove) :파일을 지운다

  -   rm –r 폴더명 : 폴더 삭제하기

- clear or 기록 지우기 컨트롤 + L

  

### 2.기본 GIT 기본명령어

---

- **$ git add <file>**

​		working drectory상의 변경 내용을 staging area에 추가하기 위해 사용

- **$git commit- m [메세지]**

  staged 상태의 파일들을 커밋을 통해 버전으로 기록

  40자로 고유커밋을 표기한다.

  git은 데이터를 파일시스템의 스냅샷으로 관리하고 매우 크기가 작다.

  commit message는 각 파일, 폴더별 설정이라기 보다는 이번의 작업에 대한 전반적인 설명을 함축(요약)해야 한다

  

- **$git status** [깃으로 관리되고 있지 않는 파일] 1통 ,2통 확인**

  - **git 사용시 init을 통해 master가 되어있는지 꼭 확인하기**

  깃 저장 이메일 닉네임 확인 - git config --global --list

  **1.(master) 있는 곳에서는 git init을 하지 않는다.**

  **2.git 명령어를 입력할 때는 항.상. 경로를 잘 보자**

  **3.명령어의 결과를 잘 읽자 (모르면 구글링)**

  

- **$git log [3통 조회]**

  현재 저장소에 기록된 커밋(commit)을 조회 ,다양한 옵션을 통해 로그를 조회할 수 있음



- .Gitignore - 버전관리를 하고 싶지 않은 폴더나 파일을 별도로 관리가능 *검색해서 찾아볼 것 

###  3.GITHUB연결 명령어

---

**사용자 정보 (commit author) : 커밋을 하기 위해 반드시 필요**

-   **git config —global [user.name](http://user.name)**

-   **git config —global user.**



**원격 저장소 경로 설정**

- **$git remote add origin [http:repository주소]**

​		원격저장소 정보를 로컬장소에 추가

​		로컬 저장소에는 한번만 설정해주면 된다.

- **$git remote -v** 

  원격저장소 주소가 잘 연결되었는지 확인



**원격저장소 연결 명령어 PUSH & PULL** (master는 branch명 변경될 수 있다)

**1.원격저장소로 보내기**

- **$git push origin master**

- **$git push origin -u master *-u는 명령어를 간단하게 만들어 git push만 적어도 푸시가 되게 만듬**

**2.원격저장소에서 가져오기** 

- **$git push origin origin master**

**github파일과 로컬파일이 다르면 발생하는 오류는 pull을 통해 파일을 다시 받고 새로 파일을 커밋하여 보내면 사라짐** -이 과정에서 merge라는 커밋이 생김 - 병합된파일



**3.원격저장소에서 파일 전체 내려받기**

- download zip

​	알집으로 받게되면 그냥 버전 하나만 다운받음 버전관리 불가.

- **$git clone [git 주소]** *주의 - 클론을 하게되면 원격저장소 이름의 폴더가 저장된다

​	클론을 통해 받게된다면 버전관리도 가능하다. 

​	

### 4. branch

---

1. 브랜치 조회 **$git branch**
2. 브랜치 생성 **$git branch** [브랜치명]
3. 브랜치 변경 **$git checkout** [브랜치명]
4. 브랜치 병합 **$git merge [**브랜치명]
5. 브랜치 만들면서 이동 **$git checkout -b** [브랜치명]

브랜치는 특정한 버전의 흐름이라고 말 할 수 있다.



### 5.Git 원격저장소에서의 병합관리방법

---

git을 통해서 병합할떄는 홈페이지에서 pr(pull request)를 통해 병합 진행

브랜치분야별로 나눠서 작업을 진행하고 git hub에 넣게되면 pr(pull request)을 통해 병합을 요청하고

관리자가 github에서 병합 



