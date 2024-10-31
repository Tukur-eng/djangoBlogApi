from django.db import models

# Create your models here.
class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length= 100)

    def __string__(self):
         return self.name
    

class Blogpost(models.Model):
     title = models.CharField(max_length= 100)
     content = models.TextField()
     published_Date = models.DateTimeField(auto_now_add = True)

     def __string__(self):
          return self.title