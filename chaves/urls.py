from chaves import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path(r'chaves/', views.ListarChave.as_view()),
    path(r'chaves/validate/<slug:chave>/', views.ValidarChave.as_view()),
    path(r'chaves/<int:pk>/', views.DetalharChave.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
