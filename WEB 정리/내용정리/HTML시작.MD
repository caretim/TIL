# 1. **HTML이란?**

HTML은 HyperText Markup Language의 약자

웹 페이지는 HTML 문서라고도 불리며, HTML 태그들로 구성됩니다.

각각의 HTML 태그는 웹 페이지의 디자인이나 기능을 결정하는데 사용

**HTML 태그(tag)**

HTML 태그는 태그 이름을 꺾쇠 괄호(<>)로 감싸서 표현합니다.

문법

1. <태그이름> // 시작 태그
2. </태그이름> // 종료 태그

HTML 태그는 보통 시작 태그(start tag, opening tag)와 종료 태그(end tag, closing tag)의 한 쌍으로 구성됩니다.

종료 태그는 시작 태그와 전부 똑같지만, 태그 이름 앞에 슬래시(/)가 존재합니다.

태그에 따라 시작 태그만 있고 종료 태그가 없는 태그도 존재합니다.

**빈 태그**

<img> <br> <hr> 등과 같이 종료 태그 없이 시작 태그만을 가지는 태그를 빈 태그(empty tag)라고 합니다.

# 2.**HTML의 기본 구조**

```bash
<!DOCTYPE html>
<html lang="ko">

<head>
	<meta charset="UTF-8">
</head>

<body>

	<h1>제목 1</h1>
	<h2>제목 2</h2>
	<h3>제목 3</h3>
	<p>단락 1</p>
	<p>단락 2</p>

</body>

</html>
```

<!DOCTYPE html> : 현재 문서가 HTML5 문서임을 명시합니다.

<html> : HTML 문서의 루트(root) 요소를 정의합니다.

<head> : HTML 문서의 메타데이터(metadata)를 정의합니다.

- 메타데이터(metadata)란 HTML 문서에 대한 정보(data)로 웹 브라우저에는 직접적으로 표현되지 않는 정보를 의미합니다.
- 이러한 메타데이터는 <title>, <style>, <meta>, <link>, <script>, <base>태그 등을 이용하여 표현할 수 있습니다.

<title> : HTML 문서의 제목(title)을 정의하며, 다음과 같은 용도로 사용됩니다.

- 웹 브라우저의 툴바(toolbar)에 표시됩니다.
- 웹 브라우저의 즐겨찾기(favorites)에 추가할 때 즐겨찾기의 제목이 됩니다.
- 검색 엔진의 결과 페이지에 제목으로 표시됩니다.

<body> : 웹 브라우저를 통해 보이는 내용(content) 부분입니다.

<h1> ~ <h6> : 제목(heading)을 나타냅니다.

<p> : 단락(paragraph)을 나타냅니다.

# 3. **HTML 요소 구조**

### HTML 요소 구조

HTML 요소(element)는 여러 속성을 가질 수 있으며, 이러한 속성(attribute)은 해당 요소에 대한 추가적인 정보를 제공합니다.

또한, HTML 요소는 시작 태그로 시작해서 종료 태그로 끝납니다.

![http://www.tcpschool.com/lectures/img_html_tag_structure.png](http://www.tcpschool.com/lectures/img_html_tag_structure.png)

속성은 HTML 요소 중에서도 언제나 시작 태그 내에서만 정의되며, 속성 이름과 속성값(value)으로 표현됩니다.

### 문법

<태그이름 속성이름="속성값">

---

### 속성 이름은 언제나 소문자로 작성하자!

HTML5 표준에서는 속성 이름에 대소문자를 구분하지 않고 있습니다.

하지만 W3C에서는 속성 이름을 사용할 때 될 수 있으면 소문자로 작성하도록 권장하고 있습니다.

또한, XHTML에서는 속성 이름을 더욱 엄격하게 소문자로만 사용해야 합니다.

---

### 속성값은 언제나 따옴표로 감싸자!

HTML5 표준에서는 속성값에 따옴표 사용을 강제하지 않습니다.

하지만 속성값을 따옴표로 감싸지 않으면, 다음과 같은 예상치 못한 오류가 발생할 수 있습니다.

<img src="quotes.jpg" alt="이미지가 없어요">

<img src="quotes.jpg" alt=이미지가 없어요>

위의 예제와 같이 속성값에 띄어쓰기가 들어가게 되면, 반드시 따옴표를 사용해야 정확한 값을 저장할 수 있습니다.

속성값을 감쌀 때는 보통 큰따옴표("")가 사용되며, 작은따옴표('')도 사용할 수 있습니다.

