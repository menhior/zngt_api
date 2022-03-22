from django.contrib import admin
from .models import Listing
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ListingResource(resources.ModelResource):
   class Meta:
      model = Listing
class ListingAdmin(ImportExportModelAdmin):
   resource_class = ListingResource

admin.site.register(Listing,ListingAdmin)