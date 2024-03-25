from django.urls import path

from todo_list import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="index"),
    path("task/create/", views.TaskCreateView.as_view(), name="task-create"),
    path(
        "task/<int:pk>/update/",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "task/<int:pk>/switch_status/",
        views.task_status_switcher,
        name="task-switcher"
    ),

    path("tags/", views.TagListView.as_view(), name="tags"),
    path("tags/create/", views.CreateTagView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/",
         views.TagUpdateView.as_view(),
         name="tag-update"
         ),
    path("tags/<int:pk>/delete/",
         views.TagDeleteView.as_view(),
         name="tag-delete"
         ),

]

app_name = "todo"
