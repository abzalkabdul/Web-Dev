from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Product, Category

def product_list(request):
    data = Product.objects.all()
    data_json = [d.to_json() for d in data]
    return JsonResponse(data_json, safe=False, json_dumps_params={"indent": 4})

def get_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id) 
    return JsonResponse(product.to_json(), json_dumps_params={"indent": 4})

def category_list(request):
    categories = Category.objects.all()
    category_json = [c.to_json() for c in categories]
    return JsonResponse(category_json, safe=False, json_dumps_params={"indent": 4})

def get_category(request, id):
    category = get_object_or_404(Category, pk=id)
    return JsonResponse(category.to_json(), json_dumps_params={"indent": 4})


def products_by_category(request, id):
    category = Category.objects.get(pk=id)
    c_products = category.products.all()
    c_products_json = [p.to_json() for p in c_products]
    return JsonResponse(c_products_json, safe=False, json_dumps_params={"indent": 4})
