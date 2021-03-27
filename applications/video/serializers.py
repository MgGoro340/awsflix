#

from rest_framework import serializers

from . import models

from .models import Video

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video

		fields = '__all__'
		#fields = {
		#	'__all__',
			#'title',
			#'url',
			#'image',
		#}
