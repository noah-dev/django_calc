from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.utils import timezone

from .models import calc_log


def index(request):
    # 5 most recent logs
    calc_log_list = calc_log.objects.order_by('-calc_time')
    context = {
        'calc_log_list': calc_log_list
    }
    return render(request, 'calc/index.html', context)


def test_in(request):
    in_string = request.POST['in_string']
    op_a = float(in_string)
    new_rec = calc_log(op_a=op_a, op='*', op_b=0, res=0, calc_time=timezone.now())
    new_rec.save()
    return redirect('/calc/')
