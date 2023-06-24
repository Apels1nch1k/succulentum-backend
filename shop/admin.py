from django.contrib import admin
from shop.models.category import Category
from shop.models.product import Product
from shop.models.order import Order, OrderProduct
from shop.models.cart import CartUser
from shop.models.comment import Comment
from shop.models.slider import Slider


from django.utils.safestring import mark_safe
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'created', 'uploaded', 'stock']
    list_filter = ['name', 'uploaded', 'created']
    # prepopulated_fields = {'slug': ('name', )}
    readonly_fields = ('created', 'uploaded')
    def image_show(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='60' />")
    
    image_show.short_description = "Фотография"





class OrderProductAdmin(admin.TabularInline):
    model = OrderProduct
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'city', 'street', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderProductAdmin]
    
@admin.register(CartUser)
class CartUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    pass