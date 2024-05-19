from django.contrib import admin
from .models import Member
from .models import user
from .models import log
from .models import message
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=("email","password","confirm_password")

class useradmin(admin.ModelAdmin):
    list_display1=("title","story")

class userlog(admin.ModelAdmin):
    list_display2=("emails","passwords")

class usermessage(admin.ModelAdmin):
    list_display3=('email','message')

admin.site.register(Member)
admin.site.register(user)

admin.site.register(log)

admin.site.register(message)