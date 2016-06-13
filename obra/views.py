from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import obra
from presupuesto.models import presupuesto
from .forms import obraForm

def inicio(request):
    Obra = obra.objects.all()
    Presupuesto = presupuesto.objects.all()
    return render(request, 'inicio.html', {'Obra': Obra, 'Presupuesto': Presupuesto})

def obraCreation(request, template='obraForm.html'):
    form = obraForm()
    if request.method == "POST":
        form = obraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'obraNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def obraList(request):
    Obra = obra.objects.all()
    return render(request, 'obraListado.html', {'Obra': Obra})

def obraDetail(request, id, template='obraDetalle.html'):
    Obra = get_object_or_404(obra, pk=id)
    return render_to_response(template, {'Obra': Obra}, context_instance=RequestContext(request))

def obraDelete(request, id_nit):
    instance = get_object_or_404(obra, id=id_nit)
    instance.delete()
    Obra = obra.objects.all()
    return render(request, 'obraListado.html', {'Obra': Obra})

def obraUpdate(request, id_nit):
     instance = get_object_or_404(obra, id=id_nit)
     form = obraForm(request.POST or None, instance=instance)
     if request.method == 'POST':
        if form.is_valid():
            form.save()
            Obra = obra.objects.all()
            return render(request, 'obraListado.html', {'Obra': Obra})
     return render(request, 'obraDetalle.html', {'form': form})
