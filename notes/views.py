from django.utils import timezone
from .models import Note
from django.shortcuts import render, get_object_or_404
from .forms import NoteForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from random import choice
colors = ["red_note", "green_note", "blue_note", "purple_note", "yellow_note"]

def note_list(request):
    notes = Note.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_by_author(request, user):
    notes = Note.objects.filter(published_date__lte=timezone.now(), author__username=user).order_by('published_date')
    return render(request, 'notes/note_list.html', {'notes': notes, 'author_name': user})


def note_secret(request):
    return render(request, 'notes/note_secret.html', {})

@login_required(login_url='/login')
def note_new(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.color = choice(colors)
            note.author = request.user
            note.published_date = timezone.now()
            note.save()
            return redirect('note_details', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_edit.html', {'form': form})

def note_details(request, pk):
   note = get_object_or_404(Note, pk=pk)
   return render(request, 'notes/note_details.html', {'note': note})

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name_suffix = '_update_form'

    success_url = reverse_lazy('note_list')


class NoteDelete(DeleteView):
    model = Note
    template_name_suffix = '_delete'
    success_url = reverse_lazy('note_list')