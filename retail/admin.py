from django.contrib import admin
from django.db.models import QuerySet
from django.utils.html import format_html

from retail.models import Contacts, Product, BaseSupplier


class ContactInline(admin.TabularInline):
    model = Contacts
    extra = 0


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


class BaseSupplierCityFilter(admin.SimpleListFilter):
    title = 'Фильтр по городу'
    parameter_name = 'city_filter'

    def lookups(self, request, model_admin):
        contacts = Contacts.objects.all()
        return [(contact.city, contact.city) for contact in contacts]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contacts__city=self.value())
        return queryset


@admin.register(BaseSupplier)
class BaseSupplierAdmin(admin.ModelAdmin):
    inlines = [ContactInline, ProductInline, ]
    list_display = ("id", "name", "level", "supplied_to", "debt")
    list_display_links = ('name', 'supplied_to')
    list_filter = (BaseSupplierCityFilter,)
    fields = [("id", "name"), ("level", "supplier"), "debt", "created_at"]
    readonly_fields = ("id", "created_at",)
    search_fields = ("name",)
    save_on_top: bool = True
    actions = ['clear_dept']

    def supplied_to(self, obj: BaseSupplier):
        """
        Функция по возвращению HTML-ссылки для поставщика
        """
        if obj.supplier is not None:
            return format_html(
                '<a href="/admin/el_shop/element/{id}">{name}</a>',
                id=obj.supplier.id,
                name=obj.supplier
            )

    @admin.action(description='clear debt')
    def clear_dept(self, request, queryset: QuerySet) -> None:
        queryset.update(debt=0)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number')
    list_filter = ('city',)
    search_fields = ('city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'price', 'manufactured_at')
