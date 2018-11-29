from django.shortcuts import render
from django.views import View


class Add(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1'))
            num2 = float(request.GET.get('num2'))
        except ValueError:
            return render(request, 'app/add.html')
        else:
            return render(request, 'app/add.html', {'answer': (num1 + num2)})


class Double(View):
    def get(self, request):
        try:
            num = float(request.GET.get('num'))
        except ValueError:
            return render(request, 'app/double.html')
        else:
            return render(request, 'app/double.html', {'answer': (num * 2)})


class Mult_three(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1'))
            num2 = float(request.GET.get('num2'))
            num3 = float(request.GET.get('num3'))
        except ValueError:
            return render(request, 'app/multthree.html')
        else:
            return render(request, 'app/multthree.html', {'answer': (num1 * num2 * num3)})

class Earnings(View):
    def get(self, request):
        try:
            num1 = float(request.GET.get('num1'))
            num2 = float(request.GET.get('num2'))
            num3 = float(request.GET.get('num3'))
        except ValueError:
            return render(request, 'app/earnings.html')
        else:
            return render(request, 'app/earnings.html', {'answer': (num1 * 15 + num2 * 12 + num3 * 9)})
