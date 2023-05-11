from django.urls import path

from . import views

urlpatterns = [
    path(
        "post/",
        views.PostView.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "post/<int:pk>/",
        views.PostView.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
