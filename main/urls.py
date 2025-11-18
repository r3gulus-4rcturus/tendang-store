from django.urls import path
import main.views as views

appname='main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('show_product/<str:product_id>', views.show_product_by_id, name='show_product_by_id'),
    # path('create_product/', create_product , name='create_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', views.delete_product, name='delete_product'),
    path('add_product_by_ajax/', views.add_product_by_ajax, name='add_product_by_ajax'),
    path('update_product_by_ajax/', views.update_product_by_ajax, name='update_product_by_ajax'),
    path('ajax/register/', views.register_ajax, name='ajax_register'),
    path('ajax/login/', views.login_ajax, name='ajax_login'),
    path('ajax/logout/', views.logout_ajax, name='ajax_logout'),
    path('proxy-image/', views.proxy_image, name='proxy_image'),
    path('create-flutter/', views.create_product_flutter, name='create_news_flutter'),
]