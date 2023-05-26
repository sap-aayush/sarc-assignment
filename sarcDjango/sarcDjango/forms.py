from django import forms
from ..jacobwatches.models import Watch, Feedback

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
