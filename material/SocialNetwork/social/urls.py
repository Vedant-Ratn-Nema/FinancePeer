from django.urls import path
from .views import (
add_post_view,
home_view,
add_comment_view,
comment,
reply,
add_reply_view
)


urlpatterns = [
    path('add_post/',add_post_view,name='add post'),
    path('home/',home_view,name='home'),
    path('comment/<int:id>',add_comment_view,name="add comment"),
    path('comment/',comment,name='comment'),
    path('reply/',reply,name='reply'),
    path('reply/<int:id>',add_reply_view,name='add reply')
]
