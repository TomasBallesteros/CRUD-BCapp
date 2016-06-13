from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from .models import presupuesto
from insumo.models import insumo
from obra.models import obra
from .forms import presupuestoForm

def inicio(request):
    Insumo = insumo.objects.all()
    Obra = obra.objects.all()
    Presupuesto = presupuesto.objects.all()
    return render(request, 'inicio.html', {'Insumo': Insumo, 'Obra': Obra, 'Presupuesto': Presupuesto})

def presupuestoCreation(request, template='presupuestoForm.html'):
    form = presupuestoForm()
    if request.method == "POST":
        form = presupuestoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'presupuestoNuevo.html')
    kwvars = {
        "form": form,
    }
    return render_to_response(template, kwvars, context_instance=RequestContext(request))

def presupuestoList(request):
    Presupuesto = presupuesto.objects.all()
    return render(request, 'presupuestoListado.html', {'Presupuesto': Presupuesto})

def presupuestoDetail(request, idPresupuesto, template='presupuestoDetalle.html'):
    Presupuesto = get_object_or_404(presupuesto, pk=idPresupuesto)
    return render_to_response(template, {'Presupuesto': Presupuesto}, context_instance=RequestContext(request))

def presupuestoDelete(request, id_Presupuesto):
    instance = get_object_or_404(presupuesto, idPresupuesto=id_Presupuesto)
    instance.delete()
    Presupuesto = presupuesto.objects.all()
    return render(request, 'presupuestoListado.html', {'Presupuesto': Presupuesto})

def presupuestoUpdate(request, id_Presupuesto):
    instance = get_object_or_404(presupuesto, idPresupuesto=id_Presupuesto)
    form = presupuestoForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            Presupuesto = presupuesto.objects.all()
            return render(request, 'presupuestoListado.html', {'Presupuesto': Presupuesto})
    return render(request, 'presupuestoDetalle.html', {'form': form})
