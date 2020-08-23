from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from subprocess import run,PIPE,Popen
import sys,os
from pathlib import Path
from .models import SketchForLife


def home(request):
    try:
        if os.path.exists("../mysite/media/"):
            for f in os.listdir("../mysite/media/"):
                os.remove(os.path.join("../mysite/media/", f))
                print ("done")
        else:
            print("oyee")
    finally:
        if request.method == 'POST' and request.FILES['ufile']:
            ufile = request.FILES['ufile']
            fs = FileSystemStorage()
            filename = fs.save(ufile.name, ufile)
            uploaded_file_url = fs.url(filename)
            

            output = SketchForLife(uploaded_file_url)
            uploaded_file_url = ""
            output = output.retval

            


            return render(request, 'ImgSketch/main.html', {
                'uploaded_file_url': uploaded_file_url,'outputf':output
            })

        return render(request, 'ImgSketch/main.html')
