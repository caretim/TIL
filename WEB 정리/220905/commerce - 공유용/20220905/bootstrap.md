
#Bootstarp

CDN를 통해 작동하는 프론트 엔드 프레임 워크

HTML 및 CSS기반의 디자인 템플릿을 제공한다.

Bootsstrap을 통해서 쉽고 간편하게 웹 개발을 할 수 있다.

Bootstrap에 저장된 CSS 스타일을 클래스를 통해 가져와 쉽게 적용 시킬 수 있다.

**다운로드가 아닌 링크와 스크립트로 실행하는 방법**

```html
링크 - head 
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">

스크립트 - body

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
```

**Bootstrap spacing**

대부분의 클래스는 축약형임

```html
{property}{sides}-{size}

mt-3  
mt = margin-top
3 =  16px

<div class="mt-3 ms-5">bootstrap-spacing</div>
```

## spacing 종합

| m | margin |
| --- | --- |
| p | padding |

| t | top |
| --- | --- |
| b | bottom |
| s | left |
| e | right |
| x | left,right |
| y | top,bottom |

| 0 | 0rem | 0px |
| --- | --- | --- |
| 1 | 0.25rem | 4px |
| 2 | 0.5rem | 8px |
| 3 | 1rem | 16px |
| 4 | 1.5rem | 24px |
| 5 | 3rem | 32px |

## Color

컬러 사스맵 ([https://getbootstrap.com/docs/5.2/customize/color/](https://getbootstrap.com/docs/5.2/customize/color/))

```html
$colors: (
  "blue":       $blue,
  "indigo":     $indigo,
  "purple":     $purple,
  "pink":       $pink,
  "red":        $red,
  "orange":     $orange,
  "yellow":     $yellow,
  "green":      $green,
  "teal":       $teal,
  "cyan":       $cyan,
  "black":      $black,
  "white":      $white,
  "gray":       $gray-600,
  "gray-dark":  $gray-800
);
```

색 연결 코드 예시

```html
<h2>Color</h2>
<div class="bg-primary">이건 파랑</div>
<div class="bg-secondary">이건 회색</div>
<div class="bg-danger">이건 빨강</div>
<p class="text-success">이건 초록색 글씨</p>
<p class="text-danger">이건 빨간색 글씨</p>
```

## Text

텍스트 코드 예시

```html
<h2>Text</h2>
<p class="text-start">margin-top 3</p>
<p class="text-center">margin 4</p>
<p class="text-end">mx-auto, 가운데 정렬</p>
<a href="#" class="text-decoration-none">Non-underlined link</a>
<p class="fw-bold">Bold text.</p>
<p class="fw-normal">Normal weight text.</p>
<p class="fw-light">Light weight text.</p>
<p class="fst-italic">Italic text.</p>
```

## Display

디스플레이 코드 예시

```html
<h2>Display</h2>
<div class="d-inline p-2 bg-primary text-white">d-inline</div>
<div class="d-inline p-2 bg-dark text-white">d-inline</div>
<div class="d-block p-2 bg-dark text-white">d-inline</div>
<div class="d-block p-2 bg-primary text-white">d-inline</div>
<div class="box bg-warning d-sm-none d-md-block">보이나?? 안보이나??</div>
<div class="box bg-success d-md-none d-xl-block">보이나?? 안보이나??</div>
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/597db54d-5326-4941-a909-99b4b22a1380/Untitled.png)

## Position

```html
<h2>Position</h2>
<div class="box fixed-top">fixed-top</div>
<div class="box fixed-bottom">fixed-bottom</div>
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c32bb66a-b1eb-4e0e-939e-dbccdba5f7c4/Untitled.png)

 **Position 예시**

```html
<div class="position-static">...</div>
<div class="position-relative">...</div>
<div class="position-absolute">...</div>
<div class="position-fixed">...</div>
<div class="position-sticky">...</div>
```

## **break point**

반응형 디스플레이를 위해 적용되는 크기 적용 포인트

| Breakpoint | Class infix | Dimensions |
| --- | --- | --- |
| Extra small | None | <576px |
| Small | sm | ≥576px |
| Medium | md | ≥768px |
| Large | lg | ≥992px |
| Extra large | xl | ≥1200px |
| Extra extra large | xxl | ≥1400px |

## Flex([https://getbootstrap.com/docs/5.2/utilities/flex/](https://getbootstrap.com/docs/5.2/utilities/flex/))

1.**display**

display : flex;

`<div class="d-flex p-2">I'm a flexbox container!</div>`

display: flex;

block: inline;

`<div class="d-inline-flex p-2">I'm an inline flexbox container!</div>`

**적용 가능한 클래스 선언 목록**

.d-flex
.d-inline-flex
.d-sm-flex
.d-sm-inline-flex
.d-md-flex
.d-md-inline-flex
.d-lg-flex
.d-lg-inline-flex
.d-xl-flex
.d-xl-inline-flex
.d-xxl-flex
.d-xxl-

2.****Direction****

```html
<div class="d-flex flex-row mb-3">
  <div class="p-2">Flex item 1</div>
  <div class="p-2">Flex item 2</div>
  <div class="p-2">Flex item 3</div>
</div>
<div class="d-flex flex-row-reverse">
  <div class="p-2">Flex item 1</div>
  <div class="p-2">Flex item 2</div>
  <div class="p-2">Flex item 3</div>
</div>
```

.flex-row
.flex-row-reverse
.flex-column
.flex-column-reverse
.flex-sm-row
.flex-sm-row-reverse
.flex-sm-column
.flex-sm-column-reverse
.flex-md-row
.flex-md-row-reverse
.flex-md-column
.flex-md-column-reverse
.flex-lg-row
.flex-lg-row-reverse
.flex-lg-column
.flex-lg-column-reverse
.flex-xl-row
.flex-xl-row-reverse
.flex-xl-column
.flex-xl-column-reverse
.flex-xxl-row
.flex-xxl-row-reverse
.flex-xxl-column
.flex-xxl-column-reverse

3.****Justify content****

.justify-content-start
.justify-content-end
.justify-content-center
.justify-content-between
.justify-content-around
.justify-content-evenly
.justify-content-sm-start
.justify-content-sm-end
.justify-content-sm-center
.justify-content-sm-between
.justify-content-sm-around
.justify-content-sm-evenly
.justify-content-md-start
.justify-content-md-end
.justify-content-md-center
.justify-content-md-between
.justify-content-md-around
.justify-content-md-evenly
.justify-content-lg-start
.justify-content-lg-end
.justify-content-lg-center
.justify-content-lg-between
.justify-content-lg-around
.justify-content-lg-evenly
.justify-content-xl-start
.justify-content-xl-end
.justify-content-xl-center
.justify-content-xl-between
.justify-content-xl-around
.justify-content-xl-evenly
.justify-content-xxl-start
.justify-content-xxl-end
.justify-content-xxl-center
.justify-content-xxl-between
.justify-content-xxl-around
.justify-content-xxl-evenly

**4.align-items**

.align-items-start
.align-items-end
.align-items-center
.align-items-baseline
.align-items-stretch
.align-items-sm-start
.align-items-sm-end
.align-items-sm-center
.align-items-sm-baseline
.align-items-sm-stretch
.align-items-md-start
.align-items-md-end
.align-items-md-center
.align-items-md-baseline
.align-items-md-stretch
.align-items-lg-start
.align-items-lg-end
.align-items-lg-center
.align-items-lg-baseline
.align-items-lg-stretch
.align-items-xl-start
.align-items-xl-end
.align-items-xl-center
.align-items-xl-baseline
.align-items-xl-stretch
.align-items-xxl-start
.align-items-xxl-end
.align-items-xxl-center
.align-items-xxl-baseline
.align-items-xxl-stretch

## Content

**1.reboot** 

단일 파일로 css변경 모음

초기 bootstrap의 빌드로 짜여져 있으며 일관되고 간단한 기준선을 가지고 있습니다.

**2.제목과 단락** 

모든 제목 요소 (예: `<h1>` 및 `<p>`)는 `margin-top`이 제거되도록 재설정됩니다. 제목에는 `margin-bottom: .5rem`이 추가되고 단락은 `margin-bottom : 1rem`이 추가되어 간격을 쉽게 조정할 수 있습니다.

**3.목록**

모든 목록 (`<ul>`,`<ol>`, `<dl>`)에는 `margin-top`이 제거되고 `margin-bottom: 1rem`이 제거됩니다. 중첩된 목록에는 `margin-bottom`이 없습니다. 또한`<ul>` 및 `<ol>` 요소에서 `padding-left`를 재설정했습니다.

**4.인라인코드**

인라인 코드 스니펫을 `<code>`로 묶습니다. HTML 꺾쇠 괄호를 이스케이프해야 합니다.

**5.코드블록**

여러 줄의 코드에는 `<pre>`를 사용하세요. 다시 한 번 올바른 렌더링을 위해 코드에서 꺾쇠 괄호를 이스케이프해야 합니다. `<pre>` 요소는 `margin-top`을 제거하고 `margin-bottom`에 `rem` 단위를 사용하도록 재설정됩니다.

**6.변수**

변수를 나타내려면 `<var>` 태그를 사용하세요.

**7.사용자입력**

일반적으로 키보드를 통해 입력되는 입력을 나타내려면 `<kbd>`를 사용해주세요.

8.**출력 예시**

프로그램의 출력 예시를 나타내려면 `<samp>` 태그를 사용해주세요.

9.**표**

표는 스타일 `<caption>`, 테두리 축소 및 전체적으로 일관된 `text-align`을 위해 약간 조정됩니다. 테두리, 패딩 등에 대한 추가 변경 사항은 `[.table` 클래스](https://getbootstrap.kr/docs/5.1/content/tables/)와 함께 제공됩니다.

10.**폼**

더 간단한 기본 스타일을 위해 다양한 폼 요소가 Reboot되었습니다. 다음은 가장 눈에 띄는 변경 사항입니다:

- `<fieldset>`에는 테두리, 패딩 또는 여백이 없으므로 개별 입력 또는 입력 그룹의 래퍼로 쉽게 사용할 수 있습니다.
- 필드셋과 마찬가지로 `<legend>`도 일종의 제목으로 표시되도록 스타일이 변경되었습니다.
- `<label>`이 `display: inline-block`으로 설정되어 `margin`이 적용될 수 있습니다.
- `<input>`, `<select>`, `<textarea>`, `<button>`은 대부분 Normalize에 의해 처리되지만 Reboot는 `margin`을 제거하고 `line-height: inherit`도 설정합니다.
- `<textarea>`는 가로 크기 조정이 종종 페이지 레이아웃을 “파괴"하므로 세로로만 크기를 조정할 수 있도록 수정됩니다.
- `<button>`과 `<input>` 버튼 요소는`:not(:disabled)`일 때 `cursor : pointer`를 갖습니다.