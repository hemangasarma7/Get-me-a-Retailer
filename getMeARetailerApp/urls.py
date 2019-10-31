from django.conf.urls import url
from . import views


app_name = 'getMeARetailerApp'


urlpatterns = [

    # getMeARetailerApp/product/
    url('^product/$', views.ProductList.as_view(), name='product'),

    # getMeARetailerApp/provider/
    url('^provider/$', views.ProviderList.as_view(), name='provider'),

    # getMeARetailerApp/logistic/
    url('^logistic/$', views.LogisticList.as_view(), name='logistic'),

    # getMeARetailerApp/productPricing/
    url('^productPricing/$', views.ProductPriceList.as_view(), name='pricing'),

    # getMeARetailerApp/deliveryTime/
    url('^deliveryTime/$', views.LogisticDeliveryList.as_view(), name='delivery-time'),

]
