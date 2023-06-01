from django.db import models

# Create your models here.
class Review (models.Model):
    review_name =models.CharField (max_length=60, null=True, blank=True)
    review_comment =models.TextField (max_length=600, null=True, blank=True)
    review_review =models.TextField (max_length=600, null=True, blank=True)
    review_date=models.DateField(null=True,blank=True)
    def __str__(self):
        return f'{self.review_name}'
    
class Contact (models.Model):
    contact_name=models.CharField(max_length=50, null=True, blank=True )    
    contact_message=models.TextField(max_length=500, null=True, blank=True)
    contact_cel= models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
    contact_email=models.EmailField(max_length=50, null=True, blank=True)
    def __str__(self):
        return f'{self.contact_name}'
    
class Blog (models.Model):
    blog_id=models.AutoField(primary_key=True)
    blog_title=models.CharField(max_length=70, null=True, blank=True)
    blog_date=models.DateField(null=True,blank=True)
    blog_text=models.TextField(max_length=100, null=True, blank=True)
    blog_img=models.ImageField (upload_to='blog/')
    def __str__(self):
        return f'{self.blog_title}'
    
class Fullblog (models.Model):
    fullblog_id = models.AutoField(primary_key=True)
    fullblog_title=models.TextField(max_length=1000, null=True, blank=True)
    fullblog_text=models.TextField(max_length=3000, null=True, blank=True)
    fullblog_img = models.ImageField(upload_to='blog/')
    fullblog_date=models.CharField(max_length=50, null = True , blank=True)
    fullblog_img2 = models.ImageField(upload_to='blog/')
    fullblog_text2=models.TextField(max_length=3000, null=True, blank=True)
    def __str__(self):
        return f'{self.fullblog_title}'
