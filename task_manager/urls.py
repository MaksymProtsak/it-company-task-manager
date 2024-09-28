from django.urls import path
from .views import (
    index,
    PositionListView,
    PositionCreateView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", index, name="tasks-list"),
    path("task-types/", index, name="task-types-list"),
    path("positions/", PositionListView.as_view(), name="positions-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),  # Need to change view
    path("positions/<int:pk>/update/", PositionListView.as_view(), name="position-update"),  # Need to change view
    path("positions/<int:pk>/delete/", PositionListView.as_view(), name="position-delete"),  # Need to change view
]

app_name = "task_manager"
