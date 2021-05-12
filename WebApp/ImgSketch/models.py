from django.db import models

# Create your models here.


# model for comments
class Comments(models.Model):
    name = models.CharField(max_length=250)
    mesg = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']