from django.shortcuts import render, redirect
from ..jacobwatches.models import Watch, Feedback
from .forms import WatchForm, FeedbackForm

def crud_form(request):
    if request.method == 'POST':
        form = WatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = WatchForm()
    return render(request, 'crud_form.html', {'form': form})

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})
