**Cascading Style Sheets**
(**CSS**)는 [HTML](https://developer.mozilla.org/ko/docs/Web/HTML)이나 [XML](https://developer.mozilla.org/ko/docs/Web/XML)(XML의 방언인 [SVG](https://developer.mozilla.org/ko/docs/Web/SVG), [XHTML](https://developer.mozilla.org/ko/docs/Glossary/XHTML)포함)로 작성된 문서의 표시 방법을 기술하기 위한 [스타일 시트](https://developer.mozilla.org/ko/docs/Web/API/StyleSheet) 언어입니다. CSS는 요소가 화면, 종이, 음성이나 다른 매체 상에 어떻게 렌더링되어야 하는지 지정합니다.

CSS (Cascading Style Sheets) 는 콘텐츠의 글꼴, 색상, 크기 및 간격을 변경하거나 여러 열로 분할하거나 애니메이션 및 기타 장식 기능을 추가하는 등의 웹 페이지 스타일 및 레이아웃에 사용됩니다. 이 모듈은 작동 방식, 구문의 모양 및 HTML에 스타일을 추가하기 위해, 이를 사용하는 방법에 대한 기본 사항을 통해 CSS 를 마스터 하는 과정을 부드럽게 시작합니다.

**CSS 전제 조건**

이 모듈을 시작하기 전에, 다음이 있어야 합니다:

1. 컴퓨터를 사용하고 웹을 수동적으로 사용하는 것에 대한 기본적인 친숙성 (예: 콘텐츠를 보는 것) 입니다.
2. [기본 소프트웨어 설치](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/Installing_basic_software) 에서 자세히 설명한 대로 설정된 기본 작업 환경과 [파일 다루기](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/Dealing_with_files) 에서 자세히 설명한 대로 파일을 생성하고 관리하는 방법을 이해합니다.
3. [HTML 소개](https://developer.mozilla.org/ko/docs/Learn/HTML/Introduction_to_HTML) 에서 설명한 바와 같이 HTML에 대한 기본적인 친숙성입니다.

### CSS  구문

CSS 는 규칙 기반 언어입니다 — 웹 페이지의 특정 요소 또는 요소 그룹에 적용할 스타일 그룹을 지정하는 규칙을 정의합니다. 예를 들어 "내 페이지의 제목이 빨간색이며 큰 텍스트로 표시 되기를 원합니다."

다음 코드는 위에서 설명한 스타일을 실행 하는 매우 간단한 CSS 규칙을 보여줍니다:

```css
h1 {
    color: red;
    font-size: 5em;
}
```

규칙은 [selector (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/CSS_Selector) 와 함께 열립니다. 스타일을 지정할 HTML 요소를 ***선택***합니다. 이 경우 level 1 제목 (`[<h1>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Heading_Elements)`) 을 스타일링합니다.

h1을 지정 {} 중괄호 안에 속성과 값 쌍의 형태를 취하는 하나 이상의 선언이 존재합니다

각 쌍은 우리가 선택한 요소의 속성을 지정하고 속성에 부여할 값을 지정합니다.

**속성 : 부여할 값 ;** 

```css
h1 {
    color: red;
    font-size: 5em;
}

p {
    color: black;
}
```

CSS스타일 시트에서는 여러 규칙이 하나씩 포함되어 있다.

## HTML에 적용하기

```html
!doctype html>
<html lang="ko-KR">
<head>
    <meta charset="utf-8">
    <title>CSS로 시작하기</title>
</head>

<body>

    <h1>레벨 1 제목입니다</h1>

    <p>이것은 단락입니다. 본문에는 <span>span 요소</span>와 <a href="http://example.com">링크</a>가 있습니다.</p>

    <p>이것은 두 번째 단락입니다. <em>강조된</em> 요소를 포함합니다.</p>

    <ul>
        <li>항목 하나</li>
        <li>항목 둘</li>
        <li>항목 <em>셋</em></li>
    </ul>

</body>

</html>
```

1. HTML에 적용할 CSS규칙을 링크를 통해 연결한다.
    
    `styles.css` 파일을 `index.html` 에 링크하려면, HTML 문서의 `[<head>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/head)`
     안에 다음 행을 추가
    
    `<link rel="stylesheet" href="styles.css">`
    
2. `styles.css` 에 규칙을 추가하여 CSS가 작동하는지 테스트를 한다.
    
    ```css
    h1 {
      color: red;
    }
    ```
    
    HTML파일과 CSS 파일을 저장 후 웹 브라우저에서 페이지를 로드하여 상단의 제목이 빨간색으로 변했는지 확인한다. ( 작동되었다면 상단 제목이 빨간색 ) 
    
    ## HTML 요소 스타일링
    
     모든 단락을 녹색으로 바꾸려면 다음을 사용
    
    ```css
    p {
      color: green;
    }
    ```
    
    ## Class 추가하기
    
    문서 HTML 요소 기반으로 요소 스타일을 지정하는 방법을 사용했다면 이번에는 
    
    클래스를 지정하여 다른 요소를 변경하지 않고 요소의 하위 부분만 선택할 수 있는 방법으로
    
    클래스를 추가하여 Class 지정을 통해서 하위 요소만 변경 해 줄 수 있다.
    
    ```html
    <ul>
      <li>항목 하나</li>
      <li class="special">항목 둘</li>
      <li>항목 <em>셋</em></li>
    </ul>
    ```
    
    CSS 에서 마침표 문자로 시작하는 선택자를 작성하여 `special`
     class 를 대상으로 할 수 있습니다. CSS 파일에 다음을 추가하십시오:
    
    ```css
    .special {
      color: orange;
      font-weight: bold;
    }
    ```
    
    special이라는 클래스를 생성하여 적용 특정 항목만 바뀌는걸 확인 할 수 있다.
    
    클래스는 다양한 요소에 사용될 수 있으며 스타일을 만들때마다 CSS를 계속 편집하지 않아도 된다.
    
    