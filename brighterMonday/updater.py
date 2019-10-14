from brighterMonday.models import Job


class Update_Jobs:

    def __init__(self, jobs):
        self.jobs = jobs.get("jobs")

    def update_models(self):
        print('------------------updating jobs-----------')
        for job in self.jobs:
            Job.objects.update_or_create(
                description=job['job_result_content'],
                defaults={
                    'title': job['job_result_title'],
                    'job_function': job['job_function'],
                    'description': job["job_result_content"],
                    'company_logo': job['job_result_card_icon'],
                    'company_logo_alt': job['job_result_card_icon_alt'],
                    'category': job['job_result_function'],
                    'location': job['job_result_location'],
                    'employer': job['job_result_meta'],
                    'more_info_link': job['job_result_more_info_link'],
                    'salary': job['job_result_salary'],
                    'job_type': job['job_result_type'],
                    'first_seen': job['time_posted'],
                    'summary_title': job['summary_title'],
                    'summary': job['summary'],
                    'description_title': job['description_title'],
                    'requirements': job['requirements']
                })
        print('------------------done updating jobs------------------')
