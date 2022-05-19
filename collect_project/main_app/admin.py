from django.contrib import admin

# Register your models here.
from .models import Fish, Feeding, Toy

admin.site.register(Fish)

admin.site.register(Feeding)

admin.site.register(Toy)