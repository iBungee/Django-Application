from django_cron import CronJobBase, Schedule

class CronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'poll.cron.CronJob'    # a unique code

    def do(self):
        print("Running cron jobs")