from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import EventFilter
from .models import Event, EventRegistration
from .serializers import EventSerializer, UserEventRegistrationSerializer, UserRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    filterset_class = EventFilter
    search_fields = ['title', 'location', 'organizer__username']
    ordering_fields = ['date', 'title']


class EventRegistrationView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, event_id):
        event = Event.objects.get(id=event_id)
        registration, created = EventRegistration.objects.get_or_create(user=request.user, event=event)
        if created:
            return Response({'message': 'Registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Already registered'}, status=status.HTTP_400_BAD_REQUEST)


class UserEventRegistrationView(generics.ListAPIView):
    serializer_class = UserEventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return EventRegistration.objects.filter(event_id=event_id)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
