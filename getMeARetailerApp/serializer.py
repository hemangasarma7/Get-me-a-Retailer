from rest_framework import serializers
from .models import Provider, Product, Logistic


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class LogisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logistic
        fields = '__all__'


class ProductTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title']


class ProductPriceWithSiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'site', 'price')


class LogisticItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logistic
        fields = ['item']


class ItemWithDeliveryTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logistic
        fields = ('title', 'delivery_time')
