from django.shortcuts import render, reverse
from .models import Upload 
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm
from django.http import HttpResponseRedirect
from fileshare_proj.settings import MEDIA_ROOT, MEDIA_URL, BASE_DIR
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadSerializer
from .models import Upload
from flask import send_file
from filetransfers.api import serve_file





import os
from os import listdir
from os.path import isfile, join 


import pdb





# Create your views here.
def index(request):
	"""The home page for File Share"""
	return render(request, 'fileshare_projs/index.html')
	
def upload(request):
	"""The upload page to upload files"""
	if request.method == 'POST':
		upload_form = UploadForm(request.POST, request.FILES)
		if upload_form.is_valid():
			upload = upload_form.save(commit=False)
			upload.save()
			return HttpResponseRedirect(reverse('fileshare_projs:index'))
	else:
		upload_form = UploadForm()	
	return render(request, 'fileshare_projs/upload.html', {'upload_form': upload_form
	})
	
def download(request):
	"""The download page to download files"""	
	#upload = get_object_or_404(Upload, pk=pk)
	#return serve_file(request, upload_file)
	return render(request, 'fileshare_projs/download.html')
	
def manage_files(request):
	"""The Manage Files page to manage your files."""
	f = Upload
	os.chdir('/Users/19dulada/fileshare_proj/media/')
	#f.file_file = Upload.file_file
	file_list = os.listdir()
	pdb.set_trace()
	#upload = get_object_or_404(Upload, pk=f.file_file)
	#return serve_file(request, upload_file)
	context = {'file_list' : file_list}
	
	return render(request, 'fileshare_projs/manage_files.html', context)
	
def troubleshooting(request):
	"""The Troubleshooting page is for getting help with coding bugs."""
	return render(request, 'fileshare_projs/troubleshooting.html')
	
def egg(request):
	"""???"""
	return render(request, 'fileshare_projs/egg.html')
