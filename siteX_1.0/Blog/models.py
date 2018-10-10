from django.db import models

# Create your models here.
   
class account_information(models.Model):
    user_id = models.CharField(max_length=20, primary_key = True)
    user_password = models.CharField(max_length=30)
    
class blog_content(models.Model):
    blog_id = models.IntegerField(primary_key = True)
    blog_text = models.TextField()
    blog_user_id = models.ForeignKey(account_information,on_delete = models.CASCADE)
    

class favorite_information(models.Model):
    user_favorite_id= models.ForeignKey(account_information, on_delete= models.CASCADE)
    favorite_blog_id = models.ForeignKey(blog_content, on_delete = models.CASCADE)
 
    


    

