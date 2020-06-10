from django.db import models
from django.contrib.auth.models import User
from accounts.forms import UserRegisterForm
from django.urls import reverse

class Donate(models.Model):

    owner = models.ForeignKey(User, related_name='books',default=None,on_delete=models.PROTECT)
    title = models.CharField( max_length=80)
    image = models.ImageField( blank=False ,upload_to='pics/',default="10", height_field=None, width_field=None, max_length=None)
    author = models.CharField( max_length=50)
    desc = models.TextField()
    bookType = models.CharField( max_length=50)

    def __str__(self):
        return self.title       

    # def get_absolute_url(self,id):
    #     return reverse("book_details", kwargs={"id":self.id})
