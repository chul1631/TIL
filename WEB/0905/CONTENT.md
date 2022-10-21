# CONTENT



### Reboot

단일 파일에 있는 요소별 CSS 변경 모음인 Reboot는 Bootstrap을 초기에 구축하는 우아하고 일관되며 간단한 기준선을 제공합니다.

Reboot는 Normalize를 기반으로 빌드되어 요소 선택자만 사용하여 다소 독선적인 스타일을 가진 많은 HTML 요소를 제공합니다. 추가 스타일링은 클래스에서만 수행됩니다. 예를 들어 더 간단한 기준선을 위해 일부 `<table>` 스타일을 재부팅하고 나중에 `.table`, `.table-border` 등을 제공합니다.

다음은 재부팅에서 Reboot할 항목을 선택하는 지침과 이유입니다:

- 확장 가능한 컴포넌트 간격에 `em` 대신`rem`을 사용하도록 일부 브라우저의 기본값을 업데이트합니다.
- `margin-top`을 제외합니다. 수직 margin은 구조적으로 불안정하며, 예상치 못한 결과를 가져올 수 있습니다. 더 중요한 것은 단방향 `margin`이 더 단순한 멘탈 모델이기 때문입니다.
- 더 쉬운 기기 간 크기 확장을 위해서 블럭 요소의 `margin`에 `rem`을 사용합니다.
- 가능하면 `inherit`를 사용하여 `font` 관련 속성의 선언을 최소한으로 유지합니다.

- #### CSS variables

  ```
  사용자 지정 속성(CSS 변수, 종속 변수)은 CSS 저작자가 정의하는 개체로, 문서 전반적으로 재사용할 임의의 값을 담습니다. 사용자 지정 속성은 전용 표기법을 사용해 정의하고, (`--main-color: black;`) [`var()`]함수를 사용해 접근할 수 있습니다. 
  ```

  - #### 기본 사용법

    ``` 
    사용자 지정 속성은 두 개의 붙임표로 시작하는 속성의 이름과 함께, 유효한 CSS 값이라면 아무거나 그 값으로 지정해 선언합니다. 다른 일반적인 속성과 마찬가지로 사용자 지정 속성도 아래와 같이 규칙 집합 내에 작성합니다.
    
    element {
      --main-bg-color: brown;
    }
    Copy to Clipboard
    규칙 집합의 선택자는 사용자 지정 속성을 사용할 수 있는 범위를 정의합니다. 흔히 보이는 패턴은 :root 의사 클래스에 선언해서 여러분의 HTML 문서 어디에서나 사용자 지정 속성에 접근할 수 있도록 구성하는 것입니다.
    
    :root {
      --main-bg-color: brown;
    }
    Copy to Clipboard
    그러나 반드시 이렇게 선언해야 하는 것은 아닙니다. 범위를 제한해야 하는 적절한 이유가 있을 수도 있으니까요.
    ```

    - 페이지 기본값

    `<html>` 과 `<body>` 요소는 더 넒은 페이지를 제공하기 위해 갱신됩니다. 구체적으로는 다음과 같습니다:

    - ```
      box-sizing은 *::before 및 *::after를 포함한 모든 요소에서 border-box로 전역적으로 설정됩니다. 이렇게 하면 요소의 선언된 너비가 패딩이나 테두리로 인해 초과되지 않습니다.
      <html>에는 기본 font-size가 선언되지 않지만 16px가 가정됩니다 (브라우저 기본값). font-size: 1rem 은 <body>에 적용되어 미디어 쿼리를 통한 손쉬운 반응형 유형 확장을 위해 사용자 설정값을 존중하고 보다 접근하기 쉬운 접근 방식을 보장합니다. 이 브라우저 기본값은 $font-size-root 변수를 수정하여 재정의할 수 있습니다.
      <body>는 전역 font-family, font-weight, line-height,color도 설정합니다. 이것은 나중에 글꼴 불일치를 방지하기 위해 일부 폼 요소에 의해 상속됩니다.
      안전을 위해서 <body>에는 선언된 background-color가 있으며 기본값은#fff입니다.
      ```



- ### Heading and paragraphs

  ```
  모든 제목 요소 (예: `<h1>` 및 `<p>`)는 `margin-top`이제거되도록 재설정됩니다. 제목에는 `margin-bottom: .5rem`이추가되고 단락은 `margin-bottom : 1rem`이 추가되어 간격을 쉽게 조정할 수 있습니다.
  ```

   ![화면 캡처 2022-09-05 151434](C:\Users\User\OneDrive\바탕 화면\화면 캡처 2022-09-05 151434.png)

## 목록

모든 목록 (`<ul>`,`<ol>`, `<dl>`)에는 `margin-top`이 제거되고 `margin-bottom: 1rem`이 제거됩니다. 중첩된 목록에는 `margin-bottom`이 없습니다. 또한`<ul>` 및 `<ol>` 요소에서 `padding-left`를 재설정했습니다.

## Horizontal rules 

```
<hr> 요소가 단순화되었습니다. 브라우저 기본값과 유사하게 <hr>은 border-top을 통해 스타일이 지정되고 기본 불투명도: .25를 가지며 부모를 통해 색상이 설정된 경우를 포함하여 색상을 통해 자동으로 테두리 색상을 상속합니다. 텍스트, 테두리 및 불투명도 유틸리티를 사용하여 수정할 수 있습니다.
```

![화면 캡처 2022-09-05 151734](C:\Users\User\OneDrive\바탕 화면\화면 캡처 2022-09-05 151734.png)

```html
<hr>

<div class="text-success">
  <hr>
</div>

<hr class="border border-danger border-2 opacity-50">
<hr class="border border-primary border-3 opacity-75">


```

## 목록

```
모든 목록(<ul>, <ol> 및 <dl>)에는 margin-top이 제거되고 margin-bottom: 1rem이 있습니다. 중첩 목록에는 margin-bottom이 없습니다. <ul> 및 <ol> 요소의 왼쪽 여백도 재설정했습니다.
더 간단한 스타일, 명확한 계층 구조, 더 나은 간격을 위해 설명 목록에는 업데이트된 margin이 포함되어 있습니다. <dd>의 margin-left를 0으로 재설정하고 margin-bottom: .5rem을 추가합니다. <dt>는 굵게 표시됩니다.
```

## 인라인 코드

인라인 코드 스니펫을 `<code>`로 묶습니다. HTML 꺾쇠 괄호를 이스케이프해야 합니다.

```html
For example, <code>&lt;section&gt;</code> should be wrapped as inline.
```

## 코드 블록

여러 줄의 코드에는 `<pre>`를 사용하세요. 다시 한 번 올바른 렌더링을 위해 코드에서 꺾쇠 괄호를 이스케이프해야 합니다. `<pre>` 요소는 `margin-top`을 제거하고 `margin-bottom`에 `rem` 단위를 사용하도록 재설정됩니다.

```html
<pre><code>&lt;p&gt;Sample text here...&lt;/p&gt;
&lt;p&gt;And another line of sample text here...&lt;/p&gt;
</code></pre>
```

## 변수

변수를 나타내려면 `<var>` 태그를 사용하세요.

```html
<var>y</var> = <var>m</var><var>x</var> + <var>b</var>
```

## 사용자 입력

일반적으로 키보드를 통해 입력되는 입력을 나타내려면 `<kbd>`를 사용해주세요.

```html
To switch directories, type <kbd>cd</kbd> followed by the name of the directory.<br>
To edit settings, press <kbd><kbd>ctrl</kbd> + <kbd>,</kbd></kbd>
```

## 출력 예시

프로그램의 출력 예시를 나타내려면 `<samp>` 태그를 사용해주세요.

```html
<samp>This text is meant to be treated as sample output from a computer program.</samp>
```



## 표

표는 스타일 `<caption>`, 테두리 축소 및 전체적으로 일관된 `text-align`을 위해 약간 조정됩니다. 테두리, 패딩 등에 대한 추가 변경 사항은 [`.table` 클래스](https://getbootstrap.kr/docs/5.0/content/tables/)와 함께 제공됩니다.

| Table heading | Table heading | Table heading | Table heading |
| ------------- | ------------- | ------------- | ------------- |
| Table cell    | Table cell    | Table cell    | Table cell    |
| Table cell    | Table cell    | Table cell    | Table cell    |
| Table cell    | Table cell    | Table cell    | Table cell    |

```html
<table>
  <caption>
    This is an example table, and this is its caption to describe the contents.
  </caption>
  <thead>
    <tr>
      <th>Table heading</th>
      <th>Table heading</th>
      <th>Table heading</th>
      <th>Table heading</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Table cell</td>
      <td>Table cell</td>
      <td>Table cell</td>
      <td>Table cell</td>
    </tr>
    <tr>
      <td>Table cell</td>
      <td>Table cell</td>
      <td>Table cell</td>
      <td>Table cell</td>
    </tr>
    <tr>
      <td>Table cell</td>
      <td>Table cell</td>
      <td>Table cell</td>
      <td>Table cell</td>
    </tr>
  </tbody>
</table>
```

------------

#### Typography

## 전역 설정

Bootstrap은 기본 전역 표시, 타이포그래피 및 링크 스타일을 설정합니다. 더 많은 제어가 필요한 경우 [텍스트 유틸리티 클래스](https://getbootstrap.kr/docs/5.0/utilities/text/)를 확인해보세요.

- 각 OS 및 기기에 가장 적합한 `font-family`를 선택하는 [기본 글꼴 스택](https://getbootstrap.kr/docs/5.0/content/reboot/#native-font-stack)을 사용합니다.
- 보다 포괄적이고 접근 가능한 유형 척도를 위해 브라우저의 기본 루트 `font-size` (일반적으로 16px)를 사용하여 방텍스트가 필요에 따라 브라우저 기본값을 사용자 지정할 수 있습니다.
- `<body>`에 적용된 타이포그래피 기반으로 `$font-family-base`, `$font-size-base` 및`$line-height-base` 속성을 사용합니다.
- `$link-color`를 통해 글로벌 링크 색상을 설정합니다.
- `$body-bg`를 사용하여 `<body>`에 `background-color`를 설정합니다 (기본적으로 `#fff`).

이러한 스타일은 `_reboot.scss`에서 찾을 수 있으며 전역 변수는 `_variables.scss`에서 정의됩니다. `rem`에 `$ font-size-base`를 설정해야 합니다.



## 제목

`<h1>`부터 `<h6>`까지의 모든 제목을 사용할 수 있습니다.

```html
<h1>h1. Bootstrap heading</h1>
<h2>h2. Bootstrap heading</h2>
<h3>h3. Bootstrap heading</h3>
<h4>h4. Bootstrap heading</h4>
<h5>h5. Bootstrap heading</h5>
<h6>h6. Bootstrap heading</h6>
```



### 사용자 정의 제목

포함된 유틸리티 클래스를 사용하여 Bootstrap 3에서의 작은 보조 제목 텍스트를 다시 만듭니다.

```html
<h3>
  For example
  <small class="text-muted">With faded secondary text</small>
</h3>
```

## 제목 표시

기존 제목 요소는 페이지 콘텐츠의 핵심에서 가장 잘 작동하도록 설계되었습니다. 눈에 띄는 제목이 필요한 경우 **표시 제목**을 사용하는 것이 좋습니다. 이 제목은 좀 더 크고 약간 더 독선적인 제목 스타일입니다.

```html
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
<h1 class="display-5">Display 5</h1>
<h1 class="display-6">Display 6</h1>
```

## 서두

`.lead`를 추가하여 단락을 눈에 띄게 만드십시오.

```html
<p class="lead">
  This is a lead paragraph. It stands out from regular paragraphs.
</p>
```

## 인라인 텍스트 요소

일반적인 인라인 HTML5 요소의 스타일링입니다.

```html
<p>You can use the mark tag to <mark>highlight</mark> text.</p>
<p><del>This line of text is meant to be treated as deleted text.</del></p>
<p><s>This line of text is meant to be treated as no longer accurate.</s></p>
<p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
<p><u>This line of text will render as underlined.</u></p>
<p><small>This line of text is meant to be treated as fine print.</small></p>
<p><strong>This line rendered as bold text.</strong></p>
<p><em>This line rendered as italicized text.</em></p>
```

이러한 태그는 시맨틱 목적으로 사용되어야합니다:

- `<mark>`는 참조 또는 표기 목적으로 표시되거나 강조된 텍스트를 나타냅니다.
- `<small>`은 저작권 및 법적 텍스트와 같은 부가적인 댓글과 작은 텍스트를 나타냅니다.
- `<s>`는 더 이상 관련이 없거나 더 이상 정확하지 않은 요소를 나타냅니다.
- `<u>`는 텍스트가 아닌 주석이 있음을 나타내는 방식으로 렌더링되어야 하는 인라인 텍스트의 범위를 나타냅니다.

텍스트 스타일을 지정해야 된다면 다음 클래스를 사용할 수도 있습니다.

- `.mark`는 `<mark>`와 동일한 스타일을 적용합니다.
- `.small`은 `<small>`과 동일한 스타일을 적용합니다.
- `.text-decoration-underline`은 `<u>`와 동일한 스타일을 적용합니다.
- `.text-decoration-line-through`는 `<s>`와 동일한 스타일을 적용합니다.

위에는 표시되지 않았지만 HTML5에서 `<b>` 및 `<i>`를 자유롭게 사용하세요. `<b>`는 추가 중요성을 전달하지 않고 단어나 구문을 강조하는 반면 `<i>`는 대부분 음성, 기술 용어 등에 사용됩니다.

## 텍스트 유틸리티

[텍스트 유틸리티](https://getbootstrap.kr/docs/5.0/utilities/text/) 및 [색상 유틸리티](https://getbootstrap.kr/docs/5.0/utilities/colors/)를 사용하여 텍스트 정렬, 변형, 스타일, 두께, 선 높이, 장식 및 색상을 변경하십시오.

## 약어

약어 및 두텍스트어에 대한 HTML의 `<abbr>` 요소를 스타일링하여 마우스 오버시 확장된 버전을 표시합니다. 약어에는 기본 밑줄이 있으며 도움말 커서를 통해 마우스 오버 시 및 보조 기술 사용자에게 추가 컨텍스트를 제공합니다.

약간 더 작은 글꼴 크기의 약어에 `.initialism`을 추가합니다.

```html
<p><abbr title="attribute">attr</abbr></p>
<p><abbr title="HyperText Markup Language" class="initialism">HTML</abbr></p>
```

## 인용문

문서 내의 다른 소스에서 콘텐츠 블록을 인용합니다. HTML을 인용문으로 `<blockquote class="blockquote">`로 감쌉니다.

```html
<blockquote class="blockquote">
  <p>A well-known quote, contained in a blockquote element.</p>
</blockquote>
```



### 출처 표기

HTML 사양에서는 인용구 속성이 `<blockquote>`외부에 배치되어야 합니다. 어트리뷰션을 제공할 때 `<blockquote>`를 `<figure>`로 감싸고 `<figcaption>` 또는 블록 레벨 요소 (예: `<p>`)를 `.blockquote-footer` 클래스와 함께 사용하세요. 소스 작품의 이름도 `<cite>`로 감싸야 합니다.

```html
<figure>
  <blockquote class="blockquote">
    <p>A well-known quote, contained in a blockquote element.</p>
  </blockquote>
  <figcaption class="blockquote-footer">
    Someone famous in <cite title="Source Title">Source Title</cite>
  </figcaption>
</figure>
```

### 정렬

인용구의 정렬을 변경하려면 필요에 따라 텍스트 유틸리티를 사용하세요.

```html
<figure class="text-center">
  <blockquote class="blockquote">
    <p>A well-known quote, contained in a blockquote element.</p>
  </blockquote>
  <figcaption class="blockquote-footer">
    Someone famous in <cite title="Source Title">Source Title</cite>
  </figcaption>
</figure>
```



## 목록

- #### 스타일 제거

  - 기본 `list-style`과 목록 항목의 왼쪽 여백을 제거합니다 (직계 자식만 해당). **이 부분은 직계 자식 목록 항목에만 적용됩니다**. 즉, 중첩된 목록에 대해서도 클래스를 추가해야 합니다.

  - ```html
    <ul class="list-unstyled">
      <li>This is a list.</li>
      <li>It appears completely unstyled.</li>
      <li>Structurally, it's still a list.</li>
      <li>However, this style only applies to immediate child elements.</li>
      <li>Nested lists:
        <ul>
          <li>are unaffected by this style</li>
          <li>will still show a bullet</li>
          <li>and have appropriate left margin</li>
        </ul>
      </li>
      <li>This may still come in handy in some situations.</li>
    </ul>
    ```

- ### 인라인

  목록의 글 머리 기호를 제거하고 `.list-inline`과 `.list-inline-item`의 두 클래스 조합으로 약간의 `margin`을 적용합니다.

  ```html
  <ul class="list-inline">
    <li class="list-inline-item">This is a list item.</li>
    <li class="list-inline-item">And another one.</li>
    <li class="list-inline-item">But they're displayed inline.</li>
  </ul>
  ```

- #### 설명 목록 정렬

  - 그리드 시스템의 사전 정의된 클래스 (또는 시맨틱 믹스인)를 사용하여 용어와 설명을 수평으로 정렬합니다. 더 긴 용어의 경우 선택적으로 `.text-truncate` 클래스를 추가하여 줄임표로 텍스트를 자를 수 있습니다.

```html
<dl class="row">
  <dt class="col-sm-3">Description lists</dt>
  <dd class="col-sm-9">A description list is perfect for defining terms.</dd>

  <dt class="col-sm-3">Term</dt>
  <dd class="col-sm-9">
    <p>Definition for the term.</p>
    <p>And some more placeholder definition text.</p>
  </dd>

  <dt class="col-sm-3">Another term</dt>
  <dd class="col-sm-9">This definition is short, so no extra paragraphs or anything.</dd>

  <dt class="col-sm-3 text-truncate">Truncated term is truncated</dt>
  <dd class="col-sm-9">This can be useful when space is tight. Adds an ellipsis at the end.</dd>

  <dt class="col-sm-3">Nesting</dt>
  <dd class="col-sm-9">
    <dl class="row">
      <dt class="col-sm-4">Nested definition list</dt>
      <dd class="col-sm-8">I heard you like definition lists. Let me put a definition list inside your definition list.</dd>
    </dl>
  </dd>
</dl>
```

- #### 반응형 글꼴 크기

  - Bootstrap 5에서는 기본적으로 반응형 글꼴 크기를 활성화하여 텍스트가 장치 및 뷰포트 크기에 따라 더 자연스럽게 확장될 수 있도록 했습니다. 어떻게 작동하는지 알아보려면 [RFS 페이지](https://getbootstrap.kr/docs/5.0/getting-started/rfs/)를 살펴보십시오.

## Sass

### 변수

제목에는 크기 및 간격에 대한 전용 변수가 있습니다.

```scss
$headings-margin-bottom:      $spacer * .5;
$headings-font-family:        null;
$headings-font-style:         null;
$headings-font-weight:        500;
$headings-line-height:        1.2;
$headings-color:              null;
```

여기와 [Reboot](https://getbootstrap.kr/docs/5.0/content/reboot/)에서 다루는 기타 타이포그래피 요소에도 전용 변수가 있습니다.

```scss
$lead-font-size:              $font-size-base * 1.25;
$lead-font-weight:            300;

$small-font-size:             .875em;

$sub-sup-font-size:           .75em;

$text-muted:                  $gray-600;

$initialism-font-size:        $small-font-size;

$blockquote-margin-y:         $spacer;
$blockquote-font-size:        $font-size-base * 1.25;
$blockquote-footer-color:     $gray-600;
$blockquote-footer-font-size: $small-font-size;

$hr-margin-y:                 $spacer;
$hr-color:                    inherit;
$hr-height:                   $border-width;
$hr-opacity:                  .25;

$legend-margin-bottom:        .5rem;
$legend-font-size:            1.5rem;
$legend-font-weight:          null;

$mark-padding:                .2em;

$dt-font-weight:              $font-weight-bold;

$nested-kbd-font-weight:      $font-weight-bold;

$list-inline-padding:         .5rem;

$mark-bg:                     #fcf8e3;
```



----



#### Images

이미지를 반응형 동작으로 선택하고 (부모 요소보다 커지지 않도록) 클래스를 통해 경량 스타일을 추가하는 문서 및 예시입니다.

## 반응형 이미지

Bootstrap의 이미지는 `.img-fluid`를 통해서 반응형으로 만들어집니다. 이렇게 하면 이미지에 `max-width: 100%;` 및 `height: auto;`가 적용되어 부모 요소와 함께 크기가 조정됩니다.https://getbootstrap.kr/docs/5.0/content/images/#변수)

```html
<img src="..." class="img-fluid" alt="...">
```



## 이미지 썸네일

[border-radius 유틸리티](https://getbootstrap.kr/docs/5.0/utilities/borders/) 유틸리티 외에도, `.img-thumbnail`을 사용하여 이미지에 둥근 1px 테두리 모양을 제공할 수 있습니다.

```html
<img src="..." class="img-thumbnail" alt="...">
```



## 이미지 정렬

[helper float 클래스](https://getbootstrap.kr/docs/5.0/utilities/float/) 또는 [텍스트 정렬 클래스](https://getbootstrap.kr/docs/5.0/utilities/text/#text-alignment)로 이미지를 정렬하세요. `block`-level 이미지는 [`.mx-auto` margin 유틸리티 클래스](https://getbootstrap.kr/docs/5.0/utilities/spacing/#horizontal-centering)로 중앙 정렬할 수 있습니다.

```html
<img src="..." class="rounded float-start" alt="...">
<img src="..." class="rounded float-end" alt="...">
```

```html
<img src="..." class="rounded mx-auto d-block" alt="...">
```

```html
<picture>
  <source srcset="..." type="image/svg+xml">
  <img src="..." class="img-fluid img-thumbnail" alt="...">
</picture>
```



## 사진

`<picture>` 요소를 사용하여 특정 `<img>`에 대해 여러 `<source>` 요소를 지정하는 경우 `<picture>` 태그가 아닌 `<img>`에 `.img-*` 클래스를 추가해야 합니다.

```html
<picture>
  <source srcset="..." type="image/svg+xml">
  <img src="..." class="img-fluid img-thumbnail" alt="...">
</picture>
```

### 변수

이미지 썸네일에 변수를 사용할 수 있습니다.

```scss
$thumbnail-padding:                 .25rem;
$thumbnail-bg:                      $body-bg;
$thumbnail-border-width:            $border-width;
$thumbnail-border-color:            $gray-300;
$thumbnail-border-radius:           $border-radius;
$thumbnail-box-shadow:              $box-shadow-sm;
```

--------------------

#### Tables

Bootstrap을 사용한 테이블의 opt-in 스타일에 대한 문서 및 예시 (JavaScript 플러그인에서 널리 사용됨)입니다.

<table> 요소는 캘린더나 날짜 선택기 같은 서드 파티 위젯에서 폭넓게 사용되고 있기 때문에 Bootstrap의 표는 opt-in 방식을 사용합니다. 기본 클래스 .table을 <table>에 넣으면 우리의 선택 수정자 클래스 또는 커스텀 스타일로 확장할 수 있습니다. 모든 표 스타일이 Bootstrap에 상속되지 않기 때문에 중첩된 테이블은 부모와 독립적으로 스타일을 지정할 수 있습니다.

가장 기본적인 표 마크업을 사용해서 `.table` 기반 표가 Bootstrap에서 어떻게 표시되는지 보여드리겠습니다.

```html
<table class="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```



## 변형

상황별 표 색상, 표 행 또는 개별 셀을 사용하세요.

```html
<!-- On tables -->
<table class="table-primary">...</table>
<table class="table-secondary">...</table>
<table class="table-success">...</table>
<table class="table-danger">...</table>
<table class="table-warning">...</table>
<table class="table-info">...</table>
<table class="table-light">...</table>
<table class="table-dark">...</table>

<!-- On rows -->
<tr class="table-primary">...</tr>
<tr class="table-secondary">...</tr>
<tr class="table-success">...</tr>
<tr class="table-danger">...</tr>
<tr class="table-warning">...</tr>
<tr class="table-info">...</tr>
<tr class="table-light">...</tr>
<tr class="table-dark">...</tr>

<!-- On cells (`td` or `th`) -->
<tr>
  <td class="table-primary">...</td>
  <td class="table-secondary">...</td>
  <td class="table-success">...</td>
  <td class="table-danger">...</td>
  <td class="table-warning">...</td>
  <td class="table-info">...</td>
  <td class="table-light">...</td>
  <td class="table-dark">...</td>
</tr>
```





## 표 강조

- #### 스트라이프 행

  - `.table-striped`를 사용하여 `<tbody>`내의 테이블 행에 줄무늬 (zebra-striping)를 추가합니다.

  - ```html
    <table class="table table-striped">
      ...
    </table>
    ```



### 호버할 수 있는 행

`.table-hover`를 추가하여 `<tbody>`내의 테이블 행에 마우스 오버 상태를 활성화합니다.

```html
<table class="table table-hover">
  ...
</table>
```

### 활성화 표

`.table-active` 클래스를 추가하여 테이블 행 또는 셀을 강조 표시합니다.

```html
<table class="table">
  <thead>
    ...
  </thead>
  <tbody>
    <tr class="table-active">
      ...
    </tr>
    <tr>
      ...
    </tr>
    <tr>
      <th scope="row">3</th>
      <td colspan="2" class="table-active">Larry the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```



## 표 테두리

### 테두리가 있는 표

셀의 모든 면에 테두리가 있는 표를 만드려면 `.table-border`를 추가하면 됩니다.

```html
<table class="table table-bordered">
  ...
</table>
```

### 테두리가 없는 표

테두리가 없는 표를 만드려면 `.table-borderless`를 추가하면 됩니다.

```html
<table class="table table-borderless">
  ...
</table>
```

## 얇은 표

`.table-sm`을 추가하여 모든 셀 `padding`을 반으로 잘라 `.table`을 더 간결하게 만듭니다.

```html
<table class="table table-sm">
  ...
</table>
```

## 수직 정렬

`<thead>`의 표 셀은 항상 하단에 수직으로 정렬됩니다. `<tbody>`의 표 셀은 `<table>`에서 정렬을 상속하며 기본적으로 상단에 정렬됩니다. [수직 정렬](https://getbootstrap.kr/docs/5.0/utilities/vertical-align/) 클래스를 사용하여 필요한 곳에 다시 정렬합니다.



```html
<div class="table-responsive">
  <table class="table align-middle">
    <thead>
      <tr>
        ...
      </tr>
    </thead>
    <tbody>
      <tr>
        ...
      </tr>
      <tr class="align-bottom">
        ...
      </tr>
      <tr>
        <td>...</td>
        <td>...</td>
        <td class="align-top">This cell is aligned to the top.</td>
        <td>...</td>
      </tr>
    </tbody>
  </table>
</div>
```

| Heading 1                                                    | Heading 2                                                    | Heading 3                                                    | Heading 4                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| This cell inherits `vertical-align: middle;` from the table  | This cell inherits `vertical-align: middle;` from the table  | This cell inherits `vertical-align: middle;` from the table  | This here is some placeholder text, intended to take up quite a bit of vertical space, to demonstrate how the vertical alignment works in the preceding cells. |
| This cell inherits `vertical-align: bottom;` from the table row | This cell inherits `vertical-align: bottom;` from the table row | This cell inherits `vertical-align: bottom;` from the table row | This here is some placeholder text, intended to take up quite a bit of vertical space, to demonstrate how the vertical alignment works in the preceding cells. |
| This cell inherits `vertical-align: middle;` from the table  | This cell inherits `vertical-align: middle;` from the table  | This cell is aligned to the top.                             | This here is some placeholder text, intended to take up quite a bit of vertical space, to demonstrate how the vertical alignment works in the preceding cells. |

## 중첩

테두리 스타일, 활성화 스타일 및 표 변형은 중첩된 표에 상속되지 않습니다.

```html
<table class="table table-striped">
  <thead>
    ...
  </thead>
  <tbody>
    ...
    <tr>
      <td colspan="4">
        <table class="table mb-0">
          ...
        </table>
      </td>
    </tr>
    ...
  </tbody>
</table>
```

## 중첩 작동 원리

*아무* 스타일이 중첩 테이블로 유출되는 것을 방지하기 위해 CSS에서 자식 결합자 (`>`) 선택자를 사용합니다. 우리는 `thead`, `tbody`, `tfoot`의 모든 `td`와 `th`를 대상으로 해야 하므로 선택자가 없으면 꽤 길어보일 것입니다. 따라서 다소 이상해 보이는 `.table > :not(caption) > * > *`선택기를 사용하여 `.table`의 모든 `td`와 `th`를 타겟팅하지만 잠재적 중첩 테이블은 없습니다.

테이블의 직계 자식으로 `<tr>`을 추가하면 해당 `<tr>`이 기본적으로 `<tbody>`에 줄바꿈되므로 선택자가 의도한 대로 작동합니다.



## 구조

### 표 머리글

표 및 어두운 표과 유사하게, 수정자 클래스 `.table-light` 또는 `.table-dark`를 사용하여 `<thead>`가 밝은 회색 또는 어두운 회색으로 표시되도록 합니다.

| #    | First | Last     | Handle   |
| ---- | ----- | -------- | -------- |
| 1    | Mark  | Otto     | @mdo     |
| 2    | Jacob | Thornton | @fat     |
| 3    | Larry | the Bird | @twitter |

```html
<table class="table">
  <thead class="table-light">
    ...
  </thead>
  <tbody>
    ...
  </tbody>
</table>
```

### 표 하단

| #      | First  | Last     | Handle   |
| ------ | ------ | -------- | -------- |
| 1      | Mark   | Otto     | @mdo     |
| 2      | Jacob  | Thornton | @fat     |
| 3      | Larry  | the Bird | @twitter |
| Footer | Footer | Footer   | Footer   |

```html
<table class="table">
  <thead>
    ...
  </thead>
  <tbody>
    ...
  </tbody>
  <tfoot>
    ...
  </tfoot>
</table>
```

### 표제

`<caption>`은 표 제목과 같은 기능을 합니다. 화면 판독기를 사용하는 사용자가 표를 찾고 그 내용을 이해하고 읽을 것인지 결정할 수 있도록 도와줍니다.

| #    | First          | Last     | Handle |
| ---- | -------------- | -------- | ------ |
| 1    | Mark           | Otto     | @mdo   |
| 2    | Jacob          | Thornton | @fat   |
| 3    | Larry the Bird | @twitter |        |

```html
<table class="table table-sm">
  <caption>List of users</caption>
  <thead>
    ...
  </thead>
  <tbody>
    ...
  </tbody>
</table>
```

`.caption-top`으로 테이블 상단에 `<caption>`을 넣을 수도 있습니다.

```html
<table class="table caption-top">
  <caption>List of users</caption>
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Handle</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">1</th>
      <td>Mark</td>
      <td>Otto</td>
      <td>@mdo</td>
    </tr>
    <tr>
      <th scope="row">2</th>
      <td>Jacob</td>
      <td>Thornton</td>
      <td>@fat</td>
    </tr>
    <tr>
      <th scope="row">3</th>
      <td>Larry</td>
      <td>the Bird</td>
      <td>@twitter</td>
    </tr>
  </tbody>
</table>
```

## 반응형 표

반응형 표를 사용하면 테이블을 쉽게 가로로 스크롤할 수 있습니다. `.table`을 `.table-responsive`로 줄바꿈하여 모든 뷰포트에서 표가 반응하도록 만듭니다. 또는 `.table-responsive{-sm|-md|-lg|-xl|-xxl}`을 사용하여 반응형 테이블을 가질 최대 중단점을 선택합니다.

### 항상 반응형

모든 중단점에서 표 수평 스크롤에 `.table-responsive`를 사용합니다.

| #    | Heading | Heading | Heading | Heading | Heading | Heading | Heading | Heading | Heading |
| ---- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| 1    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    |
| 2    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    |
| 3    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    | Cell    |

```html
<div class="table-responsive">
  <table class="table">
    ...
  </table>
</div>
```

### 중단점으로 구분

특정 중단점까지 반응형 테이블을 생성하려면 필요에 따라 `.table-responsive{-sm|-md|-lg|-xl|-xxl}`을 사용합니다. 중단점 이상에서 표는 정상적으로 작동하며 가로로 스크롤되지 않습니다.

**이러한 표는 반응형 스타일이 특정 뷰포트 너비에 적용될 때까지 깨져보일 수 있습니다.**

```html
<div class="table-responsive">
  <table class="table">
    ...
  </table>
</div>

<div class="table-responsive-sm">
  <table class="table">
    ...
  </table>
</div>

<div class="table-responsive-md">
  <table class="table">
    ...
  </table>
</div>

<div class="table-responsive-lg">
  <table class="table">
    ...
  </table>
</div>

<div class="table-responsive-xl">
  <table class="table">
    ...
  </table>
</div>

<div class="table-responsive-xxl">
  <table class="table">
    ...
  </table>
</div>
```



### 변수

```scss
$table-cell-padding-y:        .5rem;
$table-cell-padding-x:        .5rem;
$table-cell-padding-y-sm:     .25rem;
$table-cell-padding-x-sm:     .25rem;

$table-cell-vertical-align:   top;

$table-color:                 $body-color;
$table-bg:                    transparent;
$table-accent-bg:             transparent;

$table-th-font-weight:        null;

$table-striped-color:         $table-color;
$table-striped-bg-factor:     .05;
$table-striped-bg:            rgba($black, $table-striped-bg-factor);

$table-active-color:          $table-color;
$table-active-bg-factor:      .1;
$table-active-bg:             rgba($black, $table-active-bg-factor);

$table-hover-color:           $table-color;
$table-hover-bg-factor:       .075;
$table-hover-bg:              rgba($black, $table-hover-bg-factor);

$table-border-factor:         .1;
$table-border-width:          $border-width;
$table-border-color:          $border-color;

$table-striped-order:         odd;

$table-group-separator-color: currentColor;

$table-caption-color:         $text-muted;

$table-bg-scale:              -80%;
```



--------

# Figures

Bootstrap에서 피규어 컴포넌트를 사용하여 관련 이미지 및 텍스트를 표시하기 위한 문서 및 예시입니다.

선택적 캡션이 있는 이미지와 같은 콘텐츠를 표시해야 할 때마다 `<figure>`를 사용하는 것을 고려해보세요.

포함된 `.figure`, `.figure-img`, `.figure-caption` 클래스를 사용하여 HTML5 `<figure>` 및 `<figcaption>` 요소에 대한 일부 기본 스타일을 제공합니다. Figure의 이미지에는 명시적인 크기가 없으므로 `<img>`에 `.img-fluid` 클래스를 추가하여 반응하도록 해야합니다.

```html
<figure class="figure">
  <img src="..." class="figure-img img-fluid rounded" alt="...">
  <figcaption class="figure-caption">A caption for the above image.</figcaption>
</figure>
```

[텍스트 유틸리티](https://getbootstrap.kr/docs/5.0/utilities/text/#text-alignment)를 사용하면 피규어의 캡션을 쉽게 정렬할 수 있습니다.

```html
<figure class="figure">
  <img src="..." class="figure-img img-fluid rounded" alt="...">
  <figcaption class="figure-caption text-end">A caption for the above image.</figcaption>
</figure>
```









