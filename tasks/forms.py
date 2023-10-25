from django import forms
from .models import Task, TaskImage



class TaskImageForm(forms.ModelForm):
    class Meta:
        model = TaskImage
        fields = ['images']
        
        


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete']
        widgets = {
            'due_date': forms.TextInput(attrs={'type': 'date', 'class':'bg-gray-50 my-5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5  dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),

            'title': forms.TextInput(attrs={'class':"bg-gray-50 my-5 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500"}),

            'description': forms.Textarea(attrs={'class': 'block p-2.5 w-full my-5 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500', 'rows': '4'}),

            'priority': forms.Select(attrs={'class': 'bg-gray-50 border my-5 border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-white dark:border-gray-600 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),

            'is_complete': forms.CheckboxInput(attrs={'class': 'w-4 h-4 my-5 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-white dark:border-gray-600'}),
            
        }
    def save(self, commit=True, user=None):
        instance = super(TaskForm, self).save(commit=False)
        instance.user = user  # Set the user field here
        if commit:
            instance.save()
        return instance
    