from django.contrib import admin
from .models import Mascota
from .models import Historia_Clinica
from .models import Medicamento

# Register your models here.
admin.site.register(Mascota)
admin.site.register(Historia_Clinica)
admin.site.register(Medicamento)
