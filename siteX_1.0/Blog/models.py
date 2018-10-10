from django.db import models

# Create your models here.

class account_information(models.Model):
    user_id = models.CharField(max_length=20, primary_key = True)
    user_password = models.CharField(max_length=30)
    favorites = models.ForeignKey(favorite_information,on_delete = models.CASCADE)
    user_blog_id = models.ForeignKey(blog_content, on_delete = models.CASCADE)
    
class blog_content(models.Model):
    blog_id = models.IngeterField(primary_key = True)
    blog_text = models.TextField()

class favorite_information(models.Model):
    favorite_id= models.IngeterField(primary_key = True)
    favorite_blog_id = models.ForeignKey(blog_content, on_delete = models.CASCADE)
    

