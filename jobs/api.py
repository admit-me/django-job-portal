from rest_framework import generics, permissions
from .models import Application, Job
from .serializers import ApplicationSerializer, JobSerializer


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.filter(is_active=True).order_by('-created_at')
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]


class JobDetailAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.AllowAny]


class ApplicationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(candidate=self.request.user).select_related('job')

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)
