from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # 블로그에서 제목을 의미, max_length로 글자 수 제한을 둠.
    title = models.CharField(max_length=30)
    # 글에 들어갈 내용, TextField는 장문의 글을 받아올 수 있음.
    content = models.TextField()

    # 언제 작성되었는지
    created = models.DateTimeField()

    # 누가 작성을 했는지지, user라는 객체는 이미 django에서 제공. ForeignKey로 연결함.
    author = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)


