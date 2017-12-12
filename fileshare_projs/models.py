from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

# Create your models here.
class Upload(models.Model):
	"""A file the user would like to upload"""
	file_name = models.CharField(blank=True, max_length = 250)
	file_author = models.CharField(blank=True, max_length = 250)
	file_file = models.FileField(blank=True, null=True, upload_to='')
	
	
	
	
	def __str__(self):
		"""Return a string representation of the file"""
		return self.file_name
		return self.file_author
		


	
	
	

class Download(models.Model):
	"""A file the user would like to download."""
	
	
	
