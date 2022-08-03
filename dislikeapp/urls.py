from django.urls import path

from dislikeapp.views import DisLikeArticleView

app_name ="dislikeapp"
urlpatterns = [
    # path()
    path('article/dislike/<int:pk>', DisLikeArticleView.as_view(), name='article_dislike'),

]