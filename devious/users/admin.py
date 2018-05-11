from django.contrib import admin
from users.models import UserProfile,Banner,EmailCode,UserSupprot,UserFlower,Address
# Register your models here.
admin.site.register([UserProfile,Banner,EmailCode,UserSupprot,UserFlower,Address])