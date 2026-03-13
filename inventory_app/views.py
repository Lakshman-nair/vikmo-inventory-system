from rest_framework import viewsets
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product, Dealer, Order, Inventory, OrderItem
from .serializers import ProductSerializer, DealerSerializer, OrderSerializer, InventorySerializer


# ---------------- API VIEWSETS ---------------- #

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


# ---------------- DASHBOARD ---------------- #

def dashboard(request):

    product_count = Product.objects.count()
    dealer_count = Dealer.objects.count()
    inventory_count = Inventory.objects.count()

    inventory = Inventory.objects.select_related("product")

    orders = Order.objects.select_related("dealer").order_by("-created_at")[:5]

    return render(request, "inventory_app/dashboard.html", {
        "product_count": product_count,
        "dealer_count": dealer_count,
        "inventory_count": inventory_count,
        "inventory": inventory,
        "orders": orders
    })


# ---------------- INVENTORY ---------------- #

def inventory(request):

    items = Inventory.objects.select_related("product")

    return render(request, "inventory_app/inventory.html", {
        "items": items
    })


# ---------------- DELETE INVENTORY ---------------- #

def delete_inventory(request, id):

    item = get_object_or_404(Inventory, id=id)
    item.delete()

    return redirect("/inventory/")


# ---------------- CREATE ORDER ---------------- #

def create_order(request):

    dealers = Dealer.objects.all()
    products = Product.objects.all()

    if request.method == "POST":

        dealer_id = request.POST.get("dealer")

        products_list = request.POST.getlist("product[]")
        prices = request.POST.getlist("price[]")
        quantities = request.POST.getlist("quantity[]")
        totals = request.POST.getlist("line_total[]")

        dealer = get_object_or_404(Dealer, id=dealer_id)

        order_number = f"ORD-{Order.objects.count()+1:04d}"

        order = Order.objects.create(
            order_number=order_number,
            dealer=dealer,
            total_amount=0
        )

        total_amount = 0

        for i in range(len(products_list)):

            if products_list[i]:

                product = get_object_or_404(Product, id=products_list[i])
                quantity = int(quantities[i])
                price = float(prices[i])
                line_total = float(totals[i])

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    unit_price=price,
                    line_total=line_total
                )

                inventory = get_object_or_404(Inventory, product=product)

                if inventory.quantity >= quantity:
                    inventory.quantity -= quantity
                    inventory.save()

                total_amount += line_total

        order.total_amount = total_amount
        order.save()

        return redirect("/create-order/")

    return render(request, "inventory_app/create_order.html", {
        "dealers": dealers,
        "products": products
    })




def track_order(request, id):

    order = get_object_or_404(Order, id=id)

    return render(request, "inventory_app/order_tracking.html", {
        "order": order
    })


# ---------------- DEALERS ---------------- #

def dealers_page(request):

    dealers = Dealer.objects.all()

    return render(request, "inventory_app/dealers.html", {
        "dealers": dealers
    })

def orders_page(request):

    orders = Order.objects.select_related("dealer").all().order_by("-created_at")

    return render(request, "inventory_app/orders.html", {
        "orders": orders
    })