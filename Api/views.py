from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from Ecommerce.models import Product
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveAPIView


# class list_All_Product_page(APIView):
#     def get(self, request):
#         all_products = Product.objects.all()
#         serializer = ProductSerializer(all_products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    


# class single_page(APIView):
#     def get(self, request, id):
#         single = Product.objects.get(id=id)
#         serializer = ProductSerializer(single)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

# class category_page(APIView):
#     def get(self, request):
#         all_category = Product.objects.get("category")
#         serializer = ProductSerializer(all_category, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    


