from django.contrib import admin
from .models import ChaiVarity, Chaicertificate, chaiReview, Store

# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 2
    
class ChaiVarityAdmin(admin.ModelAdmin):
    inlines = [ChaiReviewInline]
    list_display = ('name', 'type', 'date')
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    filter_horizontal = ('chai_varieties',)
    
class ChaicertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issue_date')
    


admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Chaicertificate, ChaicertificateAdmin)

