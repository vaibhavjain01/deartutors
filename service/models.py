from django.db import models

# Create your models here.

class ContactNumber(models.Model):
    id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=6)
    telephone = models.PositiveIntegerField()

    class Meta:
        ordering = ('id',)

    @property
    def complete_telephone(self):
        return (self.country_code + str(self.telephone))

    def __str__(self):
        return self.complete_telephone


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    suit_num = models.PositiveIntegerField(default=None)
    floor_num = models.PositiveIntegerField(default=None)
    street_num = models.PositiveIntegerField()
    street_name = models.TextField()
    city = models.TextField()
    province = models.TextField()
    country = models.TextField()
    postal_code = models.CharField(max_length=6)

    class Meta:
        ordering = ('id',)

    @property
    def complete_address(self):
        addr = ""
        if self.suit_num != None:
            addr += "Suit " + str(self.suit_num) + ", "
        if self.floor_num != None:
            addr += "Floor " + str(self.floor_num) + ", "
        addr += "Street " + str(self.street_num) + "-" + self.street_name + ", "
        addr += self.city + ", " + self.province + ", " + self.country + ", " + self.postal_code

        return addr

    def __str__(self):
        return self.complete_address


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    logo_image = models.ImageField(upload_to='brand/logo/')
    web_page_logo = models.ImageField(upload_to='brand/tablogo/')
    contact_number = models.ForeignKey(ContactNumber, on_delete=models.CASCADE)
    title = models.TextField()
    short_desc = models.TextField()
    long_desc = models.TextField()
    email = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    facebook_url = models.URLField(default="na@na.com")
    twitter_url = models.URLField(default="na@na.com")
    linkedin_url = models.URLField(default="na@na.com")

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
    

class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='aboutus/')
    title = models.TextField()
    short_description = models.TextField()
    long_description = models.TextField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.title


class HoursOfOperation(models.Model):
    id = models.AutoField(primary_key=True)
    DAY_CHOICES = (('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), 
                   ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday'), ('All', 'All Days'))
    day = models.CharField(max_length=10, choices=DAY_CHOICES, default='Mon')
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.day


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    short_desc = models.TextField()
    long_desc = models.TextField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    short_desc = models.TextField()
    self_webpage_link = models.URLField(default="na@na.com")
    price = models.PositiveIntegerField()
    duration_in_mins = models.IntegerField()
    duration_in_hours = models.IntegerField()
    main_pic = models.ImageField(upload_to='service/thumb/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

    
class ServiceImage(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='service/others/')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        if self.service_name is None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.service_name.name


class ContactMessage(models.Model):
    id = models.AutoField(primary_key=True)
    sender_name = models.TextField(default="")
    sender_email = models.TextField(default="")
    subject = models.TextField(default="")
    msg = models.TextField(default="")
    msg_time = models.TimeField()

    def __str__(self):
        return self.subject

class AppointmentRequest(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)
    request_date = models.DateField()
    request_time = models.TimeField()
    request_duration = models.PositiveIntegerField()

    def __str__(self):
        return (self.service_name + "_" + str(request_duration))
