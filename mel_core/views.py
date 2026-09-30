from django.shortcuts import render
from .models import SGC, Project, IndicatorValue

def dashboard(request):
    sgcs = SGC.objects.all()
    projects = Project.objects.all()
    recent_measurements = IndicatorValue.objects.order_by('-date_recorded')[:10]

    context = {
        'sgcs_count': sgcs.count(),
        'projects_count': projects.count(),
        'recent_measurements': recent_measurements,
    }
    return render(request, 'mel_core/dashboard.html', context)
