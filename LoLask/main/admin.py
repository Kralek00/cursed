from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Member, Character, Deadline, EventOrg, EventMem

# Кастомизация моделей
admin.site.register(User, UserAdmin)
admin.site.register(Member)
admin.site.register(Character)
admin.site.register(Deadline)
admin.site.register(EventOrg)
admin.site.register(EventMem)


# Кастомизация отображения модели User в админке
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )


admin.site.unregister(Member)

admin.site.unregister(User)
# Регистрация модели User с кастомным админом
admin.site.register(User, CustomUserAdmin)
