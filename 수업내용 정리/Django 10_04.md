Django 는 무엇인가?

- 웹 프레임 워크

  

HTTP 서버 클라이언트

요청을 해서 응답을  받는다.



1) URL 요청을 받아
2) 처리 (views.py) -> DB활용(model)
3) 응답 (templates)



장고

1. 가상환경 및 Django 설치 

```python
$ python -m venv venv #가상환경 생성

$ source venv/Scripts/activate #가상환경 실행

$ pip install django==3.2.13 #Django 설치

$ pip freeze >  requirements.txt #기록
```

 

2. Django  프로젝트 설치

```python
$ django-admin startproject pjt [프로젝트이름]
```



3.  서버 실행

```python
cd pjt/

python manage.py runserver
```

``` 
한국어 설정
project 폴더 settings => TIME_ZONE ='Asia/Seoul'

				=> LANGUAGE_CODE ='ko-kr'
```

4. 앱 실행

```python
$ python manage.py startapp articles
=> settings.py에 만든 앱 이름 추가 'articles', (쉼표 꼭 붙이기)
```

5. pjt < urls 

   ```py
   from django.urls import path, include
   # path('admin/', admin.site.urls),
   path('articles/',include('articles.urls')), 추가
   
   ```

6.  app폴더 <urls 생성 

   ```python
   from django.urls import path
   
   pjt 폴더 urls 에서 url patterns 복붙
   from django.contrib import admin
   from django.urls import path
   from . import  views
   
   app_name = 'articles' #추가
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.index, name ='index'),
   ]
   
   
   ```

   

7. app < urls

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'articles' #추가
   
   urlpatterns = [
       path('', views.index, name ='index'),
   ]
   
   #index 실행시켜줘~
   ```

8. app <  views

   ```py
   요청 정보 받아서 페이지 render
   
   def index(request):
   	return render(request, 'articles/index.html')
   ```

9. app < templates < articles < index.html

   ``` 
   templates폴더 생성 <  templates폴더 안에 articles폴더 생성 < index.html 생성
   ```

   

10. app < urls.py

```python
path('',views.index,name='index')
```



11. Model 정의 (DB설계) app < template <models.py

    ```python
    class Article(models.Model):
        title = models.CharField(max_length=20)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True) #생성될때 시간 자동 생성
        updated_at = models.DateTimeField(auto_now=True) #시간 업데이트 자동으로 기록
    ```

12.  마이그레이션 파일 생성 python manage.py makemigrations

13.  DB 반영 python mange.py migrate

    

기능을 추가 하고싶다 => url 추가 -> view.py DB에 저장



CRUD 기능 구현

1) 게시글 생성

```
> 사용자에게 HTML From 제공, 입력한 데이터 처리
```



**(1)HTML form제공**

 http:// 127.0.0.1/articles/new/ 



app>url.py 

```
path('new/',views.new,name='new'), 추가
```



app>views.py

```
def new(request):
	return render(request, 'articles/new.html')
```

 

templates\articels < new.html 생성

```
<h1> 글 </h1>
<!-- form : 사용자에게 양식 제공, 값을 받아(input : name,value) 서버에 전송(action) -->
<form action=""> 
	<label for="title"></label>
	<input type="text" name="title" id ="title">
	<label for="content">내용:</label>
	<textarea name="content" id = content" cols= "30" rows="10> </textarea>
	<input type = "submit" value="글쓰기">
</form>
```



**(2) http:// 127.0.0.1/articles/create/  입력받은 데이터 처리**

게시글 DB에 생성하고  index 페이지로 redirect

```
<h1> 글 </h1>
<!-- form : 사용자에게 양식 제공, 값을 받아(input : name,value) 서버에 전송(action) -->
<form action=" {% url 'articles:create' %}"> 
	<label for="title"></label>
	<input type="text" name="title" id ="title">
	<label for="content">내용:</label>
	<textarea name="content" id = "content" cols= "30" rows="10"> </textarea>
	<input type = "submit" value="글쓰기">
</form>
```



articles < templates <  urls.py

```
path('create/',views.create, name='create'), 추가
```

articles < templates < views.py

```python
def create(request):
	pass #추가
```

articles < templates < views.py

```py
from django,shortcuts import render, redirect
from . models import Article #추가 => #models.py에 있는 Article을 import 하겠다.

def create(request):
#DB에 저장하는 로직
title = request.GET.get('title')
content = request.GET.get('content')
Article.objects.create(title=title, content=content)
return redirect('articles:index')
```



app <  templates < articles< index.html

```python
<body>
	<h1>게시판<h1>
	<a href="{% url 'articles:new'}"> 글쓰기 </a> # 추가
</body>
```

아직 추가 해도 안보임



게시글 목록 기능 구현

app <  templates < views

```python
#게시글을 가져와서 templates 에 뿌려줌

def index(request):
	articles = Article.objects.all()
	context = {
		'articles : articles'
	}
	return render(request,'articles/index.html', context)
```



app <  templates < articles< index.html

```python
<body>
	<h1>게시판<h1>
	<a href="{% url 'articles:create'}"> 글쓰기 </a> # 추가
	{% for article in articles %}
<h3> {{ article.title }} </h3>
<p>	{{ article.created_at }} | {{ article.updated_at }}</p>
</body>

```



app <  templates < views

```python
def index(request):
	articles = Article.objects.order_by('-pk') #추가
	context = {
		'articles' : articles
	}
	return render(request,'articles/index.html', context)
```



templates\articels > new.html 생성

```python
<h1> 글 </h1>
<!-- form : 사용자에게 양식 제공, 값을 받아(input : name,value) 서버에 전송(action) -->

<form action="{% url 'articles:create' %}" method="POST"> #추가
	{% csrf_token %}#추가
    
	<label for="title"></label>
	<input type="text" name="title" id ="title">
	<label for="content">내용:</label>
	<textarea name="content" id = content" cols= "30" rows="10> </textarea>
	<input type = "submit" value="글쓰기">
</form>
```





articles < templates < views.py

```py
from django,shortcuts import render, redirect
from . models import Article 추가 => #models.py에 있는 Article을 import 하겠다.

def create(request):
#DB에 저장하는 로직
title = request.POST.get('title') => GET을 POST로 변경
content = request.POST.get('content') => GET을 POST로 변경 

# GET /POST method 차이
# GET = 조회/URL
# POST = 기록/저장

Article.objects.create(title=title, content=content)
return redirect('articles:index')
```



app<templates<forms.py 생성

```python
from django import forms
from .models import Article

class ArticlesForms(forms.ModelForm):
	class Meta: 
		model = Article
		fields = '__all__'
```



articles < templates < views.py

```py
from django,shortcuts import render, redirect
from .models import Articles 
from .forms import ArticleForm

def create(request):
#DB에 저장하는 로직
title = request.POST.get('title') => GET을 POST로 변경
content = request.POST.get('content') => GET을 POST로 변경 

# GET /POST method 차이
# GET = 조회/URL
# POST = 기록/저장

Article.objects.create(title=title, content=content)
return redirect('articles:index')

def new(request):
    article_form = ArticleForm()
    context = {
        'article_form' :article_form
    }
	return render(request, 'articles/new.html',context=context)

```



templates\articels > new.html 

```python
<h1> 글 </h1>
<!-- form : 사용자에게 양식 제공, 값을 받아(input : name,value) 서버에 전송(action) -->

<form action="{% url 'articles:create' %}" method="POST">

	{% csrf_token %}
    {{ article_form.as_p }}
    
	<label for="title"></label>
	<input type="text" name="title" id ="title">
	<label for="content">내용:</label>
	<textarea name="content" id = "content" cols= "30" rows="10"> </textarea>
	<input type = "submit" value="글쓰기">
</form>
```





app<templates<forms.py 생성

```
from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):

	class Meta: 
		model = Article
		fields = ['title','content']
```



articles < templates < views.py

```py
from django,shortcuts import render, redirect
from .models import Articles 
from .forms import ArticleForm

def create(request):
	article_form = ArticleForm(request.POST)
	if article_form.is_valid():
       article_form.save()
    return redirect('articles:index')
else: 
    context = {
        'article_form' :article_form
    }
	return render(request, 'article/new.html',context=context)


def new(request):
    article_form = ArticleForm()
    context = {
        'article_form' :article_form
    }

	return render(request, 'article/new.html',context=context)
```



## 3.  상세보기

 특정한 글을 본다.

``` 
https:/127.0.0.1:8000/articles/<int:pk>/
```



urls < path

```
path('<int:pk>/',views.detail, name='deatail') #추가
```

views

```python
def detail(request,pk):
	#특정 글을 가져온다
	article = Article.objects.get(pk=pk)
	# template에 객체전달
	context = {
		'article':article
	}
	return render(request, 'articles/detail.html',context)
```

template< detail.html 생성

```
{{ articles:pk }번 게시글
<p>	{{ article.created_at }} | {{ article.updated_at }}</p>
<p> {{ article.content }}
```

url 정의 -> view함수정의 -> template 만듬



### 4. 삭제하기

``` 
> 특정한 글 삭제
https:/127.0.0.1:8000/articles/<int:pk>/delete/
```



### 5. 수정하기

```
> 특정한 글 수정 =>사용자게에 수정할 수 양식을 제공하고(GET) 특정한 글을 수정한다.(POST)
https:/127.0.0.1:8000/articles/<int:pk>/update/
```

app < templates < urls.py

```python
path('<int:pk>/update/',views.update,name='update')
```

app < templates <articles <detail.html

```
<a href="{% url 'articles:update' article.pk %}">수정</a>
```

urls.py

```python
path('<int:pk>/update/', view.update, name='update'),	#추가
```

views.py

```
def update(request,pk):
	#GET : Form 제공
   article_form = ArticleForm()
   context = {
   'article_form: article_form'
   }
   return render(request,'articles/update.html',context)
```



app < templates <articles < update.html 생성

```
<h1>글 수정<h1>
<form action ="{% url 'articles:update' ??? %}" method = "POST">
	{{ article_form.as_p }}
	<input type = "submit" value = "수정하기">
	
</form>
```



views.py

```
def update(request,pk):
	#GET : Form 제공
   article = Article.objects.get(pk=pk)
   article _form = ArticleForm(instance=article) 글길게 썼는데 다시써야함 => 다시 쓸 필요 없게 끌어와서 다시 쓸 필요없게 해줌
   context = {
   'article_form: article_form'
   }
   return render(request,'articles/update.html',context)
```

app < templates <articles < update.html 

```
<h1>글 수정<h1>
<form action ="{% url 'articles:update' ??? %}" method = "POST">
	{% csrf_token %}
	{{ article_form.as_p }}
	<input type = "submit" value = "수정하기">
	
</form>
```



views.py

```python
def update(request,pk):
	if request.method == 'POST':
	# POST : input 값 가져와서, 검증하고, DB에 저장
	article_form = ArticleForm(request.POST, instance=article)
	if arcitlce_form.is_valid():
		#유효성 검사 통과하면 상세보기 페이지로 보냄
        article_form.save()
		return redirect('articles:detail',article.pk)
      # 유효성 검사 통과 못하면 => context부터해서 오류메시지 담긴 articles_form을 렌더링
	
	
	else:
   article _form = ArticleForm(instance=article) 
   context = {
   'article_form: article_form'
   }
   return render(request,'articles/update.html',context)
```



Create 1.UI제공 2.DB저장

Read(Detail)  1. DB에서 특정 가져와서 조회

Delete 1. DB에서 특정 가져와서 삭제

Update 1. UI제공 (edit) 2.DB저장 (update)