from django.shortcuts import render
from django.views import View
from . import forms


class Add(View):
    def get(self, request):
        form = forms.AddForm(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            return render(request, 'app/add.html', {'answer': num1 + num2})
        else:
            return render(request, 'app/add.html')
        # try:
        #     num1 = float(request.GET.get('num1', ''))
        #     num2 = float(request.GET.get('num2', ''))
        # except ValueError:
        #     return render(request, 'app/add.html')
        # else:
        #     return render(request, 'app/add.html', {'answer': (num1 + num2)})


class Double(View):
    def get(self, request):
        form = forms.DoubleForm(data=request.GET)
        if form.is_valid():
            num = form.cleaned_data['num']
            return render(request, 'app/double.html', {'answer': num * 2})
        else:
            return render(request, 'app/double.html')
        # try:
        #     num = float(request.GET.get('num', ''))
        # except ValueError:
        #     return render(request, 'app/double.html')
        # else:
        #     return render(request, 'app/double.html', {'answer': (num * 2)})


class MultThree(View):
    def get(self, request):
        form = forms.MultThree(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            num3 = form.cleaned_data['num3']
            return render(request, 'app/multthree.html', {'answer': num1 * num2 * num3})
        else:
            return render(request, 'app/multthree.html')
        # try:
        #     num1 = float(request.GET.get('num1', ''))
        #     num2 = float(request.GET.get('num2', ''))
        #     num3 = float(request.GET.get('num3', ''))
        # except ValueError:
        #     return render(request, 'app/multthree.html')
        # else:
        #     return render(request, 'app/multthree.html', {'answer': (num1 * num2 * num3)})

class Earnings(View):
    def get(self, request):
        form = forms.Earnings(data=request.GET)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            num3 = form.cleaned_data['num3']
            return render(request, 'app/earnings.html', {'answer': num1 * 15 + num2 * 12 + num3 * 9})
        else:
            return render(request, 'app/earnings.html')
        # try:
        #     num1 = max(int(request.GET.get('num1', '')), 0)
        #     num2 = max(int(request.GET.get('num2', '')), 0)
        #     num3 = max(int(request.GET.get('num3', '')), 0)
        # except ValueError:
        #     return render(request, 'app/earnings.html')
        # else:
        #     return render(request, 'app/earnings.html', {'answer': (num1 * 15 + num2 * 12 + num3 * 9)})

class Both(View):
    def get(self, request):
        print('1')
        form = forms.Both(data=request.GET)
        print('2')
        if form.is_valid():
            print('3')
            bool1 = form.cleaned_data['bool1']
            bool2 = form.cleaned_data['bool2']
            print('bool1:', bool1, 'bool2:', bool2)
            return render(request, 'app/both.html', {'answer': (bool1 and bool2)})
        else:
            return render(request, 'app/both.html')
        # try:
        #     bool1 = request.GET.get('bool1', '') == 'True'
        #     bool2 = request.GET.get('bool2', '') == 'True'
        # except ValueError:
        #     return render(request, 'app/both.html')
        # else:
        #     return render(request, 'app/both.html', {'answer': (bool1 == True and bool2 == True)})

class WalkOrDrive(View):
    # radio button is used for the bool
    def get(self, request):
        try:
            num = float(request.GET.get('num', ''))
            bool = request.GET.get('bool', '') == 'True'
        except ValueError:
            return render(request, 'app/walk-or-drive.html')
        else:
            if num <= 0.25 and bool is True:
                return render(request, 'app/walk-or-drive.html', {'answer': 'walk'})
            else:
                return render(request, 'app/walk-or-drive.html', {'answer': 'drive'})

