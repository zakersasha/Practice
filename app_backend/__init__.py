"""App initialization."""
from flask import Flask

import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import schedule
from app_backend.metrics import generate_line_bar, hey


def create_app() -> Flask:
    """Create and configure Flask app."""
    app = Flask(__name__, template_folder='static')
    # metric.init_app(app)

    schedule = BackgroundScheduler()
    schedule.add_job(lambda: generate_line_bar(2, 10, '2'), trigger='cron', second=10)
    schedule.add_job(lambda: generate_line_bar(2, 10, '2'), trigger='cron', second=20)
    schedule.add_job(lambda: generate_line_bar(2, 10, '2'), trigger='cron', second=30)
    schedule.add_job(lambda: generate_line_bar(2, 10, '2'), trigger='cron', second=40)
    schedule.start()
    atexit.register(lambda: schedule.shutdown())

    # Инициализация и запуск h2o
    return app


app = create_app()
