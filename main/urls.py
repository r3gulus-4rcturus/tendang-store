from django.urls import path
from main.views import edit_product, delete_product, create_product, login_user, logout_user, register, show_main, show_product_by_id, show_xml, show_json, show_json_by_id, show_xml_by_id

appname='main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('show_product/<str:product_id>', show_product_by_id, name='show_product_by_id'),
    path('create_product/', create_product , name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
] 