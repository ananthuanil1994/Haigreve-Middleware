from apscheduler.schedulers.background import BackgroundScheduler
from src.handlers.zimperium_handler import deactivate_zimperium_users
from src.services.getRenewalUsersList import get_users_for_renewal, get_users_for_deactivating


def start_scheduler():
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Dhaka'})
    scheduler.add_job(deactivate_zimperium_users, 'interval', days=1)
    scheduler.start()
