from django.db import models

# Create your models here.
class Category:
    #id
    #name
    #desc
    pass

class Brand:
    #id
    #name
    #desc
    pass

class Sale:
    #id
    #name
    #desc
    #discount
    pass

class Product:
    #id
    #name
    #desc
    #price
    #brand
    #category
    pass

class ProductSale:
    #sale
    #product
    pass

class Tag:
    #id
    #name
    #desc
    pass

class ProductTags:
    #TagId
    #product