from django.shortcuts import render, get_object_or_404
from .models import Producto, Pedido, Cliente

def home(request):
    return render(request, "tienda/home.html", {})

"""
Vista para listar productos
"""
def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(request, "tienda/lista_productos.html", {"productos": productos})

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "tienda/detalle_producto.html",{"producto": producto})

def lista_pedidos(request):
    pedidos = Pedido.objects.all().order_by("-fecha")
    return render(request, "tienda/lista_pedidos.html", {"pedidos": pedidos})


def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, "tienda/detalle_pedido.html", {"pedido": pedido})
