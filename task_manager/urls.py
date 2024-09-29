from django.urls import path
from .views import (
    index,
    PositionListView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", index, name="tasks-list"),
    path("task-types/", index, name="task-types-list"),
    path("positions/", PositionListView.as_view(), name="positions-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
]

app_name = "task_manager"
