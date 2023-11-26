from account.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView
from .forms import FoodInformationForm, UserFoodForm
from .models import *


# Create your views here.


# 
class UserFoodView(View):
    """
    برای نشون دادن اطلاعات کاربر 
    
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user != request.user.id:
            return redirect('')
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        return render(request, '', {'user':user})


class UserFoodUpdateFormView(View):
    form_class = UserFoodForm

    def dispatch(self, request, *args, **kwargs):
        if request.user != request.user.id:
            return redirect('')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        user = get_object_or_404(User, id=pk)
        form = self.form_class(instance=user)
        return render(request, '', {'form': form})

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)
        form = self.form_class(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('', user.pk)


class FoodInformationCreateView(View):
    form_class = FoodInformationForm
    def get(self, request):
        form = self.form_class()
        return render(request, '', {'form':form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=True)
            new.user = request.user
            new.save()
            return redirect('')

class FoodInformationUpdateView(View):
    form_class = FoodInformationForm

    def dispatch(self, request, *args, **kwargs):
        if request.PropertyInformation.user.id != request.user.id:
            return redirect('')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, slug):
        properties = get_object_or_404(ChefInformation, slug=slug)
        form = self.form_class(instance=properties)
        return render(request, '', {'form':form})
    
    def post(self, request, slug):
        properties = get_object_or_404(ChefInformation, slug=slug)
        form = self.form_class(request.POST, request.FILES, instance=properties)
        if form.is_valid():
            form.save()
            return redirect('', properties.slug)
    

class FoodDetailView(View):
    def get(self, request, slug):
        properties = get_object_or_404(ChefInformation, slug=slug)
        return render(request, '', {'properties':properties})
    
    def post(self, request, slug):
        properties = get_object_or_404(ChefInformation, slug=slug)
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        comment = Comment.objects.create(body=body, property_post=properties, user=request.user, parent_id=parent_id)
        comment.save()
        return redirect('', properties.slug)


class DeleteCommentView(View):
    def get(self, request, pk, slug):
        properties = get_object_or_404(properties, slug=slug)
        comment = get_object_or_404(Comment, id=pk)
        if comment.user.id == request.user.id:
            comment.delete()
            return redirect('', properties.slug)



class FoodDeleteView(View):
    """
     این مدل برای پاک کردن اگهی هستش
    
    """
    def get(self, request, slug):
        food = get_object_or_404(ChefInformation, slug=slug)
        if food.user == request.user.id:
            food.delete()
            return redirect('')
        else:
            return redirect('')

