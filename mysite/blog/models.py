from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    brief = models.CharField(default='', max_length=200)
    
    r03c3 = models.CharField(default=".",max_length=99,verbose_name="格林柱-零件")
    r03c4 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度一")
    r03c5 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度二")
    r03c6 = models.CharField(default=".",max_length=99,verbose_name="格林柱-進度三")
    r03c7 = models.CharField(default=".",max_length=99,verbose_name="格林柱-備註說明")
   
    
    
    
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title