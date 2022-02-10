from django.urls import path

from .views import SourceDetailsView, SourceCreateView, ArticleCreateView, SourcesListView, ArticlesListView

urlpatterns = [
    path('', ArticlesListView.as_view(), name='index'),
    path('article/create/', ArticleCreateView.as_view(), name='create article'),
    path('sources/', SourcesListView.as_view(), name='list sources'),
    path('sources/<int:pk>', SourceDetailsView.as_view(), name='details source'),
    path('sources/create/', SourceCreateView.as_view(), name='create source'),
]