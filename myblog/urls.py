from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, \
    SearchResultView, UserPostsView, create_article, \
    contact_view, DeleteArticleView, edit_post
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('my_articles/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('write_article', create_article, name='write_article'),
    path('about/', contact_view, name='about'),
    path('my_articles', UserPostsView.as_view(), name='my_articles'),
    path('blog/<slug>/delete_article_form/', DeleteArticleView.as_view(), name='delete_article_form'),
    # path('blog/<slug>/update/', ArticleUpdateView.as_view(), name='edit_article'),
    path('blog/<slug>/edit_article', edit_post, name='edit_article'),
]

