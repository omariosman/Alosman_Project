

from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
##views



@api_view(['GET'])
def product_list_api(request):
    all_products = Product.objects.all()
    data = ProductSerializer(all_products, many=True).data
    return Response({'data': data})

@api_view(['GET'])  
def product_detail_api(request, code):
    product = Product.objects.get(code=code)
    data = ProductSerializer(product).data
    return Response({'data': data})


#Class Based View
class ProductListAPI(generics.ListAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
#Get one Product, Update, Delete
class ProductDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'code'

    

