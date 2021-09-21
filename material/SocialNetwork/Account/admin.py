from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Account.models import UserAccount
# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_login','dob')
    search_fields=('email','first_name')
    readonly_fields=('date_joined','last_login')
    ordering = ('date_joined','first_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(UserAccount,AccountAdmin)
