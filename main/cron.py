from django_cron import CronJobBase, Schedule
from blacklist.models import BlackList


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1
    RETRY_AFTER_FAILURE_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'main.my_cron_job'

    def do(self):
        b = BlackList(ip="2468")
        b.save()
