from django.shortcuts import render
from .models import Task, TaskImage
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .forms import TaskForm, TaskImageForm, TaskSearchForm
from django.urls import reverse_lazy


# Create your views here.



# def add_task(request):
#     if request.method == 'POST':
#         product_form = TaskForm(request.POST)
#         image_form = TaskImageForm(request.POST, request.FILES)
#         if product_form.is_valid() and image_form.is_valid():
#             product = product_form.save(user=request.user)
#             for img in request.FILES.getlist('images'):
#                 TaskImage.objects.create(tasks=product, images=img)
#             return redirect('tasklist')
#     else:
#         product_form = TaskForm()
#         image_form = TaskImageForm()
#     return render(request, 'add.html', {'product_form': product_form, 'image_form': image_form})


class AddTaskView(View):
    template_name = 'add.html'

    def get(self, request):
        product_form = TaskForm()
        image_form = TaskImageForm()
        return render(request, self.template_name, {'product_form': product_form, 'image_form': image_form})

    def post(self, request):
        product_form = TaskForm(request.POST)
        image_form = TaskImageForm(request.POST, request.FILES)
        if product_form.is_valid() and image_form.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            for img in request.FILES.getlist('images'):
                TaskImage.objects.create(tasks=product, images=img)
            return redirect('tasklist')
        return render(request, self.template_name, {'product_form': product_form, 'image_form': image_form})



class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user).order_by('-priority')
        form = TaskSearchForm(self.request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            creation_date = form.cleaned_data.get('creation_date')
            due_date = form.cleaned_data.get('due_date')
            priority = form.cleaned_data.get('priority')
            is_complete = form.cleaned_data.get('is_complete')
            
            if search_query:
                queryset = queryset.filter(title__icontains=search_query)
            if creation_date:
                queryset = queryset.filter(created_at__date=creation_date)
            if due_date:
                queryset = queryset.filter(due_date=due_date)
            if priority:
                queryset = queryset.filter(priority=priority)
            if is_complete is not None:
                queryset = queryset.filter(is_complete=is_complete)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = TaskSearchForm(self.request.GET)
        return context
    
class TaskDetailsView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = self.get_object()  # Get the Task object

        # Add task images to the context
        context['task_images'] = task.images.all()

        return context
    

class CompleteTaskView(View):
    template_name = 'complete.html'

    def get(self, request, task_id):
        task = get_object_or_404(Task, pk=task_id)
        # Mark the task as complete
        task.is_complete = True
        task.save()
        return render(request, self.template_name, {'task': task})
    


class EditTaskView(LoginRequiredMixin, View):
    template_name = 'edit.html'

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        form = TaskForm(instance=task)
        image_form = TaskImageForm()  # Instantiate the image form here
        return render(request, self.template_name, {'form': form, 'task': task, 'image_form': image_form})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id, user=request.user)
        form = TaskForm(request.POST, instance=task)
        image_form = TaskImageForm(request.POST, request.FILES)  # Pass request.FILES to the image form

        # Handle text fields
        if form.is_valid():
            form.save(commit=False)
            task.title = form.cleaned_data['title']
            task.description = form.cleaned_data['description']
            task.due_date = form.cleaned_data['due_date']
            task.priority = form.cleaned_data['priority']
            task.is_complete = form.cleaned_data['is_complete']
            task.user = request.user
            task.save()

        # Handle images
        if image_form.is_valid():
            for img in request.FILES.getlist('images'):
                task_image = TaskImage.objects.create(images=img, tasks=task)  # Set the task field when creating TaskImage
                task.images.add(task_image)

        messages.success(request, 'Task updated successfully.')
        return redirect('tasklist')





# def delete_image(request, task_id, image_id):
#     task = get_object_or_404(Task, id=task_id)
#     image = get_object_or_404(TaskImage, id=image_id)

#     # Check if the image belongs to the task
#     if image in task.images.all():
#         image.delete()

#     return redirect('edit-task', task_id=task.id)

class DeleteImageView(View):
    def get(self, request, task_id, image_id):
        task = get_object_or_404(Task, id=task_id)
        image = get_object_or_404(TaskImage, id=image_id)

        # Check if the image belongs to the task
        if image in task.images.all():
            image.delete()

        return redirect('edit-task', task_id=task.id)



class DeleteTaskView(View):
    template_name = 'delete.html'

    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, self.template_name, {'task': task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        messages.success(request, 'Task deleted successfully.')
        return redirect('tasklist')
