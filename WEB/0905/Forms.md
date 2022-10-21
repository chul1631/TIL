# 폼

###### // Forms

다양한 폼 사용을 위한 폼 컨트롤 스타일, 레이아웃 옵션, 사용자 정의 컴포넌트의 예시와 사용 가이드입니다.



**폼 컨트롤**

다양한 상태를 지원하는 텍스트 입력과 텍스트 영역의 스타일을 설정할 수 있습니다.

(https://getbootstrap.kr/docs/5.0/forms/form-control/)

**셀렉트**

브라우저의 기본 셀렉트 요소의 초기 표시를 재정의할 수 있게 개선하였습니다.

(https://getbootstrap.kr/docs/5.0/forms/select/)

**체크박스 & 라디오버튼****

우리가 개선한 라디오 버튼과 체크 박스를 폼으로 사용하여, 입력 옵션을 선택할 수 있습니다.

(https://getbootstrap.kr/docs/5.0/forms/checks-radios/)

**범위**

브라우저의 기본 범위 선택 폼을 우리가 개선한 버전으로 사용할 수 있습니다.

(https://getbootstrap.kr/docs/5.0/forms/range/)

**입력 그룹**

입력 폼에 라벨과 버튼을 함께 사용하여 시멘틱한 마크업을 할 수 있습니다.

(https://getbootstrap.kr/docs/5.0/forms/input-group/)

**플로팅 라벨**

입력 필드 위로 떠오르는 동적인 폼 라벨을 간단하게 만들 수 있습니다.

(https://getbootstrap.kr/docs/5.0/forms/floating-labels/)

**레이아웃**

인라인, 수평 또는 복잡한 그리드 레이아웃을 폼으로 만들 수 있습니다.

(https://getbootstrap.kr/docs/5.0/forms/layout/)

**유효성 검사**

사용자 정의 또는 브라우저 기본 동작과 스타일을 통해 폼의 유효성 검사를 할 수 있습니다.(https://getbootstrap.kr/docs/5.0/forms/validation/)

## 개요

Bootstrap의 폼 컨트롤은 [Reboot된 폼 스타일](https://getbootstrap.kr/docs/5.0/content/reboot/#폼)과 함께 사용합니다. 이 클래스를 사용해 재정의 된 표시를 선택하면 브라우저나 기기 간에 보다 일관된 렌더링을 적용시킬 수 있습니다.

메일 인증이나 숫자 선택 등의 새로운 입력 컨트롤을 사용하기 위해 모든 입력에 적절한 `type` 속성 (예: 메일 주소에는 `email`, 숫자 정보에는 `number`)을 사용해 주세요.

```html
<form>
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
  </div>
  <div class="mb-3">
    <label for="exampleInputPassword1" class="form-label">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1">
  </div>
  <div class="mb-3 form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1">
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

## 폼 텍스트

블록 라벨(block-level) 또는 인라인 라벨(inline-level)의 폼 텍스트는 `.form-text`를 사용 합니다.

```html
<label for="inputPassword5" class="form-label">Password</label>
<input type="password" id="inputPassword5" class="form-control" aria-describedby="passwordHelpBlock">
<div id="passwordHelpBlock" class="form-text">
  Your password must be 8-20 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.
</div>
```

인라인 텍스트는 전형적인 인라인 HTML 요소(`<span>`, `<small>` 등)로 `.form-text` 클래스 이외에는 사용하지 않습니다.

```html
<div class="row g-3 align-items-center">
  <div class="col-auto">
    <label for="inputPassword6" class="col-form-label">Password</label>
  </div>
  <div class="col-auto">
    <input type="password" id="inputPassword6" class="form-control" aria-describedby="passwordHelpInline">
  </div>
  <div class="col-auto">
    <span id="passwordHelpInline" class="form-text">
      Must be 8-20 characters long.
    </span>
  </div>
</div>
```

## 비활성화된 폼

입력 폼에 `disabled` 불리언 속성을 추가하여 사용자의 조작을 막고 표시를 흐리게 할 수 있습니다.

```html
<input class="form-control" id="disabledInput" type="text" placeholder="Disabled input here..." disabled>
```

`<fieldset>`에 `disabled` 속성을 추가하면 그 안의 모든 폼 컨트롤이 비활성화됩니다. 브라우저는 `<fieldset disabled>` 내의 모든 기본 폼 컨트롤(`<input>`, `<select>`, 그리고 `<button>` 요소)을 비활성화시키면서 키보드와 마우스의 양쪽 조작을 막습니다.

그러나, 만약에 폼에 `<a class="btn btn-*">...</a>`과 같은 사용자 정의 버튼과 같은 요소가 포함되어 있다면, 이 경우 버튼 요소에는 `pointer-events: none` 스타일 밖에 적용되지 않습니다. 즉 포커스가 가고 키보드 사용도 가능합니다. 이 경우 이들 컨트롤을 수동으로 수정하고 포커스를 받지 않게 하기 위해 `tabindex="-1"`를 추가하여 지원 기술에도 그 상태를 알리기 위해 `aria-disabled="disabled"`를 추가해야 합니다.

```html
<form>
  <fieldset disabled>
    <legend>Disabled fieldset example</legend>
    <div class="mb-3">
      <label for="disabledTextInput" class="form-label">Disabled input</label>
      <input type="text" id="disabledTextInput" class="form-control" placeholder="Disabled input">
    </div>
    <div class="mb-3">
      <label for="disabledSelect" class="form-label">Disabled select menu</label>
      <select id="disabledSelect" class="form-select">
        <option>Disabled select</option>
      </select>
    </div>
    <div class="mb-3">
      <div class="form-check">
        <input class="form-check-input" type="checkbox" id="disabledFieldsetCheck" disabled>
        <label class="form-check-label" for="disabledFieldsetCheck">
          Can't check this
        </label>
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </fieldset>
</form>
```

## 접근성

지원 기술 사용자에게 목적을 전달할 수 있도록 모든 폼 컨트롤에는 접근 가능한 적절한 이름이 필요합니다. 이것을 가능하게 하는 가장 간단한 방법은 `<label>` 요소를 사용하거나 버튼의 경우에는 `<button>...</button>`과 같이 콘텐츠의 일부로서 충분한 설명적인 텍스트를 포함하는 것입니다.

이같이 `<label>` 사용이나 적절한 텍스트를 콘텐츠로 포함시킬 수 없을 경우에는 다음과 같은 접근 가능한 이름을 제공하는 대체 방법이 있습니다:

- `.visually-hidden` 클래스를 사용해 숨긴 `<label>` 요소
- `aria-labelledby`를 사용하여 라벨로써 기능 할 만한 기존 요소를 지정
- `title` 속성을 제공
- `aria-label`을 사용하여 요소에 액세스 가능한 이름을 명시적으로 설정

이들 모두가 존재하지 않을 경우 지원 기술은 `<input>` 및 `<textarea>` 요소의 접근 가능한 `placeholder` 속성을 사용할 수 있습니다. 이곳의 예시에서는 몇 가지 제안된 사례별 접근 방식을 제공하고 있습니다.

시각적으로 숨긴 콘텐츠(`.visually-hidden`, `aria-label`, 그리고 더 나아가 폼 필드에 콘텐츠가 입력되면 사라지는 `placeholder` 콘텐츠)를 사용하는 것은 지원 기술 사용자에게 유익할 수 있지만, 가시화된 라벨 텍스트가 없는 것은 다른 특정 사용자에게는 여전히 문제가 될 수 있습니다. 따라서 접근성과 사용성 양쪽의 관점에서 봐도 어떠한 형식으로든 가시화된 라벨을 제공 하는것이 최적의 접근 방식입니다.

---

# 폼 컨트롤

###### // Form controls

텍스트 형식의 `<input>`이나 `<textarea>`과 같은 폼 컨트롤에 사용자 정의 스타일, 크기 조정, 포커스 상태등의 업그레이드를 실시할 수 있습니다.

```html
<div class="mb-3">
  <label for="exampleFormControlInput1" class="form-label">Email address</label>
  <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com">
</div>
<div class="mb-3">
  <label for="exampleFormControlTextarea1" class="form-label">Example textarea</label>
  <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
</div>
```



## 크기 조절

`.form-control-lg`와 `.form-control-sm` 클래스를 사용해서 크기를 다르게 설정할 수 있습니다.

```html
<input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" aria-label=".form-control-lg example">
<input class="form-control" type="text" placeholder="Default input" aria-label="default input example">
<input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" aria-label=".form-control-sm example">
```

## 비활성화

`disabled` 불리언 속성을 추가하면 비활성화외형이 되면서 포인터 이벤트가 삭제됩니다.

```html
<input class="form-control" type="text" placeholder="Disabled input" aria-label="Disabled input example" disabled>
<input class="form-control" type="text" value="Disabled readonly input" aria-label="Disabled input example" disabled readonly>
```

## 읽기 전용

`readonly` 불리언 속성을 추가함으로써 입력 값의 변경을 막을 수 있습니다.

```html
<input class="form-control" type="text" value="Readonly input here..." aria-label="readonly input example" readonly>
```

## 읽기 전용 일반 텍스트

폼 내의 `<input readonly>` 요소를 일반 텍스트로 표시하고 싶은 경우, `.form-control-plaintext` 클래스를 사용합니다. 기본 폼 필드의 스타일을 삭제하고 그에 맞는 마진과 패딩을 유지한 일반 텍스트로 보여집니다.

```html
  <div class="mb-3 row">
    <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
    <div class="col-sm-10">
      <input type="text" readonly class="form-control-plaintext" id="staticEmail" value="email@example.com">
    </div>
  </div>
  <div class="mb-3 row">
    <label for="inputPassword" class="col-sm-2 col-form-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword">
    </div>
  </div>
```

```html
<form class="row g-3">
  <div class="col-auto">
    <label for="staticEmail2" class="visually-hidden">Email</label>
    <input type="text" readonly class="form-control-plaintext" id="staticEmail2" value="email@example.com">
  </div>
  <div class="col-auto">
    <label for="inputPassword2" class="visually-hidden">Password</label>
    <input type="password" class="form-control" id="inputPassword2" placeholder="Password">
  </div>
  <div class="col-auto">
    <button type="submit" class="btn btn-primary mb-3">Confirm identity</button>
  </div>
</form>
```

## 파일 선택

```html
<div class="mb-3">
  <label for="formFile" class="form-label">Default file input example</label>
  <input class="form-control" type="file" id="formFile">
</div>
<div class="mb-3">
  <label for="formFileMultiple" class="form-label">Multiple files input example</label>
  <input class="form-control" type="file" id="formFileMultiple" multiple>
</div>
<div class="mb-3">
  <label for="formFileDisabled" class="form-label">Disabled file input example</label>
  <input class="form-control" type="file" id="formFileDisabled" disabled>
</div>
<div class="mb-3">
  <label for="formFileSm" class="form-label">Small file input example</label>
  <input class="form-control form-control-sm" id="formFileSm" type="file">
</div>
<div>
  <label for="formFileLg" class="form-label">Large file input example</label>
  <input class="form-control form-control-lg" id="formFileLg" type="file">
</div>
```

## 색상

```html
<label for="exampleColorInput" class="form-label">Color picker</label>
<input type="color" class="form-control form-control-color" id="exampleColorInput" value="#563d7c" title="Choose your color">
```

## 데이터 목록

데이터 목록을 사용하면 `<input>` 안에서 엑세스(및 자동 보완) 할 수 있는 `<option>` 그룹을 작성할 수 있습니다. 이들은 `<select>` 요소와 비슷하지만 목록 표시에는 많은 제한과 차이가 있습니다. 대부분의 브라우저나 운영 체계는 `<datalist>` 요소를 어느 정도 지원하고 있지만, 그 표시에는 일관성이 없습니다.

```html
<label for="exampleDataList" class="form-label">Datalist example</label>
<input class="form-control" list="datalistOptions" id="exampleDataList" placeholder="Type to search...">
<datalist id="datalistOptions">
  <option value="San Francisco">
  <option value="New York">
  <option value="Seattle">
  <option value="Los Angeles">
  <option value="Chicago">
</datalist>
```

### 변수

`$input-*`는 (버튼빼고)대부분의 폼 컨트롤로 공유되고 있습니다.

```scss
$input-padding-y:                       $input-btn-padding-y;
$input-padding-x:                       $input-btn-padding-x;
$input-font-family:                     $input-btn-font-family;
$input-font-size:                       $input-btn-font-size;
$input-font-weight:                     $font-weight-base;
$input-line-height:                     $input-btn-line-height;

$input-padding-y-sm:                    $input-btn-padding-y-sm;
$input-padding-x-sm:                    $input-btn-padding-x-sm;
$input-font-size-sm:                    $input-btn-font-size-sm;

$input-padding-y-lg:                    $input-btn-padding-y-lg;
$input-padding-x-lg:                    $input-btn-padding-x-lg;
$input-font-size-lg:                    $input-btn-font-size-lg;

$input-bg:                              $white;
$input-disabled-bg:                     $gray-200;
$input-disabled-border-color:           null;

$input-color:                           $body-color;
$input-border-color:                    $gray-400;
$input-border-width:                    $input-btn-border-width;
$input-box-shadow:                      $box-shadow-inset;

$input-border-radius:                   $border-radius;
$input-border-radius-sm:                $border-radius-sm;
$input-border-radius-lg:                $border-radius-lg;

$input-focus-bg:                        $input-bg;
$input-focus-border-color:              tint-color($component-active-bg, 50%);
$input-focus-color:                     $input-color;
$input-focus-width:                     $input-btn-focus-width;
$input-focus-box-shadow:                $input-btn-focus-box-shadow;

$input-placeholder-color:               $gray-600;
$input-plaintext-color:                 $body-color;

$input-height-border:                   $input-border-width * 2;

$input-height-inner:                    add($input-line-height * 1em, $input-padding-y * 2);
$input-height-inner-half:               add($input-line-height * .5em, $input-padding-y);
$input-height-inner-quarter:            add($input-line-height * .25em, $input-padding-y * .5);

$input-height:                          add($input-line-height * 1em, add($input-padding-y * 2, $input-height-border, false));
$input-height-sm:                       add($input-line-height * 1em, add($input-padding-y-sm * 2, $input-height-border, false));
$input-height-lg:                       add($input-line-height * 1em, add($input-padding-y-lg * 2, $input-height-border, false));

$input-transition:                      border-color .15s ease-in-out, box-shadow .15s ease-in-out;
```

-----

# 셀렉트

###### // Select

브라우저의 기본 `<select>`를 사용자 정의 CSS로 만들어 요소의 초기 표시를 변경할 수 있습니다.

## 기본값

사용자 정의의 `<select>`를 사용하기 위해 필요한 클래스는 `.form-select`입니다. 이 스타일은 브러우저 제한으로 `<select>`의 처음 외형만 변경할 수 있고 그 안에 있는 `<option>` 들의 스타일 변경은 불가능합니다.

```html
<select class="form-select" aria-label="Default select example">
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```

## 크기 조절

같은 크기의 텍스트 입력에 맞춰 크고 작은 사용자 정의 셀렉트를 선택해 사용할 수 있습니다.

```html
<select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>

<select class="form-select form-select-sm" aria-label=".form-select-sm example">
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```

`multiple` 속성도 지원됩니다:

```html
<select class="form-select" multiple aria-label="multiple select example">
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```

 `size` 속성도 지원됩니다:

```html
<select class="form-select" size="3" aria-label="size 3 select example">
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```

## 비활성화

불리언 속성인 `disabled`를 셀렉트에 추가하면 비활성화된 외형으로 표시되며 포인터 이벤트가 삭제됩니다.

```html
<select class="form-select" aria-label="Disabled select example" disabled>
  <option selected>Open this select menu</option>
  <option value="1">One</option>
  <option value="2">Two</option>
  <option value="3">Three</option>
</select>
```

---



# 체크박스와 라디오버튼

###### // Checks and radios

완전히 새로워 진 체크 컴포넌트를 사용해 크로스 브라우저와 크로스 기기로 일관된 체크 박스와 라디오 버튼을 만들 수 있습니다.

## 접근

브라우저의 기본 체크 박스와 라디오 버튼은 `.form-check`의 도움을 받아 대체할 수 있습니다. 이는 두 입력 유형을 위한 클래스로, HTML 요소의 레이아웃과 동작을 개선하여 보다 높은 맞춤성과 크로스 브라우저의 일관성을 제공합니다. 체크 박스는 목록 중 하나 또는 여러 개를 선택하고, 라디오 버튼은 여러 목록 중 하나를 선택하는 것입니다.

구조적으로 `<input>`과 `<label>`은 형제 요소이며, `<label>` 안에 `<input>`이 들어 있는 것과는 다릅니다. 이것은 `<input>` 이라고 `<label>`을 연관짓기 위해 `id`와 `for`속성을 지정해야 하기 때문에 약간 장황해 집니다. 또한 `:checked` 나 `:disabled` 등, 모든 `<input>` 상태에는 형제 셀렉터(`~`)를 사용합니다. `.form-check-label` 클래스와 함께 사용함으로써 `<input>` 상태에 따라 각 항목의 텍스트를 쉽게 표시할 수 있습니다.

체크 박스에서는 Bootstrap 사용자 정의 아이콘을 사용하여 선택되었거나 선택전 상태를 표시하고 있습니다.

## 체크박스

```html
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
  <label class="form-check-label" for="flexCheckDefault">
    Default checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckChecked" checked>
  <label class="form-check-label" for="flexCheckChecked">
    Checked checkbox
  </label>
</div>
```

### 비활성화

`disabled` 속성을 추가하면 `<label>`과 함께 관련된 입력 폼이 흐릿한 비활성화상태로 표시됩니다.

```html
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckDisabled" disabled>
  <label class="form-check-label" for="flexCheckDisabled">
    Disabled checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="flexCheckCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexCheckCheckedDisabled">
    Disabled checked checkbox
  </label>
</div>
```

## 라디오버튼

```html
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
  <label class="form-check-label" for="flexRadioDefault1">
    Default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
  <label class="form-check-label" for="flexRadioDefault2">
    Default checked radio
  </label>
</div>
```

## 스위치

사용자 정의 체크 박스의 마크업을 가지고 있는 스위치는 토글 스위치를 렌더링하기 위해 `.form-switch` 클래스를 사용합니다. `disabled` 속성도 지원하고 있습니다.

```html
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
  <label class="form-check-label" for="flexSwitchCheckDefault">Default switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
  <label class="form-check-label" for="flexSwitchCheckChecked">Checked switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckDisabled" disabled>
  <label class="form-check-label" for="flexSwitchCheckDisabled">Disabled switch checkbox input</label>
</div>
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" id="flexSwitchCheckCheckedDisabled" checked disabled>
  <label class="form-check-label" for="flexSwitchCheckCheckedDisabled">Disabled checked switch checkbox input</label>
</div>
```

## 기본값 (중첩됨)

기본적으로 직계 형제인 체크 박스나 라디오 버튼은 `.form-check`로 수직으로 쌓여 적절한 간격으로 배치됩니다.

```html
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="defaultCheck1">
  <label class="form-check-label" for="defaultCheck1">
    Default checkbox
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="checkbox" value="" id="defaultCheck2" disabled>
  <label class="form-check-label" for="defaultCheck2">
    Disabled checkbox
  </label>
</div>
```

```html
<div class="form-check">
  <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="option1" checked>
  <label class="form-check-label" for="exampleRadios1">
    Default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2" value="option2">
  <label class="form-check-label" for="exampleRadios2">
    Second default radio
  </label>
</div>
<div class="form-check">
  <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios3" value="option3" disabled>
  <label class="form-check-label" for="exampleRadios3">
    Disabled radio
  </label>
</div>
```

## 인라인

`.form-check`에 `.form-check-inline` 클래스를 추가해 체크 박스나 라디오 버튼을 같은 수평 방향에 놓아 그룹화할 수 있습니다.

```html
<div class="form-check form-check-inline">
  <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
  <label class="form-check-label" for="inlineCheckbox1">1</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
  <label class="form-check-label" for="inlineCheckbox2">2</label>
</div>
<div class="form-check form-check-inline">
  <input class="form-check-input" type="checkbox" id="inlineCheckbox3" value="option3" disabled>
  <label class="form-check-label" for="inlineCheckbox3">3 (disabled)</label>
</div>
```

## 라벨 없음

라벨 텍스트가 없는 체크 박스나 라디오 버튼을 사용하고 싶을 때에는 `.form-check`를 생략합니다. 지원 기술을 위해 어떤 형태로든 접근성에 맞는 이름을 제공해야 하는 것을 잊지 마세요.(예를 들어, `aria-label`을 사용 한다든지 등). 자세한 내용은 [forms overview accessibility](https://getbootstrap.kr/docs/5.0/forms/overview/#accessibility)을 참조해 주세요.

```html
<div>
  <input class="form-check-input" type="checkbox" id="checkboxNoLabel" value="" aria-label="...">
</div>

<div>
  <input class="form-check-input" type="radio" name="radioNoLabel" id="radioNoLabel1" value="" aria-label="...">
</div>
```

## 버튼 토글

버튼과 같은 체크 박스나 라디오 버튼을 작성하기 위해서는 `<label>` 요소에 `.form-check-label`이 아닌 `.btn` 스타일을 사용합니다. 이러한 토글 버튼은 필요에 따라 다시 [button group](https://getbootstrap.kr/docs/5.0/components/button-group/)으로 그룹화할 수 있습니다.

```html
<input type="checkbox" class="btn-check" id="btn-check" autocomplete="off">
<label class="btn btn-primary" for="btn-check">Single toggle</label>
```

```html
<input type="checkbox" class="btn-check" id="btn-check-2" checked autocomplete="off">
<label class="btn btn-primary" for="btn-check-2">Checked</label>
```

```html
<input type="checkbox" class="btn-check" id="btn-check-3" autocomplete="off" disabled>
<label class="btn btn-primary" for="btn-check-3">Disabled</label>
```

시각적으로 이러한 체크 박스 토글버튼은 [button plugin toggle buttons](https://getbootstrap.kr/docs/5.0/components/buttons/#button-plugin)과 같습니다. 체크 박스의 토글 버튼은 스크린 리더에서는 “checked”/“not checked"로 표시되는데(외형은 체크 박스이기 때문에), 버튼의 토글 버튼은 “button”/“button pressed"로 표시됩니다. 이러한 두 가지 접근법 중 어느 쪽을 선택할지는 만들고자 하는 토글 유형과 그 토글이 체크 박스일 때와 실제 버튼일때 중, 어느 쪽이 사용자에게 더 의미가 있는지에 따라 달라집니다.

### 라디오버튼 토글 버튼

```html
<input type="radio" class="btn-check" name="options" id="option1" autocomplete="off" checked>
<label class="btn btn-secondary" for="option1">Checked</label>

<input type="radio" class="btn-check" name="options" id="option2" autocomplete="off">
<label class="btn btn-secondary" for="option2">Radio</label>

<input type="radio" class="btn-check" name="options" id="option3" autocomplete="off" disabled>
<label class="btn btn-secondary" for="option3">Disabled</label>

<input type="radio" class="btn-check" name="options" id="option4" autocomplete="off">
<label class="btn btn-secondary" for="option4">Radio</label>
```

### 테두리 스타일

다양한 종류의 `.btn`이 지원되고 있습니다

```html
<input type="checkbox" class="btn-check" id="btn-check-outlined" autocomplete="off">
<label class="btn btn-outline-primary" for="btn-check-outlined">Single toggle</label><br>

<input type="checkbox" class="btn-check" id="btn-check-2-outlined" checked autocomplete="off">
<label class="btn btn-outline-secondary" for="btn-check-2-outlined">Checked</label><br>

<input type="radio" class="btn-check" name="options-outlined" id="success-outlined" autocomplete="off" checked>
<label class="btn btn-outline-success" for="success-outlined">Checked success radio</label>

<input type="radio" class="btn-check" name="options-outlined" id="danger-outlined" autocomplete="off">
<label class="btn btn-outline-danger" for="danger-outlined">Danger radio</label>
```

---

# 범위

###### // Range

사용자 범위 컨트롤을 사용하여 크로스 브라우저에서 일관되게 표시할 수 있으며 맞춤 제작도 가능합니다..

## 개요

`<input type="range">`에 `.form-range`를 사용합니다. track (배경)과 thumb (값)은 어느 브라우저에서도 동일하게 표시되도록 스타일링되어 있습니다. 진행 상황을 시각적으로 보여주는 수단으로 thumb의 왼쪽 또는 오른쪽을 track으로 “채우는” 것을 지원하는 것은 Firefox뿐이라서 현재는 지원하지 않습니다.

```html
<label for="customRange1" class="form-label">Example range</label>
<input type="range" class="form-range" id="customRange1">
```

## 비활성화

`disabled` 블리언 속성을 추가하면 비활성화되어 표시되고 포인터 이벤트가 삭제됩니다.

```html
<label for="disabledRange" class="form-label">Disabled range</label>
<input type="range" class="form-range" id="disabledRange" disabled>
```

## 최소와 최대

범위 입력에는 `min`과 `max`으로 각각 `0` 과 `100`이라는 암묵적인 값을 가지고 있습니다. `min` 과 `max` 속성을 사용해 새롭게 값을 지정할 수 있습니다.

```html
<label for="customRange2" class="form-label">Example range</label>
<input type="range" class="form-range" min="0" max="5" id="customRange2">
```

## 단계

기본적으로, 범위 입력은 정수 값으로 “눌러"집니다 . 이것을 변경하려면 `step` 값을 지정합니다. 아래의 예시에서는 `step="0.5"`으로 지정해 스텝수를 두 배로 하는 것을 보여주고 있습니다.

```html
<label for="customRange3" class="form-label">Example range</label>
<input type="range" class="form-range" min="0" max="5" step="0.5" id="customRange3">
```

---

# 입력 그룹

###### // Input group

텍스트 입력, 사용자 정의 셀렉트, 사용자 파일 선택 등의 폼의 좌우에 텍스트, 버튼 혹은 버튼 그룹을 추가해 폼 컨트롤을 간단하게 확장할 수 있습니다.

## 기본 예시

추가 기능(add-on) 이나 버튼을 입력의 한쪽 혹은 양쪽에 배치할 수 있습니다. `<label>`은 입력 그룹 밖에 작성해야 합니다.

```html
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon1">@</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2">
  <span class="input-group-text" id="basic-addon2">@example.com</span>
</div>

<label for="basic-url" class="form-label">Your vanity URL</label>
<div class="input-group mb-3">
  <span class="input-group-text" id="basic-addon3">https://example.com/users/</span>
  <input type="text" class="form-control" id="basic-url" aria-describedby="basic-addon3">
</div>

<div class="input-group mb-3">
  <span class="input-group-text">$</span>
  <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)">
  <span class="input-group-text">.00</span>
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Username" aria-label="Username">
  <span class="input-group-text">@</span>
  <input type="text" class="form-control" placeholder="Server" aria-label="Server">
</div>

<div class="input-group">
  <span class="input-group-text">With textarea</span>
  <textarea class="form-control" aria-label="With textarea"></textarea>
</div>
```

## 줄 바꿈

입력 그룹은 입력 그룹 내의 사용자 정의 폼 유효성 검사에 대응하기 위해 기본적으로 `flex-wrap: wrap`으로 감싸고 있습니다. 이것을 비활성화하려면 `.flex-nowrap`을 추가하여 사용합니다.

```html
<div class="input-group flex-nowrap">
  <span class="input-group-text" id="addon-wrapping">@</span>
  <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="addon-wrapping">
</div>
```

## 크기 조절

상대적으로 크기를 조정해 주는 클래스를 `.input-group`이 있는 곳에 추가하면, 그 안의 콘텐츠가 자동으로 재조정됩니다. 각 요소에 폼 컨트롤 크기 조정 클래스를 추가할 필요가 없습니다

**각각의 입력 그룹 요소의 크기 변경은 지원하지 않습니다.**

```html
<div class="input-group input-group-sm mb-3">
  <span class="input-group-text" id="inputGroup-sizing-sm">Small</span>
  <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-sm">
</div>

<div class="input-group mb-3">
  <span class="input-group-text" id="inputGroup-sizing-default">Default</span>
  <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default">
</div>

<div class="input-group input-group-lg">
  <span class="input-group-text" id="inputGroup-sizing-lg">Large</span>
  <input type="text" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-lg">
</div>
```

## 체크박스와 라디오버튼

입력 그룹의 추가 기능 자리에 텍스트 대신 체크 박스나 라디오 버튼 같은 옵션을 배치할 수 있습니다. 우리는 입력 부분에 표시되는 텍스트가 없는 경우 `.form-check-input`에 `.mt-0`을 추가하는 것을 권장합니다.

```html
<div class="input-group mb-3">
  <div class="input-group-text">
    <input class="form-check-input mt-0" type="checkbox" value="" aria-label="Checkbox for following text input">
  </div>
  <input type="text" class="form-control" aria-label="Text input with checkbox">
</div>

<div class="input-group">
  <div class="input-group-text">
    <input class="form-check-input mt-0" type="radio" value="" aria-label="Radio button for following text input">
  </div>
  <input type="text" class="form-control" aria-label="Text input with radio button">
</div>
```

## 복수 입력

복수의 `<input>`은 시각적으로 지원되고 있지만, 유효성 검사 확인을 사용할 때에는 하나의 `<input>`을 가진 입력 그룹에서만 사용 가능합니다.

```html
<div class="input-group">
  <span class="input-group-text">First and last name</span>
  <input type="text" aria-label="First name" class="form-control">
  <input type="text" aria-label="Last name" class="form-control">
</div>
```

## 복수 애드온

복수의 추가 기능을 지원하고 있어 체크 박스나 라디오 버튼과 함께 사용할 수 있습니다.

```html
<div class="input-group mb-3">
  <span class="input-group-text">$</span>
  <span class="input-group-text">0.00</span>
  <input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
</div>

<div class="input-group">
  <input type="text" class="form-control" aria-label="Dollar amount (with dot and two decimal places)">
  <span class="input-group-text">$</span>
  <span class="input-group-text">0.00</span>
</div>
```

## 버튼 애드온

```html
<div class="input-group mb-3">
  <button class="btn btn-outline-secondary" type="button" id="button-addon1">Button</button>
  <input type="text" class="form-control" placeholder="" aria-label="Example text with button addon" aria-describedby="button-addon1">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="button-addon2">
  <button class="btn btn-outline-secondary" type="button" id="button-addon2">Button</button>
</div>

<div class="input-group mb-3">
  <button class="btn btn-outline-secondary" type="button">Button</button>
  <button class="btn btn-outline-secondary" type="button">Button</button>
  <input type="text" class="form-control" placeholder="" aria-label="Example text with two button addons">
</div>

<div class="input-group">
  <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username with two button addons">
  <button class="btn btn-outline-secondary" type="button">Button</button>
  <button class="btn btn-outline-secondary" type="button">Button</button>
</div>
```

## 드롭다운이 있는 버튼

```html
<div class="input-group mb-3">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
  <input type="text" class="form-control" aria-label="Text input with dropdown button">
</div>

<div class="input-group mb-3">
  <input type="text" class="form-control" aria-label="Text input with dropdown button">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
</div>

<div class="input-group">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action before</a></li>
    <li><a class="dropdown-item" href="#">Another action before</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
  <input type="text" class="form-control" aria-label="Text input with 2 dropdown buttons">
  <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
</div>
```

## 분할 버튼

```html
<div class="input-group mb-3">
  <button type="button" class="btn btn-outline-secondary">Action</button>
  <button type="button" class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
  <input type="text" class="form-control" aria-label="Text input with segmented dropdown button">
</div>

<div class="input-group">
  <input type="text" class="form-control" aria-label="Text input with segmented dropdown button">
  <button type="button" class="btn btn-outline-secondary">Action</button>
  <button type="button" class="btn btn-outline-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu dropdown-menu-end">
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item" href="#">Another action</a></li>
    <li><a class="dropdown-item" href="#">Something else here</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated link</a></li>
  </ul>
</div>
```

## 사용자 지정 폼

입력 그룹에는 사용자 정의 셀렉트 및 사용자 정의 파일 선택 지원이 표함되어 있습니다. 브라우저의 기본 버전에서는 이러한 기능은 지원되지 않습니다.

### 사용자 지정 셀렉트

```html
<div class="input-group mb-3">
  <label class="input-group-text" for="inputGroupSelect01">Options</label>
  <select class="form-select" id="inputGroupSelect01">
    <option selected>Choose...</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </select>
</div>

<div class="input-group mb-3">
  <select class="form-select" id="inputGroupSelect02">
    <option selected>Choose...</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </select>
  <label class="input-group-text" for="inputGroupSelect02">Options</label>
</div>

<div class="input-group mb-3">
  <button class="btn btn-outline-secondary" type="button">Button</button>
  <select class="form-select" id="inputGroupSelect03" aria-label="Example select with button addon">
    <option selected>Choose...</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </select>
</div>

<div class="input-group">
  <select class="form-select" id="inputGroupSelect04" aria-label="Example select with button addon">
    <option selected>Choose...</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </select>
  <button class="btn btn-outline-secondary" type="button">Button</button>
</div>
```

### 사용자 지정 파일 선택

```html
<div class="input-group mb-3">
  <label class="input-group-text" for="inputGroupFile01">Upload</label>
  <input type="file" class="form-control" id="inputGroupFile01">
</div>

<div class="input-group mb-3">
  <input type="file" class="form-control" id="inputGroupFile02">
  <label class="input-group-text" for="inputGroupFile02">Upload</label>
</div>

<div class="input-group mb-3">
  <button class="btn btn-outline-secondary" type="button" id="inputGroupFileAddon03">Button</button>
  <input type="file" class="form-control" id="inputGroupFile03" aria-describedby="inputGroupFileAddon03" aria-label="Upload">
</div>

<div class="input-group">
  <input type="file" class="form-control" id="inputGroupFile04" aria-describedby="inputGroupFileAddon04" aria-label="Upload">
  <button class="btn btn-outline-secondary" type="button" id="inputGroupFileAddon04">Button</button>
</div>
```

---

# 플로팅 라벨

###### // Floating labels

입력 필드 위로 떠오르는 예쁘고 간단한 폼 라벨을 작성할 수 있습니다.

## 예시

`<input class="form-control">`과 `<label>` 요소를 함께 `.form-floating`으로 감싸면, Bootstrap의 텍스트 형식의 폼 필드에서 플로팅 라벨 사용이 가능합니다. CSS만으로 플로팅 라벨을 실현하는 방법은 `:placeholder-shown` 가상 요소를 사용하기 때문에 각 `<input>`에는 `placeholder`가 필요합니다. 또한 형제 셀렉터(예를 들어, `~`)를 사용하기 때문에 `<input>`이 처음에 와야 하는 순서에 주의해 주세요.

```html
<div class="form-floating mb-3">
  <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
  <label for="floatingInput">Email address</label>
</div>
<div class="form-floating">
  <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
  <label for="floatingPassword">Password</label>
</div>
```

`value`가 이미 정의되어 있는 경우에는 `<label>`이 자동으로 플로팅 되어져 있습니다.

```html
<form class="form-floating">
  <input type="email" class="form-control" id="floatingInputValue" placeholder="name@example.com" value="test@example.com">
  <label for="floatingInputValue">Input with value</label>
</form>
```

또한, 폼 유효성 검사에서도 기대한대로 잘 동작합니다.

```html
<form class="form-floating">
  <input type="email" class="form-control is-invalid" id="floatingInputInvalid" placeholder="name@example.com" value="test@example.com">
  <label for="floatingInputInvalid">Invalid input</label>
</form>
```

## Textarea

기본적으로, `.form-control`을 사용하는 `<textarea>`는 `<input>`의 높이와 동일합니다.

```html
<div class="form-floating">
  <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea"></textarea>
  <label for="floatingTextarea">Comments</label>
</div>
```

`<textarea>`의 높이를 변경하고 싶다면, `rows`속성 대신, 명시적인 `height`를 사용해 설정해 주세요(인라인 또는 사용자 CSS를 사용합니다).

```html
<div class="form-floating">
  <textarea class="form-control" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"></textarea>
  <label for="floatingTextarea2">Comments</label>
</div>
```

## 셀렉트

`.form-control` 이외에서의 플로팅 라벨은 `.form-select`에서만 사용할 수 있습니다. 이들은 똑같이 동작하지만, `<input>`과는 다르게 `<label>`이 항상 플로팅 된 상태로 표시됩니다. **`size`와 `multiple` 선택자는 지원되지 않습니다.**

```html
<div class="form-floating">
  <select class="form-select" id="floatingSelect" aria-label="Floating label select example">
    <option selected>Open this select menu</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </select>
  <label for="floatingSelect">Works with selects</label>
</div>
```

---

## 레이아웃

Bootstrap 그리드 시스템을 사용할 경우, 폼 요소는 반드시 컬럼 클래스 내에 배치해야 합니다.

```html
<div class="row g-2">
  <div class="col-md">
    <div class="form-floating">
      <input type="email" class="form-control" id="floatingInputGrid" placeholder="name@example.com" value="mdo@example.com">
      <label for="floatingInputGrid">Email address</label>
    </div>
  </div>
  <div class="col-md">
    <div class="form-floating">
      <select class="form-select" id="floatingSelectGrid" aria-label="Floating label select example">
        <option selected>Open this select menu</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
      </select>
      <label for="floatingSelectGrid">Works with selects</label>
    </div>
  </div>
</div>
```



---

# 레이아웃

###### // Layout

인라인, 수평, 사용자 그리드 등의 구현 방법까지 폼에 구조를 갖게 하는 폼 레이아웃 옵션을 준비하고 있습니다.

## 폼

폼 필드의 모든 그룹은 `<form>` 요소 안에 존재해야 합니다. Bootstrap은 `<form>` 요소에 기본 스타일링은 제공하지 않지만 기본 제공되는 몇 가지 강력한 브라우저 기능이 있습니다.

- 브라우저 폼은 처음이신가요? 사용 가능한 속성의 개요 및 전체 목록에 대해서는 [the MDN form docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)를 참조해 주세요.
- `<form>` 내 `<button>`의 기본은 `type="submit"` 이므로, 구체적으로 항상 `type`을 사용해 주세요.
- `<form>`의 `disabled` 속성을 사용하여 폼 내의 모든 폼 요소를 무효화 시킬수 있습니다.

Bootstrap은 거의 모든 폼 컨트롤에 `display: block`과 `width: 100%`를 적용하여 기본적으로 수직으로 쌓고 있습니다. 추가 클래스를 사용하여 폼 별로 이 레이아웃을 바꿀 수 있습니다.



## 유틸리티

[마진 유틸리티](https://getbootstrap.kr/docs/5.0/utilities/spacing/)는 폼에 구조를 추가하는 가장 간단한 방법입니다. 이들은 라벨, 컨트롤, 옵션 폼 텍스트, 폼 검증 문구의 기본적인 그룹화를 제공합니다. 우리는 일관성을 유지하기 위해 `margin-bottom`유틸리티를 사용해 폼 전체에 하나의 방향성을 사용할 것을 권장합니다.

`<fieldset>`나 `<div>` 등의 거의 모든 요소를 사용하여 자유롭게 폼을 작성해 주세요.

```html
<div class="mb-3">
  <label for="formGroupExampleInput" class="form-label">Example label</label>
  <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input placeholder">
</div>
<div class="mb-3">
  <label for="formGroupExampleInput2" class="form-label">Another label</label>
  <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Another input placeholder">
</div>
```

## 폼 그리드

보다 복잡한 폼은 그리드 클래스를 사용하여 만들 수 있습니다. 그리드 클래스를 사용해 여러 개의 컬럼, 다양한 너비, 추가 배치 옵션이 필요한 폼 레이아웃 표현이 가능합니다.

**Sass 변수 `$enable-grid-classes`가 활성화 되어 있어야 합니다** (기본이 활성화 상태임).

```html
<div class="row">
  <div class="col">
    <input type="text" class="form-control" placeholder="First name" aria-label="First name">
  </div>
  <div class="col">
    <input type="text" class="form-control" placeholder="Last name" aria-label="Last name">
  </div>
</div>
```

## 거터

[거터 제어자 클래스](https://getbootstrap.kr/docs/5.0/layout/gutters/)를 추가하는 것으로, 인라인이나 블록 방향으로 거터의 너비를 조정할 수 있습니다. **이또한 Sass 변수 `$enable-grid-classes`가 활성화 되어 있어야 합니다.** (기본값이 활성화 상태임).

```html
<div class="row g-3">
  <div class="col">
    <input type="text" class="form-control" placeholder="First name" aria-label="First name">
  </div>
  <div class="col">
    <input type="text" class="form-control" placeholder="Last name" aria-label="Last name">
  </div>
</div>
```

그리드 시스템을 사용하여 보다 복잡한 레이아웃을 만들 수도 있습니다.



```html
<form class="row g-3">
  <div class="col-md-6">
    <label for="inputEmail4" class="form-label">Email</label>
    <input type="email" class="form-control" id="inputEmail4">
  </div>
  <div class="col-md-6">
    <label for="inputPassword4" class="form-label">Password</label>
    <input type="password" class="form-control" id="inputPassword4">
  </div>
  <div class="col-12">
    <label for="inputAddress" class="form-label">Address</label>
    <input type="text" class="form-control" id="inputAddress" placeholder="1234 Main St">
  </div>
  <div class="col-12">
    <label for="inputAddress2" class="form-label">Address 2</label>
    <input type="text" class="form-control" id="inputAddress2" placeholder="Apartment, studio, or floor">
  </div>
  <div class="col-md-6">
    <label for="inputCity" class="form-label">City</label>
    <input type="text" class="form-control" id="inputCity">
  </div>
  <div class="col-md-4">
    <label for="inputState" class="form-label">State</label>
    <select id="inputState" class="form-select">
      <option selected>Choose...</option>
      <option>...</option>
    </select>
  </div>
  <div class="col-md-2">
    <label for="inputZip" class="form-label">Zip</label>
    <input type="text" class="form-control" id="inputZip">
  </div>
  <div class="col-12">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="gridCheck">
      <label class="form-check-label" for="gridCheck">
        Check me out
      </label>
    </div>
  </div>
  <div class="col-12">
    <button type="submit" class="btn btn-primary">Sign in</button>
  </div>
</form>
```

## 수평 폼

폼 그룹에 `.row` 클래스를 추가하고 `.col-*-*` 클래스를 사용해 라벨이나 컨트롤의 폭을 지정하는 것으로, 그리드를 사용한 수평 방향의 폼을 작성할 수 있습니다. `<label>`에는 반드시 `.col-form-label`을 추가하여 관련 폼 컨트롤과 함께 수직 방향의 중앙에 배치하도록 합니다.

때에 따라서는 완벽한 배치를 위해 여백(마진이나 패딩) 유틸리티를 사용할 필요가 있을지도 모릅니다. 예를 들어 아래의 예시와 같이 오른쪽의 싸인 라디오 버튼의 라벨과의 정렬을 맞추기 위해 `padding-top`을 삭제하는 유틸리티를 추가합니다.

```html
<form>
  <div class="row mb-3">
    <label for="inputEmail3" class="col-sm-2 col-form-label">Email</label>
    <div class="col-sm-10">
      <input type="email" class="form-control" id="inputEmail3">
    </div>
  </div>
  <div class="row mb-3">
    <label for="inputPassword3" class="col-sm-2 col-form-label">Password</label>
    <div class="col-sm-10">
      <input type="password" class="form-control" id="inputPassword3">
    </div>
  </div>
  <fieldset class="row mb-3">
    <legend class="col-form-label col-sm-2 pt-0">Radios</legend>
    <div class="col-sm-10">
      <div class="form-check">
        <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1" checked>
        <label class="form-check-label" for="gridRadios1">
          First radio
        </label>
      </div>
      <div class="form-check">
        <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios2" value="option2">
        <label class="form-check-label" for="gridRadios2">
          Second radio
        </label>
      </div>
      <div class="form-check disabled">
        <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios3" value="option3" disabled>
        <label class="form-check-label" for="gridRadios3">
          Third disabled radio
        </label>
      </div>
    </div>
  </fieldset>
  <div class="row mb-3">
    <div class="col-sm-10 offset-sm-2">
      <div class="form-check">
        <input class="form-check-input" type="checkbox" id="gridCheck1">
        <label class="form-check-label" for="gridCheck1">
          Example checkbox
        </label>
      </div>
    </div>
  </div>
  <button type="submit" class="btn btn-primary">Sign in</button>
</form>
```

### 수평 폼 라벨 크기 조절

`.form-control-lg`와 `.form-control-sm`의 사용에 따라 `<label>`이나 `<legend>`에 `.col-form-label-sm` 이나 `.col-form-label-lg`를 사용해 주세요.

```html
<div class="row mb-3">
  <label for="colFormLabelSm" class="col-sm-2 col-form-label col-form-label-sm">Email</label>
  <div class="col-sm-10">
    <input type="email" class="form-control form-control-sm" id="colFormLabelSm" placeholder="col-form-label-sm">
  </div>
</div>
<div class="row mb-3">
  <label for="colFormLabel" class="col-sm-2 col-form-label">Email</label>
  <div class="col-sm-10">
    <input type="email" class="form-control" id="colFormLabel" placeholder="col-form-label">
  </div>
</div>
<div class="row">
  <label for="colFormLabelLg" class="col-sm-2 col-form-label col-form-label-lg">Email</label>
  <div class="col-sm-10">
    <input type="email" class="form-control form-control-lg" id="colFormLabelLg" placeholder="col-form-label-lg">
  </div>
</div>
```

## 열 크기 조절

지금까지의 예시에서 봐왔듯 그리드 시스템에는 `.row` 안에 `.col`을 몇 개라도 배치할 수 있습니다. 이 열들은 이용 가능한 너비를 균등하게 분할합니다. 또한 `.col-sm-7`와 같은 특정 컬럼 클래스를 사용하여 컬럼 서브셋을 선택하여 공간을 늘리거나 줄이거나 나머지 `.col`들을 균등 분할할 수도 있습니다.

```html
<div class="row g-3">
  <div class="col-sm-7">
    <input type="text" class="form-control" placeholder="City" aria-label="City">
  </div>
  <div class="col-sm">
    <input type="text" class="form-control" placeholder="State" aria-label="State">
  </div>
  <div class="col-sm">
    <input type="text" class="form-control" placeholder="Zip" aria-label="Zip">
  </div>
</div>
```

## 자동 크기 조절

아래 예시에서는 플렉스박스 유틸리티를 사용하여 콘텐츠를 수직 방향으로 중앙에 오게 하고 `.col`을 `.col-auto`로 변경함으로써 필요한 만큼 컬럼이 공간을 차지하도록 하고 있습니다. 콘텐츠에 따라 컬럼의 크기가 다르게 설정됩니다.

```html
<form class="row gy-2 gx-3 align-items-center">
  <div class="col-auto">
    <label class="visually-hidden" for="autoSizingInput">Name</label>
    <input type="text" class="form-control" id="autoSizingInput" placeholder="Jane Doe">
  </div>
  <div class="col-auto">
    <label class="visually-hidden" for="autoSizingInputGroup">Username</label>
    <div class="input-group">
      <div class="input-group-text">@</div>
      <input type="text" class="form-control" id="autoSizingInputGroup" placeholder="Username">
    </div>
  </div>
  <div class="col-auto">
    <label class="visually-hidden" for="autoSizingSelect">Preference</label>
    <select class="form-select" id="autoSizingSelect">
      <option selected>Choose...</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>
  </div>
  <div class="col-auto">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="autoSizingCheck">
      <label class="form-check-label" for="autoSizingCheck">
        Remember me
      </label>
    </div>
  </div>
  <div class="col-auto">
    <button type="submit" class="btn btn-primary">Submit</button>
  </div>
</form>
```

그리고 그것을 크기별 컬럼 클래스에서 다시 한번 조합할 수 있습니다.

```html
<form class="row gx-3 gy-2 align-items-center">
  <div class="col-sm-3">
    <label class="visually-hidden" for="specificSizeInputName">Name</label>
    <input type="text" class="form-control" id="specificSizeInputName" placeholder="Jane Doe">
  </div>
  <div class="col-sm-3">
    <label class="visually-hidden" for="specificSizeInputGroupUsername">Username</label>
    <div class="input-group">
      <div class="input-group-text">@</div>
      <input type="text" class="form-control" id="specificSizeInputGroupUsername" placeholder="Username">
    </div>
  </div>
  <div class="col-sm-3">
    <label class="visually-hidden" for="specificSizeSelect">Preference</label>
    <select class="form-select" id="specificSizeSelect">
      <option selected>Choose...</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>
  </div>
  <div class="col-auto">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="autoSizingCheck2">
      <label class="form-check-label" for="autoSizingCheck2">
        Remember me
      </label>
    </div>
  </div>
  <div class="col-auto">
    <button type="submit" class="btn btn-primary">Submit</button>
  </div>
</form>
```

## 인라인 폼

`.row-cols-*` 클래스를 사용해, 수평 방향의 레이아웃을 만듭니다. [거터 제어자 클래스](https://getbootstrap.kr/docs/5.0/layout/gutters/)를 추가함으로써 수평 방향과 수직 방향에 거터를 적절하게 줄 수 있습니다. 좁은 모바일 뷰포트에서 `.col-12` 는 폼 컨트롤 등을 쌓을 수 있도록 도와줍니다. `.align-items-center`를 사용해 폼 요소를 중앙에 오게 해 `.form-checkbox`의 위치가 예쁘게 적용되었습니다.

```html
<form class="row row-cols-lg-auto g-3 align-items-center">
  <div class="col-12">
    <label class="visually-hidden" for="inlineFormInputGroupUsername">Username</label>
    <div class="input-group">
      <div class="input-group-text">@</div>
      <input type="text" class="form-control" id="inlineFormInputGroupUsername" placeholder="Username">
    </div>
  </div>

  <div class="col-12">
    <label class="visually-hidden" for="inlineFormSelectPref">Preference</label>
    <select class="form-select" id="inlineFormSelectPref">
      <option selected>Choose...</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>
  </div>

  <div class="col-12">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="inlineFormCheck">
      <label class="form-check-label" for="inlineFormCheck">
        Remember me
      </label>
    </div>
  </div>

  <div class="col-12">
    <button type="submit" class="btn btn-primary">Submit</button>
  </div>
</form>
```

----

# 유효성 검사

###### // Validation

HTML5 폼 유효성 검사에서는 브라우저의 기본 동작이나 사용자 정의 스타일과 JavaScript를 이용해 사용자에게 가치있고 실용적인 전달을 제공합니다.

## 작동 원리

Bootstrap에서 사용하고 있는 폼 유효성 검사 구조를 소개합니다:

- HTML의 폼 유효성 검사는 CSS의 두개의 가상 클래스 `:invalid`와 `:valid`를 사용해 `<input>`, `<select>`, `<textarea>` 요소에 적용됩니다.
- Bootstrap는 `:invalid` 과 `:valid` 스타일을 부모 클래스 `.was-validated`에 범위를 지정하고 일반적으로 `<form>`에 적용합니다. 그렇지 않으면 값이 없는 필수 필드는 페이지 로드 시 잘못된 상태로 표시됩니다. 이와 같이 해서 그것들을 유효하게 하는 시기를 선택할 수 있습니다.(보통은 폼의 송신이 시도된 후)
- 폼의 외형을 새로 적용하려면(예를 들어, AJAX를 사용한 동적인 폼 송신의 경우), 송신 후에 `.was-validated` 클래스를 `<form>`으로부터 다시 삭제합니다.
- 폴백으로서 [server-side validation](https://getbootstrap.kr/docs/5.0/forms/validation/#server-side)의 가상 클래스 대신 `.is-invalid`와 `.is-valid` 클래스를 사용할 수 있습니다. 이 클래스들은 부모 클래스인 `.was-validated`를 필요로 하지 않습니다.
- (현시점에서는)CSS 동작에 제약이 있기 때문에 사용자 정의 JavaScript의 도움을 받지 않고 DOM 내에서 폼 컨트롤의 앞에 있는 `<label>`에 스타일을 적용할 수 없습니다.
- 모든 모던 브라우저는 폼 컨트롤을 유효성 검사하기 위한 일련의 JavaScript 메소드인 [constraint validation API](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#the-constraint-validation-api)를 지원합니다.
- 전달 문구는 [browser defaults](https://getbootstrap.kr/docs/5.0/forms/validation/#browser-defaults) (브라우저별로 다르기 때문에 CSS에서 스타일 변경은 할 수 없습니다)나 HTML과 CSS를 추가한 사용자 정의 전달 스타일을 이용할 수도 있습니다.
- JavaScript의 `setCustomValidity`를 사용해 사용자 정의의 유효성 문구를 제공할 수도 있습니다.

이 점들을 고려하여 사용자 정의 폼 유효성 검사 스타일, 선택적인 서버 사이드 클래스 및 브라우저 기본값에 대해, 아래의 데모를 확인 부탁드립니다.

## 사용자 지정 스타일

Bootstrap 폼 유효성 검사 문구를 사용자 정의 하려면, `<form>`에 `novalidate`라고 하는 불리언 속성을 추가할 필요가 있습니다. 이는 브라우저의 기본 전달 툴팁을 비활성화시켜 JavaScript에서 폼 검증 API에 대한 접근을 제공합니다. 아래 예시의 전송 버튼을 눌러 보세요. JavaScript가 전송 버튼을 가로채고 전달합니다. 전송 버튼을 누르면, 폼 컨트롤에 `:invalid` 과 `:valid`의 스타일이 적용되고 있는 것을 알 수 있습니다.

색상, 모서리, 포커스 스타일 및 배경 아이콘을 이용해 더 나은 사용자 정의 전달 스타일을 적용하고 있습니다. `<select>`의 배경 아이콘은 `.form-select`에서만 사용 가능하며 `.form-control`에서는 사용할 수 없습니다.

https://getbootstrap.kr/docs/5.0/forms/validation/