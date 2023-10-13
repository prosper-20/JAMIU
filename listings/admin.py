from django.contrib import admin
from .models import Property, Agent, Listing, Inquiry

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['Agent','title','price','location','image',"description"]
    list_editable = ["location","price","image","description",]
    list_display_links = ["title"]

class AgentAdmin(admin.ModelAdmin):
    list_display = ["name","email","phone","photo"]


class ListingAdmin(admin.ModelAdmin):
    list_display = ["property","is_published","sold_date","list_date"]


class InquiryAdmin(admin.ModelAdmin):
    list_display = ["property","name","email", "phone"]

admin.site.register(Property,PropertyAdmin)

admin.site.register(Agent,AgentAdmin)

admin.site.register (Listing,ListingAdmin )

admin.site.register (Inquiry,InquiryAdmin )