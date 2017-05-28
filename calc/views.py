from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import calc_log


def index(request):
    # 5 most recent logs
    calc_log_list = calc_log.objects.order_by('-calc_time')[:5]
    context = {
        'calc_log_list': calc_log_list
    }
    return render(request, 'calc/index.html', context)
