from django.urls import path
from .views import NewsList, PostDetail, PostCreate, PostSearch, ArticleCreate



urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('posts/', NewsList.as_view()),
   path('posts/<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('posts/search/',PostSearch.as_view(), name = 'post_search'),
   path('news/create/', PostCreate.as_view(), name='news_create'),
   path('articles/create/', ArticleCreate.as_view(), name='articles_create'),

]