from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Provider, Product, Logistic
from .serializer import ProviderSerializer, ProductSerializer, LogisticSerializer, \
    ProductTitleSerializer, LogisticItemSerializer, ProductPriceWithSiteSerializer, ItemWithDeliveryTimeSerializer
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
class ProviderList(APIView):

    def get(self, request):
        providers = Provider.objects.all()
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogisticList(APIView):

    def get(self, request):
        logistics = Logistic.objects.all()
        serializer = LogisticSerializer(logistics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LogisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductPriceList(APIView):

    def post(self, request):
        serializer = ProductTitleSerializer(data=request.data)
        try:
            if serializer.is_valid():
                product_prices = Product.objects.filter(title=serializer.data['title'])
                price_site_serializer = ProductPriceWithSiteSerializer(product_prices, many=True)
                return Response(price_site_serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class LogisticDeliveryList(APIView):

    def post(self, request):
        serializer = LogisticItemSerializer(data=request.data)
        try:
            if serializer.is_valid():
                logistics = Logistic.objects.filter(item=serializer.data['item'])
                delivery_serializer = ItemWithDeliveryTimeSerializer(logistics, many=True)
                product = Product.objects.filter(id=serializer.data['item'])
                product_serializer = ProductSerializer(product, many=True)
                provider = Provider.objects.filter(id=product[0].site.id)
                provider_serializer = ProviderSerializer(provider, many=True)
                return Response(product_serializer.data + provider_serializer.data +
                                delivery_serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
