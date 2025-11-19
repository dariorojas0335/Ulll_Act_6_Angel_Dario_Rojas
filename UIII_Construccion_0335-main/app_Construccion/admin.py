from django.contrib import admin
from .models import Empleado, Cliente, Proyecto, Material, Maquinaria, Factura

admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Material)
admin.site.register(Maquinaria)
admin.site.register(Factura)