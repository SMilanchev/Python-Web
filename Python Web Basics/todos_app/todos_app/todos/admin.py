from django.contrib import admin

# Register your models here.
from todos_app.todos.models import Todo
from todos_app.todos.models.models import Person, Category


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'state')
    sortable_by = ['text', 'owner']
    list_filter = ['owner']

    # def has_change_permission(self, request, obj=None):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     pass


admin.site.register(Todo, TodoAdmin)
admin.site.register(Person)
admin.site.register(Category)
