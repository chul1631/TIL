## Layout - Breakpoints

```
Breakpoints는 부트스트랩의 장치 또는 뷰포트 크기에서 반응형 레이아웃이 작동하는 방식을 결정하는 사용자 지정 가능한 너비입니다.
브레이크 포인트의 개념은 매우 간단합니다. 특정한 지시를 수행하기 바로 직전, 프로그램을 중단시키도록 간섭을 일으키는 것뿐이기 때문입니다. 그 구현은 하드웨어와 소프트웨어 상에서 모두 가능하지만 여기서는 그에 대해서는 다루지 않기로 합니다. 비록 브레이크포인트는 간단하지만, 복잡한 조합을 통해 버그를 손쉽게 해결해 줄 수 있는 기능도 있습니다.
```

### 핵심 개념

```
Breakpoints는 반응형 디자인의 구성 요소입니다. Breakpoints를 사용하여 레이아웃을 특정 뷰포트 크기 또는 기기에서 조정할 수 있는 시기를 제어합니다.

미디어 쿼리를 사용하여 Breakpoints로 CSS를 설계하세요. 미디어 쿼리는 브라우저 및 운영체제의 매개 변수 세트를 기반으로 조건부로 스타일을 적용 할 수있는 CSS의 기능입니다. 미디어 쿼리에서는 일반적으로 min-width를 사용합니다.

반응형 디자인과 모바일 우선이 목표입니다. Bootstrap의 CSS는 최소한의 스타일을 적용하여 가장 작은 Breakpoints에서 레이아웃이 작동하도록 설정 한 후 스타일에 계층을 적용하여 더 큰 기기에 맞게 해당 디자인이 조정 되도록 하는 것을 목표로 합니다. 이를 통해 CSS를 최적화하고 렌더링 시간을 개선하며 방텍스트에게 훌륭한 경험을 제공합니다.
```

## Available breakpoints![image-20220905143054805](C:\Users\User\OneDrive\바탕 화면\화면 캡처 2022-09-05 143059.png)

```
$grid-breakpoints: (
  xs: 0,
  sm: 576px,
  md: 768px,
  lg: 992px,
  xl: 1200px,
  xxl: 1400px
);
```



### 미디어 쿼리

```
Bootstrap은 모바일 우선으로 개발되었기 때문에 몇 가지 미디어 쿼리를 사용하여 레이아웃과 인터페이스에 적합한 중단점을 만듭니다. 이러한 중단점은 대부분 최소 뷰포트 너비를 기반으로 하며 뷰포트가 변경됨에 따라 요소를 확장할 수 있습니다.
```



#### Min-width

```
Bootstrap은 기본적으로 레이아웃, 그리드 시스템 및 구성 요소에 대한 소스 Sass 파일에서 다음 미디어 쿼리 범위(또는 중단점)를 사용합니다.

// Source mixins

// No media query necessary for xs breakpoint as it's effectively `@media (min-width: 0) { ... }`
@include media-breakpoint-up(sm) { ... }
@include media-breakpoint-up(md) { ... }
@include media-breakpoint-up(lg) { ... }
@include media-breakpoint-up(xl) { ... }
@include media-breakpoint-up(xxl) { ... }

// Usage

// Example: Hide starting at `min-width: 0`, and then show at the `sm` breakpoint
.custom-class {
  display: none;
}
@include media-breakpoint-up(sm) {
  .custom-class {
    display: block;
  }
}

```

### min-width를 사용하는 경우

- 스마트폰 등 가장 작은 사이즈에서의 레이아웃을 기본으로 하고, 점차 확장되어가는 형태로 CSS를 작성합니다.

![화면 캡처 2022-09-05 144827](C:\Users\User\OneDrive\바탕 화면\화면 캡처 2022-09-05 144827.png)



### Max-width를 사용하는 경우

```
데스크탑용의 가장 큰 화면 사이즈의 레이아웃을 기본으로 하고, 점차 축소하는 형태로 CSS를 작성합니다.
```

![화면 캡처 2022-09-05 144842](C:\Users\User\OneDrive\바탕 화면\화면 캡처 2022-09-05 144842.png)

### Single breakpoint

```
최소 및 최대 중단점 넓이를 사용하여 화면 크기의 단일 세그먼트를 대상으로하는 미디어 쿼리 및 믹스 인도 있습니다.
```

```scss
@include media-breakpoint-only(xs) { ... }
@include media-breakpoint-only(sm) { ... }
@include media-breakpoint-only(md) { ... }
@include media-breakpoint-only(lg) { ... }
@include media-breakpoint-only(xl) { ... }
@include media-breakpoint-only(xxl) { ... }
```

예를들어 `@include media-breakpoint-only(md) { ... }` 결과는 다음과 같습니다:

```scss
@media (min-width: 768px) and (max-width: 991.98px) { ... }
```

### Between breakpoints  

마찬가지로 미디어쿼리는 여러 breakpoint 넓이에 걸쳐있을 수 있습니다.

```scss
@include media-breakpoint-between(md, xl) { ... }
```

결과:

```scss
// Example
// Apply styles starting from medium devices and up to extra large devices
@media (min-width: 768px) and (max-width: 1199.98px) { ... }
```