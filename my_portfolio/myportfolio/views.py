from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .serializers import ContactSerializer
from .models import Contact

class ContactView(CreateAPIView):
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        # Save the contact message to the database
        contact = serializer.save()

        # Send email notification
        send_mail(
            f'Contact Form Submission from {contact.name}',
            contact.message,
            contact.email,
            ['mangalbodele123@gmail.com'],  # Your email
                                 fail_silently=False,
        )

        # Return a success response
        return Response({'message': 'Message sent successfully'}, status=status.HTTP_201_CREATED)
