from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import SubjectForm, TeacherForm

# Create your views here.
from .models import Subject, Teachers


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})
    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("teacher_edit", args=[form.instance.pk]))

    return render(request, "teacher_form.html", {"form": form})


def teacher_edit(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_edit.html", {"form": form})

    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect(reverse("teacher_edit", args=[pk]))

    return render(request, "teacher_edit.html", {"form": form})


def subject_form(request):
    if request.method == "GET":
        form = SubjectForm()
        return render(request, "subject_form.html", {"form": form})
    form = SubjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse("subject_edit", args=[form.instance.pk]))

    return render(request, "subject_form.html", {"form": form})


def subject_edit(request, pk):
    subject = Subject.objects.get(pk=pk)
    if request.method == "GET":
        form = SubjectForm(instance=subject)
        return render(request, "subject_edit.html", {"form": form})

    form = SubjectForm(request.POST, instance=subject)
    if form.is_valid():
        form.save()
        form.instance.teachers.clear()
        form.instance.teachers.set(form.cleaned_data["teachers"])
        return redirect(reverse("subject_edit", args=[pk]))

    return render(request, "subject_edit.html", {"form": form})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, "subject_list.html", {"subjects": subjects})
