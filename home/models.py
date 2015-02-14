from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.models import ImageSpecField
from helpers.image import path_and_rename


class Section(models.Model):
	TYPES = (
		('0', 'Intro'),
		('1', 'Biography'),
	)
	part = models.CharField(max_length=1, choices=TYPES, unique=True)
	header = models.CharField(max_length=300)
	content = models.TextField()
	background = ProcessedImageField(
		upload_to = path_and_rename('pictures/'),
		processors=[ResizeToFill(1900, 1000)],
		format='JPEG',
		options={'quality': 80}
		)
	
	def __unicode__(self):
		return self.TYPES[int(self.part)][1]

	class Meta:
		ordering = ['part']




class Tag(models.Model):
	name = models.CharField(max_length=300)

	def __unicode__(self):
		return self.name



class GaleryImage(models.Model):
	title = models.CharField(max_length=300)
	description = models.TextField()
	large = ProcessedImageField(
		upload_to = path_and_rename('pictures/'),
		format='JPEG',
		options={'quality': 75}
		)

	thumbnail = ImageSpecField(
		source='large',
		processors=[ResizeToFill(250, 250)],
		format='JPEG',
		options={'quality': 65}
		)

	def __unicode__(self):
		return self.title



class GaleryItem(models.Model):
	title = models.CharField(max_length=300)
	image = models.ManyToManyField(GaleryImage)
	tag = models.ManyToManyField(Tag)

	def __unicode__(self):
		return self.title

