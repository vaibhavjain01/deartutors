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
        return self.complete_telephone()


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
        return self.complete_address()


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    logo_image = models.ImageField(upload_to='brand/logo/')
    web_page_logo = models.ImageField(upload_to='brand/tablogo/')
    contact_number = models.ForeignKey(ContactNumber, on_delete=models.CASCADE)
    title = models.TextField()
    short_desc = models.TextField()
    long_desc = models.TextField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
    

class AboutUs(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='aboutus/')
    title = models.TextField()
    description = models.TextField()

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
    desc = models.TextField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    short_desc = models.TextField()
    self_webpage_link = models.URLField()
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
    #service = models.CharField(max_length=50, choices=get_service_choices, default='Mon')
    image = models.ImageField(upload_to='service/others/')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        if self.service_name is None:
            return "ERROR-CUSTOMER NAME IS NULL"
        return self.service_name.name
