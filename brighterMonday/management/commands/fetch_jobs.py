from brighterMonday.scraper import Crawler
from django.core.management.base import BaseCommand, CommandError
from apscheduler.schedulers.blocking import BlockingScheduler
from django.conf import settings
from brighterMonday.sms import SMS
from django.utils import timezone


class Command(BaseCommand):
    help = "This function fetchs and updates jobs in jobs db"

    def handle(self, *args, **options):
        sched = BlockingScheduler()
        sms = SMS()
        # runs `crawler.fetch_jobs()` function every day at interval of 6 hours
        time = 20
        started_msg = "Started Fetching jobs at %s" % timezone.now()
        done_msg = "Done Fetching jobs at %s" % timezone.now()
        @sched.scheduled_job('interval', minutes=time)
        def fetch_jobs():
            print('------------------starting cron job --------------------')
            sms.send_sms(settings.PHONE_NUMBER, started_msg)
            crawler = Crawler()
            crawler.fetch_jobs()
            # sending sms
            sms.send_sms(settings.PHONE_NUMBER, done_msg)

            print('------------------cron job done --------------------')
            print('------------------sleeping for %s minutes--------------------' % time)

        sched.start()
