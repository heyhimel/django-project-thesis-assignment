from django.db import models

# Create your models here.
class userAuthenTable(models.Model):
    userId = models.BigAutoField(primary_key=True)
    userType = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    userName = models.CharField(max_length=30)
    passWord = models.CharField(max_length=40)

    

    def __str__(self):
        return f"{self.userId},{self.userType},{self.name},{self.name},{self.gmail},{self.userName},{self.passWord}"