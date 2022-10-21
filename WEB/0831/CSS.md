## *CSS

#### 박스 모델의 영역

- 박스는 모두 특정 작업을 수행하는 별개의 박스 모델 영역으로 구성되어 있습니다.

![박스 모델의 네 가지 주요 영역을 보여주는 다이어그램 - 콘텐츠 박스, 패딩 박스, 테두리 박스 및 여백 박스](https://web-dev.imgix.net/image/VbAJIREinuYvovrBzzvEyZOpw5w1/ECuEOJEGnudhXW5JEFih.svg)

-  **Content box **- 콘텐츠의 크기를 제어할 수 있으며, 그렇기에 일반적으로 가장 다양한 크기의 영역도 제어합니다.
- **Padding box** - 콘텐츠 박스를 둘러싸고 있으며 [`padding`](https://developer.mozilla.org/docs/Web/CSS/padding) 속성에 의해 생성된 공간입니다. 패딩이 박스 안에 있기 때문에 박스의 배경을 박스가 만드는 공간에서 볼 수 있습니다. 박스에 `overflow: auto` 또는 `overflow: scroll`과 같은 오버플로 규칙이 설정되어 있으면 스크롤바도 이 공간을 차지하게 됩니다.

- **Border box** - 패딩 박스를 둘러싸고 있으며 그 공간은 `border` 값으로 채워집니다. 테두리 박스는 박스의 경계이며 **테두리 가장자리**는 시각적으로 볼 수 있는 영역의 한계입니다. [`border`](https://developer.mozilla.org/docs/Web/CSS/border) 속성은 요소를 시각적으로 프레임하는 데 사용됩니다.

- **Margin box** - 박스의 `margin` 규칙에 의해 정의된 여러분의 박스 주변의 공간. outline및 [`box-shadow`](https://developer.mozilla.org/docs/Web/CSS/box-shadow)와 같은 속성이 페인트처럼 상단을 칠하며 이 공간을 차지하기에 우리 박스의 크기에 영향을 미치지 않습니다. 박스의 `outline-width`가 `200px`일 수 있으며 테두리 박스를 포함하여 내부의 모든 것이 정확히 같은 크기일 수 있습니다.

---------------------------

### *CSS position

• 문서 상에서 요소의 위치를 지정 

• static : 모든 태그의 기본 값(기준 위치) 

• 일반적인 요소의 배치 순서에 따름(좌측 상단)

• 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

 • 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능 

#### 1.relative 2. absolute 3. fixed 4. sticky

1. relative : 상대 위치 • 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지) 

​	레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset) 

2. absolute : 절대 위치 • 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남) • static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)

3.  fixed : 고정 위치 • 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남) • 부모 요소와 관계없이 viewport를 기준으로 이동 • 스크롤 시에도 항상 같은 곳에 위치함 CSS position CSS Position 

4. sticky: 스크롤에 따라 static -> fixed로 변경 • 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

--------

-  **absolute는 언제 사용?**

  -특정 영역 위에 나타낼때 - CSS 기본 원칙인 좌측 상단에 배치되지 않음. 부모를 기준으로 가운데 위치

- **fixed는 언제 사용?**

  -브라우저 기준으로 위치 CSS 기본 원칙인 좌측상단에 배치되지 않음. 브라우저를 기준으로 우측 하단에 위치. EX) 홈페이지 상담채팅

---------------

### *position sticky

- sticky: 스크롤에 따라 static -> fixed로 변경 
-  속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만, 스크롤 위 치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성
-  일반적으로 Navigation Bar에서 사용됨. 

-------

### CSS 원칙

- **CSS 원칙 I, II : Normal flow** 

  - 모든 요소는 네모(박스모델), 좌측상단에 배치 

  - display에 따라 크기와 배치가 달라짐 

    

-  **CSS 원칙 III** 
  - position으로 위치의 기준을 변경
  -  relative : 본인의 원래 위치 
  -  absolute : 특정 부모의 위치 
  -  fixed : 화면의 위치 
  -  sticky: 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경

----

## *CSS layout

#### Float

- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함 

-  요소가 Normal flow를 벗어나도록 함

  

#### Flexbox

- CSS Flexible Box Layout
  - 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
  - 축
    - main axis (메인 축)
    - cross axis (교차 축)

![](C:\Users\User\OneDrive\바탕 화면\KDT\TIL\WEB\0831\1.png)

- 구성 요소

  - Flex Container (부모 요소)

  - Flex Item (자식 요소)

    

#### *FLEX BOX 축

![](C:\Users\User\OneDrive\바탕 화면\KDT\TIL\WEB\0831\2.png)

#### *Flexbox 구성 요소

- **Flex Container (부모 요소)** 
  -  flexbox 레이아웃을 형성하는 가장 기본적인 모델 
  -  Flex Item들이 놓여있는 영역 
  -  display 속성을 flex 혹은 inline-flex로 지정 
-  **Flex Item (자식 요소)**
  -   컨테이너에 속해 있는 컨텐츠(박스)



***왜 Flexbox를 사용해야 할까?** 

-이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position 정도밖에 없었음

​	=> 수동값 부여없이 수직정렬 어려움

​	=> 각각의 아이템의 너비와 높이  혹은 간격을 동일하게 배치하기 어려움

