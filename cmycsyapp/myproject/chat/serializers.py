from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username', read_only=True)
    receiver = serializers.CharField(source='receiver.username')

    class Meta:
        model = ChatMessage
        fields = ('id', 'sender', 'receiver', 'message', 'timestamp')
        read_only_fields = ('id', 'sender', 'timestamp')
