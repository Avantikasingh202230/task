from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category', 'product_image']
@admin.register(Customer)
class CustomerModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class CartModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
@admin.register(Payment)
class PaymentModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_status', 'razorpay_payment_id','paid']
@admin.register(OrderPlaced)
class OrderPlacedModelsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','customer', 'product', 'quantity','ordered_date', 'status', 'payment']
