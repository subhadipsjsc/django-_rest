from django.urls import path , include
from app2.views import (
    func_blog_view,
    Class_APiView
) 

urlpatterns = [
    path('func_view/', func_blog_view),
    path('class_view/', Class_APiView.as_view() ),
]