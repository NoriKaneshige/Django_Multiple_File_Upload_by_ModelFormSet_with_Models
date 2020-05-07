from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import SingleUploadModelForm, UploadModelFormSet
from .models import UploadFile



# from .forms import SingleUploadForm, SingleUploadModelForm, UploadFormSet, UploadModelFormSet

class SingleUploadWithModelView(generic.CreateView):
    """ view to upload file model """
    model = UploadFile
    form_class = SingleUploadModelForm
    template_name = 'app/upload.html'
    success_url = reverse_lazy('app:file_list')


def multi_upload_with_model(request):
    formset = UploadModelFormSet(request.POST or None, files=request.FILES or None, queryset=UploadFile.objects.none())
    # if queryset=UploadFile.objects.none() is not set, already uploaded files are also displayed in the form

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:file_list')

    context = {
        'form': formset
    }

    return render(request, 'app/upload.html', context)


class FileListView(generic.ListView):
    """ view for page listing all uploaded files """
    model = UploadFile