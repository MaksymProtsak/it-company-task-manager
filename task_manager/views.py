from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

from .forms import (
    PositionSearchForm,
    TaskTypeSearchForm,
    TaskForm,
    TaskSearchForm,
    WorkerCreateForm,
    WorkerForm,
    WorkerSearchForm,
    SignUpForm
)
from .models import Worker, Task, TaskType, Position


@login_required
def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_task_types = TaskType.objects.count()
    num_positions = Position.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_task_types": num_task_types,
        "num_positions": num_positions,
        "num_visits": num_visits + 1,
    }

    return render(request, "home/index.html", context=context)


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Account created successfully.'
            success = True
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "registration/register.html", {"form": form, "msg": msg, "success": success})


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"
    template_name = "task_manager/position_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PositionListView, self).get_context_data(**kwargs)
        position = self.request.GET.get("position", "")
        context["search_form"] = PositionSearchForm(
            initial={"position": position}
        )
        return context

    def get_queryset(self):
        queryset = Position.objects.all()
        form = PositionSearchForm(self.request.GET)
        if form.is_valid() and form.data.get(key="position") is not None:
            return queryset.filter(
                name__icontains=self.request.GET.get("position")
            )
        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:positions-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:positions-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:positions-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task_manager/task_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskTypeListView, self).get_context_data(**kwargs)
        task_type = self.request.GET.get("task_type", "")
        context["search_form"] = TaskTypeSearchForm(
            initial={"task_type": task_type}
        )
        return context

    def get_queryset(self):
        queryset = TaskType.objects.all()
        form = TaskTypeSearchForm(self.request.GET)
        if form.is_valid() and form.data.get(key="task_type") is not None:
            return queryset.filter(
                name__icontains=self.request.GET.get("task_type")
            )
        return queryset


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-types-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-types-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("task_manager:task-types-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "task_manager/task_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        task = self.request.GET.get("task", "")
        context["search_form"] = TaskSearchForm(
            initial={"task": task}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all().select_related("task_type").prefetch_related("assignees")
        form = TaskSearchForm(self.request.GET)
        if form.is_valid() and form.data.get("task") is not None:
            return queryset.filter(
                name__icontains=self.request.GET.get("task")
            )
        return queryset


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:tasks-list")


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    queryset = Task.objects.all(
    ).select_related("task_type").prefetch_related("assignees__position")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse_lazy(
            "task_manager:task-detail",
            kwargs={"pk": self.object.id}
        )


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:tasks-list")


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"
    template_name = "task_manager/worker_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        worker = self.request.GET.get("worker", "")
        context["search_form"] = WorkerSearchForm(
            initial={"worker": worker}
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.all().select_related("position")
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid() and form.data.get(key="worker") is not None:
            return queryset.filter(
                username__icontains=self.request.GET.get("worker")
            )
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.all(
    ).select_related("position").prefetch_related("tasks__task_type")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    success_url = reverse_lazy("task_manager:workers-list")
    form_class = WorkerCreateForm


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerForm
    success_url = reverse_lazy("task_manager:workers-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager:workers-list")


class ToggleAssignToWorkerView(LoginRequiredMixin, generic.View):
    @staticmethod
    def get(request, pk):
        worker = Worker.objects.get(id=request.user.id)
        task = Task.objects.get(id=pk)
        if (
            task in worker.tasks.all()
        ):
            worker.tasks.remove(task)
        else:
            worker.tasks.add(task)
        return HttpResponseRedirect(
            reverse_lazy(
                "task_manager:task-detail", args=[pk]
            )
        )
