from django.shortcuts import render,redirect,HttpResponseRedirect
import segno
from hashlib import shake_256
from time import localtime
from pathlib import Path
import random
import numpy as np
from django.urls import reverse
from .forms import  QR_Form
from .models import QR


BASE_DIR = Path(__file__).resolve().parent.parent

def add_prefix():
    print(random.random())
    prefix = shake_256(f"{np.random.rand(50)}{localtime}".encode('utf-8')).hexdigest(20)
    return prefix  #f"{BASE_DIR}/static/images_ortho/{prefix}",prefix



def index(request):
    
    return render(request,"main.html",{})

def barcode_view(request):
    
    return render(request,"barcode_view.html",{})


def create_barcode(request):
    
    return render(request,"create_barcode.html",{})


def qr_lists(request):
    
    query = QR.objects.all()
    
    
    return render(request,"qr_view.html",{"query":query})



def show_qr(request,slug):
    
    return render(request,"show_qr.html",{'slug':slug})



def create_qr(request):
    if request.method == 'POST':
        form = QR_Form(request.POST or None, request.FILES or None)
        print(form.is_valid(), form.errors)
        if form.is_valid():
            print(request.POST)
                        
            sampled_by   = form.cleaned_data['sampled_by']
            unit         = form.cleaned_data['unit']
            sample_point = form.cleaned_data['sample_point']
            sample_type  = form.cleaned_data['sample_type']
            data_time    = form.cleaned_data['data_time']
            color        = request.POST.get('color')
            
            hash = add_prefix()
            qrcode = segno.make([{'sampled_by':sampled_by, 'unit':unit, 'sample_point':sample_point, 'sample_type':sample_type,'data_time':data_time}])
            qrcode.save(f"{BASE_DIR}/static/qr_images/{hash}.svg", scale=40,dark=color, light='#ffffff',)
            
            form.instance.hashing_name = hash
            
            form.save()
            return redirect(f'/show_qr/{hash}',hash,permanent=True)
    else:
        return render(request,"create_qr.html",{})



