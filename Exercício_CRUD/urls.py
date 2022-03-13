
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.produtolist, name='produto_list'),
    path('produto/<int:id>', views.produtoView, name='produto-view'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>', views.editarProduto, name='editar-produto'),
    path('deletar/<int:id>', views.deletarProduto, name='deletar-produto')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
