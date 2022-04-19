from apscheduler.schedulers.background import BackgroundScheduler
from src.services.getRenewalUsersList import get_users_for_renewal


def start_scheduler():
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Dhaka'})
    scheduler.add_job(get_users_for_renewal, 'interval', days=1)
    scheduler.start()

