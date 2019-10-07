from brighterMonday.scraper import Crawler
from django.core.management.base import BaseCommand, CommandError
from apscheduler.schedulers.blocking import BlockingScheduler


class Command(BaseCommand):
    help = "This function fetchs and updates jobs in jobs db"

    def handle(self, *args, **options):
        sched = BlockingScheduler()
        # runs `crawler.fetch_jobs()` function every day at interval of 6 hours
        time = 3
        @sched.scheduled_job('interval', minutes=time)
        def fetch_jobs():
            print('------------------starting cron job --------------------')
            crawler = Crawler()
            crawler.fetch_jobs()
            print('------------------cron job done --------------------')
            print('------------------sleeping for %s --------------------' % time)

        sched.start()
