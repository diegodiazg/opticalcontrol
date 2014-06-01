#encoding:utf8
from django.forms import ModelForm
from django import forms
from pos.models import producto, cliente, factura_venta, detalle_factura, facturaAdmin

class ContactForm(forms.Form):
	correo = forms.EmailField(label = 'Tu correo electronico')
	mensaje = forms.CharField(widget=forms.Textarea)

class ProductoForm(ModelForm):
	class Meta:
		model = producto

class ClienteForm(ModelForm):
	class Meta:
		model = cliente

class FacturaForm(ModelForm):
	nit=forms.CharField()
	nombre=forms.CharField()
	apellido=forms.CharField()
	direccion=forms.CharField()
	cliente=forms.CharField(widget=forms.HiddenInput())
	


	class Meta:
		model = factura_venta
		fields=['serie_factura', 'no_factura',  'estado_factura','total_factura', 'cliente' ]
		


	

class DetalleFacturaForm(ModelForm):
	class Meta:
		model = detalle_factura
		fields=['producto', 'cantidad',  'precio_unidad' ]

		


		



