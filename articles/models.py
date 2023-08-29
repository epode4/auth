from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set = 

    # User 모델 참조
    # 방법1. 유지보수 측면에서 어려움 (권장 X)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)

    # 방법2. settings.AUTH_USER_MODEL == 'accounts.User' (권장) 
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 방법3. get_user_model() == 'User' (권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id = 

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id = 

    # User 모델 참조
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # user_id = 