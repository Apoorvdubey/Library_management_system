from django.contrib import admin
from .models import UserAdminQueries, UserAdminQueriesContents
# Register your models here.

admin.site.register(UserAdminQueries)
admin.site.register(UserAdminQueriesContents)