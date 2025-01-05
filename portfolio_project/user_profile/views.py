from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile, Portfolio, ProjectShowcase
from .forms import UserProfileForm, PortfolioForm, ProjectShowcaseForm

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'user_profile/user_list.html', {'users': users})

def user_create(request):
    form = UserProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'user_profile/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    form = UserProfileForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'user_profile/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    user.delete()
    return redirect('user_list')

def user_detail(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'user_profile/user_detail.html', {'user': user})

# Portfolio Views
def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'user_profile/portfolio_list.html', {'portfolios': portfolios})

def portfolio_create(request):
    form = PortfolioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio_list')
    else:
        form = PortfolioForm()
    return render(request, 'user_profile/portfolio_form.html', {'form': form})

def portfolio_update(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    form = PortfolioForm(request.POST or None, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('portfolio_list')
    return render(request, 'user_profile/portfolio_form.html', {'form': form})

def portfolio_delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    portfolio.delete()
    return redirect('portfolio_list')

def project_list(request):
    projects = ProjectShowcase.objects.all()
    return render(request, 'user_profile/project_list.html', {'projects': projects})
def project_create(request):
    form = ProjectShowcaseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('project_list')
    return render(request, 'user_profile/project_form.html', {'form': form})

def project_update(request, pk):
    project = get_object_or_404(ProjectShowcase, pk=pk)
    form = ProjectShowcaseForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('portfolio_list')
    return render(request, 'user_profile/project_form.html', {'form': form})

def project_delete(request, pk):
    project = get_object_or_404(ProjectShowcase, pk=pk)
    project.delete()
    return redirect('portfolio_list')

# Create your views here.
