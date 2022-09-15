# JavaScript

# JavaScript

1.자바스크립트는 가벼운 인터프리터 OR 컴파일 프로그래밍 언어이다.

2.웹페이지를 동적으로 만들어주는 역활을 해준다.

3.JavaScript와 java는 다른 언어

4.웹페이지를 위한 스크립트 언어로 잘 알려져 있지만 NODE.JS, APCHECHDB, ADOBE ACROBAT처럼 비 브라우저 환경에서도 사용되고 있음

- [HTML](https://developer.mozilla.org/ko/docs/Glossary/HTML)은 웹 콘텐츠의 구조를 짜고 의미를 부여하는 마크업 언어입니다. 예를 들어 페이지의 어디가 문단이고, 헤딩이고, 데이터 표와 외부 이미지/비디오인지 정의합니다.
- [CSS](https://developer.mozilla.org/ko/docs/Glossary/CSS)는 HTML 콘텐츠에 스타일을 적용할 수 있는 스타일 규칙 언어입니다. 배경색을 추가하고, 글꼴을 바꾸고, 콘텐츠를 신문처럼 다열 레이아웃으로 배치할 수 있습니다.
- [JavaScript](https://developer.mozilla.org/ko/docs/Glossary/JavaScript)는 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어입니다. (정말 모든게 가능하지는 않겠지만, JavaScript 코드 몇 줄만으로도 놀라운 결과를 이룰 수 있습니다)

## JavaScript로 브라우저에서 할 수 있는 일

- DOM 조작
• 문서(HTML) 조작
• BOM 조작
• navigator, screen, location, frames, history, XHR
• JavaScript Core (ECMAScript)
• Data Structure(Object, Array), Conditional Expression, Iteration

## DOM (Document Object Model)

브라우저를 통해 문서(HTML)을 조작하는 방법

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
• 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
• 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급
• 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
• 주요 객체
• window : DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략 가능)
• document : 페이지 컨텐츠의 Entry Point 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함
• navigator, location, history, screen

## DOM 조작

파싱(parsing)
• 구문 분석, 해석
• 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
[https://hacks.mozilla.org/2017/08/inside-a-super-fast-css-engine-quantum-css-aka-stylo/](https://hacks.mozilla.org/2017/08/inside-a-super-fast-css-engine-quantum-css-aka-stylo/)

#BOM (Browser Object Model)

BOM 이란?
Browser Object Model

- 자바스크립트가 브라우저와 소통하기 위한 모델
• 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
• 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
• window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

![[Pasted image 20220915163609.png]]

#Java 기본문법

JavaScript는 문법의 대부분을 Java와 C, C++로부터 차용하고 있으며, Awk, Perl, Python의 영향도 받았습니다.

JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용합니다. 예를 들면, Früh(독일어로 "이른")을 변수명으로 사용할 수도 있습니다

## 주석

```
// 한 줄 주석

/* 이건 더 긴,
 * 여러 줄 주석입니다.
 */

/* 그러나, /* 중첩된 주석은 쓸 수 없습니다 */ SyntaxError */

```

## 선언

1.var
변수를 선언. 추가로 동시에 값을 초기화.

2.let
블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화.

3.const
블록 스코프 읽기 전용 상수를 선언.

## 변수

- `var x = 42`와 같이 var 키워드로 변수를 선언할 수 있습니다. 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있습니다.

`let y = 13`와 같이 `let` 키워드로 변수를 선언할 수 있습니다. 이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있습니다.

간단히 변수에 값을 할당 할 수도 있습니다. 예를 들어, `x = 42` 와 같은 구문은 [**선언되지 않은 전역변수**]를 만듭니다. 뿐만 아니라, 자바스크립트의 엄격한 경고를 만들어냅니다. 선언되지 않은 전역변수는 의도되지 않은 동작을 만들어내고는 합니다. 따라서 선언되지 않은 전역변수를 사용하면 안됩니다.

## 변수할당

지정된 초기 값 없이 `var` 혹은 `let` 문을 사용해서 선언된 변수는 `undefined` 값을 갖습니다.

선언되지 않은 변수에 접근을 시도하는 경우 `ReferenceError` 예외가 발생합니다

## 변수 호이스팅

### 호이스팅이란 ?

자바스크립트 함수는 실행되기 전에 함수 안에 필요한 변수값들을 모두 모아서 유효 범위의 최상단에 선언한다.
자바스크립트 Parser가 함수 실행 전 해당 함수를 한 번 훑는다.
함수 안에 존재하는 변수/함수선언에 대한 정보를 기억하고 있다가 실행시킨다.
유효 범위: 함수 블록 {} 안에서 유효
즉, 함수 내에서 아래쪽에 존재하는 내용 중 필요한 값들을 끌어올리는 것이다.
실제로 코드가 끌어올려지는 건 아니며, 자바스크립트 Parser 내부적으로 끌어올려서 처리하는 것이다.
실제 메모리에서는 변화가 없다.
[https://gmlwjd9405.github.io/2019/04/22/javascript-hoisting.html](https://gmlwjd9405.github.io/2019/04/22/javascript-hoisting.html)

JavaScript 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조할 수 있다는 것입니다.

이 개념은 **호이스팅**(hoisting)으로 알려져 있습니다. 즉 JavaScript 변수가 어떤 의미에서 함수나 문의 최상단으로 "올려지는" (혹은 "끌어올려지는") 것을 말합니다. 하지만, 끌어올려진 변수는 `undefined` 값을 반환합니다. 그래서 심지어 이 변수를 사용 혹은 참조한 후에 선언 및 초기화하더라도, 여전히 `undefined`를 반환합니다.

```
/**
 * Example 1
 */
console.log(x === undefined); // true
var x = 3;

/**
 * Example 2
 */
// undefined 값을 반환함.
var myvar = "my value";

(function() {
  console.log(myvar); // undefined
  var myvar = "local value";
})();

```

호이스팅 때문에, 함수 내의 모든 `var` 문은 가능한 함수 상단 근처에 두는 것이 좋습니다. 이 방법은 코드를 더욱 명확하게 만들어줍니다.

ECMAScript 2015의 `let`과 `const`는 변수를 블록의 상단으로 **끌어올리지만 초기화하지 않습니다.** 변수가 선언되기 전에 블록 안에서 변수를 참조하게 되면 `[ReferenceError](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)`를 발생시키게 되는데, 변수는 블록 시작부터 선언이 처리될 때까지 "temporal dead zone"에 위치하게 되기 때문입니다.

```
console.log(x); // ReferenceError
let x = 3;

```

## 데이터형

최신 ECMAScript 표준은 8가지 데이터 형을 정의합니다.

- 7가지 [원시](https://developer.mozilla.org/ko/docs/Glossary/Primitive) 데이터 형
****JavaScript**의 타입**
- Boolean 타입
`true`와 `false`
- Null 타입
null 값을 나타내는 특별한 키워드. (JavaScript는 대소문자를 구분하므로, `null`은 `Null`, `NULL` 혹은 다른 변형과도 다릅니다.
- Undefined 타입
값이 정의되어 있지 않은 최상위 속성.
- Number 타입
정수 또는 실수형 숫자. 예: `42` 혹은 `3.14159`.
- BigInt 타입
임의 정밀도의 정수. 예: `9007199254740992n`.
- String 타입
문자열. 예:"안녕"
- Symbol 타입
(ECMAScript 2015에 도입) 인스턴스가 고유하고 불변인 데이터 형.
- object타입
    
    var num = 10;          // 숫자
    
    var myName = "홍길동"; // 문자열
    
    var str;               // undefined
    

## 자료형변환

JavaScript는 동적 형지정(정형) 언어입니다. 이는 변수를 선언할 때 데이터 형을 지정할 필요가 없음을 의미합니다. 또한 데이터 형이 스크립트 실행 도중 필요에 의해 자동으로 변환됨을 뜻합니다.

그래서, 예를 들어, 다음과 같이 변수를 정의할 수 있습니다.

```
var answer = 42;

```

Copy to Clipboard

그리고 나중에, 동일한 변수에 문자열 값을 할당할 수도 있습니다. 아래와 같이,

```
answer = 'Thanks for all the fish...';

```

Copy to Clipboard

JavaScript는 동적 형지정 언어이므로, 이 할당은 오류 메시지가 발생하지 않습니다.

## 숫자와 +연산자

숫자와 문자열 값 사이에 `+` 연산자를 포함한 식에서, JavaScript는 숫자 값을 문자열로 변환합니다. 예를 들어, 아래와 같은 문이 있습니다.

```
x = 'The answer is ' + 42 // "The answer is 42"
y = 42 + ' is the answer' // "42 is the answer"

```

Copy to Clipboard

다른 연산자를 포함한 식의 경우, JavaScript는 숫자 값을 문자열로 변환하지 않습니다. 예를 들면,

```
'37' - 7 // 30
'37' + 7 // "377"

```

##문자열을 숫자로 변환하기

숫자를 나타내는 값이 문자열로 메모리에 있는 경우, 변환을 위한 메서드가 있습니다.

- parseInt()
- parseFloat()

parseInt`는 오직 정수만 반환하므로, 소수에서는 사용성이 떨어집니다.

```
parseInt('101', 2) // 5

```

문자열을 숫자로 변환하는 대안은 `+` (단항 더하기) 연산자입니다.

```
'1.1' + '1.1' // '1.11.1'
(+'1.1') + (+'1.1') // 2.2
// 참고: 괄호는 명확성을 위해 추가, 필요한 것은 아닙니다.

```

## 리터럴

JavaScript에서 값을 나타내기 위해 리터럴을 사용합니다. 이는 말 그대로 스크립트에 부여한 고정 값으로, 변수가 아닙니다. 이 구획에서는 다음과 같은 형태의 리터럴을 설명합니다.

- [배열 리터럴]
- [불리언 리터럴]
- [부동 소수점 리터럴]
- [숫자 리터럴]
- [객체 리터럴]
- [정규식 리터럴]
- [문자열 리터럴]

1.배열리터럴

```
배열 리터럴은 0개 이상의 식(expression) 목록입니다. 각 식은 배열 요소를 나타내고 대괄호(`[]`)로 묶입니다. 배열 리터럴을 사용하여 배열을 만들 때, 그 요소로 지정된 값으로 초기화되고, 그 `length`는 지정된 인수의 갯수로 설정됩니다.

아래 예제는 요소가 3개로 `length`가 3인 `coffees` 배열을 만듭니다.

```
let coffees = ['French Roast', 'Colombian', 'Kona'];
```

이 배열은 값이 있는 두 요소와 빈 요소 하나를 가집니다.

   `fish[0]`은 "Lion"
   `fish[1]`은 `undefined`
   `fish[2]`는 "Angel"

다음 예제에서, 배열의 `length`는 3입니다. `myList[3]`은 없습니다. 목록의 다른 모든 쉼표는 새로운 요소를 나타냅니다.

```
var myList = ['home', , 'school', ];
```

아래 예제에서, 배열의 `length`는 4이며, `myList[1]`과 `myList[3]`은 값이 빠졌습니다. **마지막 쉼표는 무시됩니다.**

```
var myList = ['home', , 'school', , ];
```

추가 쉼표의 동작을 이해하는 것은 JavaScript를 언어로서 이해하는데 중요합니다.

하지만 코드를 작성할 때는 빠진 요소의 값을 명시적으로 `undefined`로 선언하는 것이 코드의 명확성과 유지보수성을 높입니다.

```

2.불리언 리터럴

```
불리언 형은 `true`와 `false`의 리터럴 값을 가집니다.

```

3.숫자 리터럴

```
JavaScript 숫자 리터럴은 다른 진법의 정수 리터럴과 10진수의 부동 소수점 리터럴이 포함됩니다.

언어 명세서에 따르면 숫자 리터럴에 부호가 없어야 합니다. 그럼에도 불구하고, `-123.4` 와 같은 코드 괜찮습니다. 숫자 리터럴 `123.4` 에 단항 연산자 `-` 가 붙은 것으로 해석됩니다.

```

1. 정수 리터럴

정수와 `BigInt`1 리터럴은 10진수, 16진수, 8진수 및 2진수로 표현될 수 있습니다.

- 10진수 정수 리터럴은 `0`으로 시작(leading zero)하지 않는 숫자열로 이루어집니다.
- 정수 리터럴에서 `0`으로 시작하거나 `0o`(혹은 `0O`)으로 시작하는 숫자열은 8진수임을 나타냅니다. 8진수 정수 리터럴은 오직 숫자 `0``7`만 포함할 수 있습니다.
- `0x`(나 `0X`)로 시작하는 숫자열은 16진수 정수 리터럴 임을 나타냅니다. 16진수 정수는 숫자 (`0``9`) 및 문자 `a``f`, `A``F`를 포함할 수 있습니다. (문자의 대소문자는 그 값을 변경하지 않습니다. 그러므로 `0xa` = `0xA` = `10` 그리고 `0xf` = `0xF` = `15` 입니다.)
- `0b` (나 `0B`)로 시작하는 숫자열은 2진수 정수 리터럴 임을 나타냅니다. 2진수 정수 리터럴은 오직 숫자 `0`과 `1`만 포함할 수 있습니다.
- `n`으로 끝나는 숫자열은 [`BigInt`]gInt) 리터럴 임을 나타냅니다. 정수 리터럴은 위의 어떤 진수든 사용할 수 있습니다. `0123n`과 같은 `0`으로 시작하는 8진수 구문은 허용되지 않으나, `0o123n`은 허용됩니다.
1. 부동 소수점 리터럴

부동 소수점 리터럴은 아래와 같은 부분으로 이루어집니다.

- 부호없는 10진 정수,
- 소수점 ("`.`"),
- 소수 (또 다른 10진수),
- 지수.

지수부는 "`e`"나 "`E`" 다음에 오며 부호("`+`"나 "`-`")가 달릴 수 있는 정수입니다. 부동 소수점 리터럴은 적어도 숫자 하나와 소수점 혹은 "`e`"(나 "`E`")가 있어야 합니다.

더 간결하게 설명하면, 구문은 다음과 같습니다.

[digits].[digits][(E|e)[(+|-)]digits]

예를 들면,

3.1415926
.123456789
3.1E+12
.1e-23

1. [객체 리터럴])

객체 리터럴은 중괄호(`{}`)로 묶인 0개 이상인 객체의 속성명과 관련 값 쌍 목록입니다.

> 주의: 문(statement)의 시작에 객체 리터럴을 사용해서는 안됩니다. 이는 {가 블록의 시작으로 해석되기 때문에 오류를 유발하거나 의도한 대로 동작하지 않습니다.
> 

아래는 객체 리터럴의 예제입니다. `car` 객체의 첫째 요소는 `myCar` 속성을 정의하고 문자열 `"Saturn"`을 할당합니다. 반면 둘째 요소인 `getCar` 속성은 함수 `(carTypes("Honda"))`을 호출한 결과가 즉시 할당됩니다. 셋째 요소 `special` 속성은 기존 변수 (`sales`)를 사용합니다.

```
var sales = 'Toyota';

function carTypes(name) {
  if (name === 'Honda') {
    return name;
  } else {
    return "Sorry, we don't sell " + name + ".";
  }
}

var car = { myCar: 'Saturn', getCar: carTypes('Honda'), special: sales };

console.log(car.myCar);   // Saturn
console.log(car.getCar);  // Honda
console.log(car.special); // Toyota

```

Copy to Clipboard

게다가, 속성명으로 숫자나 문자열 리터럴을 사용하거나 또다른 객체 리터럴 내부에 객체를 중첩할 수도 있습니다. 아래 예제는 이 옵션을 사용합니다.

```
var car = { manyCars: {a: 'Saab', b: 'Jeep'}, 7: 'Mazda' };

console.log(car.manyCars.b); // Jeep
console.log(car[7]); // Mazda

```

Copy to Clipboard

객체 속성명은 빈 문자열 포함 어떤 문자열도 될 수 있습니다. 속성명이 유효한 JavaScript [식별자](https://developer.mozilla.org/ko/docs/Glossary/Identifier)나 숫자가 아닌 경우, 따옴표로 묶여야 합니다.

또한 유효한 식별자가 아닌 속성명은 점(`.`) 속성으로 접근할 수 없습니다. 대신 배열 같은 표기법("`[]`")으로 접근하고 값을 설정할 수 있습니다.

```
var unusualPropertyNames = {
  '': 'An empty string',
  '!': 'Bang!'
}
console.log(unusualPropertyNames.'');   // SyntaxError: Unexpected string
console.log(unusualPropertyNames['']);  // An empty string
console.log(unusualPropertyNames.!);    // SyntaxError: Unexpected token !
console.log(unusualPropertyNames['!']); // Bang!

```

# 제어문

1. 블록문
가장 기본적인 명령문은, 명령문들을 그룹으로 묶을 수 있는 **블록문**입니다. 블록문의 블록은 한 쌍의 중괄호로 감싸는 것으로 나타냅니다.

```
{
  statement_1;
  statement_2;
  ⋮
  statement_n;
}

```

블록문은 제어 흐름 명령문과 많이 사용합니다. (`if`, `for`, `while`)

```
while (x < 10) {
  x++;
}

```

Copy to Clipboard

여기서 `{ x++; }`가 블록문입니다.

2.조건문

조건문은 지정한 조건이 참인 경우에 실행하는 명령 집합입니다. JavaScript는 `if...else`와 `switch` 두 종류의 조건문을 지원합니다.

###`if...else`문

명령문을 논리 조건이 참일 때 실행하려면 `if` 문을 사용하세요. 선택적으로, `else` 절을 추가해서 조건이 거짓인 경우에 실행할 명령문을 지정할 수 있습니다.

`if` 문의 형태는 다음과 같습니다.

```
if (condition) {
  statement_1;
} else {
  statement_2;
}

```

Copy to Clipboard

위 코드에서, `condition`에는 `true`나 `false`로 평가할 수 있는 아무 표현식이나 대입할 수 있습니다. (`[Boolean](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Boolean)` 문서에서 `true`와 `false` 평가에 대해 더 알아보세요.)

`condition`이 `true`로 평가되면 `statement_1`을 실행합니다. 그렇지 않으면 `statement_2`를 실행합니다. `statement_1`과 `statement_2`에는 다른 `if` 문을 포함해 아무 명령문이나 사용할 수 있습니다.

`else if`를 사용해서 다수의 조건을 순차적으로 검사할 수도 있습니다.

```
if (condition_1) {
  statement_1;
} else if (condition_2) {
  statement_2;
} else if (condition_n) {
  statement_n;
} else {
  statement_last;
}

```

Copy to Clipboard

이 경우, 처음으로 `true`로 평가되는 조건의 명령문들만 실행됩니다.

### 모범 사례

일반적으로는 `if`에 항상, 특히 `if` 문을 중첩할 때는 블록문을 함께 사용하는 것이 좋습니다.

```
if (condition) {
  statement_1_runs_if_condition_is_true;
  statement_2_runs_if_condition_is_true;
} else {
  statement_3_runs_if_condition_is_false;
  statement_4_runs_if_condition_is_false;
}

```

Copy to Clipboard

또한 `if...else`의 조건에 "`x = y`"와 같은 할당은 지양하세요.

```
if ((x = y)) {
  /* 명령문 */
}

```

### 거짓 값

다음 값은 `false`로 평가됩니다. ([거짓](https://developer.mozilla.org/ko/docs/Glossary/Falsy) 값이라고 부릅니다)

- `false`
- `undefined`
- `null`
- `0`
- `NaN`
- 빈 문자열 (`""`)

객체를 포함해 다른 모든 값은 조건문에 전달했을 때 `true`로 평가됩니다.

**참고:** `true`와 `false` 원시 값을 `[Boolean](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Boolean)` 객체의 참과 거짓 값과 혼동하지 마세요!

예를 들어,

`const b = new Boolean(false);
if (b)         // 참으로 평가
if (b == true) // 거짓으로 평가`