from django.db import models


class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)





class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True, default=0)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name