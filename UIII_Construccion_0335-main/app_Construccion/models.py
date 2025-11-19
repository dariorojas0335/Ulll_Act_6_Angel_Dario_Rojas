from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    tipo_cliente = models.CharField(
        max_length=50,
        choices=[
            ("Residencial", "Residencial"),
            ("Comercial", "Comercial"),
            ("Gubernamental", "Gubernamental"),
        ],
        default="Residencial"
    )
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cargo}"

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"

class Maquinaria(models.Model):
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    num_serie = models.CharField(max_length=100, unique=True)
    fecha_adq = models.DateField()
    horas_uso = models.IntegerField(default=0)
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="maquinarias")
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.marca} {self.modelo}"

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.DecimalField(max_digits=12, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="proyectos")
    empleados = models.ManyToManyField(Empleado, related_name="proyectos")
    materiales = models.ManyToManyField(Material, related_name="proyectos", blank=True)
    maquinarias = models.ManyToManyField(Maquinaria, related_name="proyectos", blank=True)
    factura_total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    estado = models.CharField(
        max_length=50,
        choices=[
            ("En planificación", "En planificación"),
            ("En curso", "En curso"),
            ("Finalizado", "Finalizado"),
        ],
        default="En planificación",
    )
    factura_generada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    def generar_factura(self):
        """Método para generar factura automáticamente"""
        if not self.factura_generada and self.factura_total > 0:
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
                    factura_total=self.factura_total
                )
                self.factura_generada = True
                self.save()
                return True
        return False

class Factura(models.Model):
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="facturas")
    id_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="facturas")
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="facturas")
    factura_total = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_emision = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Factura {self.id} - {self.id_cliente.nombre} - ${self.factura_total}"