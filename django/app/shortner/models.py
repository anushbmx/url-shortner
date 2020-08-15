from django.db import models
from django.utils import crypto


class Shortner(models.Model):
	# Django has models.URLField but it limits character length to 255 max
	short_url = models.CharField(max_length=255, db_index=True, unique=True, help_text='Shorterned URL')
	original_url = models.TextField(help_text='Original URL')

	created = models.DateTimeField(auto_now_add=True)
	time = models.DateTimeField(auto_now=True)
	status = models.BooleanField(default=True, null=False)

	@staticmethod
	def create_short_url(short_url, original_url):
		try:
			return Shortner.objects.create(short_url=short_url, original_url=original_url)
		except:
			# if url exist, recursive call after attaching random string to the end
			return Shortner.create_short_url(
				short_url='%s-%s'%(short_url, crypto.get_random_string(3)), 
				original_url=original_url
			)