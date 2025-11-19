from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Cliente, Proyecto, Material, Maquinaria, Factura

def inicio_construccion(request):
    return render(request, 'inicio.html')

# Funciones para Empleados
# Funciones para Empleados (corregidas)
def agregar_empleado(request):
    if request.method == 'POST':
        salario = float(request.POST['salario']) if request.POST['salario'] else 0
        
        empleado = Empleado(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            cargo=request.POST['cargo'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            fecha_contratacion=request.POST['fecha_contratacion'],
            salario=salario
        )
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html')

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        salario = float(request.POST['salario']) if request.POST['salario'] else 0
        
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.cargo = request.POST['cargo']
        empleado.telefono = request.POST['telefono']
        empleado.email = request.POST['email']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = salario
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

# Funciones para Material (corregidas)
def agregar_material(request):
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad']) if request.POST['cantidad'] else 0
        peso = float(request.POST['peso']) if request.POST['peso'] else 0
        precio = float(request.POST['precio']) if request.POST['precio'] else 0
        
        material = Material(
            nombre=request.POST['nombre'],
            marca=request.POST['marca'],
            cantidad=cantidad,
            peso=peso,
            tipo=request.POST['tipo'],
            precio=precio
        )
        material.save()
        return redirect('ver_materiales')
    return render(request, 'material/agregar_material.html')
def actualizar_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad']) if request.POST['cantidad'] else 0
        peso = float(request.POST['peso']) if request.POST['peso'] else 0
        precio = float(request.POST['precio']) if request.POST['precio'] else 0
        
        material.nombre = request.POST['nombre']
        material.marca = request.POST['marca']
        material.cantidad = cantidad
        material.peso = peso
        material.tipo = request.POST['tipo']
        material.precio = precio
        material.save()
        return redirect('ver_materiales')
    return render(request, 'material/actualizar_material.html', {'material': material})

# Funciones para Maquinaria (corregidas)
def agregar_maquinaria(request):
    if request.method == 'POST':
        horas_uso = int(request.POST['horas_uso']) if request.POST['horas_uso'] else 0
        cantidad = int(request.POST['cantidad']) if request.POST['cantidad'] else 0
        
        maquinaria = Maquinaria(
            nombre=request.POST['nombre'],
            modelo=request.POST['modelo'],
            marca=request.POST['marca'],
            num_serie=request.POST['num_serie'],
            fecha_adq=request.POST['fecha_adq'],
            horas_uso=horas_uso,
            id_empleado_id=request.POST['id_empleado'],
            cantidad=cantidad
        )
        maquinaria.save()
        return redirect('ver_maquinarias')
    
    empleados = Empleado.objects.all()
    return render(request, 'maquinaria/agregar_maquinaria.html', {'empleados': empleados})

def actualizar_maquinaria(request, maquinaria_id):
    maquinaria = get_object_or_404(Maquinaria, id=maquinaria_id)
    if request.method == 'POST':
        horas_uso = int(request.POST['horas_uso']) if request.POST['horas_uso'] else 0
        cantidad = int(request.POST['cantidad']) if request.POST['cantidad'] else 0
        
        maquinaria.nombre = request.POST['nombre']
        maquinaria.modelo = request.POST['modelo']
        maquinaria.marca = request.POST['marca']
        maquinaria.num_serie = request.POST['num_serie']
        maquinaria.fecha_adq = request.POST['fecha_adq']
        maquinaria.horas_uso = horas_uso
        maquinaria.id_empleado_id = request.POST['id_empleado']
        maquinaria.cantidad = cantidad
        maquinaria.save()
        return redirect('ver_maquinarias')
    
    empleados = Empleado.objects.all()
    return render(request, 'maquinaria/actualizar_maquinaria.html', {
        'maquinaria': maquinaria,
        'empleados': empleados
    })
# Funciones para Factura (corregidas)
def agregar_factura(request):
    if request.method == 'POST':
        factura_total = float(request.POST['factura_total']) if request.POST['factura_total'] else 0
        
        factura = Factura(
            id_cliente_id=request.POST['id_cliente'],
            id_empleado_id=request.POST['id_empleado'],
            id_proyecto_id=request.POST['id_proyecto'],
            factura_total=factura_total
        )
        factura.save()
        return redirect('ver_facturas')
    
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, 'factura/agregar_factura.html', {
        'clientes': clientes,
        'empleados': empleados,
        'proyectos': proyectos
    })
def actualizar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        factura_total = float(request.POST['factura_total']) if request.POST['factura_total'] else 0
        
        factura.id_cliente_id = request.POST['id_cliente']
        factura.id_empleado_id = request.POST['id_empleado']
        factura.id_proyecto_id = request.POST['id_proyecto']
        factura.factura_total = factura_total
        factura.save()
        return redirect('ver_facturas')
    
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, 'factura/actualizar_factura.html', {
        'factura': factura,
        'clientes': clientes,
        'empleados': empleados,
        'proyectos': proyectos
    })

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.cargo = request.POST['cargo']
        empleado.telefono = request.POST['telefono']
        empleado.email = request.POST['email']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = request.POST['salario']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado})

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    return render(request, 'empleado/borrar_empleado.html', {'empleado': empleado})

# Funciones para Clientes
def agregar_cliente(request):
    if request.method == 'POST':
        cliente = Cliente(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            tipo_cliente=request.POST['tipo_cliente'],
            telefono=request.POST['telefono'],
            email=request.POST['email'],
            direccion=request.POST['direccion']
        )
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def ver_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})

def actualizar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST['nombre']
        cliente.apellido = request.POST['apellido']
        cliente.tipo_cliente = request.POST['tipo_cliente']
        cliente.telefono = request.POST['telefono']
        cliente.email = request.POST['email']
        cliente.direccion = request.POST['direccion']
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# Funciones para Proyectos
def agregar_proyecto(request):
    if request.method == 'POST':
        # Convertir los valores numéricos del formulario
        factura_total = float(request.POST['factura_total']) if request.POST['factura_total'] else 0
        presupuesto = float(request.POST['presupuesto']) if request.POST['presupuesto'] else 0
        
        proyecto = Proyecto(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            fecha_inicio=request.POST['fecha_inicio'],
            fecha_fin=request.POST['fecha_fin'],
            presupuesto=presupuesto,
            cliente_id=request.POST['cliente'],
            factura_total=factura_total,
            estado=request.POST['estado']
        )
        proyecto.save()
        
        # Asignar empleados al proyecto (ManyToMany)
        empleados_ids = request.POST.getlist('empleados')
        proyecto.empleados.set(empleados_ids)
        
        # Asignar materiales al proyecto (ManyToMany)
        materiales_ids = request.POST.getlist('materiales')
        proyecto.materiales.set(materiales_ids)
        
        # Asignar maquinarias al proyecto (ManyToMany)
        maquinarias_ids = request.POST.getlist('maquinarias')
        proyecto.maquinarias.set(maquinarias_ids)
        
        # Generar factura automáticamente si hay un total definido
        if factura_total > 0:
            proyecto.generar_factura()
        
        return redirect('ver_proyectos')
    
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    materiales = Material.objects.all()
    maquinarias = Maquinaria.objects.all()
    return render(request, 'proyecto/agregar_proyecto.html', {
        'clientes': clientes,
        'empleados': empleados,
        'materiales': materiales,
        'maquinarias': maquinarias
    })

def ver_proyectos(request):
    proyectos = Proyecto.objects.all().select_related('cliente').prefetch_related('empleados', 'materiales', 'maquinarias')
    return render(request, 'proyecto/ver_proyecto.html', {'proyectos': proyectos})

def actualizar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    
    if request.method == 'POST':
        # Guardar el valor anterior como float para comparación
        factura_anterior = float(proyecto.factura_total)
        
        # Convertir los nuevos valores del formulario
        nuevo_factura_total = float(request.POST['factura_total']) if request.POST['factura_total'] else 0
        nuevo_presupuesto = float(request.POST['presupuesto']) if request.POST['presupuesto'] else 0
        
        proyecto.nombre = request.POST['nombre']
        proyecto.descripcion = request.POST['descripcion']
        proyecto.fecha_inicio = request.POST['fecha_inicio']
        proyecto.fecha_fin = request.POST['fecha_fin']
        proyecto.presupuesto = nuevo_presupuesto
        proyecto.cliente_id = request.POST['cliente']
        proyecto.factura_total = nuevo_factura_total
        proyecto.estado = request.POST['estado']
        proyecto.save()
        
        # Actualizar empleados del proyecto
        empleados_ids = request.POST.getlist('empleados')
        proyecto.empleados.set(empleados_ids)
        
        # Actualizar materiales del proyecto
        materiales_ids = request.POST.getlist('materiales')
        proyecto.materiales.set(materiales_ids)
        
        # Actualizar maquinarias del proyecto
        maquinarias_ids = request.POST.getlist('maquinarias')
        proyecto.maquinarias.set(maquinarias_ids)
        
        # Generar o actualizar factura si el total cambió
        if nuevo_factura_total > 0 and nuevo_factura_total != factura_anterior:
            # Eliminar factura existente si hay cambio
            Factura.objects.filter(id_proyecto=proyecto).delete()
            proyecto.factura_generada = False
            proyecto.save()
            # Generar nueva factura
            proyecto.generar_factura()
        
        return redirect('ver_proyectos')
    
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    materiales = Material.objects.all()
    maquinarias = Maquinaria.objects.all()
    return render(request, 'proyecto/actualizar_proyecto.html', {
        'proyecto': proyecto,
        'clientes': clientes,
        'empleados': empleados,
        'materiales': materiales,
        'maquinarias': maquinarias
    })
def borrar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('ver_proyectos')
    return render(request, 'proyecto/borrar_proyecto.html', {'proyecto': proyecto})

# Funciones para Material
def agregar_material(request):
    if request.method == 'POST':
        material = Material(
            nombre=request.POST['nombre'],
            marca=request.POST['marca'],
            cantidad=request.POST['cantidad'],
            peso=request.POST['peso'],
            tipo=request.POST['tipo'],
            precio=request.POST['precio']
        )
        material.save()
        return redirect('ver_materiales')
    return render(request, 'material/agregar_material.html')

def ver_materiales(request):
    materiales = Material.objects.all()
    return render(request, 'material/ver_material.html', {'materiales': materiales})

def actualizar_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        material.nombre = request.POST['nombre']
        material.marca = request.POST['marca']
        material.cantidad = request.POST['cantidad']
        material.peso = request.POST['peso']
        material.tipo = request.POST['tipo']
        material.precio = request.POST['precio']
        material.save()
        return redirect('ver_materiales')
    return render(request, 'material/actualizar_material.html', {'material': material})

def borrar_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    if request.method == 'POST':
        material.delete()
        return redirect('ver_materiales')
    return render(request, 'material/borrar_material.html', {'material': material})

# Funciones para Maquinaria
def agregar_maquinaria(request):
    if request.method == 'POST':
        maquinaria = Maquinaria(
            nombre=request.POST['nombre'],
            modelo=request.POST['modelo'],
            marca=request.POST['marca'],
            num_serie=request.POST['num_serie'],
            fecha_adq=request.POST['fecha_adq'],
            horas_uso=request.POST['horas_uso'],
            id_empleado_id=request.POST['id_empleado'],
            cantidad=request.POST['cantidad']
        )
        maquinaria.save()
        return redirect('ver_maquinarias')
    
    empleados = Empleado.objects.all()
    return render(request, 'maquinaria/agregar_maquinaria.html', {'empleados': empleados})

def ver_maquinarias(request):
    maquinarias = Maquinaria.objects.all().select_related('id_empleado')
    return render(request, 'maquinaria/ver_maquinaria.html', {'maquinarias': maquinarias})

def actualizar_maquinaria(request, maquinaria_id):
    maquinaria = get_object_or_404(Maquinaria, id=maquinaria_id)
    if request.method == 'POST':
        maquinaria.nombre = request.POST['nombre']
        maquinaria.modelo = request.POST['modelo']
        maquinaria.marca = request.POST['marca']
        maquinaria.num_serie = request.POST['num_serie']
        maquinaria.fecha_adq = request.POST['fecha_adq']
        maquinaria.horas_uso = request.POST['horas_uso']
        maquinaria.id_empleado_id = request.POST['id_empleado']
        maquinaria.cantidad = request.POST['cantidad']
        maquinaria.save()
        return redirect('ver_maquinarias')
    
    empleados = Empleado.objects.all()
    return render(request, 'maquinaria/actualizar_maquinaria.html', {
        'maquinaria': maquinaria,
        'empleados': empleados
    })

def borrar_maquinaria(request, maquinaria_id):
    maquinaria = get_object_or_404(Maquinaria, id=maquinaria_id)
    if request.method == 'POST':
        maquinaria.delete()
        return redirect('ver_maquinarias')
    return render(request, 'maquinaria/borrar_maquinaria.html', {'maquinaria': maquinaria})

# Funciones para Factura
def agregar_factura(request):
    if request.method == 'POST':
        factura = Factura(
            id_cliente_id=request.POST['id_cliente'],
            id_empleado_id=request.POST['id_empleado'],
            id_proyecto_id=request.POST['id_proyecto'],
            factura_total=request.POST['factura_total']
        )
        factura.save()
        return redirect('ver_facturas')
    
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, 'factura/agregar_factura.html', {
        'clientes': clientes,
        'empleados': empleados,
        'proyectos': proyectos
    })

def ver_facturas(request):
    facturas = Factura.objects.all().select_related('id_cliente', 'id_empleado', 'id_proyecto')
    return render(request, 'factura/ver_factura.html', {'facturas': facturas})

def actualizar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        factura.id_cliente_id = request.POST['id_cliente']
        factura.id_empleado_id = request.POST['id_empleado']
        factura.id_proyecto_id = request.POST['id_proyecto']
        factura.factura_total = request.POST['factura_total']
        factura.save()
        return redirect('ver_facturas')
    
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, 'factura/actualizar_factura.html', {
        'factura': factura,
        'clientes': clientes,
        'empleados': empleados,
        'proyectos': proyectos
    })

def borrar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        factura.delete()
        return redirect('ver_facturas')
    return render(request, 'factura/borrar_factura.html', {'factura': factura})


def generar_factura(self):
        """Método para generar factura automáticamente"""
        factura_total_float = float(self.factura_total) if self.factura_total else 0
        
        if not self.factura_generada and factura_total_float > 0:
            # Obtener el primer empleado asignado al proyecto (o un empleado por defecto)
            empleado_responsable = self.empleados.first()
            if not empleado_responsable:
                # Si no hay empleados asignados, obtener el primero disponible
                empleado_responsable = Empleado.objects.first()
            
            if empleado_responsable:
                Factura.objects.create(
                    id_cliente=self.cliente,
                    id_empleado=empleado_responsable,
                    id_proyecto=self,
                    factura_total=factura_total_float
                )
                self.factura_generada = True
                self.save()
                return True
        return False