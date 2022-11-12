from django.contrib import admin

class OrderItemInline(admin.TabularInline):
model = OrderItem
raw_id_fields = ['product']
@admin.register(Order)