from django.db import models

# Create your models here.

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images/')


class ContactNumber(models.Model):
    id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=6)
    telephone = models.PositiveIntegerField()


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    suit_num = models.PositiveIntegerField()
    floor_num = models.PositiveIntegerField()
    street_num = models.PositiveIntegerField()
    street_name = models.TextField()
    city = models.TextField()
    province = models.TextField()
    country = models.TextField()
    postal_code = models.CharField(max_length=6)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    logo_image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='%(class)s_logo_image')
    web_page_logo = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='%(class)s_web_page_logo')
    contact_number = models.ForeignKey(ContactNumber, on_delete=models.CASCADE)
    title = models.TextField()
    short_desc = models.TextField()
    long_desc = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    

class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    
    

class HoursOfOperation(models.Model):
    id = models.AutoField(primary_key=True)
    DAY_CHOICES = (('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), 
                   ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday'), ('All', 'All Days'))
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default='Mon')
    start_time = models.TimeField()
    end_time = models.TimeField()
    

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    desc = models.TextField()
    

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    short_desc = models.TextField()
    self_webpage_link = models.URLField()
    price = models.PositiveIntegerField()
    duration_in_mins = models.IntegerField()
    duration_in_hours = models.IntegerField()
    main_pic = models.ForeignKey(Image, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class ServiceImage(models.Model):
    id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
