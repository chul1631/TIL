# 변수와 식별자

• 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함

 • 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작 

• 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작 

• 예약어* 사용 불가능 

• 예약어 예시: for, if, function 등

• (참고) 선언, 할당, 초기화

• 선언 (Declaration) 

• 변수를 생성하는 행위 또는 시점 

• 할당 (Assignment)

 • 선언된 변수에 값을 저장하는 행위 또는 시점 

• 초기화 (Initialization)

 • 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점



| let           | const         |
| ------------- | ------------- |
| 재할당 가능   | 재할당 불가능 |
| 재선언 불가능 | 재선언 불가능 |





## 블록 스코프* (block scope) 

• if, for, 함수 등의 중괄호 내부를 가리킴 

• 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능



## var

• var로 선언한 변수는 재선언 및 재할당 모두 가능

• ES6 이전에 변수를 선언할 때 사용되던 키워드

• 호이스팅*되는 특성으로 인해 예기치 못한 문제 발생 가능 

• 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장 



## 함수 스코프 (function scope)

• 함수의 중괄호 내부를 가리킴

 • 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능





## 호이스팅 (hoisting)

 • 변수를 선언 이전에 참조할 수 있는 현상 

• 변수 선언 이전의 위치에서 접근 시 undefined를 반환 

• 자바스크립트는 모든 선언을 호이스팅한다.

 • 즉, var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생 하여 일시적 사각지대가 존재하지 않는다. 



|       | 재선언 | 재할당 |   스코프    |     비고     |
| :---: | :----: | :----: | :---------: | :----------: |
|  let  |   X    |   O    | 블록 스코프 | ES6부터 도입 |
| const |   X    |   X    | 블록 스코프 | ES6부터 도입 |
|  var  |   O    |   O    | 함수 스코프 |    사용x     |





# 데이터 타입

• 자바스크립트의 모든 값은 특정한 데이터 타입을 가짐

• 크게 원시 타입* (Primitive type)과 참조 타입* (Reference type)으로 분류됨



#### 원시 타입 (Primitive type)

• 객체 (object)가 아닌 기본 타입 

• 변수에 해당 타입의 값이 담김 

• 다른 변수에 복사할 때 실제 값이 복사됨



**참조 타입 (Reference type)**

• 객체 (object) 타입의 자료형 

• 변수에 해당 객체의 참조 값이 담김 

• 다른 변수에 복사할 때 참조 값이 복사됨



**숫자 (Number) 타입**

• 정수, 실수 구분 없는 하나의 숫자 타입 

• 부동소수점 형식을 따름 • (참고) NaN (Not-A-Number) 

• 계산 불가능한 경우 반환되는 값 • ex) 'Angel' / 1004 => NaN



**문자열 (String) 타입**

• 텍스트 데이터를 나타내는 타입 

• 16비트 유니코드 문자의 집합 

• 작은따옴표 또는 큰따옴표 모두 가능

• 템플릿 리터럴 (Template Literal) 

​	- ES6부터 지원 

​	- 따옴표 대신 backtick()으로 표현 

​	- ${ expression } 형태로 표현식 삽입 가능



**undefined**

• 변수의 값이 없음을 나타내는 데이터 타입 

• 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨



**null**

• 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입 

• (참고) null 타입과 typeof 연산자*

 • typeof 연산자*: 자료형 평가를 위한 연산자

 • null 타입은 ECMA 명세의 원시 타입의 정의에 따라 원시 타입에 속하지만, typeof 연산자의 결과는 객체(object)로 표현됨 



**Boolean 타입**

• 논리적 참 또는 거짓을 나타내는 타입 

• true 또는 false로 표현 • 조건문 또는 반복문*에서 유용하게 사용

 • (참고) 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true 또는 false로 변 환됨



| 데이터 타입 |    거짓    |        참        |
| :---------: | :--------: | :--------------: |
|  Undefined  | 항상 거짓  |        X         |
|    Null     | 항상 거짓  |        X         |
|   Number    | 0, -0, NaN | 나머지 모든 경우 |
|   String    | 빈 문자열  | 나머지 모든 경우 |
|   Object    |     X      |     항상 참      |

**할당 연산자**

• 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자 

• 다양한 연산에 대한 단축 연산자 지원 

• (참고) Increment 및 Decrement 연산자* 

• Increment(++): 피연산자의 값을 1 증가시키는 연산자

 • Decrement(--): 피연산자의 값을 1 감소시키는 연산자

 • Airbnb Style Guide에서는 ‘+=’ 또는 ‘-=’와 같이 더 분명한 표현으로 적을 것을 권장



**비교 연산자**

• 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자 

• 문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교

• ex) 알파벳끼리 비교할 경우 • 알파벳 순서상 후순위가 더 크다 

• 소문자가 대문자보다 더 크다



**동등 비교 연산자 (==)**

• 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환

• 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교 

• 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별 

• 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음



**일치 비교 연산자 (===)**

• 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환 

• 엄격한 비교*가 이뤄지며 암묵적 타입 변환이 발생하지 않음 *

*• 엄격한 비교*: 두 비교 대상의 타입과 값 모두 같은지 비교



**논리 연산자**

• 세 가지 논리 연산자로 구성 

• and 연산은 ‘&&’ 연산자를 이용

• or 연산은 ‘||’ 연산자를 이용 • not 연산은 ‘!’ 연산자를 이용 

• 단축 평가 지원 • ex) false && true => false 

• ex) true || false => true



**삼항 연산자 (Ternary Operator)**



• 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자 

• 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용

• 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능 

• 한 줄에 표기하는 것을 권장



#  조건문



## **조건문의 종류와 특징**

• **‘if’ statement** 

​	- 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단 

**• ‘switch’ statement** 

• 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별 

• (참고*) 주로 특정 변수의 값에 따라 조건을 분기할 때 활용 

​	- 조건이 많아질 경우 if문보다 가독성이 나을 수 있음



**조건문의 종류와 특징**

• if, else if, else 

• 조건은 소괄호(condition) 안에 작성

 • 실행할 코드는 중괄호{} 안에 작성

 • 블록 스코프 생성



## **반복문의 종류와 특징**

 **while** 

​	- 조건문이 참(true)인 동안 반복 시행

​	- 조건은 소괄호 안에 작성

​	- 실행할 코드는 중괄호 안에 작성 

​	- 블록 스코프 생성

**for** 

• 세미콜론(;)으로 구분되는 세 부분 으로 구성

​	- initialization • 최초 반복문 진입 시 1회만 실행되는 부분

​	- condition • 매 반복 시행 전 평가되는 부분

​	- expression • 매 반복 시행 이후 평가되는 부분 

​	- 블록 스코프 생성

**• for...in**  (객체 순회 적합)

​	- 주로 객체(object)의 속성들을 순회할 때 사용 

​	- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음 

**• for...of** (배열 순회 적합)

​	-  반복 가능한(iterable)* 객체를 순회하며 값을 꺼낼 때 사용 

​	-  반복 가능한(iterable) 객체*의 종류: Array, Map, Set, String 등

	-  실행할 코드는 중괄호 안에 작성 • 블록 스코프 생성

































# JavaScript 구성요소

이번 과정에서는 조건문, 반복문, 함수, 이벤트 등 일반적으로 발생하는 코드 종류를 중심으로 JavaScript의 중요한 기본 기능에 대해 설명

# 판단 내리기 — 조건문

## [if ... else 문](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/conditionals#if_..._else_문)

여러분이 자바스크립트에서 쓸 단연코 가장 일반적인 형태의 조건문을 살펴봅시다 — 변변찮은 [`if ... else` 문](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/if...else)입니다.

### [기본 if ... else 문법](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/conditionals#기본_if_..._else_문법)

기본 `if...else` 문법은 의사 코드([pseudocode](https://developer.mozilla.org/ko/docs/Glossary/Pseudocode))로 다음과 같이 보입니다:

```
if (조건) {
  만약 조건(condition)이 참일 경우 실행할 코드
} else {
  대신 실행할 다른 코드
```

### [else if](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/conditionals#else_if)

### [비교 연산자에 대한 메모](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/conditionals#비교_연산자에_대한_메모)

비교 연산자는 우리의 조건문 안의 조건을 테스트하는데 사용됩니다. 우리는 먼저 이전의 [자바스크립트의 기본적인 연산 - 숫자와 연산자](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps/Math#comparison_operators) 문서에서 비교 연산자를 봤습니다. 우리의 선택들은 다음과 같습니다:

- `===`와 `!==` — 한 값이 다른 값과 같거나 다른지 테스트한다.
- `<` 와 `>` — 한 값이 다른 값보다 작은지 큰지 테스트한다.
- `<=` 와 `>=` — 한 값이 다른 값보다 작거나 같은지, 크거나 같은지 테스트한다

----

## [함수 ](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Functions)

코딩에서의 또 다른 필수적인 개념은 **함수**입니다. **함수**를 사용하면 정의된 블록 안에 하나의 작업을 수행하는 코드 조각을 저장할 수 있고, 언제든지 그 코드 조각이 필요할 때 같은 코드를 여러번 입력하지 않고도 짧은 명령을 사용해 그 코드를 호출할 수 있습니다. 이 문서에서는 기본 문법, 어떻게 함수를 호출하고 정의하는지, 스코프, 그리고 매개변수와 같은 함수의 기본 개념을 탐사할 것입니다.



• 참조 타입 중 하나로써 function 타입에 속함

• JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분 

• 함수 선언식 (function declaration)

• 함수 표현식 (function expression) 

• (참고) JavaScript의 함수는 일급 객체*(First-class citizen)에 해당 *

*• 일급 객체*: 다음의 조건들을 만족하는 객체를 의미함 

• 변수에 할당 가능

• 함수의 매개변수로 전달 가능 

• 함수의 반환 값으로 사용 가능





## 함수의 정의

#### 3가지 부분으로 구성

• 함수의 이름 (name) 

• 매개변수 (args) 

• 함수 body (중괄호 내부)



**함수 표현식(function expression)**

• 함수를 표현식* 내에서 정의하는 방식 

• (참고) 표현식*: 어떤 하나의 값으로 결정되는 코드의 단위 

• 함수의 이름을 생략하고 익명 함수*로 정의 가능

• 익명 함수*(anonymous function): 이름이 없는 함수 

• 익명 함수는 함수 표현식에서만 가능 • 3가지 부분으로 구성 

• 함수의 이름 (생략 가능) 

• 매개변수 (args) 

• 몸통 (중괄호 내부)



**기본 인자(default arguments)**

• 인자 작성 시 ‘=’ 문자 뒤 기본 인자 선언 가능

• 매개변수와 인자의 개수 불일치 허용



* 매개변수보다 인자의 개수가 많을 경우,

```javascript
const noArgs = function () {
return 0
}
noArgs(1, 2, 3) // 0
const twoArgs = function (arg1, arg2) {
return [arg1, arg2]
}
twoArgs(1, 2, 3) // [1, 2]
```



* 매개변수보다 인자의 개수가 적을 경우,

```java
const threeArgs = function (arg1, arg2, arg3) {
return [arg1, arg2, arg3]
}
threeArgs() // [undefined, undefined, undefined]
threeArgs(1) // [1, undefined, undefined]
threeArgs(1, 2) // [1, 2, undefined]
```

**Rest Parameter**

 • rest parameter(…)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음 (python 의 *args 와 유사)

 • 만약 rest parameter로 처리한 매개변수에 인자가 넘어오지 않을 경우에는, 빈 배열로 처리

```java
const restOpr = function (arg1, arg2, ...restArgs) {
return [arg1, arg2, restArgs]
}
restArgs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
restArgs(1, 2) // [1, 2, []]
```

**Spread operator**

•spread operator(…)를 사용하면 배열 인자를 전개하여 전달 가능.

```java
const spreadOpr = function (arg1, arg2, arg3) {
return arg1 + arg2 + arg3
}
const numbers = [1, 2, 3]
spreadOpr(...numbers) // 6
```



### 함수 선언식과 표현식 비교 정리



|        |              함수 선언식(declartion)               |              함수 표현식(expression)               |
| :----: | :------------------------------------------------: | :------------------------------------------------: |
| 공통점 | 데이터 타입, 함수 구성 요소 (이름 ,매개변수, 몸통) | 데이터 타입, 함수 구성 요소 (이름 ,매개변수, 몸통) |
| 차이점 |            익명 함수 불가능 호이스팅 O             |             익명 함수 가능 호이스팅 X              |



**함수의 타입**

​	• 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

**호이스팅(hoisting) – 함수 선언식**

​	• 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생 

​	• 함수 호출 이후에 선언 해도 동작

​	• 함수 표현식을 var 키워드로 작성한 경우, 변수가 선언 전 undefined 로 초기화 되어 다른 에러가 발생

---

### 화살표 함수 (Arrow Function)

• 함수를 비교적 간결하게 정의할 수 있는 문법 

• function 키워드 생략 가능 

• 함수의 매개변수가 단 하나 뿐이라면, ‘( )’ 도 생략 가능 

• 함수 몸통이 표현식 하나라면 ‘{ }’과 return도 생략 가능 

```javascript
const arrow1 = function (name) {
return `hello, ${name}`
}
// 1. function 키워드 삭제
const arrow2 = (name) => { return `hello, ${name}` }
// 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
const arrow3 = name => { return `hello, ${name}` }
// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제
가능
const arrow4 = name => `hello, ${name}`
```

 

문자열 관련 주요 메서드 목록

|  메서드  |                   설명                    |                     비고                     |
| :------: | :---------------------------------------: | :------------------------------------------: |
| includes | 특정 문자열의 존재여부를 참/거짓으로 반환 |                                              |
|  split   |   문자열을 토큰 기준으로 나눈 배열 반환   | 인자가 없으면 기존 문자열을 배열에 담아 반환 |
| replace  | 해당 문자열을 대상 문자열로 교체하여 반환 |                  replaceAll                  |
|   trim   |     문자열의 좌우 공백 제거하여 반환      |              trimStart, trimEnd              |



**문자열 관련 주요 메서드 – includes**

• string.includes(value) 

• 문자열에 value가 존재하는지 판별 후 참 또는 거짓 반환



**문자열 관련 주요 메서드 - split**

• string.split(value) 

• value가 없을 경우, 기존 문자열을 배열에 담아 반환

• value가 빈 문자열일 경우 각 문자로 나눈 배열을 반환

• value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환



**문자열 관련 주요 메서드 – replace**

**• string.replace(from, to)** 

​	• 문자열에 from 값이 존재할 경우, 1개만 to 값으로 교체하여 반환

**• string.replaceAll(from, to)** 

​	• 문자열에 from 값이 존재할 경우, 모두 to 값으로 교체하여 반환



---

# 배열 (Arrays)

배열의 정의와 특징

• 키와 속성들을 담고 있는 참조 타입의 객체(object) 

• 순서를 보장하는 특징이 있음 

• 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

• 배열의 길이는 array.length 형태로 접근 가능 

•  배열의 마지막 원소는 array.length – 1로 접근





## 배열 관련 주요 메서드 목록 (1) – 기본편



| 메서드        | 설명                                             | 비고                     |
| ------------- | ------------------------------------------------ | ------------------------ |
| reverse       | 원본 배열의 요소들의 순서를 반대로 정렬          |                          |
| push&pop      | 배열의 가장 뒤에 요소를 추가 또는 제거           |                          |
| unshift&shift | 배열의 가장 앞에 요소를 추가 또는 제거           |                          |
| includes      | 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환 |                          |
| indexOf       | 배열에 특정 값이 존재하는지 판별 후 인덱스 반환  | 요소가 없을 경우 -1 반환 |
| join          | 배열의 모든 요소를 구분자를 이용하여 연결        | 구분자 생략 시 쉼표 기준 |



**배열 관련 주요 메서드 - reverse**

• array.reverse()

• 원본 배열의 요소들의 순서를 반대로 정렬

**배열 관련 주요 메서드 – push & pop**

• array.unshift()

​	- 배열의 가장 앞에 요소 추가

• array.shift() 

​	- 배열의 첫번째 요소 제거

**배열 관련 주요 메서드 – includes**

• array.includes(value) 

​	- 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환



**배열 관련 주요 메서드 – indexOf**

• array.indexOf(value) 

​	- 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환 • 만약 해당 값이 없을 경우 -1 반환

**배열 관련 주요 메서드 – join**

• array.join([separator]) 

​	- 배열의 모든 요소를 연결하여 반환

​	- separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용







## 배열 관련 주요 메서드 목록 (2)

• 배열을 순회하며 특정 로직을 수행하는 메서드

• 메서드 호출 시 인자로 callback 함수를 받는 것이 특징





| 메서드  | 설명                                                         | 비고         |
| ------- | ------------------------------------------------------------ | ------------ |
| forEach | 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행               | 반환 값 없음 |
| map     | 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환           |              |
| filter  | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |              |
| reduce  | 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환        |              |
| find    | 콜백 함수의 반환 값이 참이면 해당 요소를 반환                |              |
| some    | 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환       |              |
| every   | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환            |              |

**배열 관련 주요 메서드 – forEach**

• array.forEach(callback(element[, index[,array]])) 

• 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 • 콜백 함수는 3가지 매개변수로 구성

• element: 배열의 요소 

• index: 배열 요소의 인덱스

• array: 배열 자체 

• 반환 값(return)이 없는 메서드



**배열 관련 주요 메서드 – map**

• array.map(callback(element[, index[, array]])) 

• 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 

• 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환 

• 기존 배열 전체를 다른 형태로 바꿀 때 유용



**배열 관련 주요 메서드 – filter**

• array.filter(callback(element[, index[, array]])) 

• 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 

• 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 

• 기존 배열의 요소들을 필터링할 때 유용



**배열 관련 주요 메서드 – reduce**

• array.reduce(callback(acc, element, [index[, array]])[, initialValue]) 

• 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

• 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

• reduce 메서드의 주요 매개변수 

​	- acc 

​	-이전 callback 함수의 반환 값이 누적되는 변수

 • initialValue(optional) 

​	- 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값

​	- (참고) 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생



**배열 관련 주요 메서드 – find**

• array.find(callback(element[, index[, array]])) • 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 • 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환 • 찾는 값이 배열에 없으면 undefined 반환





**배열 관련 주요 메서드 –** **some**

• array.some(callback(element[, index[, array]])) 

• 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환 

• 모든 요소가 통과하지 못하면 거짓 반환 

• (참고) 빈 배열은 항상 거짓 반환





**배열 관련 주요 메서드 – every**

• array.every(callback(element[, index[, array]])) 

• 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환 

• 하나의 요소라도 통과하지 못하면 거짓 반환 

• 빈 배열은 항상 참 반환



## 객체 (Objects)

### 객체 정의와 특징

• 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현 

• key는 문자열 타입*만 가능 

• (참고) key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

 • value는 모든 타입(함수포함) 가능 

• 객체 요소 접근은 점 또는 대괄호로 가능 

• (참고) key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

• 메서드는 객체의 속성이 참조하는 함수 

• 객체.메서드명() 으로 호출 가능 

• 메서드 내부에서는 this 키워드가 객체를 의미함



[JSON (JavaScriptObjectNotation)](https://www.ecma-international.org/publications-and-standards/standards/ecma-404/)

• key-value쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷 • 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입 • 따라서 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수 • 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공 • JSON.parse() • JSON => 자바스크립트 객체 • JSON.stringify() 

• 자바스크립트 객체 => JSON















## [함수 대 메소드](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Functions#함수_대_메소드)

## [함수 스코프와 충돌(conflicts)](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Functions#함수_스코프와_충돌conflicts)

### [함수 내부의 함수](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Functions#함수_내부의_함수)



### 함수 반환 값(return value)

## [반환 값이 무엇인가요?](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks/Return_values#반환_값이_무엇인가요)

