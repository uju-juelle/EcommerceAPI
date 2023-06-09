from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from Ecommerce.models import Product


class list_All_Product_page(APIView):
    def get(self, request):
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "not valid"}, status=status.HTTP_400_BAD_REQUEST)
    


class single_page(APIView):
    def get(self, request, id):
        single = Product.objects.get(id=id)
        serializer = ProductSerializer(single)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        serializers = Product.objects.get(id=id)
        serializers.delete()
        return Response("successfully deleted", status=status.HTTP_200_OK)
    




