from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('favorit-book', views.FavoritView.as_view(), name='fav-book'),
    path('book/<slug:slug>/', views.BookDetailsView.as_view(), name='book_info'),
    
]