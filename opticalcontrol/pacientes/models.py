from django.db import models
from pos.models import factura, cliente

# Create your models here.
class paciente(models.Model):
	nombre_paciente = models.CharField (max_length = 100)
	apellido_paciente = models.CharField (max_length = 100)
	fecha_nacimiento = models.DateTimeField('Fecha Nacimiento')
	direccion = models.CharField (max_length = 200)
	telefono = models.CharField (max_length = 50)
	ocupacion = models.CharField (max_length = 100)

class examen (models.Model):
	paciente = models.ForeignKey(paciente)
	fecha = models.DateTimeField('Fecha Factura', default=datetime.now())
	factura = pos.models.ForeignKey(factura_venta)



class antecedentes(models.Model):
	examen = models.ForeignKey(examen)
	diabetes = models.BooleanField(default=0)
	examen_previo = models.BooleanField(default=0)

	def si(self):
        return bool(self.diabetes)
		return bool(self.examen_previo)



class AGSA(models.Model):
    cefalea= models.BooleanField(default=0)
    ardor= models.BooleanField(default=0)
    prurito = models.BooleanField(default=0)
    diabetico= models.BooleanField(default=0)
    embarazo= models.BooleanField(default=0)
    mareos= models.BooleanField(default=0)
    vision_borrosa= models.BooleanField(default=0)
    sinusitis= models.BooleanField(default=0)
    cardiopatia= models.BooleanField(default=0)
    secreciones= models.BooleanField(default=0)
    varicela= models.BooleanField(default=0)
    gastritis= models.BooleanField(default=0)
    irritacion= models.BooleanField(default=0)
    somnolencia= models.BooleanField(default=0)

	def __unicode__(self):
		return self.cefalea
		return self.ardor
		return self.prurito
		return self.diabetico
		return self.embarazo
		return self.mareos
		return self.vision_borrosa
		return self.sinusitis
		return self.cardiopatia
		return self.secreciones
		return self.varicela
		return self.gastritis
		return self.irritacion
		return self.somnolencia

class graduacion_actual(models.Model):
    od_esfera= models.DecimalField(max_digits=10, decimal_places=2)
    od_cilindro= models.DecimalField(max_digits=10, decimal_places=2)
    od_eje= models.DecimalField(max_digits=10, decimal_places=2)
    od_adicion= models.DecimalField(max_digits=10, decimal_places=2)
    color= models.DecimalField(max_digits=10, decimal_places=2)
    oi_esfera= models.DecimalField(max_digits=10, decimal_places=2)
    oi_cilindro= models.DecimalField(max_digits=10, decimal_places=2)
    oi_eje= models.DecimalField(max_digits=10, decimal_places=2)
    oi_adicion= models.DecimalField(max_digits=10, decimal_places=2)
  
    
	def __unicode__(self):
		return self.od_esfera
		return self.od_cilindro
		return self.od_eje
		return self.od_adicion
		return self.color
		return self.od_esfera
		return self.od_cilindro
		return self.od_esfera
		return self.od_adicion


class graduacion_anteriorl(models.Model):
    od_esfera= models.DecimalField(max_digits=10, decimal_places=2)
    od_cilindro= models.DecimalField(max_digits=10, decimal_places=2)
    od_eje= models.DecimalField(max_digits=10, decimal_places=2)
    od_adicion= models.DecimalField(max_digits=10, decimal_places=2)
    color= models.DecimalField(max_digits=10, decimal_places=2)
    oi_esfera= models.DecimalField(max_digits=10, decimal_places=2)
    oi_cilindro= models.DecimalField(max_digits=10, decimal_places=2)
    oi_eje= models.DecimalField(max_digits=10, decimal_places=2)
    oi_adicion= models.DecimalField(max_digits=10, decimal_places=2)
  
    
    def __unicode__(self):
		return self.od_esfera
		return self.od_cilindro
		return self.od_eje
		return self.od_adicion
		return self.color
		return self.od_esfera
		return self.od_cilindro
		return self.od_esfera
		return self.od_adicion

class autorefractometro(models.Model):
    od_esfera= models.DecimalField(max_digits=10, decimal_places=2)
    od_cilindro= models.DecimalField(max_digits=10, decimal_places=2)
    od_eje= models.DecimalField(max_digits=10, decimal_places=2)
    od_prisma= models.DecimalField(max_digits=10, decimal_places=2)
    oi_esfera= models.DecimalField(max_digits=10, decimal_places=2)
    oi_cilindro= models.DecimalField(max_digits=10, decimal_places=2)
    oi_eje= models.DecimalField(max_digits=10, decimal_places=2)
    oi_prisma= models.DecimalField(max_digits=10, decimal_places=2)
  
    
    def __unicode__(self):
		return self.od_esfera
		return self.od_cilindro
		return self.od_eje
		return self.od_primas
		return self.od_esfera
		return self.od_cilindro
		return self.od_eje
		return self.od_prisma

class agudesavisual(models.Model):
    avsc_od= models.DecimalField(max_digits=10, decimal_places=2)
    avsc_os= models.DecimalField(max_digits=10, decimal_places=2)
    avsc_ov= models.DecimalField(max_digits=10, decimal_places=2)
    avant_od= models.DecimalField(max_digits=10, decimal_places=2)
    avant_os= models.DecimalField(max_digits=10, decimal_places=2)
    avant_ov= models.DecimalField(max_digits=10, decimal_places=2)
    pinhole_od= models.DecimalField(max_digits=10, decimal_places=2)
    pinhole_os= models.DecimalField(max_digits=10, decimal_places=2)
	pinhole_ov= models.DecimalField(max_digits=10, decimal_places=2)
	avactual_od= models.DecimalField(max_digits=10, decimal_places=2)
	avactual_os= models.DecimalField(max_digits=10, decimal_places=2)
	avactual_ov= models.DecimalField(max_digits=10, decimal_places=2)
  
    
    def __unicode__(self):
		return self.avsc_od
		return self.avsc_os
		return self.avsc_ov
		return self.avant_od
		return self.avant_os
		return self.avant_ov
		return self.pinhole_od
		return self.pinhole_os
		return self.pinhole_ov
		return self.avactual_od
		return self.avactual_os
		return self.avactual_ov
