from django.db import models

# Create your models here.
class Reg(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    age=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)

    def __int__(self):
        return self.sno