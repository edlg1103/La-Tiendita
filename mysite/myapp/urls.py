from django.contrib import admin
from django.urls import path
from . import views

app_name='myapp'

urlpatterns = [
    path("",views.index),
    path('products/',views.products,name='products' ),
    path('products/<int:pk>',views.ProductDetailView.as_view()),
    path('products/add/',views.add_product,name='add_product'),
    path('products/update/<int:id>',views.update_product,name="update_product"),
    path('products/delete/<int:id>',views.delete_product,name="delete_product"),
    path('products/mylistings',views.my_listings,name='mylistings' ),
    path('success/',views.PaymentSuccessView.as_view(),name='success'),
    path('Failed/',views.PaymentFailedView.as_view(),name='failed'),
    path('api/checkout-session/<id>',views.create_checkout_session,name='api_checkout_session')
]
