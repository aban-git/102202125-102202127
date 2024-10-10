from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from django.contrib.auth.models import User

class ChatMessageListCreateView(generics.ListCreateAPIView):
    serializer_class = ChatMessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        receiver_username = self.request.query_params.get('receiver')
        if receiver_username:
            try:
                receiver = User.objects.get(username=receiver_username)
            except User.DoesNotExist:
                return ChatMessage.objects.none()
            return ChatMessage.objects.filter(
                (models.Q(sender=user) & models.Q(receiver=receiver)) |
                (models.Q(sender=receiver) & models.Q(receiver=user))
            ).order_by('timestamp')
        return ChatMessage.objects.none()

    def perform_create(self, serializer):
        receiver_username = self.request.data.get('receiver')
        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            raise serializers.ValidationError({"receiver": "接收者不存在"})
        serializer.save(sender=self.request.user, receiver=receiver)
