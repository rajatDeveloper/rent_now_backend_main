from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category_image = models.ImageField(upload_to='category_images/')
    def __str__(self):
        return self.name 
    class Meta:
        verbose_name_plural = "Categories"
    
    
class Address (models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    address = models.TextField()
    pin_code = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.address   
    
class RentTypeList(models.TextChoices):
    ONE_DAY = "one_day", "One Day"
    ONE_WEEK = "one_week", "One Week"
    ONE_MONTH = "one_month", "One Month"
    ONE_YEAR = "one_year", "One Year"
    DIRECT_BUY = "direct_buy", "Direct Buy"
    

class StatusType(models.TextChoices):
    REQUESTED = "requested", "Requested"
    ACCEPTED = "accepeted", "Accepted"
    COMPLETED = "completed", "Completed"
    
    
class RentRequest (models.Model):
    rent_type =  models.CharField(
        max_length=10,
        choices=RentTypeList.choices,
        # Use the .choices property of the TextChoices class
    ) 
    pay_per_duration = models.FloatField()
    
    def __str__(self):
        return self.rent_type.__str__()
    
    

class RentPost(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    rent_request = models.ForeignKey(RentRequest , on_delete=models.CASCADE)
    address = models.ForeignKey(Address , on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='post_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    whatsapp_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    term_and_condition = models.TextField()
    
    def __str__(self):
        return self.title +" | "+ self.user.username
    
class RentOrder(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    rent_post = models.ForeignKey(RentPost , on_delete=models.CASCADE)
    rent_request = models.ForeignKey(RentRequest , on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=StatusType.choices,
        default=StatusType.REQUESTED
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_address = models.ForeignKey(Address , on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=15)
    user_whatsapp_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.username +" | "+ self.rent_post.title +" | "+ self.status    
    

    
    
    
    
    
    
   
    
     



