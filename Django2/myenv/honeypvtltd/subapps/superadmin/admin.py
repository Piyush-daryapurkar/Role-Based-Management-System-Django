from django.contrib import admin
from .models import Superadmin_data,Manager_data,Manager_image
# Register your models here.

class managerdata(admin.ModelAdmin):
    list_display=['name','email','password','birth_date','joining_date','emp_id']
    
class managerimage(admin.ModelAdmin):
    list_display=['fkey','pan_card','aadhar_card','address','image']

admin.site.register(Superadmin_data)
admin.site.register(Manager_data)
admin.site.register(Manager_image)
