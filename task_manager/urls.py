from django.urls import path
from .views import (
    index,
)
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("", index, name="index"),
] + debug_toolbar_urls()

app_name = "task_manager"
