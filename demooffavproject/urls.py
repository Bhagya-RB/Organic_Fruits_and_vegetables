"""demooffavproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import include, path
from mainapp import views as main_views
from consumerapp import views as consumer_views
from supplierapp import views as supplier_views
from adminapp import views as admin_views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_views.home, name='home'),
    path('about',main_views.about, name='about'),
    path('products',main_views.products, name='products'),
    # path('vegetables',main_views.vegetables,name='vegetables'),
    # path('millets',main_views.millets, name='millets'),
    # path('dried',main_views.dried, name='dried'),
    path('contact',main_views.contact, name='contact'),
    path('cart',main_views.cart, name='cart'),

    # consumers path
    path('consumer-home',consumer_views.consumer_home, name='consumer-home'),
    path('consumer-viewproducts',consumer_views.consumer_view_products,name='consumer-viewproducts'),

  
    
    path('consumer-registration',consumer_views.consumer_reg, name='consumer-registration'),
    path('consumer-login',consumer_views.consumer_login, name='consumer-login'),
    path('consumer-viewprofile',consumer_views.consumer_view_profile, name='consumer-viewprofile'),

    path('consumer-viewprofile/<int:id>/',consumer_views.consumer_view_profile, name='consumer-viewprofile'),


    path('consumer-detailofproduct',consumer_views.consumer_detail_of_products, name='consumer-detailofproduct'),
  

    #To view the detailsbased on category F=products, V=Vegetables, M=Millets, D=Dried
    path('consumer-detailofproduct/<str:id>/',consumer_views.consumer_detail_of_products,name='consumer-detailofproduct'),
    

    path('consumer-CartModel',consumer_views.consumer_add_to_cart, name='consumer-CartModel'),
    path('consumer-addtowishlist',consumer_views.consumer_add_to_wishlist, name='consumer-addtowishlist'),
    path('consumer-checkout',consumer_views.consumer_checkout, name='consumer-checkout'),
    path('consumer-debitcardpayment',consumer_views.consumer_debit_card_payment, name='consumer-debitcardpayment'),
    path('consumer-creditcardpayment',consumer_views. consumer_credit_card_payment, name='consumer-creditcardpayment'),
    path('consumer-netbanking',consumer_views.conusmer_net_banking, name='consumer-netbanking'),
    path('consumer-feedback',consumer_views.consumer_feedback,name='consumer-feedback'),

    #CONSUMER forgot password - To reset password urls
    # path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    # path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    #suppliers path
    path('supplier-home',supplier_views.supplier_home,name='supplier-home'),
    path('supplier-registration',supplier_views.supplier_reg, name='supplier-registration'),
    path('supplier-login',supplier_views.supplier_login, name='supplier-login'),
    path('supplier-viewprofile',supplier_views.supplier_view_profile, name='supplier-viewprofile'),
    path('supplier-orders',supplier_views.supplier_view_orders, name='supplier-orders'),
    path('supplier-orderhistory',supplier_views.supplier_order_history, name='supplier-orderhistory'),
    path('supplier-verifysupplier',supplier_views.supplier_verify_supplier, name='supplier-verifysupplier'),
    path('supplier-feedback',supplier_views.supplier_view_feedback, name='supplier-feedback'),

    #admin path
    path('admin-home',admin_views.admin_home, name='admin-home'),
    path('admin-login',admin_views.admin_login, name='admin-login'),
    path('admin-viewprofile',admin_views.admin_view_profile, name='admin-viewprofile'),
    path('admin-addproducts',admin_views.admin_add_products,name='admin-addproducts'),

    path('admin-viewconsumer',admin_views.admin_view_consumer, name='admin-viewconsumer'),

     #Admin view consumer accept reject
    path('accept_consumer/<int:id>/',admin_views.accept_consumer, name='accept_consumer'),
    path('reject_consumer/<int:id>/',admin_views.reject_consumer, name='reject_consumer'),

    path('admin-viewsupplier',admin_views.admin_view_supplier, name='admin-viewsupplier'),

     #Admin view supplier accept reject
    path('accept_supplier/<int:id>/',admin_views.accept_supplier, name='accept_supplier'),
    path('reject_supplier/<int:id>/',admin_views.reject_supplier, name='reject_supplier'),

    path('admin-verifysupplier',admin_views.admin_verify_supplier, name='admin-verifysupplier'),

    #Admin verify supplier accept reject
    path('accept_verify_supplier/<int:id>/',admin_views.accept_verify_supplier, name='accept_verify_supplier'),
    path('reject_verify_supplier/<int:id>/',admin_views.reject_verify_supplier, name='reject_verify_supplier'),

    path('admin-vieworders',admin_views.admin_view_orders, name='admin-vieworders'),
    path('admin-viewenquiry',admin_views.admin_view_enquiry, name='admin-viewenquiry'),

    path('admin-viewpayments',admin_views.admin_view_payment, name='admin-viewpayments'),
    path('admin-viewalladdedproducts',admin_views.admin_view_added_products, name='admin-viewalladdedproducts'),

    path('admin-viewalladdedproducts/<str:id>/',admin_views.delete_products, name='admin-viewalladdedproducts'),

    path('admin-editaddedproducts',admin_views.admin_edit_added_products, name='admin-editaddedproducts'),
    path('admin-editaddedproducts/<str:id>/',admin_views.admin_edit_added_products, name='admin-editaddedproducts'),

    path('admin-viewfeedback',admin_views.admin_view_feedback, name='admin-viewfeedback'),

    path('accounts/',include('allauth.urls'))

    ]

urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)