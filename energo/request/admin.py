from typing import Any
from django.contrib import admin
from django.contrib import messages
from .models import Part, Topic, Request_Man, Request_Part, Write_Off

class PartAdmin(admin.ModelAdmin):
    list_display = ( 'pub_date', 'prod_name', 
     'full_prod_name', 'topic_work',
      'count', 'unit_storage', 'cell_store', 'man',
      )
    # list_editable = ('topic_work',)
    search_fields = ('prod_name',)
    list_filter = ('pub_date', )
    autocomplete_fields = ('topic_work', )
admin.site.register(Part, PartAdmin)

class TopicAdmin(admin.ModelAdmin):
  list_display = ('title', 'description',)
  search_fields = ('title',)
  list_filter = ('description',)
  # ordering = ['title', ]
admin.site.register(Topic, TopicAdmin)


class ItemInline(admin.StackedInline):
  model = Request_Part
  extra = 1
  autocomplete_fields = ('part', )


class RequestAdmin(admin.ModelAdmin):
  list_filter = ('pub_date', )
  inlines = [ItemInline]
  list_display = ('pub_date', 'fio', 'topic', )
  autocomplete_fields = ('topic', )   
admin.site.register(Request_Man, RequestAdmin)

class Write_Off_Admin(admin.ModelAdmin):
  list_filter = ('pub_date', )
  list_display = ('pub_date', 'fio', 'part', 'count',)
  exclude = ('fio',)
  autocomplete_fields = ('part', )

  def save_model(self, request: Any, obj, form: Any, change: Any):
    obj.fio = request.user.get_full_name()
    part = obj.part
    if part.count < obj.count:
      messages.error(request, f'На складе только {part.count}! Заказывайте')
    else:
      part.count = part.count - obj.count
      part.save()
      return super().save_model(request, obj, form, change)
admin.site.register(Write_Off, Write_Off_Admin)

