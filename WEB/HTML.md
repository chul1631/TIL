# HTML: Hypertext Markup Language



**HTML**(HyperText Markup Language)은 웹을 이루는 가장 기초적인 구성 요소로, 웹 콘텐츠의 의미와 구조를 정의할 때 사용합니다. HTML 이외의 다른 기술은 일반적으로 웹 페이지의 모양/표현 ([CSS](https://developer.mozilla.org/ko/docs/Web/CSS)), 또는 기능/동작 ([JavaScript](https://developer.mozilla.org/ko/docs/Web/JavaScript))을 설명하는 데 사용됩니다.

HTML은 웹 브라우저에 표시되는 글과 이미지 등의 다양한 콘텐츠를 표시하기 위해 "마크업"을 사용합니다. HTML 마크업은 다양한 "요소"를 사용하는데, 요소에는 많은 종류가 존재합니다.



#### 1) `<area>` 요소

- `<map>`태그로 정의되는 이미지맵에서 개별 링크 영역을 지정. 

- 이미지의 핫스팟 영역을 정의하고 [하이퍼링크 (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Hyperlink)를 추가할 수 있습니다.

-  [`<map>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/map) 요소 안에서만 사용할 수 있습니다. 

  

##### (1) alt

- 이미지를 출력하지 않는 브라우저에서 대신 표시할 대안 텍스트입니다. 텍스트의 내용은 대안 텍스트 없이 이미지만 표시할 때와 동일한 수준의 선택지를 나타낼 수 있어야 합니다. [`href`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/area#attr-href) 특성이 존재할 경우 필수 사항입니다.

##### (2) href 

- `<area>` 하이퍼링크의 대상입니다. 유효한 URL이야 합니다. 생략할 경우, 이 `<area>` 요소는 하	이퍼링크를 나타내지 않습니다.

#####  (3) coords 

- 핫스팟 영역을 지정하는 일련의 좌표입니다. 값의 수와 의미는 `shape` 특성의 값에 따라 달라집니다.

- `rect`: 좌상단과 우하단을 나타내는 두 개의 x, y 쌍입니다.
- `circle`: `x,y,r`로서 `x,y`는 원의 중심 좌표이며 `r`은 반지름입니다.
- `poly`: 다각형의 꼭지점을 나타내는 다수의 x, y 쌍(`x1,y1,x2,y2,x3,y3,...`)입니다.

​		값의 단위는 CSS 픽셀입니다.



**구조**

```html
<map name="primary">
  <area shape="circle" coords="200,250,25" href="another.htm" />
  <area shape="default" nohref />
</map>
<img usemap="#primary" src="http://placehold.it/350x150" alt="350 x 150 pic">
```



##### 예시)

- <map name="Search_Engine">
    <area shape="rect" coords="4,3,68,21" href="http://naver.com" target="_blank" onFocus="blur()">
    <area shape="rect" coords="78,4,119,20" href="http://daum.net" target="_blank" onFocus="blur()">
    <area shape="rect" coords="128,5,193,19" href="http://www.paran.com" target="_blank" onFocus="blur()">
    <area shape="rect" coords="204,3,259,20" href="http://nate.com" target="_blank" onFocus="blur()">
    <area shape="rect" coords="269,2,323,20" href="http://www.google.co.kr/" target="_blank" onFocus="blur()">
    <area shape="rect" coords="331,4,385,18" href="http://kr.yahoo.com/" target="_blank" onFocus="blur()">
  </map><img src="https://i.imgur.com/NUjTqSd.gif" width="389" height="26" border="0" usemap="#Search_Engine">
  <map name="Search_Engine">
    <area shape="rect" coords="4,3,68,21" href="http://naver.com" target="_blank" onFocus="blur()">
    <area shape="rect" coords="78,4,119,20" href="http://daum.net" target="_blank" onFocus="blur()">
    <area shape="rect" coords="128,5,193,19" href="http://www.paran.com" target="_blank" onFocus="blur()">
    <area shape="rect" coords="204,3,259,20" href="http://nate.com" target="_blank" onFocus="blur()">
    <area shape="rect" coords="269,2,323,20" href="http://www.google.co.kr/" target="_blank" onFocus="blur()">
    <area shape="rect" coords="331,4,385,18" href="http://kr.yahoo.com/" target="_blank" onFocus="blur()">
  </map>
  
  

--------

#### 2) `<audio>` 요소

- **HTML `<audio>` 요소**는 문서에 소리 콘텐츠를 포함할 때 사용합니다. `src` 특성 또는 [`<source>` (en-US)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) 요소를 사용해 한 개 이상의 오디오 소스를 지정할 수 있으며, 다수를 지정한 경우 가장 적절한 소스를 브라우저가 고릅니다. [`MediaStream` (en-US)](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)을 사용하면 미디어 스트림을 바라볼 수도 있습니다.

  |   속성   |                        설명                        |
  | :------: | :------------------------------------------------: |
  |   src    |           오디오 파일의 주소를 명시한다.           |
  | controls | 오디오 동작을 제어할 수 있는 컨트롤 바를 명시한다. |
  |   loop   |           오디오의 반복여부를 명시한다.            |
  | autoplay |        오디오의 자동 재생 여부를 명시한다.         |



#### 구조

  ```html
  1. <audio controls loop>    <source src="#" type="audio/mp3">   <source src="#" type="audio/ogg"> </audio> 
  
  2. <audio controls autoplay>    <source src="#" type="audio/mp3">   <source src="#" type="audio/ogg"> </audio>
  ```

`<source>` Tag: 오디오 파일 주소 및 파일 형식을 여러개 지정해주었으며, 웹 브라우저는 위쪽에서부터 가장 먼저 인식되는 오디오 파일 주소 및 파일 형식을 사용한다.

##### 예시)

1. <audio controls loop>    <source src="#" type="audio/mp3">   <source src="#" type="audio/ogg"> </audio> 
2. <audio controls autoplay>    <source src="#" type="audio/mp3">   <source src="#" type="audio/ogg"> </audio>

----------

#### 3) `<iframe>` : 인라인 프레임 요소

-  중첩 [브라우징 맥락](https://developer.mozilla.org/ko/docs/Glossary/Browsing_context)을 나타내는 요소로, 현재 문서 안에 다른 HTML 페이지를 삽입합니다.

#### 구조

```html
<iframe src="삽입하는 웹페이지 URL" title="내용" width="100%" height="300px"></iframe>
```

- `src` : source의 약자로, 삽입하려는 웹페이지의 주소를 입력한다.
- `title` : 웹 브라우저에게 해당 iframe이 어떤 iframe인지를 알린다. 이 속성은 필수사항은 아니지만 권장한다.
- width, height 속성을 사용하면 iframe의 너비와 높이를 지정할 수 있다.

##### 예시)

<iframe id = "USAF"
        title = "USAF MUSEUM"
        width="200" 
        height="200"
        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3646.309620939214!2d-84.11208029705683!3d39.78076955883591!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8840832fc83ffd85%3A0x71e29a127c5a32c9!2z642UIOycoOyXkOyKpCDsl5DslrQg7Y-s7IqkIOq1reumveuwleusvOq0gA!5e0!3m2!1sko!2skr!4v1661750121045!5m2!1sko!2skr"  style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

-----

#### 4) `<img>`: 이미지 삽입 요소

**HTML `<img>` 요소**는 문서에 이미지를 넣습니다.

**구조**

```xml
<img src="url" alt="대체 텍스트">
```

img는 HTML 문서에 이미지를 삽입하는 태그이다. 주요 속성은 다음과 같다.

- src : 이미지의 경로
- alt : 이미지를 표시할 수 없을 때 출력할 내용
- width : 이미지의 가로 크기
- height : 이미지의 세로 크기
- loading : 이미지 로딩 방식

##### 예시)

<img class="fit-picture"
     src="https://image-notepet.akamaized.net/resize/620x-/seimage/20181123%2Fcd25e169842f9d2277761bb3f012a961.jpg"
     alt="dogdog">

---

#### 5) `<map>`

**`<map>` 요소**는  [`<area>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/area) 요소와 함께 이미지 맵(클릭 가능한 링크 영역)을 정의할 때 사용합니다.

이미지맵의 태그의 기본 구조는 아래와 같습니다.

**구조**

```html
<img src="imgmap.gif" alt="imgmap.gif" usemap="#ex" border="0">
	<map name="ex">
 		<area shape="rect" coords="42,41,154,66" href="/01/homepage.php" target="_blank">
 		<area shape="rect" coords="42,76,152,100" href="/03/html.php" target="_blank">
	</map>
```

```
1. 이미지의 usemap="이름"과 map name="이름"을 통일하게 지정해줍니다.

2. shape="속성값"은 영역의 모양을 의미합니다.
- react : 직사각형
- circle : 원형 모양
- poly : 형 영역
- default : 전체 영역

3. coords="정의"는 영역의 좌표를 의미합니다.

4. 링크가 없을땐 nohref 로 정의해줍니다. 

출처: https://eunyoe.tistory.com/65 
```



---

#### 6) `<param>`: 객체 매개변수 요소

**HTML `<param>` 요소**는 [`<objct>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/object) 요소의 매개변수를 정의합니다.

`<object>` 요소는 이미지나, 중첩된 브라우저 컨텍스트, 플러그인에 의해 다뤄질수 있는 리소스와 같은 외부 리소스를 나타냅니다.



#### 7) `<track>`: 텍스트 트랙 삽입 요소

- **HTML `<track>` 요소**는 미디어 요소([`<audio>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/audio), [`<video>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video))의 자식으로서, 자막 등 시간별 텍스트 트랙(시간 기반 데이터)를 지정할 때 사용합니다. 트랙은 [WebVTT](https://developer.mozilla.org/en-US/docs/Web/API/WebVTT_API)(Web Video Text Tracks, `.vtt` 파일) 또는 [Timed Text Markup Language(TTML)](https://w3c.github.io/ttml2/index.html)형식을 사용해야 합니다.

  

**구조**

```html
<video controls
       src="/media/cc0-videos/friday.mp4">
    <track default
           kind="captions"
           srclang="en"
           src="/media/examples/friday.vtt" />
    Sorry, your browser doesn't support embedded videos.
</video>
```





####  8) `<video>`: 비디오 삽입 요소

`<video>` 요소는 비디오 플레이백을 지원하는 미디어 플레이어를 문서에 삽입합니다. 오디오 콘텐츠에도 사용할 수 있으나, `<audio>` 요소가 사용 자 경험에 좀 더 적합합니다.

**구조**

```html
1.
 <video style="width:500; height:300" controls loop> 
 <source src="#" type="video/mp4">
 <source src="#" type="video/ogg">
</audio>

 2.
<video style="width:500; height:300" controls autoplay> 
<source src="#" type="video/mp4">
<source src="#" type="video/ogg">
</audio>
```



1.

<video style="width:500; height:300" controls loop>  <source src="#" type="video/mp4"> <source src="#" type="video/ogg"> </audio> 



2.

<video style="width:500; height:300" controls autoplay>  <source src="#" type="video/mp4"> <source src="#" type="video/ogg"> </audio>



### video 속성

|   속성   |                        설명                        |
| :------: | :------------------------------------------------: |
|   src    |           비디오 파일의 주소를 명시한다.           |
| controls | 비디오 동작을 제어할 수 있는 컨트롤 바를 명시한다. |
|   loop   |           비디오의 반복여부를 명시한다.            |
| autoplay |        비디오의 자동 재생 여부를 명시한다.         |
|  width   |             비디오의 너비를 명시한다.              |
|  height  |             비디오의 높이를 명시한다.              |



`<video></video> 태그 안의 콘텐츠는 브라우저가 <video> 요소를 지원하지 않을 때 보여집니다.`

