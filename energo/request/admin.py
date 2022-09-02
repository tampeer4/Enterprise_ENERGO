from django.contrib import admin
from .models import Part, Topic, Request, Request_Part

class PartAdmin(admin.ModelAdmin):
    list_display = ('pk', 'pub_date', 'prod_name', 
     'full_prod_name', 'topic_work',
      'count', 'unit_storage', 'cell_store', 'man',
      'email',
      )
    # list_editable = ('topic_work',)
    search_fields = ('prod_name',)
    list_filter = ('pub_date', )

    empty_value_display = '-пусто-'
admin.site.register(Part, PartAdmin)

class TopicAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'description',)
  search_fields = ('title',)
  list_filter = ('description',)
admin.site.register(Topic, TopicAdmin)

class ItemInline(admin.StackedInline):
  model = Request_Part
  extra = 1

class RequestAdmin(admin.ModelAdmin):
  search_fields = ('part',)
  inlines = [ItemInline]
  list_display = ('pub_date', 'fio', 'topic', )
admin.site.register(Request, RequestAdmin)

