from django.conf.urls import url
from django.urls import path


from . import views
from . import api

app_name="products"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^products/$', views.all_products, name="all_products"), #This name will be used in templates in url
    url(r'^(?P<code>[a-zA-Z0-9]+)/$', views.product, name="product"),
    url(r'^add_product/$', views.add_product, name="add_product"),
    url(r'^(?P<code>[a-zA-Z0-9]+)/edit_product/$', views.edit_product, name="edit_product"),
    url(r'^add_transactions/$', views.add_transactions, name="add_transactions"),
    url(r'^add_transaction/$', views.add_transaction, name="add_transaction"),
    
    #api 
    path('api/products', api.product_list_api, name="product_list_api"),
    path('api/products/<code>', api.product_detail_api, name="product_detail_api"),
    
    #class Based Views
    path('api/v2/products', api.ProductListAPI.as_view(), name="ProductListAPI"),
    path('api/v2/products/<code>', api.ProductDetailAPI.as_view(), name="ProductDetailAPI"),

]
