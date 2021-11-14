from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

# лучше ссылаться на пользователя так чем через settings, описано в:
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#referencing-the-user-model
User = get_user_model()


# TODO во всех полях лучше использовать help_text, это не даст запутаться когда полей будет много
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    # лучше использовать auto_now_add, так импортов меньше будет в случае когда timezone используется только здесь
    # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#referencing-the-user-model
    created_date = models.DateTimeField(auto_now_add=True)
    # TODO тогда уж и updated_date можно добавить сразу с auto_now=True
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
