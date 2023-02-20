from django.shortcuts import render
from products.models import  Product
# Create your views here.

def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': [
                {
                    'id': product.id,
                    'title': product.title,
                    'rate': product.rate,
                    'image': product.image,
                    'hashtags': product.hashtags.all()

                }
                for product in products
            ]
        }
        return  render(request, 'products/products.html', context=context)
