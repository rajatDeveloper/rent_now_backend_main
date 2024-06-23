from django.contrib import admin
from rent_now.models import Address , Category , RentPost , RentRequest, RentOrder
admin.site.register(Address , list_display=['id','address','city','state','country'])

admin.site.register(Category , list_display=['id','name','description'])

admin.site.register(RentPost , list_display=['id','title','category','user','address','created_at'])

admin.site.register(RentRequest , list_display=['id','rent_type','pay_per_duration'])

admin.site.register(RentOrder , list_display=['id','user','rent_post','status','created_at'])
