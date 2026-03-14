from django.contrib import admin
from .models import Enquiry
from .models import Service
from django.contrib import admin
from .models import Project, ProjectMedia

class ProjectMediaInline(admin.TabularInline):
    model = ProjectMedia
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectMediaInline]

admin.site.register(Project, ProjectAdmin)

admin.site.register(Service)
admin.site.register(Enquiry)
# Register your models here.
