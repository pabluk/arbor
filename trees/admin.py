from django.contrib import admin
from trees.models import Tree, Name

class TreeAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'binomial_name', 'address', 'latitude', 'longitude')


class NameAdmin(admin.ModelAdmin):
    list_display = ('name', 'vote', 'tree')

admin.site.register(Tree, TreeAdmin)
admin.site.register(Name, NameAdmin)
