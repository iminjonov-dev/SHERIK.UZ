from django.db import models
from django.db.models import Model, ForeignKey, CASCADE, ManyToManyField, ImageField, SET_NULL
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, TextField, FloatField, IntegerField, BooleanField, DecimalField, \
    DateTimeField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Region(Model):
    name=CharField(max_length=255,verbose_name=_('region name'))
    def __str__(self):
        return self.name
class District(Model):
    name=CharField(max_length=255,verbose_name=_('district name'))
    region=ForeignKey('properties.Region',CASCADE,related_name='districts')
    def __str__(self):
        return self.name
class Amenities(Model):
    name=CharField(max_length=255,verbose_name=_('name'))
class Property(Model):
    class STATUS(TextChoices):
        ACTIVE='active',_('Active'),
        BLOCKED='blocked',_('Blocked'),
        ARCHIVED='archived',_('Archived')
    owner=ForeignKey('user.User',CASCADE,related_name='properties')
    title=CharField(max_length=255,verbose_name=_('title'))
    description=TextField(verbose_name=_('description'))
    district=ForeignKey('properties.District',CASCADE,blank=True,null=True)
    address=CharField(max_length=255,verbose_name=_('address'))
    latitude=FloatField(verbose_name=_('latitude'))
    longitude=FloatField(verbose_name=_('longitude'))
    rooms=IntegerField(verbose_name=_('rooms'))
    floor=IntegerField(verbose_name=_('floor'))
    total_floor=IntegerField(verbose_name=_('total_floor'))
    area=FloatField(verbose_name=_('area'))
    amenities=ManyToManyField('properties.Amenities')
    furnished=BooleanField(default=False,verbose_name=_('furnished'))
    price_day=DecimalField(max_digits=100,decimal_places=2,verbose_name=_('price_day'))
    price_week=DecimalField(max_digits=100,decimal_places=2,verbose_name=_('price_week'))
    price_year=DecimalField(max_digits=100,decimal_places=2,verbose_name=_('price_year'))
    status=CharField(max_length=15,choices=STATUS.choices,default=STATUS.ARCHIVED,verbose_name=_('status'))
    created_at=DateTimeField(auto_now_add=True,verbose_name=_('created at'))
    updated_at=DateTimeField(auto_now_add=True,verbose_name=_('updated at'))


class PropertyImage(Model):
    property=ForeignKey('properties.Property',CASCADE,verbose_name=_('property'))
    image=ImageField(upload_to='media',verbose_name=_('image'))
    created_at=DateTimeField(auto_now_add=True)
class Comment(Model):
    user=ForeignKey('user.User',SET_NULL,null=True,blank=True)
    property=ForeignKey('properties.Property',CASCADE)
    comment=TextField(verbose_name=_('comment'))
    created_at=DateTimeField(auto_now_add=True)

