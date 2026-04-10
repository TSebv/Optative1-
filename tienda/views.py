from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Pedido, Cliente
from .forms import ProductoForm


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

def detalle_cliente(request, pk):
    cliente = get_object_or_404(cliente, pk=pk)
    pedidos = cliente.pedidos.select_related("cliente").prefetch_related("productos)").order_by("-fecha")
    return render(
        request,
        "tienda/detalle_cliente.html",
        {
            "cliente": cliente,
            "pedidos": pedidos
        }
    )

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tienda:lista_productos")
    else:
        form = ProductoForm()
    return render(request, "tienda/crear_producto.html", {"form": form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("tienda:detalle_producto", pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)

    return render(request,"tienda/editar_producto.html", {"form": form, "producto": producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.delete()
        return redirect("tienda:lista_productos")

    return render(request,"tienda/eliminar_producto.html", {"producto": producto})

from .models import Cliente
from .forms import ClienteForm
from django.shortcuts import render, redirect, get_object_or_404

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "tienda/lista_clientes.html", {"clientes": clientes})


def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("lista_clientes")
    return render(request, "tienda/crear_cliente.html", {"form": form})


def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("lista_clientes")
    return render(request, "tienda/editar_cliente.html", {"form": form})


def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        cliente.delete()
        return redirect("tienda:lista_clientes")

    return render(request, "tienda/eliminar_cliente.html", {"cliente": cliente})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    pedidos = Pedido.objects.filter(cliente=cliente)\
        .select_related("cliente")\
        .prefetch_related("productos")\
        .order_by("-fecha")

    return render(
        request,
        "tienda/detalle_cliente.html",
        {
            "cliente": cliente,
            "pedidos": pedidos
        }
    )

