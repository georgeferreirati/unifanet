from django.urls import path
from. import views
app_name = 'calendario'

#criando as urls que serão utilizadas
urlpatterns = [
    path('', views.index, name='index'),
    path('entry/<int:pk>', views.details, name='details'),
    path('entry/add', views.add, name='add'),
    path('entry/delete/<int:id>', views.delete, name='delete'),
    path('entry/alterar/<int:id>', views.alterar, name='alterar'),
]


