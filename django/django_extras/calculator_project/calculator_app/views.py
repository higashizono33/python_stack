from django.shortcuts import render, HttpResponse
from django.views.generic import View
from django.core.exceptions import ImproperlyConfigured

class Main(object):
    template = ''
    favorite_number = None
    least_favorite_number = None
    result = None
    
    def get(self, request):
        context = Calculator.result
        return render(request, self.template, context)
    
    def get_template(self):
        if self.template == '':
            raise ImproperlyConfigured('"Template" not defined.')
        return self.template
    
    def add(self, num1, num2):
        result = num1 + num2
        return result
    
    def subtract(self, num1, num2):
        result = num1 - num2
        return result
    
    def multiply(self, num1, num2):
        result = num1 * num2
        return result
    
    def divide(self, num1, num2):
        result = num1 / num2
        return result

class Calculator(Main, View):
    template = 'calculator/index.html'
    favorite_number = 22
    least_favorite_number = 1
    result = {}
    sum = Main.add(None, favorite_number, least_favorite_number)
    result.update({'sum': sum})
    difference = Main.subtract(None, favorite_number, least_favorite_number)
    result.update({'difference': difference})
    product = Main.multiply(None, favorite_number, least_favorite_number)
    result.update({'product': product})
    factor = Main.divide(None, favorite_number, least_favorite_number)
    result.update({'factor': int(factor)})