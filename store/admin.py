from django.contrib import admin
from .models import Product, Cash, Order, Setting, Purchase, OtherPurchase

# Register your models here.
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(OtherPurchase)
admin.site.register(Cash)
admin.site.register(Order)

# Admin Models
@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):

    # You really shouldn't add random settings
    def has_add_permission(self, request):
        return False

    # Deleting a setting seems odd...
    def has_delete_permission(self, *args, **kwargs):
        return False