from django.shortcuts import render
from .models import Section, GaleryItem
from django.http import HttpResponse
import json

def home(request):
	sections = Section.objects.all()
	if len(sections)<2:
		intro = biography = contact = {}
	else:
		intro = sections[0]
		biography = sections[1]
		contact = sections[2]

	return render(request, 'home/index.jade', {
		'intro': intro,
		'biography': biography,
		'contact': contact
		})

def galeryJson(request):
	result = []

	for el in GaleryItem.objects.all():
		item = {}
		item['titles'] = []
		item['descriptions'] = []
		item['tags'] = []
		item['thumbnail'] = []
		item['large'] = []

		for tag in el.tag.all():
			item['tags'].append(tag.name)

		for image in el.image.all():
			item['thumbnail'].append(image.thumbnail.url)
			item['large'].append(image.large.url)
			item['titles'].append(image.title)
			item['descriptions'].append(image.description)
			

			
		result.append(item)
	return HttpResponse(json.dumps(result), content_type="application/json")

