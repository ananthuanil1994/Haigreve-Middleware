from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def start_scheduler():
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Dhaka'})
    scheduler.add_job(sent_renewal_notification, 'interval', seconds=10)
    scheduler.start()

def sent_renewal_notification():
    time_now = datetime.now()
    print(f"Scheduler is alive : {time_now}")