### HTML 기본

HTML(HyperText Markup Language)은 웹을 이루는 가장 기초적인 구성 요소로, 웹 콘텐츠의 의미와 구조를 정의할 때 사용합니다. HTML 이외의 다른 기술은 일반적으로 웹 페이지의 모양/표현 ([CSS](https://developer.mozilla.org/ko/docs/Web/CSS)
), 또는 기능/동작 ([JavaScript](https://developer.mozilla.org/ko/docs/Web/JavaScript))을 설명하는 데 사용됩니다.

HTML은 웹 페이지와 그 내용을 구조화하기 위해 사용하는 코드입니다. 예를 들면, 컨텐트는 여러 개의 문단, 글 머리 목록이 구조화된 것이거나 사진이나 데이터 테이블 일 수 있습니다.

HTML은 컨텐츠의 서로 다른 부분들을 씌우거나(wrap) 감싸서(enclose) 다른 형식으로 보이게하거나 특정한 방식으로 동작하도록 하는 일련의 **요소([elements](https://developer.mozilla.org/ko/docs/Glossary/Element))**로 이루어져 있습니다.

`내 고양이는 고약해`

그 한 줄의 문장이 독립적인 구문이길 원한다면, 문단 태그(paragraph tags)로 둘러쌈으로해서 그것이 하나의 문단임을 명시할 수 있습니다:

`<p>내 고양이는 고약해</p>`

<p>둘러쌓아 하나의 문단으로 명시

1. **Hypertext(하이퍼텍스트)**

Hypertext(하이퍼텍스트)"란 웹 페이지를 다른 페이지로 연결하는 링크를 말합니다. 링크는 웹의 근본적인 속성으로, 인터넷에 자료를 올리고 다른 사람이 만든 페이지로 링크함으로써 여러분도 월드 와이드 웹 세계의 능동적인 일원이 될 수 있습니다.

1. **HTML의 요소**

HTML은 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위해 "마크업"을 사용합니다. HTML 마크업은 다양한 "요소"를 사용하는데, 요소에는 `[<head>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/head)`, `[<title>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title)`, `[<body>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/body)`, `[<header>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/header)`, `[<footer>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/footer)`, `[<article>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/article)`, `[<section>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/section)`, `[<p>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p)`, `[<div>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div)`, `[<span>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/span)`, `[<img>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img)`, `[<aside>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/aside)`, `[<audio>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/audio)`, `[<canvas>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/canvas)`, `[<datalist>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/datalist)`, `[<details>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/details)`, `[<embed>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/embed)`, `[<nav>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/nav)`, `[<output>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/output)`, `[<progress>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/progress)`, `[<video>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video)`, `[<ul>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul)`, `[<ol>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol)`, `[<li>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li)` 등 많은 종류가 존재합니다.

HTML 요소는 "태그"를 사용해서 문서의 다른 텍스트와 구분합니다. 

태그는 "`<`", 태그 이름, "`>`"로 이루어집니다. 태그 안의 요소 이름은 대소문자를 구분하지 않습니다. 즉, 대문자, 소문자, 아니면 섞어서도 작성할 수 있습니다. 예를 들어 `<title>`요소는 `<Title>`
, `<TITLE>`, 그 외 기타 가능한 모든 방법으로 작성할 수 있습니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a67963a-246d-4d26-81c0-1e22438eea7f/Untitled.png)

## [이미지](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EC%9D%B4%EB%AF%B8%EC%A7%80)

`[<img>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img)` 요소를 다시 살펴보도록 합시다:

`<img src="images/firefox-icon.png" alt="My test image">`Copy to Clipboard

앞에서 설명한 것처럼 이 요소는 이미지가 나타나야 할 위치에 이미지를 끼워 넣습니다. 이미지 파일의 경로를 포함하는 `src` (source) 속성을 통해 이러한 일을 합니다.

`alt` (alternative) 속성도 존재합니다. — 이 속성에는 다음과 같은 이유로 이미지를 볼 수 없는 사용자들을 위한 설명문(descriptive text)을 지정할 수 있습니다.:

1. 시각 장애자인 경우. 시각 장애가 심한 사용자들은 alt 텍스트(대체 텍스트)를 읽어주는 스크린 리더라는 도구를 자주 사용합니다.
2. 무언가 잘못되어서 이미지를 표시할 수 없는 경우. 예를 들면, `src` 속성 안의 경로를 일부러 틀리게 변경해보세요. 저장한 후에 페이지를 다시 열면, 이미지가 표시되어야할 위치에 다음과 같은 것을 보게 될 것입니다.

### [빈 요소](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EB%B9%88_%EC%9A%94%EC%86%8C)

어떤 요소들은 내용을 갖지 않습니다, 그리고 이것을 **빈 요소(empty elements)**라고 합니다. `[<img>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img)` 요소는 이미 우리 HTML 코드에 있습니다.

`<img src="images/firefox-icon.png" alt="My test image">`

이 요소는 두 개의 속성을 포함하고 있으나 닫는 </img> 태그가 없습니다. 이미지 요소는 효과를 주기 위해 컨텐츠를 감싸지 않기 때문입니다. 이 요소의 목적은 HTML 페이지에서 이미지가 나타날 위치에 이미지를 끼워 넣는 것입니다.

## [연결](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EC%97%B0%EA%B2%B0)

연결은 아주 중요합니다 — 이것은 웹을 웹으로 만들어줍니다. 연결을 하기 위해, 간단한 요소를 사용할 필요가 있습니다 — `[<a>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/a)` — *a* 는 "anchor" 의 약자입니다. 문장 안의 어떤 단어를 링크로 만들기 위해, 아래의 순서를 따르시면 됩니다:

1. 어떤 단어를 선택하세요. "Mozilla Manifesto" 를 선택하겠습니다.
2. 문자를 <a> 요소로 감쌉니다, 이렇게요:
    
    `<a>Mozilla Manifesto</a>`Copy to Clipboard
    
3. <a> 요소에 href 속성을 줍니다, 이렇게요:
    
    `<a href="">Mozilla Manifesto</a>`Copy to Clipboard
    
4. 이 속성의 값에 여러분이 연결하길 원하는 웹 주소를 채웁니다.:
    
    `<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>`Copy to Clipboard
    

만약 웹 주소의 시작부분에 *프로토콜*이라 불리는 https:// 또는 http:// 부분을 빼먹으셨다면 예상하지 못한 결과를 얻을 것입니다. 이렇게 링크를 만든 후에, 원하는 곳으로 이동하는지 클릭해보세요.

## [문자 나타내기](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EB%AC%B8%EC%9E%90_%EB%82%98%ED%83%80%EB%82%B4%EA%B8%B0)

여기에서는 문자를 나타내기 위해 사용하는 몇 개의 기본적인 HTML 엘리먼트를 다룰 것입니다.

### [제목](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EC%A0%9C%EB%AA%A9)

제목 요소는 여러분이 내용의 특정 부분이 제목 또는 내용의 하위 제목임을 구체화 할 수 있게 해줍니다. 책에 중심 제목이 있고 그 다음 각각의 장에 제목을 가지고, 그리고 그 안에 부제가 있는 것과 같은 방식으로 HTML 문서도 제목들을 갖습니다. HTML 은 여섯 단계의 제목을 갖고, `[<h1>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Heading_Elements)`–`[<h6>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Heading_Elements)` 여러분은 아마 3-4 만을 주로 사용하게 될겁니다:

`<h1>My main title</h1><h2>My top level heading</h2><h3>My subheading</h3><h4>My sub-subheading</h4>`Copy to Clipboard

지금 한번 해보세요, 여러분의 HTML 페이지에 있는 `[<img>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img)` 요소 위에 적당한 제목을 추가합시다.

### [문단](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EB%AC%B8%EB%8B%A8)

위에서 설명했듯이, `[<p>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p)` 요소는 문자의 문단을 포함하기 위한 것입니다; 일반적인 문자 내용을 나타낼 때 많이 사용하게 될 것입니다:

`<p>This is a single paragraph</p>`Copy to Clipboard

**간단한 문자 (*[웹사이트의 외관은 어떻게 할까요?](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/What_will_your_website_look_like)* 에서 보셨을겁니다)를 하나 또는 몇 개의 문단에 추가하고, <img> 요소 바로 아래 둡시다.**

### [목록](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EB%AA%A9%EB%A1%9D)

많은 웹의 내용은 목록이기 때문에, HTML은 이것을 위한 특별한 요소를 가지고 있습니다. 목록을 나타내는 것은 항상 최소 두 개의 요소로 구성됩니다. 가장 일반적인 목록의 종류는 순서가 있는 것과 순서 없는 것이 있습니다.

1. **순서 없는 목록은** 쇼핑 목록과 같이 항목의 순서에 관계가 없는 목록을 위한 것입니다. `[<ul>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul)` 요소로 둘러 쌓여 있습니다.
2. **순서 있는 리스트**는 조리법처럼 항목의 순서가 중요한 목록을 위한 것입니다. `[<ol>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol)` 요소로 둘러 쌓여 있습니다.

목록의 각 항목은 `[<li>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li)` (목록 항목) 요소 안에 놓여야 합니다.

그러니까 예를 들면, 만약 아래 문단의 한 부분을 목록으로 분리하길 원한다면:

`<p>At Mozilla, we’re a global community of technologists, thinkers, and builders working together ... </p>`Copy to Clipboard

이렇게 해볼 수 있습니다:

`<p>At Mozilla, we’re a global community of</p><ul><li>technologists</li><li>thinkers</li><li>builders</li></ul><p>working together ... </p>`Copy to Clipboard

**여러분의 예시 페이지에서 순서 있는 목록과 순서 없는 목록을 추가해보세요.**

## [연결](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/HTML_basics#%EC%97%B0%EA%B2%B0)

연결은 아주 중요합니다 — 이것은 웹을 웹으로 만들어줍니다. 연결을 하기 위해, 간단한 요소를 사용할 필요가 있습니다 — `[<a>](https://developer.mozilla.org/ko/docs/Web/HTML/Element/a)` — *a* 는 "anchor" 의 약자입니다. 문장 안의 어떤 단어를 링크로 만들기 위해, 아래의 순서를 따르시면 됩니다:

1. 어떤 단어를 선택하세요. "Mozilla Manifesto" 를 선택하겠습니다.
2. 문자를 <a> 요소로 감쌉니다, 이렇게요:
    
    `<a>Mozilla Manifesto</a>`Copy to Clipboard
    
3. <a> 요소에 href 속성을 줍니다, 이렇게요:
    
    `<a href="">Mozilla Manifesto</a>`Copy to Clipboard
    
4. 이 속성의 값에 여러분이 연결하길 원하는 웹 주소를 채웁니다.:
    
    `<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>`Copy to Clipboard
    

만약 웹 주소의 시작부분에 *프로토콜*이라 불리는 https:// 또는 http:// 부분을 빼먹으셨다면 예상하지 못한 결과를 얻을 것입니다. 이렇게 링크를 만든 후에, 원하는 곳으로 이동하는지 클릭해보세요.