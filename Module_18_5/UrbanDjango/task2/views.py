from django.shortcuts import render
from django.views.generic import TemplateView

def class_template(request):
    return render(request,'second_task/class_template.html')

class Func_template(TemplateView):
    template_name = 'second_task/func_template.html'

# Create your views here.
