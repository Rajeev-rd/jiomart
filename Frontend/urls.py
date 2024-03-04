from django.urls import path
from Frontend import views

urlpatterns = [
    path('Home/',views.Home,name="Home"),
    path('productpage/<catname>/',views.productpage,name="productpage"),
    path('aboutview/',views.aboutview,name="aboutview"),
    path('contactview/',views.contactview,name="contactview"),
    path('singleproduct/<int:proid>',views.singleproduct,name="singleproduct"),
    path('contactsave/',views.contactsave,name="contactsave"),
    path('loginsignup/',views.loginsignup,name="loginsignup"),
    path('saveuser/',views.saveuser,name="saveuser"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('cart/',views.cart,name="cart"),
    path('cartsave/',views.cartsave,name="cartsave"),
    ]