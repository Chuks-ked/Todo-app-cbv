from django.urls import path
from . import views

urlpatterns = [
    path('', views.alltodos.as_view(), name="alltodos"),
    path('<pk>/delete/', views.deleteItem.as_view(), name="deleteItem"),
    path('<pk>/update', views.updateItem.as_view(), name="updateItem")
]
