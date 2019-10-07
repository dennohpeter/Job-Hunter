from apscheduler.schedulers.background import BackgroundScheduler
from brighterMonday.scraper import Crawler

scheduler = BackgroundScheduler()
crawler = Crawler()
# runs `crawler.fetch_jobs()` function every day at interval of 6 hours
sched_task = scheduler.add_job(crawler.fetch_jobs(), 'interval', minutes=5)
sched_task.start()
