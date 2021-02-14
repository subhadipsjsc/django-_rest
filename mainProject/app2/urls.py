from django.urls import path , include
from app2.views import (
    func_blog_view,
) 

urlpatterns = [
    path('func_view/', func_blog_view),
]