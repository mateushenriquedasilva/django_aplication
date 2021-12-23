# Django🐍
<div align="center">
	<img src="https://www.djangoproject.com/m/img/logos/django-logo-negative.png" alt="logo django">
</div>

[Django](https://www.djangoproject.com/) é um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view.

### Agenda🐍
* Sistemas Web
* Vantagens de um sistema Web
* Python para web
* Framework Django 

### Objetivos do curso🐍
* Aprender mais sobre sistemas web
* Aprender a utilizar Python para desenvolvimento Web
* Aprender o framework Django
* Aprender a manipular informações em bancos de dados na sua aplicação
  
---

## Python para web🐍

Python é uma linguagem que é utilizada em muitos seguimentos, como Ciência de dados, administração de sistemas, desenvolvimento de software desktop(GUI), jogos, aplicativos e é claro para sistemas web.

Além do Django, existem outros frameworks que auxiliam no desenvolvimento web com Python que também são muito populares, como: Flask, Pyramid, Tornado, web2py e Bottle.

---

## PIP🐍

* Sistema de gerenciamento de pacotes
* Utilizado para instalar e gerenciar pacotes/bibliotecas em Python
* Já vem empacotado com Python desde a versão 3.4 do Python


```bash
$ python -m pip install Django
```

## Virtualenv🐍

* Ferramenta para criar ambientes Python isolados
* Vem integrado com Python desde a versão 3.3 do Python
* Extremamemte útil para se trabalhar com projetos que utilizam bibliotecas com versões difirentes

```bash
$ python -m venv ./folder
$ pip install django
```

---

## Criando um projeto Django🐍

Para criar um projeto Django é necessário uma estrutura padrão que pode ser criada a partir do comando "django-admin startprojct" || "python -m django startproject mysite"

## Criando um app🐍

Para criar um app no Django é necessário uma estrutura padrão que pode ser criada a partir do comando "django-admin startapp" || "python -m django startapp myapp"

## Start Django

```bash
$ python manage.py runserver
```
