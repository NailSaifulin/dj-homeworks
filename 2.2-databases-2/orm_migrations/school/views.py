from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render
from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.order_by('group').all()\
        .prefetch_related(Prefetch('teachers', to_attr='prefetched_student'))
    context = {'object_list': object_list}
    return render(request, template, context)
