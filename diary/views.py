from django.shortcuts import render, redirect
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.http import JsonResponse
import json
from django.shortcuts import get_object_or_404

def diary_detail(request, id):
    entry = get_object_or_404(DiaryEntry, id=id)
    return render(request, 'diary_detail.html', {'entry': entry})

def calendar_view(request):
    return render(request, 'calender.html')

def diary_entries_json(request):
    entries = DiaryEntry.objects.all()
    events = []
    for entry in entries:
        events.append({
            'title': entry.title,
            'start': entry.date.strftime('%Y-%m-%d'),
            'url': f"/entry/{entry.id}/"
        })
    return JsonResponse(events, safe=False)

def diary_list(request):
    entries = DiaryEntry.objects.all().order_by('-date')
    return render(request, 'diary_list.html', {'entries': entries})

def diary_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary_list')  # Redirect to appropriate URL after form submission
    else:
        form = DiaryEntryForm()  # Create a blank form for GET requests

    return render(request, 'diary_form.html', {'form': form})
