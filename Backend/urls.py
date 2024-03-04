
from django.urls import path
from Backend import views

urlpatterns = [
    path('indexview/',views.indexview,name="indexview"),
    path('registercat/',views.registercat,name="registercat"),
    path('catsave/',views.catsave,name="catsave"),
    path('displaycat/',views.displaycat,name="displaycat"),
    path('editcat/<int:c_id>/',views.editcat,name="editcat"),
    path('deletecat/<int:c_id>/',views.deletecat,name="deletecat"),
    path('updatecat/<int:c_id>/',views.updatecat,name="updatecat"),



    path('product/',views.product,name="product"),
    path('prodcutsave/',views.prodcutsave,name="prodcutsave"),
    path('displayproduct/',views.displayproduct,name="displayproduct"),
    path('editproduct/<int:p_id>',views.editproduct,name="editproduct"),
    path('updateproduct/<int:p_id>',views.updateproduct,name="updateproduct"),
    path('deleteproduct/<int:p_id>',views.deleteproduct,name="deleteproduct"),

    path('logicpage/',views.logicpage,name="logicpage"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
]
