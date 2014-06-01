#encoding:utf-8
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User, check_password


# Create your models here.
class optica(models.Model):
    nombre_optica = models.CharField(max_length = 200)
    direccion_optica = models.CharField(max_length = 300)
    telefono_optica = models.CharField(max_length = 50)
    emali_optica = models.CharField(max_length = 50)
    nit_optica = models.IntegerField(default = 0)
    
    def __unicode__(self):
   	 return self.nombre_optica
   	 return self.direccion_optica
   	 return self.telefono_optica
   	 return self.email_optica
   	 return self.nit_optica


    
class sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=200)
    direccion_sucursal  = models.CharField(max_length=300)
    telefono_sucursal  = models.CharField(max_length = 50)
    email_sucursal  = models.CharField(max_length=50)
    tienda = models.ForeignKey(optica)

    def __unicode__(self):
   	 return self.nombre_sucursal
   	 return self.direccion_sucursal
   	 return self.telefono_sucursal
   	 return self.email_sucursal
   	 return self.tienda
    
class cargo (models.Model):
    nombre_cargo = models.CharField(max_length = 100)
    descripcion_cargo = models.CharField(max_length=100)

    def __unicode__(self):
   	 return self.nombre_cargo
   	 return self.descripcion_cargo
    


class empleado(models.Model):
    usuario= models.ForeignKey(User)
    nombre_empleado = models.CharField (max_length = 100)
    apellido_empleado = models.CharField(max_length = 100)
    dpi_empleado = models.IntegerField(default=0)
    direccion_empleado = models.CharField(max_length = 300)
    telefono_empleado = models.CharField(max_length = 50)
    sucursal = models.ForeignKey(sucursal)
    cargo = models.ForeignKey(cargo)

    def __unicode__(self):
   	 return self.nombre_empleado
   	 return self.apellido_empleado
      	 return self.dpi_empleado
   	 return self.direccion_empleado
   	 return self.telefono_empleado
   	 return self.sucursal
   	 return self.cargo
    
class producto (models.Model):
    codigo_producto = models.CharField(max_length = 200)
    nombre_producto  = models.CharField(max_length = 200)
    descripcion_producto  = models.CharField(max_length = 300)
    marca_producto  = models.CharField(max_length = 200)
    precio_unidad_producto  = models.DecimalField(max_digits=10, decimal_places=2)
    existencia_producto  = models.IntegerField(default = 0)

    def __unicode__(self):
   	 return self.nombre_producto
   	 return self.descripcion_producto
   	 return self.marca_producto
   	 return self.precio_unidad_producto

class cliente (models.Model):
    nombre_cliente = models.CharField(max_length = 100)
    apellido_cliente = models.CharField(max_length = 100)
    nit_cliente = models.IntegerField()
    direccion_cliente = models.CharField(max_length = 300)
    telefono_cliente = models.CharField(max_length = 50)

    def __unicode__(self):
   	 return self.nombre_cliente
   	 return self.apellido_cliente
   	 return self.nit_cliente
   	 return self.direccion_cliente
   	 return self.telefono_cliente

class proveedor (models.Model):
    nombre_proveedor = models.CharField(max_length = 200)
    nit_proveedor = models.IntegerField()
    direccion_proveedor = models.CharField(max_length = 300)
    telefono_proveedor = models.CharField(max_length = 50)

    def __unicode__(self):
   	 return self.nombre_proveedor
   	 return self.nit_proveedor
   	 return self.direccion_proveedor
   	 return self.telefono_proveedor
    
class factura_venta (models.Model):
    serie_factura = models.CharField(max_length = 20)
    no_factura = models.IntegerField()
    fecha_factura = models.DateTimeField('Fecha Factura', default=datetime.now())
    vendedor = models.ForeignKey(empleado)
    estado_factura = models.IntegerField(default=1)
    cliente = models.ForeignKey(cliente)
    total_factura = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
   	 return self.serie_factura
   	 return self.no_factura
   	 return self.fecha_factura
   	 return self.vendedor
   	 return self.estado_factura
   	 return self.cliente
   	 return self.total_factura
    
class detalle_factura (models.Model):
    factura_venta = models.ForeignKey(factura_venta)
    producto = models.ForeignKey(producto)
    cantidad = models.IntegerField ()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
   	 return self.factura_venta
   	 return self.producto
   	 return self.cantidad
   	 return self.precio_unidad

class detalle_facturaInline(admin.TabularInline):
    model = detalle_factura

class facturaAdmin(admin.ModelAdmin):
    inlines = (detalle_facturaInline,)
    
class credito_venta (models.Model):
    factura_venta = models.ForeignKey(factura_venta)
    fecha_credito_venta = models.DateTimeField('Fecha credito')
    cantidad_pagos = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __unicode__(self):
   	 return self.factura_venta
   	 return self.fecha_credito_venta
   	 return self.cantidad_pagos
   	 return self.monto
   	 return self.saldo

class abono (models.Model):
    credito = models.ForeignKey(credito_venta)
    fecha_pago = models.DateTimeField('Fecha credito')
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
   	 return self.credito
   	 return self.fecha_pago
   	 return self.monto_pago

class compra (models.Model):
    serie = models.CharField(max_length = 20)
    no_factura = models.IntegerField()
    fecha_compra = models.DateTimeField('Fecha Factura')
    sucursal = models.ForeignKey(sucursal)
    estado = models.IntegerField()
    proveedor = models.ForeignKey(proveedor)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
   	 return self.serie
   	 return self.no_factura
   	 return self.fecha_compra
   	 return self.sucursal
   	 return self.estado
   	 return self.proveedor
   	 return self.total

class detalle_compra (models.Model):
    factura_compra = models.ForeignKey(compra)
    producto = models.ForeignKey(producto)
    cantidad = models.IntegerField ()
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
   	 return self.factura_compra
   	 return self.producto
   	 return self.cantidad
   	 return self.precio_unidad


class credito_compra (models.Model):
    factura_compra = models.ForeignKey(compra)
    fecha_credito_compra = models.DateTimeField('Fecha credito')
    cant_pagos = models.IntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __unicode__(self):
   	 return self.factura_compra
   	 return self.fecha_credito_compra
   	 return self.cant_pagos
   	 return self.monto
   	 return self.saldo

class Abono_compra (models.Model):
    credito = models.ForeignKey(credito_compra)
    fecha_pago = models.DateTimeField('Fecha credito')
    monto_pago = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
   	 return self.credito
   	 return self.fecha_pago
   	 return self.monto_pago
