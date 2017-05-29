from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import calc_log


def index(request):
    # 5 most recent logs
    raw = calc_log.objects.order_by('-calc_time')
    first = raw[0]
    calc_log_list = []
    for log in raw:
        calc_log_list.append(log.__str__())
    context = {
        'first': first,
        'calc_log_list': calc_log_list
    }
    return render(request, 'calc/index.html', context)


class IndexView(generic.ListView):
    template_name = 'calc/index.html'
    context_object_name = 'calc_log_list'

    def get_queryset(self):
        return calc_log.objects.order_by('-calc_time')


def boot_submit(request):
    print(request.POST)
    if 'submit' in request.POST:
        op_a = request.POST['op_a']
        op = request.POST['op']
        op_b = request.POST['op_b']
        op_a = float(op_a)
        op_b = float(op_b)

        if op == "+":
            res = op_a + op_b
        elif op == "-":
            res = op_a - op_b
        elif op == "*":
            res = op_a * op_b
        elif op == "/":
            res = op_a / op_b
        elif op == "^":
            res = op_a ** op_b
        new_rec = calc_log(op_a=op_a, op=op, op_b=op_b, res=res, calc_time=timezone.now())
        new_rec.save()
        # Used instead of redirect so that back button goes back to calc page
    elif 'clear' in request.POST:
        new_rec = calc_log(op_a=0, op='c', op_b=0, res=0, calc_time=timezone.now())
        new_rec.save()

    return HttpResponseRedirect(reverse('calc:generic_index'))
