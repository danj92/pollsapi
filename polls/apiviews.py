from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Poll, Choice
from  .serializers import PollSerializer

class PollListViewset(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    # def get(self, request):
    #     polls = Poll.objects.all()[:20]
    #     data = PollSerializer(polls, many=True).data
    #     return Response(data)


#class PollDetailViewset(viewsets.ModelViewSet):
#    pass
    # def get(self, request, pk):
    #     poll = get_object_or_404(Poll, pk=pk)
    #     data = PollSerializer(poll).data
    #     return Response(data)