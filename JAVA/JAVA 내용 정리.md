# 1. [JavaScript란?](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Introduction#javascript%EB%8A%94_%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80) 

*링크 참조

- JavaScript는 크로스-플랫폼, 객체지향 스크립트 언어입니다. 

- 클라이언트 측 JavaScript*는 브라우저와 문서 객체 모델(DOM) 을 제어하는 객체를 제공하여 코어 언어를 확장합니다. 예를 들어, 클라이언트 측 확장은 어플리케이션이 요소(element)를 HTML 폼에 두고, 마우스 클릭, 폼 입력 및 페이지 탐색 같은 사용자 이벤트에 응답하게 해줍니다.
- *서버 측 JavaScript*는 서버에서 JavaScript 실행에 관련된 객체를 제공하여 코어 언어를 확장합니다. 예를 들어, 서버 측 확장은 어플리케이션이 데이터베이스와 통신하고, 한 번의 호출 정보의 연속성을 어플리케이션의 다른 곳에 제공하거나, 서버에서 파일 조작을 수행할 수 있도록 해줍니다.



- JavaScript는 웹 페이지에서 복잡한 기능을 구현할 수 있도록 하는 스크립팅 언어 또는 프로그래밍 언어

-  페이지의 내용이 — 가만히 정적인 정보만 보여주는 것이 아니라 — 주기적으로 갱신되거나, 사용자와 상호작용이 가능하거나, 애니메이션이 적용된 2D/3D 그래픽을 볼 수 있다면 JavaScript가 관여하고 있을 거라고 생각해도 좋습니다

-  JavaScript는 표준 웹 기술이라는 케이크의 세 번째 층입니다. 

  - [HTML](https://developer.mozilla.org/ko/docs/Glossary/HTML)은 웹 콘텐츠의 구조를 짜고 의미를 부여하는 마크업 언어입니다. 예를 들어 페이지의 어디가 문단이고, 헤딩이고, 데이터 표와 외부 이미지/비디오인지 정의합니다.

  - [CSS](https://developer.mozilla.org/ko/docs/Glossary/CSS)는 HTML 콘텐츠에 스타일을 적용할 수 있는 스타일 규칙 언어입니다. 배경색을 추가하고, 글꼴을 바꾸고, 콘텐츠를 신문처럼 다열 레이아웃으로 배치할 수 있습니다.

  - [JavaScript](https://developer.mozilla.org/ko/docs/Glossary/JavaScript)는 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어입니다. (정말 모든게 가능하지는 않겠지만, JavaScript 코드 몇 줄만으로도 놀라운 결과를 이룰 수 있습니다)

----

## [JavaScript 와 Java](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Introduction#javascript_와_java)

JavaScript 와 Java는 여러 면에서 비슷하지만 어떤 면에서는 근본적으로 다릅니다.

* **JavaScript 언어**는 Java의 정적 형지정(static typing)과 강한 형 검사(strong type checking)가 없습니다. 

* **JavaScript**는 대부분의 Java 식 구문, 명명 규칙 및 기본적인 흐름 제어 구조를 따릅니다. 그것이 LiveScript에서 JavaScript로 이름이 바뀐 이유였습니다.

Java의 선언에 의해 생성되는 클래스의 컴파일-타임 시스템과는 달리, **JavaScript**는 **숫자, 불리언, 그리고 문자열 값을 표현하는 적은 수의 자료 형을 기반으로 한 런타임 시스템을 지원**합니다. 

JavaScript 는 더 일반적인 클래스 기반 객체 모델 대신에 프로토타입 기반 객체 모델을 갖습니다. 

프로토타입 기반 모델은 동적 상속을 제공합니다. 즉, 상속된 대상은 각각의 객체에 따라 다양할 수 있습니다. JavaScript는 또한 어떤 특정한 선언을 요구하지 않는 함수도 지원합니다. 함수는 객체의 속성이나, 타입이 느슨하게 형지정된 채 실행되는 메소드가 될 수 있습니다.

**JavaScript는** Java에 비해 **매우 자유로운 형태의 언어**입니다. 



**Java**는 ***빠른 실행**과 ***형 안전성(type safety)**을 위해 설계된 클래스 기반 프로그래밍 언어입니다. 

***형 안전성**은, 예를 들어, 여러분이 Java 정수를 객체의 레퍼런스로 형변환(cast)하거나 Java 바이트코드를 변경하여 private 메모리에 접근할 수 없음을 의미합니다. Java의 클래스 기반 모델은 프로그램이 오로지 클래스와 그 메소드로만 구성된다는 것을 뜻합니다.

Java의 클래스 상속과 강한 형지정은 보통 단단하게 결합된 객체 계층구조를 요구합니다. 이러한 요구는 Java 프로그래밍을 JavaScript 프로그래밍보다 더 복잡하게 만듭니다.

***반면**에, **JavaScript**는 HyperTalk 과 dBASE 같은 더 작고 동적 형지정이 가능한 언어들의 정신을 계승했습니다. 이러한 스크립팅 언어는 더 쉬운 구문과 특별한 내장(built-in) 기능 및 객체 생성을 위한 최소 요구사항으로 인해 훨씬 더 많은 사람들에게 프로그래밍 도구를 제공합니다.

| JavaScript                                                   | Java                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| 객체 지향. 객체의 형 간에 차이 없음. 프로토타입 메커니즘을 통한 상속, 그리고 속성과 메서드는 어떤 객체든 동적으로 추가될 수 있음. | 클래스 기반. 객체는 클래스 계층구조를 통한 모든 상속과 함께 클래스와 인스턴스로 나뉨. 클래스와 인스턴스는 동적으로 추가된 속성이나 메소드를 가질 수 없음. |
| 변수 자료형이 선언되지 않음(dynamic typing, loosely typed).  | 변수 자료형은 반드시 선언되어야 함(정적 형지정, static typing). |
| 하드 디스크에 자동으로 작성 불가.                            | 하드 디스크에 자동으로 작성 가능.                            |

## [JavaScript 시작하기](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Introduction#javascript_시작하기)



### [웹 콘솔](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Introduction#웹_콘솔)

[웹 콘솔](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html)은 현재 로드된 페이지에 대한 정보를 보이고, 또한 여러분이 현재 페이지에서 JavaScript 식을 실행해볼 수 있는 [명령어 입력줄(command line)](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html#the_command_line_interpreter)을 제공합니다.

웹 콘솔을 열기 위해서는, Firefox의 "도구" 메뉴 하위에 있는 "개발자" 메뉴의 "웹 콘솔"을 선택(윈도우와 리눅스에서는 Ctrl+Shift+I, 맥에서는 Cmd-Option-K)합니다. 브라우저 창의 아래에 웹 콘솔이 나타납니다. 콘솔의 바닥을 따라 나온 것이 여러분이 JavaScript를 입력할 수 있는 명령어 입력줄이고, 실행 결과는 바로 위 공간에 표시됩니다:

이 콘솔은 eval과 완전히 동일하게 동작합니다:마지막 입력된 표현식이 반환되죠. 간단하게 생각해서, 콘솔에 뭔가 입력할 때마다 eval로 감싼 console.log로 둘러싸인 형태라고 보시면 됩니다.\



```
function greetMe(yourName) { alert('Hello ' + yourName); } console.log(eval('3 + 5'));
```

### [Scratchpad](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Introduction#scratchpad)

Web Console은 한 줄 JavaScript를 실행하기에 훌륭합니다. 하지만 비록 여러 줄을 실행할 수 있지만, 아주 불편하고 Web Console을 사용해 여러분의 샘플 코드를 저장할 수도 없습니다. 그러므로 좀 더 복잡한 예제를 위해서는 [Scratchpad](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/ko/docs/도구들/Scratchpad)가 더 나은 도구입니다.

Scratchpad를 열기 위해, Firefox의 메뉴 "Tools" 의 하위에 있는 "Web Developer" 메뉴의 "Scratchpad" 를 선택합니다(단축키: Shift+F4). 이것은 분리된 창에서 열리고 브라우저에서 JavaScript를 작성하고 실행하기 위해 사용할 수 있는 에디터입니다. 여러분은 또한 디스크로부터 스크립트를 부르거나 저장할 수도 있습니다.







## 그래서 어떤 일을 할 수 있나요?

- 변수에 값을 저장할 수 있습니다.

  

- 프로그래밍에서 "문자열"(string)이라고 부르는, 텍스트 조각을 조작합니다. 

  

- 웹 페이지에서 발생하는 어떤 이벤트에 코드가 응답하도록 합니다.

  

- API

  - API는 개발자가 직접 구현하기는 어렵거나 불가능한 기능들을 미리 만들어서 제공하는 것입니다

  - [API](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/browser.png)는 일반적으로 두 개의 범주로 분류할 수 있습니다.

    - **브라우저 API**는 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행합니다.\

      - [DOM (Document Object Model) API](https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model)로 HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있습니다. 페이지 위에 뜨는 팝업창이나, (위쪽의 간단한 예제처럼) 새로운 콘텐츠가 나타나는 것을 본 적이 있으면 DOM이 동작한 겁니다.

        

      - [Geolocation API](https://developer.mozilla.org/ko/docs/Web/API/Geolocation)로 지리정보를 가져올 수 있습니다.

        

      - [Canvas](https://developer.mozilla.org/ko/docs/Web/API/Canvas_API)와 [WebGL API](https://developer.mozilla.org/ko/docs/Web/API/WebGL_API)로 애니메이션을 적용한 2D와 3D 그래픽을 만들 수 있습니다. 

        

      - [`HTMLMediaElement`](https://developer.mozilla.org/ko/docs/Web/API/HTMLMediaElement)와 [`WebRTC`](https://developer.mozilla.org/ko/docs/Web/API/WebRTC_API)를 포함하는 [오디오와 비디오 API](https://developer.mozilla.org/ko/docs/Web/Guide/Audio_and_video_delivery)로는 멀티미디어를 사용한 흥미로운 일을 할 수 있습니다. 예를 들어 오디오나 비디오를 웹 페이지에서 바로 재생하거나, 웹캠으로 비디오를 찍어 다른 사람의 화면에 보여줄 수 있습니다.

      

    -  **서드파티 API**는 브라우저에 탑재되지 않은 API로, 웹의 어딘가에서 직접 코드와 정보를 찾아야 합니다.

      - [Twitter API](https://developer.twitter.com/en/docs)로 여러분의 최신 트윗을 웹 사이트가 보여주도록 구현할 수 있습니다.

      - [Google 지도 API](https://developers.google.com/maps/)와 [OpenStreetMap API](https://wiki.openstreetmap.org/wiki/API)로 웹 사이트에 지도를 삽입하고, 지도 관련 기능을 추가할 수 있습니다.

- ETC



---

## 웹 페이지에서 JavaScript는 어떤 일을 하나요?

 웹 페이지를 브라우저로 불러오면, 브라우저는  코드(HTML, CSS, JavaScript)를 실행 환경(브라우저 탭)에서 실행합니다. 원자재(코드)를 가져와서 상품(웹 페이지)을 생산하는 공장처럼 생각할 수 있습니다. [이미지 참고](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript/execution.png)



### 브라우저 보안

각각의 브라우저 탭은 코드를 실행하기 위한 독립적인 그릇(기술 용어로 "실행 환경"이라고 부릅니다)입니다. 

독립적이라는 것은 대부분의 탭이 서로에게서 완전히 분리되어 한 탭의 코드가 다른 탭의 코드, 또는 다른 사이트에 직접적인 영향을 줄 수 없다는 뜻입니다. 



---

### JavaScript 실행 순서

브라우저가 JavaScript 블록을 마주치면, 일반적으로는  위에서 아래로 실행합니다. 따라서 코드 배치 순서에도 주의를 기울여야 합니다.

예를 들기 위해 맨 위의 첫 예제 코드로 돌아가봅시다.

```JAVA
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```

위 코드는 텍스트 문단을 선택(1번 줄)해서 이벤트 수신기를 부착(3번 줄)하여, 사용자가 문단을 클릭하면 `updateName()` 코드 블록(5번 ~ 8번 줄)을 실행하도록 합니다. `updateName()` 코드 블록(이렇게 재사용 가능하도록 나눠놓은 코드 블록을 "함수"라고 합니다)은 사용자에게 새로운 이름을 물어보고, 그 이름을 문단에 삽입해서 화면을 업데이트합니다.

만약 1번 줄의 코드와 3번 줄의 코드 순서를 서로 바꿔서 실행했으면 원하는 동작 대신 [브라우저 개발자 콘솔 (en-US)](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools)에 오류, `TypeError: para is undefined`가 나타나며, `para` 객체가 아직 존재하지 않으므로 이벤트 수신기를 부착할 수도 없다는 뜻입니다.

---

### 인터프리터와 컴파일러

- 프로그래밍에서의 **인터프리터**와 **컴파일러**라는 단어를 들어본 적이 있는지 생각해보세요. 인터프리터를 사용하는 언어에서는 코드를 위에서 아래로 실행하고, 코드 구동 결과는 즉시 반환됩니다. 브라우저에서 JavaScript 코드를 실행하기 전에 다른 형태로 변환할 필요가 없다는 점을 기억하세요. 코드는 프로그래머가 읽을 수 있는 형태로 입력되고, 별도의 처리 없이 그대로 실행됩니다.

  

  

- **반면**, 컴파일러를 사용하는 컴파일 언어에서는 컴퓨터가 코드를 실행하기 전에 다른 형태로 변환(컴파일)해야 합니다. 예를 들어, C/C++에서는 코드를 컴파일러로 기계언어로 변환하여, 그 결과를 컴퓨터가 실행합니다. 프로그램은 프로그램의 원본 소스 코드에서 생성한 이진 형식(바이너리)으로부터 실행됩니다.

JavaScript는 가볍고, 인터프리터를 사용하는 프로그래밍 언어입니다. 

웹 브라우저는 JavaScript 코드를 원문 텍스트 형식으로 입력받아 실행합니다.

 기술적인 측면으로 따지자면, 대부분의 모던 JavaScript 인터프리터들은 사실 **JIT 컴파일**(just-in-time 컴파일)이라는 기술을 사용해 성능을 향상하기는 합니다.

 스크립트의 실행과 동시에 소스 코드를 더 빠르게 실행할 수 있는 이진 형태로 변환하여 최대한 높은 실행 속도를 얻는 방법입니다. 하지만 JavaScript는 여전히 인터프리터 언어로 분류됩니다.

 컴파일을 먼저 해놔야 하는 것이 아니라 런타임에 일어나기 때문입니다.

---

### 동적 코드와 정적 코드

클라이언트 사이드 JavaScript와 서버 사이드 언어들 모두 **동적**이라는 단어로 설명할 수 있습니다. 

동적인 이유는 웹 페이지/웹 앱의 서로 다른 상황에 서로 다른 화면을 보여줄 수 있고, 필요하면 새로운 콘텐츠를 생성할 수 있기 때문입니다.



 **서버 사이드 코드**는 서버에서 새로운 콘텐츠를 생성 데이터베이스에서 데이터를 가져오는 등  

**클라이언트 사이드 JavaScript는** 클라이언트의 브라우저 내에서 새로운 콘텐츠를 생성 

새로운 HTML 표를 생성하고, 서버에서 받아온 데이터로 채운 후, 사용자가 보고 있는 웹 페이지에 표시 합니다. 두 맥락 내에서 '동적'이라는 단어의 정확한 뜻은 약간 다르지만, 그럼에도 서로 연관되어 있으며, 두 방법(서버와 클라이언트 사이드)을 보통 함께 사용합니다.



---

## - [웹 페이지에 JavaScript를 넣는 방법](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript#웹_페이지에_javascript를_어떻게_넣나요)

### - [외부 JavaScript](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/What_is_JavaScript#외부_javascript) JavaScript를 외부 파일로 분리하고 싶을때



---

## 주석

HTML 및 CSS와 동일하게, JavaScript에서도 브라우저는 무시하는 주석을 작성해서 다른 개발자들에게 안내를 제공할 수 있습니다. 



주석에는 두 종류가 있습니다.

1. 한 줄 짜리 주석은 맨 앞에 이중 빗금(//)으로 작성합니다.

```
// 나, 주석
```

2. 여러 줄 주석은 /*과 */의 사이에 작성합니다.

   ```
   /*
     나 또한
     주석
   */
   ```



# 2. 문법과 자료형

JavaScript는 문법의 대부분을 Java와 C, C++로부터 차용하고 있으며, Awk, Perl, Python의 영향도 받았습니다.

JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용합니다. 예를 들면, Früh(독일어로 "이른")을 변수명으로 사용할 수도 있습니다.

```java
var 갑을 = "병정";
var Früh = "foobar";
```

- JavaScript에서는 명령을 [명령문(statement) (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Statement)이라고 부르며, 세미콜론(;)으로 구분합니다.

​	-  **명령문이 한 줄을 다 차지할 경우**에는 세미콜론이 필요하지 않습니다. 

​	- 그러나 **한 줄에 두 개 이상의 명령문이 필요**하다면 **반드시 세미콜론**으로 구분해야 합니다.

*** ** **하지만**, 세미콜론이 필요하지 않은 경우라도 항상 세미콜론으로 끝마치는 편이 버그 예방 차원에서 더 좋은 습관이라고 여겨집니다.

- JavaScript의 스크립트 소스는 왼쪽에서 오른쪽으로 탐색하면서 토큰, 제어 문자, 줄바꿈 문자, 주석이나 공백 으로 이루어진 입력 요소의 시퀀스로 변환됩니다.



---



## [선언](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#선언)

JavaScript의 선언에는 3가지 방법이 있습니다.

- [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var)

  변수를 선언. 추가로 동시에 값을 초기화.

- [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let)

  블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화.

- [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const)

  블록 스코프 읽기 전용 상수를 선언.

---



### [변수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수)

애플리케이션에서 값에 상징적인 이름으로 변수를 사용합니다. 변수명은 [식별자(identifiers)](https://developer.mozilla.org/ko/docs/Glossary/Identifier)라고 불리며 특정 규칙을 따릅니다.

​	JavaScript 식별자는 문자, 밑줄 (`_`) 혹은 달러 기호 (`$`)로 시작해야 하는 반면 이후는 숫자 (`0`–`9`) 일 	수도 있습니다.

​	JavaScript가 대소문자를 구분하기에, 문자는 "`A`"부터 "`Z`" (대문자)와 "`a`"부터 "`z`" (소문자)까지 모	두 포함합니다.

### [변수 선언](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_선언)

변수 선언은 아래 3가지 방법으로 가능합니다.

- `var x = 42`와 같이 [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var) 키워드로 변수를 선언할 수 있습니다. 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있습니다.
- `let y = 13`와 같이 [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 혹은 [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let) 키워드로 변수를 선언할 수 있습니다. 이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있습니다. 아래 [변수 스코프](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_스코프)를 참고하세요.

### [변수 할당](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_할당)

지정된 초기 값 없이 `var` 혹은 `let` 문을 사용해서 선언된 변수는 [`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined) 값을 갖습니다.

선언되지 않은 변수에 접근을 시도하는 경우 [`ReferenceError`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError) 예외가 발생합니다.

### [변수 스코프](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_스코프)

어떤 함수의 바깥에 변수를 선언하면, 현재 문서의 다른 코드에 해당 변수를 사용할 수 있기에 전역 변수라고 합니다. 만약 함수 내부에 변수를 선언하면, 오직 그 함수 내에서만 사용할 수 있기에 지역 변수라고 부릅니다.



### [변수 호이스팅](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#변수_호이스팅)

또 다른 JavaScript 변수의 특이한 점은 예외를 받지 않고도, 나중에 선언된 변수를 참조할 수 있다는 것입니다.

이 개념은 **호이스팅**(hoisting)으로 알려져 있습니다. 즉 JavaScript 변수가 어떤 의미에서 함수나 문의 최상단으로 "올려지는" (혹은 "끌어올려지는") 것을 말합니다. 하지만, 끌어올려진 변수는 `undefined` 값을 반환합니다. 그래서 심지어 이 변수를 사용 혹은 참조한 후에 선언 및 초기화하더라도, 여전히 `undefined`를 반환합니다.

---

## [데이터 구조 및 형](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#데이터_구조_및_형)

### [데이터 형](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#데이터_형)

최신 ECMAScript 표준은 8가지 데이터 형을 정의합니다.

- 7가지 원시 데이터 형
  1. [Boolean](https://developer.mozilla.org/ko/docs/Glossary/Boolean). `true`와 `false`
  2. [null](https://developer.mozilla.org/ko/docs/Glossary/Null). null 값을 나타내는 특별한 키워드. (JavaScript는 대소문자를 구분하므로, `null`은 `Null`, `NULL` 혹은 다른 변형과도 다릅니다.)
  3. [undefined](https://developer.mozilla.org/ko/docs/Glossary/undefined). 값이 정의되어 있지 않은 최상위 속성.
  4. [Number (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Number). 정수 또는 실수형 숫자. 예: `42` 혹은 `3.14159`.
  5. [BigInt (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/BigInt). 임의 정밀도의 정수. 예: `9007199254740992n`.
  6. [String](https://developer.mozilla.org/ko/docs/Glossary/String). 문자열. 예:"안녕"
  7. [Symbol](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Symbol). (ECMAScript 2015에 도입) 인스턴스가 고유하고 불변인 데이터 형.
- 그리고 [Object](https://developer.mozilla.org/ko/docs/Glossary/Object)

---

### [자료형 변환](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#자료형_변환)

JavaScript는 동적 형지정(정형) 언어입니다. 이는 변수를 선언할 때 데이터 형을 지정할 필요가 없음을 의미합니다. 또한 데이터 형이 스크립트 실행 도중 필요에 의해 자동으로 변환됨을 뜻합니다.

### [숫자와 '+' 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#숫자와_연산자)

숫자와 문자열 값 사이에 `+` 연산자를 포함한 식에서, JavaScript는 숫자 값을 문자열로 변환합니다.

## [리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#리터럴)

JavaScript에서 값을 나타내기 위해 리터럴을 사용합니다. 이는 말 그대로 스크립트에 부여한 고정 값으로, 변수가 아닙니다. 

- [배열 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#배열_리터럴)
- [불리언 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#불리언_리터럴)
- [부동 소수점 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#부동_소수점_리터럴)
- [숫자 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#숫자_리터럴)
- [객체 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#객체_리터럴)
- [정규식 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#정규식_리터럴)
- [문자열 리터럴](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Grammar_and_types#문자열_리터럴)

#### 문자열에서 특수 문자 사용

보통 문자에 더해서, 문자열에 아래 예제와 같이 특수 문자도 포함할 수 있습니다.

| 문자          | 뜻                                                           |
| :------------ | :----------------------------------------------------------- |
| `\0`          | Null Byte                                                    |
| `\b`          | Backspace                                                    |
| `\f`          | Form feed                                                    |
| `\n`          | New line                                                     |
| `\r`          | Carriage return                                              |
| `\t`          | Tab                                                          |
| `\v`          | Vertical tab                                                 |
| `\'`          | Apostrophe 혹은 작은 따옴표                                  |
| `\"`          | 큰 따옴표                                                    |
| `\\`          | 백슬래시                                                     |
| `\*XXX*`      | Latin-1 인코딩 문자는 `0` - `377` 사이 8진수 3자리 *XXX*까지 지정될 수 있습니다. 예를 들어, `\251`은 copyright 심볼을 표현하는 8진수 시퀀스입니다. |
| `\x*XX*`      | Latin-1 인코딩 문자는 `00` - `FF` 사이의 16진수 2자리 *XX*로 지정될 수 있습니다. 예를 들어, `\xA9`는 copyright 심볼을 표현하는 16진수 시퀀스입니다. |
| `\u*XXXX*`    | 유니코드 문자는 16진수 4자리 *XXXX*로 지정될 수 있습니다. 예를 들어, `\u00A9`는 copyright 심볼을 표현하는 유니코드 시퀀스입니다. [Unicode escape sequences](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Lexical_grammar#string_literals)를 참고하세요. |
| `\u*{XXXXX}*` | 유니코드 코드 포인트 이스케이프. 예를 들어, `\u{2F804}`는 간단한 유니코드 이스케이프 `\uD87E\uDC04`와 같습니다. |

#### 문자 이스케이프

표에 없는 문자의 경우 전행 백슬래시는 무시되지만, 이 용법은 더 이상 사용되지 않으며, 사용을 피해야 합니다.

---

# 3.제어 흐름과 오류 처리

JavaScript는 애플리케이션에 다양한 상호작용을 추가하기 위한 일련의 명령문, 특히 제어 흐름 명령문을 지원합니다. 

모든 JavaScript 표현식은 명령문 입니다.

---



## [블록문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#블록문)

가장 기본적인 명령문은, 명령문들을 그룹으로 묶을 수 있는 **블록문**입니다. 블록문의 블록은 한 쌍의 중괄호로 감싸는 것으로 나타냅니다.



## [조건문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#조건문)

조건문은 지정한 조건이 참인 경우에 실행하는 명령 집합입니다. JavaScript는 `if...else`와 `switch` 두 종류의 조건문을 지원합니다.

### [`if...else` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#if...else_문)

명령문을 논리 조건이 참일 때 실행하려면 `if` 문을 사용하세요. 선택적으로, `else` 절을 추가해서 조건이 거짓인 경우에 실행할 명령문을 지정할 수 있습니다.

`if` 문의 형태는 다음과 같습니다.

```
if (condition) {
  statement_1;
} else {
  statement_2;
}
```

Copy to Clipboard

위 코드에서, `condition`에는 `true`나 `false`로 평가할 수 있는 아무 표현식이나 대입할 수 있습니다.

#### 거짓 값

다음 값은 `false`로 평가됩니다. ([거짓](https://developer.mozilla.org/ko/docs/Glossary/Falsy) 값이라고 부릅니다)

- `false`
- `undefined`
- `null`
- `0`
- `NaN`
- 빈 문자열 (`""`)

객체를 포함해 다른 모든 값은 조건문에 전달했을 때 `true`로 평가됩니다.



### [`switch` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#switch_문)

`switch` 문은 프로그램이 표현식을 평가한 후, 그 값과 `case` 레이블의 값을 비교해 일치하는 `case`의 명령문을 실행합니다.

#### break 문

각각의 `case`에는 선택적으로 `break` 문을 추가할 수 있습니다. `break`는 `case`의 명령문을 실행한 후에 프로그램이 `switch`의 밖으로 나가도록 합니다. `break`를 생략하면 프로그램은 `switch` 문을 탈출하지 않고, 다음 `case`의 명령문을 실행합니다.

## [예외 처리 명령문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#예외_처리_명령문)

`throw` 문을 사용하면 예외를 던질 수 있고, 던진 예외는 `try...catch` 문으로 처리할 수 있습니다.

- [`throw` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#throw_문)
- [`try...catch` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#try...catch_문)

### [예외 유형](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#예외_유형)

JavaScript에서는 모든 것을 `throw`로 던질 수 있습니다. 그래서 숫자나 문자열을 오류로 던지는 경우도 많지만, 예외를 나타내기 위해 사전에 정의된 예외 유형을 쓰는 것이 보통 더 효과적입니다.

- [ECMAScript 예외](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Error#오류_유형)
- [DOMException (en-US)](https://developer.mozilla.org/en-US/docs/Web/API/DOMException), [DOMError (en-US)](https://developer.mozilla.org/en-US/docs/Web/API/DOMError)

### [`throw` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#throw_문)

예외를 던질 땐 `throw` 문을 사용하세요. `throw`에 던질 값을 지정하면 됩니다.

```
throw expression;
```

Copy to Clipboard

특정 타입의 표현식이 아니라 무엇이든 던질 수 있습니다. 아래 코드에서 다양한 타입을 예외로 던지는 모습을 볼 수 있습니다.



### [`try...catch` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Control_flow_and_error_handling#try...catch_문)

`try...catch` 문은 실행을 시도할 블록을 표시하고, 그 안에서 예외가 발생할 경우 처리를 맡을 하나 이상의 반응 명령문을 지정합니다. 예외가 발생하면, `try...catch` 문이 잡아냅니다.



`try...catch` 문은 하나 이상의 명령문을 포함하는 `try` 블록, 그리고 `try`에서 예외가 발생할 경우 그 예외를 처리할 명령문을 담은 하나의 `catch` 블록으로 구성합니다.



다르게 설명해보면, `try...catch`는 성공하길 바라는 코드(`try` 블록)가 만약 실패하면 `catch`로 제어권을 넘겨야 할 때 사용합니다. `try` 블록의 명령문 중 하나에서 예외를 던지면, 실행 제어권은 그 즉시 `catch` 블록으로 넘어갑니다. `try` 블록 내에서 예외가 발생하지 않았으면 `catch` 블록은 실행되지 않습니다.

#### `catch` 블록

`try` 블록에서 발생할 수 있는 모든 예외는 `catch` 블록에서 처리할 수 있습니다.

```
catch (catchID) {
  statements;
}
```

Copy to Clipboard

`catch` 블록은 `throw` 명령문이 던진 예외의 값을 담을 식별자(위 코드 블록에서는 `catchID`)를 지정합니다. 이 식별자를 통해, 발생한 예외의 정보를 알아낼 수 있습니다.

JavaScript는 `catch` 블록에 진입해야 예외의 식별자를 생성하고, `catch` 블록의 밖으로 나가면 식별자를 더 이상 유지하지 않습니다. 즉, `catch` 블록의 실행이 끝나면 예외 식별자에 접근할 수 없습니다.



#### `finally` 블록

`finally` 블록은 `try`와 `catch` 블록 실행이 끝난 후 이어서, 그리고 `try...catch...finally` 문 이후의 명령문들보다는 먼저 실행할 명령문을 담습니다.

`finally` 블록은 `try` 블록 안에서 예외가 발생했는지 여부에 관계 없이, `catch` 블록이 따로 존재하지 않더라도 항상 실행됩니다.

`finally` 블록을 활용하면 예외가 발생했을 때 프로그램이 우아하게 실패하도록 방어할 수 있습니다. 예를 들어, 예외의 발생 여부를 따지지 않고 스크립트가 점유한 리소스를 해제해야 할 때 사용하세요.

#### try...catch 문 중첩하기

`try...catch` 문을 하나 이상 중첩할 수 있습니다.

안쪽 `try` 블록이 `catch` 블록을 가지지 않을 경우,

1. 이 `try` 블록에는 반드시 `finally` 블록이 있어야 합니다.
2. 바깥 `try...catch` 문의 `catch` 블록이 안쪽 예외를 처리하게 됩니다.



---



# 4.루프와 반복

루프는 어떤 것을 반복적으로 시행할때 빠르고 간편한 방법을 제공합니다.

예를들어, "동쪽으로 5만큼 가세요"는 다음과 같이 반복문으로 표현 될 수 있습니다.

```
var step;
for (step = 0; step < 5; step++) {
  // Runs 5 times, with values of step 0 through 4.
  console.log('Walking east one step');
}
```

Copy to Clipboard

반복문은 매우 다양한 종류가 있습니다. 하지만 반복문이 기본적으로 하는일은 모두 같습니다. 반복문은 한 동작을 여러 번 반복합니다. (사실 0회 반복하는 것도 가능합니다.) 다양한 반복문 메커니즘은 다양한 방법으로 반복문의 시작점과 끝나는 점을 정할 수 있습니다.

자바스크립트가 지원하는 반복문은 다음과 같습니다:

- [for 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#for_문)
- [do...while 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#do...while_문)
- [while 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#while_문)
- [레이블 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#레이블_문)
- [break 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#break_문)
- [continue 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#continue_문)
- [for...in 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#for...in_문)
- [for...of 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#for...of_문)

## [`for` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#for_문)

for 반복문은 어떤 특정한 조건이 거짓으로 판별될 때까지 반복합니다. 자바스크립트의 반복문은 C의 반복문과 비슷합니다. for 반복문은 다음과 같습니다.

```
    for ([초기문]; [조건문]; [증감문])
      문장
```

for문이 실행될 때, 다음과 같이 실행됩니다.:

1. 초기화 구문인 초기문이 존재한다면 초기문이 실행됩니다. 이 표현은 보통 1이나 반복문 카운터로 초기 설정이 됩니다. 그러나 복잡한 구문으로 표현 될 때도 있습니다. 또한 변수로 선언 되기도 합니다.
2. 조건문은 조건을 검사합니다. 만약 조건문이 참이라면, 그 반복문은 실행됩니다. 만약 조건문이 거짓이라면, 그 for문은 종결됩니다. 만약 그 조건문이 생략된다면, 그 조건문은 참으로 추정됩니다.
3. 문장이 실행됩니다. 많은 문장을 실행할 경우엔, { } 를 써서 문장들을 묶어 줍니다.
4. 갱신 구문인 증감문이 존재한다면 실행되고 2번째 단계로 돌아갑니다.



## [`do...while` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#do...while_문)

do...while 문은 특정한 조건이 거짓으로 판별될 때까지 반복합니다. do...while 문은 다음과 같습니다.

```
    do
      문장
    while (조건문);
조건문을 확인하기 전에 문장은 한번 실행됩니다. 많은 문장을 실행하기 위해선 { }를 써서 문장들을 묶어줍니다. 만약 조건이 참이라면, 그 문장은 다시 실행됩니다. 매 실행 마지막마다 조건문이 확인됩니다. 만약 조건문이 거짓일 경우, 실행을 멈추고 do...while 문 바로 아래에 있는 문장으로 넘어가게 합니다.
```

## [`while` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#while_문)

while 문은 어떤 조건문이 참이기만 하면 문장을 계속해서 수행합니다. while 문은 다음과 같습니다.

```
    while (조건문)
      문장
```

만약 조건문이 거짓이 된다면, 그 반복문 안의 문장은 실행을 멈추고 반복문 바로 다음의 문장으로 넘어갑니다.

조건문은 반복문 안의 문장이 실행되기 전에 확인 됩니다. 만약 조건문이 참으로 리턴된다면, 문장은 실행되고 그 조건문은 다시 판별됩니다. 만약 조건문이 거짓으로 리턴된다면, 실행을 멈추고 while문 바로 다음의 문장으로 넘어가게 됩니다.





## [레이블 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#레이블_문)

[레이블](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)은 여러분이 프로그램에서 다른 곳으로 참조할 수 있도록 식별자로 문을 제공합니다. 예를 들어, 여러분은 루프를 식별하기 위해 레이블을 사용하고, 프로그램이 루프를 방해하거나 실행을 계속할지 여부를 나타내기 위해 break나 continue 문을 사용할 수 있습니다.





## [`break` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#break_문)

break문은 반복문, switch문, 레이블 문과 결합한 문장을 빠져나올 때 사용합니다.

- 레이블 없이 break문을 쓸 때: 가장 가까운 `while`, `do-while`, `for`, 또는 `switch`문을 종료하고 다음 명령어로 넘어갑니다.
- 레이블 문을 쓸 때: 특정 레이블 문에서 끝납니다.

break문의 문법은 다음과 같습니다.

1. `break;`
2. `break [레이블];`

break문의 첫번째 형식은 가장 안쪽의 반복문이나 switch문을 빠져나옵니다. 두번째 형식는 특정한 레이블 문을 빠져나옵니다.





## [continue 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#continue_문)

[`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue) 문은 while, do-while, for, 레이블 문을 다시 시작하기 위해 사용될 수 있습니다.

- 레이블없이 continue를 사용하는 경우, 그것은 가장 안쪽의 while, do-while, for 문을 둘러싼 현재 반복을 종료하고, 다음 반복으로 루프의 실행을 계속합니다. break문과 달리, continue 문은 전체 루프의 실행을 종료하지 않습니다. while 루프에서 그것은 다시 조건으로 이동합니다. for 루프에서 그것은 증가 표현으로 이동합니다.
- 레이블과 함께 continue를 사용하는 경우, continue는 그 레이블로 식별되는 루프 문에 적용됩니다.

continue 문의 구문은 다음과 같습니다:

1. `continue;`
2. `continue`*`label;`*

## [`for...in` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#for...in_문)

[`for...in`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) 문은 객체의 열거 속성을 통해 지정된 변수를 반복합니다. 각각의 고유한 속성에 대해, JavaScript는 지정된 문을 실행합니다. for...in 문은 다음과 같습니다:

```
for (variable in object) {
  statements
}
```



### [**배열**](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#배열)

`배열` 요소를 반복하는 방법으로 이를 사용하도록 유도될 수 있지만, **for...in** 문은 숫자 인덱스에 추가하여 사용자 정의 속성의 이름을 반환합니다. 따라서 만약 여러분이 사용자 정의 속성 또는 메서드를 추가하는 등 Array 객체를 수정한다면, 배열 요소 이외에도 사용자 정의 속성을 통해 **for...in** 문을 반복하기 때문에, 배열을 통해 반복할 때 숫자 인덱스와 전통적인 [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for) 루프를 사용하는 것이 좋습니다.

## [`for...of` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Loops_and_iteration#for...of_문)

[`for...of`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of) 문은 각각의 고유한 특성의 값을 실행할 명령과 함께 사용자 지정 반복 후크를 호출하여, [반복 가능한 객체](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/iterable)(`배열`, [`Map` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), [`Set`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set), [인수](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions_and_function_scope/arguments) 객체 등을 포함)를 통해 반복하는 루프를 만듭니다.

---



# 5. 함수

함수는 JavaScript에서 기본적인 구성 블록 중의 하나입니다. 함수는 작업을 수행하거나 값을 계산하는 문장 집합 같은 자바스크립트 절차입니다. 함수를 사용하려면 함수를 호출하고자 하는 범위 내에서 함수를 정의해야만 합니다.

세부 사항에 대해서는 [exhaustive reference chapter about JavaScript functions](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions)를 참조하세요.

## [함수 정의](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#함수_정의)

### [함수 선언](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#함수_선언)

함수 정의(또는 함수 선언)는 다음과 같은 [`함수`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/function) 키워드로 구성되어 있습니다:

- 함수의 이름
- 괄호 안에서 쉼표로 분리된 함수의 매개변수 목록
- 중괄호 `{ }` 안에서 함수를 정의하는 자바스크립트 표현

### [함수 표현식](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#함수_표현식)

위에서 함수 선언은 구문적인 문(statement)이지만, **함수 표현식(** [function expression](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/function)**)**에 의해서 함수가 만들어 질 수도 있습니다. 이 같은 함수를 **익명**이라고 합니다. 이 말은 모든 함수가 이름을 가질 필요는 없다는 것을 뜻합니다.



## [함수 호출](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#함수_호출)

함수를 정의하는 것은 함수를 실행하는 것이 아닙니다. 함수를 정의하는 것은 간단히 함수의 이름을 지어주고, 함수가 호출될 때 무엇을 할지 지정 해주는 것입니다. 사실 함수를 **호출**하는 것은 나타나있는 매개변수를 가지고 지정된 행위를 수행하는 것입니다. 예를 들어, 만약 여러분이 함수 `square`를 정의한다면, 함수를 다음과 같이 호출할 수 있습니다.

```java
square(5);
```

Copy to Clipboard

위의 문장은 5라는 인수를 가지고 함수를 호출합니다. 함수는 이 함수의 실행문을 실행하고 값 25를 반환합니다.

함수는 호출될 때 범위 내에 있어야 합니다. 그러나 함수의 선언은 이 예에서와 같이, 호이스팅 될 수 있습니다. (코드에서 호출 아래에 선언문이 있습니다.):

```java
console.log(square(5));
/* ... */
function square(n) { return n*n }
```

Copy to Clipboard

함수의 범위는 함수가 선언된 곳이거나, 전체 프로그램 에서의 최상위 레벨(전역)에 선언된 곳입니다.

## [함수의 범위](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#함수의_범위)

함수 내에서 정의된 변수는 변수가 함수의 범위에서만 정의되어 있기 때문에, 함수 외부의 어느 곳에서든 액세스할 수 없습니다. 그러나, 함수가 정의된 범위 내에서 정의된 모든 변수나 함수는 액세스할 수 있습니다. 즉, 전역함수는 모든 전역 변수를 액세스할 수 있습니다. 다른 함수 내에서 정의 된 함수는 부모 함수와 부모 함수가 액세스 할 수 있는 다른 변수에 정의된 모든 변수를 액세스할 수 있습니다.

## [범위와 함수 스택](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#범위와_함수_스택)





### [재귀](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#재귀)

함수는 자신을 참조하고 호출할 수 있습니다. 함수가 자신을 참조하는 방법은 세 가지가 있습니다.

1. 함수의 이름

2. [`arguments.callee`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/arguments/callee)

3. 함수를 참조하는 범위 내 변수

   예를 들어, 다음 함수의 정의를 고려해보세요.

   ```java
   var foo = function bar() {
      // statements go here
   };
   ```

함수 본문 내에서 다음은 모두 동일합니다.

1. `bar()`
2. `arguments.callee()`
3. `foo()`

자신을 호출하는 함수를 *재귀 함수*라고 합니다. 어떤 면에서, 재귀는 루프와 유사합니다. 둘 다 동일한 코드를 여러 번 실행하고, 조건(무한 루프를 방지하거나, 이 경우에는 오히려 무한 재귀하는)을 요구합니다.

### [중첩된 함수와 클로저](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#중첩된_함수와_클로저)

- 내부 함수는 외부 함수의 명령문에서만 액세스할 수 있습니다.

- 내부 함수는 클로저를 형성합니다: 외부 함수는 내부 함수의 인수와 변수를 사용할 수 없는 반면에, 내부 함수는 외부 함수의 인수와 변수를 사용할 수 있습니다.

### [변수의 보존](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#변수의_보존)

- 중첩된 내부 함수가 반환될 때 외부 함수의 인수 `x`가 보존된다는 점을 알 수 있습니다. 

- 클로저는 그것을 참조하는 모든 범위에서 인수와 변수를 보존해두어야 합니다. 

- 매번 호출될 때마다 잠재적으로 다른 인수를 제공할 수 있기 때문에, 클로저는 외부 함수에 대하여 매번 새로 생성됩니다. 메모리는 그 무엇도 내부 함수에 접근하지 않을 때만 해제됩니다.

- 변수의 보존은 일반 객체에서 참조를 저장해두는 것과 다르지 않지만, 사용자가 직접 참조를 설정하는 것이 아니고 자세히 들여다볼 수 없어서 종종 명확하지 않습니다.



### [다중 중첩 함수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#multiply-nested_functions)

함수는 다중 중첩될 수 있습니다. 

즉, 함수 (C)를 포함하는 함수 (B)를 포함하는 함수 (A) 여기에서 두 함수 B와 C는 모두 클로저를 형성합니다. 

그래서 B는 A를 엑세스할 수 있고, C는 B를 액세스 할 수 있습니다. 이와 같이, 클로저는 다중 범위를 포함 할 수 있습니다; 그들은 재귀적으로 그것을 포함하는 함수의 범위를 포함합니다.



### [이름 충돌](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#이름_충돌)

클로저의 범위에서 두 개의 인수 또는 변수의 이름이 같은 경우, *이름 충돌*이 있습니다. 더 안쪽 범위가 우선순위를 갖습니다. 그래서 가장 바깥 범위는 우선순위가 가장 낮은 반면에, 가장 안쪽 범위는 가장 높은 우선순위를 갖습니다. 이것이 범위 체인(scope chaini)입니다. 체인에서 첫번째는 가장 안쪽 범위이고, 마지막은 가장 바깥 쪽의 범위입니다. 다음 사항을 고려하세요:

```javascript
function outside() {
  var x = 10;
  function inside(x) {
    return x;
  }
  return inside;
}
result = outside()(20); // returns 20 instead of 10
```



이름 충돌이 x를 반환하는 문과 내부의 매개 변수 x와 외부 변수 x 사이에서 발생합니다. 여기에서 범위 체이닝은 {내부, 외부, 전역 객체}입니다. 따라서 내부의 x는 외부의 x보다 높은 우선순위를 갖게 되고, 20(내부의 x)이 10(외부의 x) 대신에 반환됩니다.





## [클로저](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#클로저)

클로저는 자바스크립트의 강력한 기능 중 하나입니다. 자바스크립트는 함수의 중첩(함수 안에 함수를 정의하는것)을 허용하고, 내부함수가 외부 함수 안에서 정의된 모든 변수와 함수들을 완전하게 접근 할 수 있도록 승인해줍니다.(그리고 외부함수가 접근할수 있는 모든 다른 변수와 함수들까지) 그러나 외부 함수는 내부 함수 안에서 정의된 변수와 함수들에 접근 할 수 없습니다. 이는 내부 함수의 변수에 대한 일종의 캡슐화를 제공합니다. 또한, 내부함수는 외부함수의 범위에 접근할 수 있기 때문에, 내부 함수가 외부 함수의 수명을 초과하여 생존하는 경우, 외부함수에서 선언된 변수나 함수는 외부함수의 실행 기간보다 오래갑니다. 클로저는 내부 함수가 어떻게든 외부 함수 범위 밖의 모든 범위에서 사용 가능해지면 생성됩니다.

```java
var pet = function(name) {   // 외부 함수는 'name'이라 불리는 변수를 정의합니다.
  var getName = function() {
    return name;             // 내부 함수는 외부 함수의 'name' 변수에 접근합니다.
  }
  return getName;            // 내부 함수를 리턴함으로써, 외부 범위에 노출됩니다.
},
myPet = pet("Vivie");

myPet();                     // "Vivie"로 리턴합니다.
```

## [화살표 함수](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#화살표_함수)

[화살표 함수 표현](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) (**뚱뚱한 화살표(fat arrow) 함수라고 알려진**)은 함수 표현과 비교하였을때 짧은 문법을 가지고 있고 사전적으로 this 값을 묶습니다. 화살표 함수는 언제나 익명입니다

## [미리 정의된 함수들](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Functions#미리_정의된_함수들)

자바스크립트에는 최고 등급의 몇가지 내장함수가 있습니다:

- [`eval()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/eval)

  **`eval()`** 메소드는 문자열로 표현된 자바스크립트 코드를 수행합니다.

- [`uneval()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Deprecated_and_obsolete_features) Non-standard

  **`uneval()`** 메소드는 [`Object`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object)의 소스코드를 표현하는 문자열을 만듭니다.

- [`isFinite()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/isFinite)

  전역 **`isFinite()`** 함수는 전달받은 값이 유한한지 결정합니다. 만약 필요하다면, 매개변수는 첫번째로 숫자로 변환됩니다.

- [`isNaN()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/isNaN)

  **`isNaN()`** 함수는 [`NaN`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/NaN)인지 아닌지 결정합니다. Note: `isNaN` 함수 안의 강제 변환은 [흥미로운](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/isNaN#Description) 규칙을 가지고 있습니다; [`Number.isNaN()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Number/isNaN)을 대신 사용하고 싶을것입니다, ECMAScript 6 에서 정의된,또는 값이 숫자값이 아닐때, [`typeof`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) 를 사용할 수도 있습니다 .

- [`parseFloat()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseFloat)

  **`parseFloat()`** 함수는 문자열 인수 값을 해석하여 부동소숫점 수를 반환합니다.

- [`parseInt()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/parseInt)

  **`parseInt()`** 함수는 문자열 인수 값을 해석하여 특정한 진법의 정수를 반환합니다 (수학적 수 체계를 기반으로 해서).

- [`decodeURI()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)

  **`decodeURI()`** 함수는 사전에 [`encodeURI`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)을 통해 만들어지거나 비슷한 과정을 통해 만들어진 URI(Uniform Resource Identifier) 를 해독합니다.

- [`decodeURIComponent()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)

  **`decodeURIComponent()`** 메소드는 사전에[`encodeURIComponent`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)를 통하여 만들어 지거나 또는 비슷한 과정을 통해 만들어진 URI (Uniform Resource Identifier) 컴포넌트를 해독합니다.

- [`encodeURI()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)

  **`encodeURI()`** 메소드는 URI(Uniform Resource Identifier)를 각 인스턴스의 특정한 문자를 한개, 두개,세개, 또는 네개의 UTF-8인코딩으로 나타내어지는 연속된 확장문자들과 바꾸는 방법으로 부호화 합니다 .(두"surrogate"문자로 구성된 문자들은 오직 네개의 연속된 확장문자 입니다. ).

- [`encodeURIComponent()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)

  **`encodeURIComponent()`** 메소드는 URI(Uniform Resource Identifier) 컴포넌트를 각 인스턴스의 특정한 문자를 한개, 두개,세개, 또는 네개의 UTF-8인코딩으로 나타내어지는 연속된 확장문자들과 바꾸는 방법으로 부호화 합니다 .(두"surrogate"문자로 구성된 문자들은 오직 네개의 연속된 확장문자 입니다. ).).

- [`escape()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/escape) Deprecated

  곧 사라질 **`escape()`** 메소드는 한 문자열에서 특정 문자들이 16진 확장 비트열로 바뀌어진 문자열로 계산합니다. [`encodeURI`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURI) 또는 [`encodeURIComponent`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) 를 사용하세요.

- [`unescape()` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/unescape) Deprecated

  곧 사라질 **`unescape()`** 메소드는 문자열에서 확장 비트열이 확장 비트열이 나타내는 문자로 바뀌어진 문자열로 계산합니다. [`escape` (en-US)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/escape)에서 확장 비트열이 소개될 것입니다. `unescape()` 메소드가 곧 사라지기 때문에, [`decodeURI()`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/decodeURI) or [`decodeURIComponent`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent) 를 대신 사용하세요.

# 6.표현식과 연산자



## [연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#연산자)

JavaScript의 연산자는 다음과 같은 유형으로 나눌 수 있습니다. 이 절은 각각의 연산자에 대해 설명하고, 연산자 우선순위에 관한 정보를 제공합니다.

- ### [할당 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#할당_연산자)

  할당 연산자는 오른쪽 피연산자의 값을 왼쪽 피연산자에 할당합니다. 기본적인 할당 연산자는 오른쪽의 피연산자 값을 왼쪽 피연산자 값에 할당하는 등호(`=`)로, `x = y` 는 `y`의 값을 `x`에 할당합니다.
  
- ### [비교 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#비교_연산자)

  비교 연산자는 피연산자를 서로 비교하고, 비교 결과가 참인지에 따라 논리 값을 반환합니다. 피연산자로는 숫자, 문자열, 논리형, [객체](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Working_with_Objects) 값을 사용할 수 있습니다. 문자열은 Unicode 값을 사용한 표준 사전식 순서에 따라 비교합니다. 만약 두 피연산자가 서로 다른 타입이면, JavaScript는 피연산자들을 서로 비교하기에 적합한 타입으로 변환합니다. 

  이 동작은 대개 두 값을 모두 숫자로 변환한 후 비교한 결과를 낳습니다. 비교 연산에서 발생하는 타입 변환의 유일한 예외는 `===`과 `!==` 연산자를 사용해 엄격 일치와 불일치 비교를 수행하는 경우인데, 두 연산자는 비교 전에 피연산자를 변환하지 않습니다. 

  ### 

- ### [산술 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#산술_연산자)

  산술 연산자는 두 개의 숫자 값(리터럴 또는 변수)을 피연산자로 받아서 하나의 숫자 값을 반환합니다. 표준 산술 연산자는 더하기(`+`), 빼기(`-`), 곱하기(`*`), 나누기(`/`)입니다. 이 연산자들은 대부분의 다른 프로그래밍 언어에서 부동소수점 값을 연산할 때와 동일하게 동작합니다. (0 으로 나눌 경우 [`Infinity`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Infinity)를 반환하는 것에 주의하세요)

  

- ### [비트 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#비트_연산자)

  비트 연산자는 피연산자를 10진수, 16진수, 8진수 숫자로 취급하지 않고, 대신 32개 비트의 집합으로 취급합니다. 예를 들어, 10진수 9는 2진수 1001로 나타냅니다. 비트 연산자는 이러한 이진법 표현에 대해 연산을 수행하지만, 반환할 땐 JavaScript 표준 숫자로 반환합니다.

  

- ### [논리 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#논리_연산자)

  논리 연산자는 보통 불리언(논리) 값과 함께 사용해서 불리언 값을 반환합니다. 그러나 `&&`와 `||` 연산자는 사실 두 피연산자 중 하나를 반환하는 것으로, 만약 둘 중 하나가 불리언 값이 아니라면 논리 연산자의 반환 값도 불리언 값이 아닐 수 있습니다. 

  

- ### [문자열 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#문자열_연산자)

  문자열에 사용할 수 있는 비교 연산자들 외에도, 문자열 연결(`+`) 연산자는 두 문자열의 값을 서로 연결한 새로운 문자열을 반환합니다.

  

- ### [조건 (삼항) 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#조건_삼항_연산자)

  [조건 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)는 JavaScript에서 세 개의 피연산자를 받는 유일한 연산자입니다. 조건 연산자는 주어진 조건에 따라 두 값 중 하나를 반환합니다.

  

- ### [쉼표 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#쉼표_연산자)

  [쉼표 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Comma_Operator)(`,`)는 두 피연산자를 모두 평가한 후 오른쪽 피연산자의 값을 반환합니다. 쉼표 연산자는 주로 `for` 반복문 안에서 사용하여 한 번의 반복으로 여러 변수를 변경할 때 사용합니다. 꼭 필요하지 않다면, 그 외의 상황에 사용하는 것은 좋지 않은 코드 스타일로 여겨집니다. 대개 쉼표 연산자보다는 두 개의 분리된 명령문을 사용하는 편이 낫습니다.

  

- ### [단항 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#단항_연산자)

  단항 연산은 오직 하나의 피연산자만 사용하는 연산입니다.

  

- ### [관계 연산자](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#관계_연산자)

  관계 연산자는 피연산자를 서로 비교하고, 비교 결과가 참인지에 따라 불리언 값을 반환합니다.



- ### [연산자 우선순위](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#연산자_우선순위)

  연산자의 우선순위는 표현식을 평가할 때 연산자를 적용하는 순서를 결정합니다. 괄호를 사용하면 우선순위를 바꿀 수 있습니다.

  아래 표는 우선순위가 높은 순서에서 낮은 순서로 연산자를 나열합니다.

  | 연산자 유형        | 개별 연산자                                                  |
  | :----------------- | :----------------------------------------------------------- |
  | 맴버 접근          | `.` `[]`                                                     |
  | 인스턴스 호출/생성 | `()` `new`                                                   |
  | 증감               | `!` `~` `-` `+` `++` `--` `typeof` `void` `delete`           |
  | 거듭제곱           | `**`                                                         |
  | 곱하기/나누기      | `*` `/` `%`                                                  |
  | 더하기/빼기        | `+` `-`                                                      |
  | 비트 시프트        | `<<` `>>` `>>>`                                              |
  | 관계               | `<` `<=` `>` `>=` `in` `instanceof`                          |
  | 동등/일치          | `==` `!=` `===` `!==`                                        |
  | 비트 AND           | `&`                                                          |
  | 비트 XOR           | `^`                                                          |
  | 비트 OR            | `|`                                                          |
  | 논리 AND           | `&&`                                                         |
  | 논리 OR            | `||`                                                         |
  | 조건               | `?:`                                                         |
  | 할당               | `=` `+=` `-=` `**=` `*=` `/=` `%=` `<<=` `>>=` `>>>=` `&=` `^=` `|=` `&&=` `||=` `??=` |
  | 쉼표               | `,`                                                          |

  각각의 연산자로 향하는 링크를 포함한 더 자세한 표는 [JavaScript 참고서](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Operator_Precedence#table)에서 찾을 수 있습니다.

- ## [표현식](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Expressions_and_Operators#표현식)

  표현식이란 어떤 값으로 이행하는 임의의 유효한 코드 단위를 말합니다.

  모든 표현식은 구문이 유효하다면 어떤 값으로 이행하지만, 개념적으로는 두 가지 범주로 나뉩니다. 하나는 부수 효과가 있는 (예시: 변수에 값을 할당) 표현식이고, 다른 하나는 평가하면 어떤 값으로 이행하는 표현식입니다.



#### 그룹 연산자

그룹연산자 `()`는 표현식 평가의 우선순위를 조절합니다. 예를 들어, 곱하기와 나누기보다 더하기와 빼기 연산을 먼저 수행할 수 있습니다.



#### super

[super 키워드](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/super)는 객체의 부모가 가진 함수를 호출할 때 사용합니다. 예를 하나 들면, [클래스](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes)에서 부모의 생성자를 호출해야 할 때 유용하게 쓸 수 있습니다.