from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_construccion, name='inicio_construccion'),
    
    # URLs para Empleados
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleado/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),
    
    # URLs para Clientes
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_clientes, name='ver_clientes'),
    path('cliente/actualizar/<int:cliente_id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/borrar/<int:cliente_id>/', views.borrar_cliente, name='borrar_cliente'),
    
    # URLs para Proyectos
    path('proyecto/agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('proyecto/ver/', views.ver_proyectos, name='ver_proyectos'),
    path('proyecto/actualizar/<int:proyecto_id>/', views.actualizar_proyecto, name='actualizar_proyecto'),
    path('proyecto/borrar/<int:proyecto_id>/', views.borrar_proyecto, name='borrar_proyecto'),
    
    # URLs para Materiales
    path('material/agregar/', views.agregar_material, name='agregar_material'),
    path('material/ver/', views.ver_materiales, name='ver_materiales'),
    path('material/actualizar/<int:material_id>/', views.actualizar_material, name='actualizar_material'),
    path('material/borrar/<int:material_id>/', views.borrar_material, name='borrar_material'),
    
    # URLs para Maquinaria
    path('maquinaria/agregar/', views.agregar_maquinaria, name='agregar_maquinaria'),
    path('maquinaria/ver/', views.ver_maquinarias, name='ver_maquinarias'),
    path('maquinaria/actualizar/<int:maquinaria_id>/', views.actualizar_maquinaria, name='actualizar_maquinaria'),
    path('maquinaria/borrar/<int:maquinaria_id>/', views.borrar_maquinaria, name='borrar_maquinaria'),
    
    # URLs para Facturas (solo ver, actualizar y borrar - NO agregar)
    path('factura/ver/', views.ver_facturas, name='ver_facturas'),
    path('factura/actualizar/<int:factura_id>/', views.actualizar_factura, name='actualizar_factura'),
    path('factura/borrar/<int:factura_id>/', views.borrar_factura, name='borrar_factura'),
]