from django.contrib import admin
from .models import AuthorProxy, BookProxy, OrderProxy, AuthenticationProxy
from django.utils.html import format_html

@admin.register(AuthorProxy)
class AuthorProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic') 
    list_filter = ('name', 'surname', 'patronymic')


@admin.register(BookProxy)
class BookProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author_names','description', 'count', 'year_of_publish', 'date_of_issue') 
    list_filter = ('year_of_publish',)
    list_editable = ('date_of_issue',)
    search_fields = ['name']
    
    def author_names(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])  # Повертаємо розділені комою імена авторів для відображення у списку

    author_names.short_description = 'Authors'


@admin.register(OrderProxy)
class OrderProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'user_id', 'created_at', 'end_at', 'plated_end_at') 
    list_filter = ('book__name', 'user__id')
    
    def book_name(self, obj):
        return obj.book.name 

    def user_id(self, obj):
        return obj.user.id


@admin.register(AuthenticationProxy)
class AuthenticationProxyAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'middle_name', 'email', 'role', 'is_active', 'is_staff')
    list_filter = ('role', 'is_active', 'is_staff')
    list_display_links = ('first_name',)  # Зробити ім'я користувача посиланням

    def full_name(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:authentication_authenticationproxy_change', args=[obj.id]), obj.get_full_name())

    full_name.short_description = 'Name'
    

