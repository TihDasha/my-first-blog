from django.contrib import admin

from .models import Post


# немного кастомизируем админку, чтобы было удобнее, эти параметры влияют только на отображение в админке
class PostAdmin(admin.ModelAdmin):
    # добавим поиск по полям
    search_fields = ('title', 'text', 'author__username')
    # разделение по датам создания в виде дерева
    date_hierarchy = 'created_date'
    # и отображаемые поля
    list_display = ('title', 'author__username', 'published_date', 'created_date')


admin.site.register(Post, PostAdmin)
