from django.contrib import admin
from .models import QueryTypes, UserAdminQueries, UserAdminQueriesContents
# Register your models here.

admin.site.register(UserAdminQueries)
admin.site.register(UserAdminQueriesContents)
admin.site.register(QueryTypes)