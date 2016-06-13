from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import insumo
from presupuesto.models import presupuesto
from .forms import insumoForm

def inicio(request):
    Insumo = insumo.objects.all()
    Presupuesto = presupuesto.objects.all()
    return render(request, 'inicio.html', {'Insumo': Insumo, 'Presupuesto': Presupuesto})

def insumoCreation(request, template='insumoForm.html'):
    form = insumoForm()
    if request.method == "POST":
        form = insumoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'insumoNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def insumoList(request):
    Insumo = insumo.objects.all()
    return render(request, 'insumoListado.html', {'Insumo': Insumo})

def insumoDetail(request, id, template='insumoDetalle.html'):
    Insumo = get_object_or_404(insumo, pk=id)
    return render_to_response(template, {'Insumo': Insumo}, context_instance=RequestContext(request))

def insumoDelete(request, id_codigo):
    instance = get_object_or_404(insumo, id=id_codigo)
    instance.delete()
    Insumo = insumo.objects.all()
    return render(request, 'insumoListado.html', {'Insumo': Insumo})

def insumoUpdate(request, id_codigo):
    instance = get_object_or_404(insumo, id=id_codigo)
    form = insumoForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Insumo = insumo.objects.all()
            return render(request, 'insumoListado.html', {'Insumo': Insumo})
    return render(request, 'insumoDetalle.html', {'form': form})
