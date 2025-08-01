from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import ResumePermissions

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [ResumePermissions]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'candidate':
            return Resume.objects.filter(user=user)
        return Resume.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

