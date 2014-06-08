from pos.models import producto, cliente, factura_venta, detalle_factura, sucursal, empleado
from pos.forms import ContactForm, ProductoForm, ClienteForm, FacturaForm, DetalleFacturaForm 
from django.forms.formsets import formset_factory

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage




from datetime import datetime

# Create your views here.

def formulario(request):
	
	if request.method=='GET':
		
		formularioset = formset_factory(DetalleFacturaForm, extra=3)
		formulario =formularioset()
		
		#data =( {'producto': data.producto, 'cantidad': data.cantidad})
		#data=serializers.serialize('json', data)
      	
      	#data = serializers.serialize('json', data)
      	

      	#data = simplejson.dumps(data, ensure_ascii=False)
	#return render_to_response(data, {'formulario':formulario}, context_instance=RequestContext(request))
	#return HttpResponse( rdict)
	return render_to_response(formulario)




def busqueda_producto(request):

	if request.method=='GET':
		
		id=request.GET['id']
	
		data = producto.objects.filter(pk=id)

		#data = cliente.objects.all()



		#dic= {'datos': data.nombre_cliente}
		#print data.pk
		#print dic.datos
		data=serializers.serialize('json', data, fields=('precio_unidad_producto', 'existencia_producto', 'descripcion_producto',' marca_producto'))

		#print data[].nombre_cliente
		#return HttpResponse({'data':data})

	#return SreamingHttpResponse({'data':data})
	#print 'aletar'+data.fields.nombre_cliente
	return HttpResponse(data, mimetype='application/json')

def busqueda_cliente(request):

	if request.method=='GET':
		
		nit=request.GET['valor']
		data = cliente.objects.filter(nit_cliente=nit)
		data=serializers.serialize('json', data, fields=('nombre_cliente', 'apellido_cliente', 'direccion_cliente'))

	return HttpResponse(data, mimetype='application/json')



def inicio(request):
	productos = producto.objects.all()
	return render_to_response('inicio.html', {'productos':productos}, context_instance
		=RequestContext(request))

def clientes(request):
	client = cliente.objects.all()
	return render_to_response('clientes.html', {'cliente':client}, context_instance
		=RequestContext(request))

def productos(request):
	productos = producto.objects.all()
	return render_to_response('productos.html', {'productos':productos}, context_instance
		=RequestContext(request))

def contacto(request):
	if request.method=='POST':
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje de la app de Optica Lupita'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a: '+ formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['gilitobar@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactForm()
	return render_to_response('contacto.html',{'formulario':formulario}, context_instance=RequestContext(request))

def agregar_producto(request):
	if request.method=='POST':
		formulario = ProductoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/productos')
	else:
		formulario = ProductoForm()
	return render_to_response('productoform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def cliente_nuevo(request):
	if request.method=='POST':
		formulario = ClienteForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
		return HttpResponseRedirect('/cliente')
	else:
		formulario = ClienteForm()
	return render_to_response('clienteform.html', {'formulario':formulario}, context_instance=RequestContext(request))

def ventas(request):
	
	if request.method=='POST':
		factura = FacturaForm(request.POST, request.FILES)
		formularioset = formset_factory(DetalleFacturaForm)
		detallefactura =formularioset(request.POST, request.FILES)
		#detallefactura = DetalleFacturaForm(request.POST, request.FILES)
		#detallefactura = DetalleFacturaForm(request.POST, request.FILES)

		
		if factura.is_valid() and detallefactura.is_valid():
			fac = factura.save(commit=False)
			nit=request.POST['nit']
			clien = cliente.objects.get(nit_cliente=nit)
			fac.cliente=clien
			fac.fecha_factura= datetime.now()
			usur1 = request.user.id
			vendedor_id=empleado.objects.get(usuario=usur1)
			fac.vendedor=vendedor_id
			fac.save()
	
			#cd = detallefactura.cleaned_data
			#detallefactura = detallefactura.save(commit=False)

			for obj in detallefactura:
				obj2 = obj.save(commit=False)
				obj2.factura_venta = fac
				obj2.save()
				
			#detallefactura.factura_venta = fac

      		#detallefactura.save()

      		#prod_ids = obj2.producto.id
      		#cantidad1 =producto.objects.get(pk=prod_ids)
      		#if cantidad1.existencia_producto >= obj2.cantidad: #validacion para descontar de inventario
      			#descuento_prod= cantidad1.existencia_producto-detallefactura.cantidad #se realiza el descuento
      			#menos =producto.objects.filter(pk=prod_ids).update(existencia_producto=descuento_prod) # se actualiza en la db el descuento
      			#alerta = 'La transaccion fue exitosa' #mensaje de exitos
      			#return render_to_response('ventas.html', {'alerta':alerta}, context_instance=RequestContext(request)) #se envia el mensaje de exito al fronend
      		#else:
      			#alerta = 'La cantidad a Despachar no disponible en existencia!!' #se envia mensaje de error de no existir la cantidad necesaria en inventario
      			#return render_to_response('ventas.html', {'alerta':alerta}, context_instance=RequestContext(request)) #se envia el mensaje de error de fracaso al fronend


		return HttpResponseRedirect('/ventas') #se redirecciona a la misma pagina luego de realizar la operacion

	else:
		factura = FacturaForm()
		formsimple=DetalleFacturaForm()
		formularioset = formset_factory(DetalleFacturaForm)
		detallefactura =formularioset()
		return render_to_response('ventas.html', {'factura':factura,  'formsimple':formsimple, 'detallefactura':detallefactura}, context_instance=RequestContext(request))

