from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from checklist.views import CourseListView


urlpatterns = [
    path("search", views.program_search, name="program-search"),
    path("program/", views.program_list, name="program-list"),
    path("program/<int:pk>", views.program_detail, name="program-detail"),
    # path('course/', views.course_list, name='course-list'),
    path("course/", CourseListView.as_view(), name="course-list"),
    path("checklist/", views.checklist_list, name="checklist-list"),
    path("programs/<int:pk>", views.program_edit, name="program-edit"),
    path("programs/new", views.program_edit, name="program-new"),
    path("upload/", views.upload_checklist, name="upload-checklist"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)