from django.conf import settings
from django.shortcuts import redirect, render

from uploads.models import Upload

from .utils import get_all_custom_models
from django.core.management import call_command
from django.contrib import messages
# Create your views here.
def import_data(request):
    if request.method=="POST":
        file_path = request.FILES.get('file-path')
        model_name = request.POST.get('model_name')
        #store the file in the Upload model
        upload=Upload.objects.create(file=file_path,model_name=model_name)
        #construct the full path
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        file_path = base_url+relative_path
        print(file_path)
        
        #trigger the import data command
        try:
            call_command('importdata',file_path,model_name)
            messages.success(request, 'Data impoted successfully')
        except Exception as e:
            messages.error(request,str(e))
        return redirect('import_data')

    else:
        all_models= get_all_custom_models()
        context = {
            'all_models': all_models,
        }
        
    
    return render(request,'dataentry/importdata.html',context)