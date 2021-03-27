from rest_framework.generics import ListAPIView



from django.shortcuts import render

# Create your views here.
#
#
from .models import Video

#
from .serializers import VideoSerializer


class VideoListApiView(ListAPIView):

	serializer_class = VideoSerializer
	
	def get_queryset(self):
		
		return Video.objects.all()

