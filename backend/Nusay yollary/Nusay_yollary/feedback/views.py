from django.shortcuts import render
from django.contrib import messages
# Create your views here.
# views.py

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Geri bildiriminiz başarıyla kaydedildi.')
            # return ('success')  # Başarıyla gönderildiği sayfaya yönlendir
    else:
        # form = FeedbackForm()
        messages.error(request, 'Geri bildirim kaydedilemedi. Lütfen tekrar deneyin.')
    # return render(request, {'form': form})
