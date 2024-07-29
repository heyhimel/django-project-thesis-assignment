from django.db import models

# Create your models here.
class supCreateProject(models.Model):
    projId = models.BigAutoField(primary_key=True)
    supProjId = models.ForeignKey('home_login_signup.userAuthenTable',on_delete=models.CASCADE)
    projName = models.CharField(max_length=50)
    projDetails = models.TextField()
    startDate = models.DateField(auto_now=False, auto_now_add=False) 
    endDate = models.DateField(auto_now=False, auto_now_add=False) 
    approveOrNot = models.BooleanField(default=True)
    highestStudents = models.IntegerField()

    def __str__(self):
        return f"{self.projtId},{self.supProjId},{self.projName},{self.projDetails},{self.startDate},{self.endDate},{self.approveOrNot}, {self.highestStudents}"
    