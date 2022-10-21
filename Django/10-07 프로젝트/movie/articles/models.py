from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    movie_name = models.TextField(null=True)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], help_text="0~5")
    created_at = models.DateTimeField(default=timezone.now)
    # auto_now_add로 속성 정의했더니 django.core.exceptions.FieldError: 'created_at' cannot be specified for Review model form as it is a non-editable field  라는 오류가 떠서
    # default=timezone.now으로 임시로 적어둠.
    updated_at = models.DateTimeField(default=timezone.now)

    