from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import os

from .core.ImageToSketch import Image2Sketch

PATHOUT = "./ImgSketch/static/SketchYourLife/sketched/"
KERNEL_SIZE = 121
SIGMA = 30

def home(request):
    try:    #TODOdelete from file system storage
        if os.path.exists("./media/"):#"../WebApp/media/"
            for f in os.listdir("./media/"):
                os.remove(os.path.join("./media/", f))
        else:
            pass #TODOraise error and refresh page
    finally:
        if request.method == 'POST':
            try:
                ufile = request.FILES['ufile']
            except:
                return render(request, 'SketchYourLife/upload.html')
            fs = FileSystemStorage()
            fs.save(ufile.name, ufile)

            im2sk = Image2Sketch(pathIn=ufile,pathOut=PATHOUT,nameOut=ufile.name)
<<<<<<< HEAD
            im2sk.set_kernelsize_sigma(k=111,s=30)
            im2sk.sketch_it()
=======
            im2sk.set_kernelsize_sigma(k=KERNEL_SIZE,s=SIGMA)
            success = im2sk.sketch_it()
            if success:
                print("COnverted successfully!!")
            else:
                print("something went wrong")
>>>>>>> cde038c2e3957628a61262e84cd5cce58edf4948

            for a in os.listdir(PATHOUT):
                sketched = os.path.join("static/SketchYourLife/sketched/",a)
            
            return render(request, 'SketchYourLife/sketch.html', {
                'sketched': sketched
            })
        if os.path.exists("./ImgSketch/static/SketchYourLife/sketched/"):#"../WebApp/media/"
                for f in os.listdir("./ImgSketch/static/SketchYourLife/sketched/"):
                    os.remove(os.path.join("./ImgSketch/static/SketchYourLife/sketched/", f))
        else:
            pass

        return render(request, 'SketchYourLife/upload.html')