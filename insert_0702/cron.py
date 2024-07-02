from crontab import CronTab
cron = CronTab(user=True)
job = cron.new(command="echo'Halo world'")
job.minute.every(1)
cron.write()