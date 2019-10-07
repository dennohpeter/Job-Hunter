from django.test import TestCase
from brighterMonday.models import Job

class ModelTest(TestCase):
    """This class defines the test suite for Job Model."""

    def setUp(self):
        """Defines the test variables"""
        self.title = "Senior Java Developer - IoT - Kenya",
        self.description = "JAVA, JAVASCRIPT, HTML, CSS, SQL, GIT. Am I speaking your language? Then this new role might be the perfect opportunity that you have been waiting for",
        self.company_logo = "https://i.roamcdn.net/kazi/ke/m/66883601aadf5a9e1670c14afda22412/-/aimg.brightermonday.co.ke/dealer-images/advid70034/adv70034_1543413906.jpg",
        self.company_logo_alt = "AltGen LTD",
        self.category = "IT & Software",
        self.location = "Nairobi",
        self.employer = "AltGen LTD",
        self.more_info_link = "https://www.brightermonday.co.ke/job/senior-java-developer-iot-veg5gg",
        self.salary = "KSh: Confidential",
        self.job_type = "Full Time",
        self.first_seen = "5d ago",
        self.job = Job(title=self.title, description=self.description,
                              company_logo=self.company_logo, company_logo_alt=self.company_logo_alt,
                              category=self.category, location=self.location, employer=self.employer,
                              more_info_link=self.more_info_link, salary=self.salary, job_type=self.job_type,
                              first_seen=self.first_seen)

    def test_model_can_create_a_job(self):
        old_count = Job.objects.count()
        self.job.save()
        new_count = Job.objects.count()
        self.assertNotEqual(old_count, new_count)
