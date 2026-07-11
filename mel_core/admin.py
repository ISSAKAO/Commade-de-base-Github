from django.contrib import admin
from .models import SGC, Project, Indicator, IndicatorValue

admin.site.register(SGC)
admin.site.register(Project)
admin.site.register(Indicator)
admin.site.register(IndicatorValue)
