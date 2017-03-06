from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=200)
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text