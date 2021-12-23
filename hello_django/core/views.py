from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))

def soma(request, fist_number, second_number):
    number = fist_number + second_number
    return HttpResponse('<h1>Resultado: {}</h1>'.format(number))

def multiplicacao(request, fist_number, second_number):
    number = fist_number - second_number
    return HttpResponse('<h1>Resultado: {}</h1>'.format(number))

def divisao(request, fist_number, second_number):
    number = fist_number / second_number
    return HttpResponse('<h1>Resultado: {}</h1>'.format(number))

def subtracao(request, fist_number, second_number):
    number = fist_number - second_number
    return HttpResponse('<h1>Resultado: {}</h1>'.format(number))