# portfolio/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import CVSection
from .forms import CVSectionForm

def about_me(request):
    return render(request, 'portfolio/about.html')

def view_cv(request):
    sections = CVSection.objects.all().order_by('order')
    return render(request, 'portfolio/view_cv.html', {'sections': sections})

def edit_cv(request):
    sections = CVSection.objects.all().order_by('order')
    return render(request, 'portfolio/edit_cv.html', {'sections': sections})

def add_cv_section(request):
    if request.method == 'POST':
        form = CVSectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edit_cv')
    else:
        form = CVSectionForm()
    return render(request, 'portfolio/add_edit_cv_section.html', {'form': form, 'action': 'Adaugă'})

def edit_cv_section(request, pk):
    section = get_object_or_404(CVSection, pk=pk)
    if request.method == 'POST':
        form = CVSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('edit_cv')
    else:
        form = CVSectionForm(instance=section)
    return render(request, 'portfolio/add_edit_cv_section.html', {'form': form, 'action': 'Editează'})

def delete_cv_section(request, pk):
    section = get_object_or_404(CVSection, pk=pk)
    if request.method == 'POST':
        section.delete()
        return redirect('edit_cv')
    return render(request, 'portfolio/confirm_delete.html', {'section': section})