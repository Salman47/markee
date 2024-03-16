from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'rank', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'rank')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'rank', 'password1', 'password2'),
        }),
    )

    search_fields = ('email', 'name')
    ordering = ('id', 'email', 'is_admin')
    filter_horizontal = ()


admin.site.register(User, UserModelAdmin)
