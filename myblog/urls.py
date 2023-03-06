from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, \
    SearchResultView, WriteArticleView, UserPostsView, create_article, contact_view, post_edit
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('write_article', create_article, name='write_article'),
    path('about/', contact_view, name='about'),
    path('my_articles', UserPostsView.as_view(), name='my_articles'),
    path('blog/<int:post_id>/article_update/', post_edit, name='article_update'),
]

