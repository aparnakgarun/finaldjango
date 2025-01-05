from django import forms
from .models import UserProfile, Portfolio, ProjectShowcase

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = '__all__'


class ProjectShowcaseForm(forms.ModelForm):
    class Meta:
        model = ProjectShowcase
        fields = ['portfolio', 'project_name', 'description', 'image', 'link']

    portfolio = forms.ModelChoiceField(queryset=Portfolio.objects.all(), empty_label="Select a Portfolio")