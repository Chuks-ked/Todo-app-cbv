from django.urls import path
from . import views

urlpatterns = [
    path('', views.Alltodos.as_view(), name="alltodos"),
    path('<pk>/delete/', views.DeleteItem.as_view(), name="deleteItem"),
    path('<pk>/update', views.UpdateItem.as_view(), name="updateItem")
]
