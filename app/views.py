from django.shortcuts import render
from django.views import View


class Add(View):
    def get(self, request):
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')

        if num1 is not None and num2 is not None:
            try:
                num1 = float(num1)
                num2 = float(num2)
            except ValueError:
                print('ooops')
                return render(request, 'app/add.html')
            answer = num1 + num2
            return render(request, 'app/add.html', {'answer': answer})
        else:
            return render(request, 'app/add.html')

class Double(View):
    def get(self, request):
        num = request.GET.get('num')

        if num is not None:
            answer = float(num) * 2
            return render(request, 'app/double.html', {'answer': answer})
        else:
            return render(request, 'app/double.html')

class Mult_three(View):
    def get(self, request):
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')
        num3 = request.GET.get('num3')

        if num1 is not None and num2 is not None and num3 is not None:
            answer = float(num1) * float(num2) * float(num3)
            return render(request, 'app/multthree.html', {'answer': answer})
        else:
            return render(request, 'app/multthree.html')
