from django.contrib import admin # type: ignore

from .models import LongToShort

# Register your models here.

admin.site.register(LongToShort)