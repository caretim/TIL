# BOX 모델
CSS가 표히하는 모든 것은 박스
CSS BOX MODEL이 작동핫는 방식을 이해하는 것이 CSS의 핵심 기반
 `border-radius`을 사용하여 원처럼 보이는 박스 또는 텍스트만 있더라도 모든 것은 **박스**로 되어있다.

- #### 콘텐츠 및 크기
박스는 `display` 값, 설정된 치수 및 박스 안에 있는 내용에 따라 다르게 동작
**외부 크기 조정**을 사용하여 이를 제어하거나 **내부 크기 조정**을 사용하여 콘텐츠 크기를 기반으로 브라우저가 계속 결정하도록 할 수 있습니다.

콘텐츠가 박스에 비해 너무 크면 이를 **오버플로**라고 합니다. `overflow` 속성을 사용하여 요소가 오버플로 콘텐츠를 처리하는 방법을 관리할 수 있습니다.


- #### 박스모델의 영역 
![[Pasted image 20220831151125.png]]


1. **콘텐츠 박스** 
콘텐츠는 부모 콘텐츠의 크기를 제어할 수 있으며, 그렇기에 일반적으로 가장 다양한 크기의 영역도 제어합니다.

2. **패딩 박스**
 콘텐츠 박스를 둘러싸고 있으며 padding 속성에 의해 생성된 공간입니다. 패딩이 박스 안에 있기 때문에 박스의 배경을 박스가 만드는 공간에서 볼 수 있습니다. 박스에 `overflow: auto` 또는 `overflow: scroll`과 같은 오버플로 규칙이 설정되어 있으면 스크롤바도 이 공간을 차지하게 됩니다.

3. **보더 박스** (테두리 박스)
패딩 박스를 둘러싸고 있으며 그 공간은 `border` 값으로 채워집니다. 테두리 박스는 박스의 경계이며 **테두리 가장자리**는 시각적으로 볼 수 있는 영역의 한계입니다. boder 속성은 요소를 시각적으로 프레임하는 데 사용됩니다.

4. **마진 박스** (여백 박스)
박스의 `margin` 규칙에 의해 정의된 여러분의 박스 주변의 공간입니다. outline 와  box-shoadow 같은 속성이 페인트처럼 상단을 칠하며 이 공간을 차지하기에 우리 박스의 크기에 영향을 미치지 않습니다. 박스의 `outline-width`가 `200px`일 수 있으며 테두리 박스를 포함하여 내부의 모든 것이 정확히 같은 크기일 수 있습니다.





``` css
.my-box {  
width: 200px;  
border: 10px solid;  
padding: 20px;  
}
```

이 박스의 실제 너비는 260px입니다. CSS는 기본 `box-sizing: content-box`를 사용하기 때문에 적용되는 너비는 콘텐츠의 너비이며 `padding`과 `border`가 양쪽에 추가됩니다. 따라서 콘텐츠 200px + 패딩 40px + 테두리 20px로 총 260px의 가시 너비를 만듭니다.


하지만 대체 박스 모델인 `border-box`를 사용하도록 다음과 같이 수정하면 이를 제어하는 것이 _가능_합니다.

```css
.my-box {  
box-sizing: border-box;  
width: 200px;  
border: 10px solid;  
padding: 20px;  
}
```





# CSS Position
CSS Position이란 ?
문서 상에서 요소의 위치를 지정하는것 

#### ! **static**: 모든 태그의 기본 값 (기준 위치)

	 -일반적인 요소의 배치 순서에 따름(좌측 상단) 
	 -부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

 
 
 
#### !아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능 


1. **relative** :상대 위치

• 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
• 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)

2. absolute 절대 위치


• 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남) 
• static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)

3. fixed 고정위치

• 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남) 
• 부모 요소와 관계없이 viewport를 기준으로 이동 
• 스크롤 시에도 항상 같은 곳에 위치함

4. sticky 스크롤에 따라 static -> fixed로 변경 

• 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성


### CSS의 원칙

• CSS 원칙 I, II : Normal flow 

모든 요소는 네모(박스모델), 좌측상단에 배치
display에 따라 크기와 배치가 달라짐 

CSS 원칙 III • position으로 위치의 기준을 변경 

• relative : 본인의 원래 위치 
• absolute : 특정 부모의 위치 
• fixed : 화면의 위치 
• sticky: 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경



# CSS Layout

## Float
•박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함
• 요소가 Normal flow를 벗어나도록 함



## FLEXBOX 
행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

CSS Flexible Box Layout

축 
• main axis (메인 축) 
• cross axis (교차 축) 


구성 요소 
• Flex Container (부모 요소) 
• Flex Item (자식 요소)
![[Pasted image 20220831165858.png]]


Flex Container (부모 요소)

• flexbox 레이아웃을 형성하는 가장 기본적인 모델 
• Flex Item들이 놓여있는 영역 
• display 속성을 flex 혹은 inline-flex로 지정

 Flex Item (자식 요소) 
• 컨테이너에 속해 있는 컨텐츠(박스)

```css
.flex-container {
	display: flex; 
}
```


 **justify-content**

-   `flex-start`: 요소들을 컨테이너의 왼쪽으로 정렬합니다.
-   `flex-end`: 요소들을 컨테이너의 오른쪽으로 정렬합니다.
-   `center`: 요소들을 컨테이너의 가운데로 정렬합니다.
-   `space-between`: 요소들 사이에 동일한 간격을 둡니다.
-   `space-around`: 요소들 주위에 동일한 간격을 둡니다.

![[Pasted image 20220901054235.png]]

align-items
-   `flex-start`: 요소들을 컨테이너의 꼭대기로 정렬합니다.
-   `flex-end`: 요소들을 컨테이너의 바닥으로 정렬합니다.
-   `center`: 요소들을 컨테이너의 세로선 상의 가운데로 정렬합니다.
-   `baseline`: 요소들을 컨테이너의 시작 위치에 정렬합니다.
-   `stretch`: 요소들을 컨테이너에 맞도록 늘립니다.

![[Pasted image 20220901054338.png]]
![[Pasted image 20220901054343.png]]
 
 
 flex-direction
 -   `row`: 요소들을 텍스트의 방향과 동일하게 정렬합니다.
-   `row-reverse`: 요소들을 텍스트의 반대 방향으로 정렬합니다.
-   `column`: 요소들을 위에서 아래로 정렬합니다.
-   `column-reverse`: 요소들을 아래에서 위로 정렬합니다.
![[Pasted image 20220831170259.png]]


flex-wrap
-   `nowrap`: 모든 요소들을 한 줄에 정렬합니다.
-   `wrap`: 요소들을 여러 줄에 걸쳐 정렬합니다.
-   `wrap-reverse`: 요소들을 여러 줄에 걸쳐 반대로 정렬합니다.

![[Pasted image 20220831170328.png]]