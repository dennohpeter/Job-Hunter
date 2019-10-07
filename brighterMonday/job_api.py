from rest_framework import serializers, viewsets
from brighterMonday.models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ('title', 'description', 'company_logo', 'company_logo_alt', 'category', 'location',
                  'employer', 'more_info_link', 'salary', 'job_type', 'first_seen', 'created_at')


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
