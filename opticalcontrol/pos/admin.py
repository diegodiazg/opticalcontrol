#encoding:utf-8
from pos.models import optica
from pos.models import sucursal
from pos.models import cargo
from pos.models import empleado
from pos.models import producto
from pos.models import cliente
from pos.models import proveedor
from pos.models import factura_venta
from pos.models import detalle_factura
from pos.models import facturaAdmin
from pos.models import credito_venta
from pos.models import abono
from pos.models import compra
from pos.models import detalle_compra
from pos.models import credito_compra
from pos.models import Abono_compra
from django.contrib import admin

admin.site.register(optica)
admin.site.register(sucursal)
admin.site.register(cargo)
admin.site.register(empleado)
admin.site.register(producto)
admin.site.register(cliente)
admin.site.register(proveedor)
admin.site.register(detalle_factura)
admin.site.register(credito_venta)
admin.site.register(abono)
admin.site.register(compra)
admin.site.register(detalle_compra)
admin.site.register(credito_compra)
admin.site.register(Abono_compra)
admin.site.register(factura_venta, facturaAdmin)