from django.contrib import admin
from pedagogy_manager.contents.models.contents import Content, Area, Company
from pedagogy_manager.contents.models.contents import Route, RouteModule, Module
from pedagogy_manager.contents.models.contents import ContentModule, Blog

# Inlines admin


class InlineRouteModule(admin.TabularInline):
    model = RouteModule
    autocomplete_fields = ['module']
    extra = 0


class InlineContentModule(admin.TabularInline):
    model = ContentModule
    autocomplete_fields = ['content']
    extra = 0


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    autocomplete_fields = ['blog']
    search_fields = ['title', 'slug_name']
    prepopulated_fields = {'slug_name': ('title',)}


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug_name']
    search_fields = ['name', 'slug_name']
    exclude = ['slug_name']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug_name']
    search_fields = ['name', 'slug_name']
    exclude = ['slug_name']


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug_name']
    exclude = ['slug_name']
    autocomplete_fields = ['area', 'company']
    inlines = [InlineRouteModule]


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'slug_name']
    exclude = ['slug_name']
    inlines = [InlineContentModule]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    search_fields = ['title', 'slug_name', 'author']
    exclude = ['slug_name']
