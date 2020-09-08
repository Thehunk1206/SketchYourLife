from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os

from .core.ImageToSketch import Image2Sketch

PATHOUT = "./media/"
KERNEL_SIZE = 121
SIGMA = 30

def home(request):
    fs = FileSystemStorage()
    try:
        for f in os.listdir("./media/"):
            fs.delete(f)
        else:
            pass #TODOraise error and refresh page
    finally:
        if request.method == 'POST':
            try:
                ufile = request.FILES['ufile']
            except:
                return render(request, 'SketchYourLife/upload.html')
            fs.save(ufile.name, ufile)

            im2sk = Image2Sketch(pathIn=ufile,pathOut=PATHOUT,nameOut=ufile.name)
            im2sk.set_kernelsize_sigma(k=KERNEL_SIZE,s=SIGMA)
            im2sk.sketch_it()

            for file in os.listdir("./media/"):
                if (file == "sketched_"+ufile.name):
                    sketched = fs.url(file)
            
            return render(request, 'SketchYourLife/sketch.html', {
                'sketched': sketched
            })


        return render(request, 'SketchYourLife/upload.html')