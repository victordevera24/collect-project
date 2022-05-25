from django.contrib import admin

# Register your models here.
from .models import Fish, Feeding, Toy, Photo

admin.site.register(Fish)

admin.site.register(Feeding)

admin.site.register(Toy)

admin.site.register(Photo)