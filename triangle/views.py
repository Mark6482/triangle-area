from django.shortcuts import render
import math
from .forms import TriangleForm

def triangle_area(request):
    area = None
    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            a = float(form.cleaned_data['first_side'])
            b = float(form.cleaned_data['second_side'])
            c = float(form.cleaned_data['third_side'])
            if a<=0 or b<=0 or c<=0:
                area = "Некорректные значения, стороны <= 0"
            elif a+b <= c or a+c <= b or b+c <= a:
                area = "Некорректные значения, не образуется треугольник"
            else:
                p=(a+b+c)/2
                try:
                    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
                    print(area)
                except ValueError:
                    area = "Некорректные значения"
                    print(area)
            request.session['triangle_area'] = area
            context = {'form': form, 'area': area}
            return render(request, 'triangle/triangle.html', context)
        else:
            area = "Некорректные значения"
            context = {'form': form, 'area': area}
            return render(request, 'triangle/triangle.html', context)
    else:
        form=TriangleForm()
    context = {'form': form, 'area': area}
    return render(request, 'triangle/triangle.html', context)
    