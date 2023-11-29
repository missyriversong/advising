from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Program, Course, ProgramCourses
from .forms import CourseForm, ProgramForm, SearchProgramForm, UploadForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib import messages
import io, csv, os
from pathlib import Path
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
    return render(request, "checklist/base.html")


def program_search(request):
    search_input = request.GET.get("search", "")
    search_history = request.session.get("search_history", [])
    form = SearchProgramForm(request.GET)
    programs = set()
    programcourses_list = ProgramCourses.objects.select_related(
        "programs", "courses"
    ).all()

    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_by = form.cleaned_data.get("search_by")
        if search_by == "level_abbrev":
            programs = Program.objects.filter(level_abbrev__icontains=search)
        elif search_by == "major":
            programs = Program.objects.filter(major__icontains=search)
        elif search_by == "specialization":
            programs = Program.objects.filter(specialization__icontains=search)
        search_history.append([search_by, search])
        request.session["search_history"] = search_history

    elif search_history:
        initial = dict(search=search_input, search_by=search_history[-1][0])
        form = SearchProgramForm(initial=initial)

    return render(
        request,
        "checklist/program_search.html",
        {
            "form": form,
            "search_input": search_input,
            "programs": programs,
            "programcourses_list": programcourses_list,
            "search_history": search_history,
        },
    )


def program_list(request):
    programs = Program.objects.all()
    context = {"programs": programs}
    return render(request, "checklist/program_list.html", context)


def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    programcourses_list = ProgramCourses.objects.select_related(
        "programs", "courses"
    ).all()

    context = {"program": program, "programcourses_list": programcourses_list}
    return render(request, "checklist/program_detail.html", context)


# """
# def course_list(request):
#   courses = Course.objects.all()
#   context = {'courses': courses}
#   return render(request, 'checklist/course_list.html', context)
# """


class CourseListView(ListView):
    model = Course
    template = "checklist/course_list.html"


def checklist_list(request):
    programcourses = ProgramCourses.objects.select_related("programs", "courses").all()
    order_by = request.GET.get("order_by", "programs__level_abbrev")
    programcourses_list = programcourses.order_by(order_by)

    context = {"programcourses_list": programcourses_list}
    return render(request, "checklist/checklist_list.html", context)


def program_edit(request, pk=None):
    if pk is not None:
        program = get_object_or_404(Program, pk=pk)
    else:
        program = None
    if request.method == "POST":
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            updated_program = form.save()
            if program is None:
                messages.success(
                    request, 'Program "{}" was created.'.format(updated_program)
                )
            else:
                messages.success(
                    request, 'Program "{}" was updated.'.format(updated_program)
                )
            return redirect("program_edit", updated_program.pk)
    else:
        form = ProgramForm(instance=program)

    return render(
        request,
        "checklist/instance_update.html",
        {
            "method": request.method,
            "form": form,
            "model_type": "Program",
            "instance": program,
        },
    )


def upload_checklist(request):
    # form = UploadForm()
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = os.path.join(settings.MEDIA_ROOT, request.FILES['file'])
            # #https://ordinarycoders.com/blog/article/django-file-image-uploads
            # file = request.FILES['file']
            # fss = FileSystemStorage()
            # file_saved = fss.save(file.name, file)
            # file_url = fss.url(file_saved)

            # file = os.path.join(settings.MEDIA_ROOT, file)
            return redirect("/course/")
            # file = form.cleaned_data[
            #     "file"
            # ]  # validaetes form inputs, returns object
            # save_path = settings.MEDIA_ROOT
            # # with open(save_path, "wb") as output_file:
            # #   for chunk in csv_file.chunks():
            # #     output_file.write(chunk)
    else:
        form = UploadForm()
        return render(request, "checklist/upload_checklist.html", {"form": form})

    # with open(save_path, "r") as output_file:
    #     reader = csv.reader(output_file, newline="")  # return reader object, opens
    #     next(reader)  # skips header?

    for row in reader:
        course, created_course = Course.objects.get_or_create(
            subj_abbrev=row[0],  # subj_abbrev=row['Subj_abbrev']
            no=row[1],
            name=row[2],
            hours=row[3],
            programs=row[4],
        )


# https://docs.python.org/3/library/csv.html
# https://docs.djangoproject.com/en/4.2/topics/files/


# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
# def parse_csv_file(csv_file):
#     with open('file_saved')

# ? def import?


def get_courses_per_semester(request):
    course = Course.objects.all().values("course__id").distinct.count()
    programcourses = ProgramCourses.objects.select_related("programs", "courses").all()


# Use ctrl / to comment
#  """ is for more detailed information about a thing """
# remember to use black for python ~ prettier ? but for indenting
# shift tab  - > does something can't remember
# from now on, follow through on one resource at a time, comment out where ya found it for later fyis
# also comment out what didn't work so you don't keep trying doing a hundred renditions of it -> delete later
