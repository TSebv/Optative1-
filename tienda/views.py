from django.shortcuts import render
from .models import Producto,Pedido,cliente

def home(request):
    return render(request, "tienda/home.html", {})

"""
Vista para listar productos
"""
def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos":productos})