from rest_framework import serializers, viewsets
from brighterMonday.models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ('title', 'job_function', 'description', 'company_logo', 'company_logo_alt', 'category', 'location',
                  'employer', 'salary', 'job_type', 'first_seen', 'created_at', 'summary_title', 'summary', 'description_title', 'requirements')


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
