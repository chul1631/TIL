from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # 아래 주소에 들어오면 어떤 화면을 보여줄지
    # 생각하면서 path 를 작성 ...
    # http://127.0.0.1:8000/articles/
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
