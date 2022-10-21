생성

- HTML Form  	 URL: /article/new/ 	views.py: new
- DB 저장 과정  URL: /article/create/ 	views.py: create



조회

- 글을 누르면 DB값 조회  URL: /article/~~/detail/ 	views.py:  detail



삭제

- 버튼을 누르면 DB값 삭제  URL : /articles/~~/delete URL: /article/new/ 	views.py: delete



수정

- HTML Form +기존 값  URL: /article/~~/ edit/ 	views.py: edit

  

- DB 저장 과정  URL: /article/~~/update/ 	views.py: update



#### 클라이언트는 URL 요청 (HTTP 요청 메세지)

Path/  mathod/ header/ protocol



**ModelForm** 

1.  DB 필드가 사실상 HTML Form 이다.

2. Input 값 => DB 유효성 검사

   

<img src="C:\Users\User\OneDrive\바탕 화면\Whiteboard_27.png" alt="Whiteboard_27" style="zoom:200%;" />