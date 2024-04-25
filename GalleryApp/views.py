from django.views import generic
from django.shortcuts import render, redirect
from .forms import DjangoForm
from .models import Django

from django.shortcuts import get_object_or_404

class DjangoDetail(generic.DetailView):
    model = Django
    template_name = 'django_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # You can access the object using 'self.object'
        context['django'] = self.object
        return context

class AllPostsView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        django_posts = Django.objects.all()  # Retrieve all Django posts
        context['django_posts'] = django_posts
        return context




class DjangoList(generic.ListView):
    model = Django
    queryset = Django.objects.all().order_by('-created_on')  # Remove the filter on the status field
    template_name = 'django.html'

   



def create_post(request):
    if request.method == 'POST':
        form = DjangoForm(request.POST)
        if form.is_valid():
            Django.objects.create(
                title=form.cleaned_data['title'],
                image=form.cleaned_data['image'],
                author=form.cleaned_data['author'],
                about=form.cleaned_data['about'],  # Use 'about' instead of 'Price'
            )
            return redirect('home')
    else:
        form = DjangoForm()
    return render(request, 'create_post.html', {'form': form})