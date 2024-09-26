from  django.contrib.auth.models import  User
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE);

    def __str__(self):
        return self.title


    def get_short_text(self, SHORT_TEXT_LEN=300):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN] + '...'
        else:
            return self.text