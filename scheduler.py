import schedule
import time
from mindfulness_bot.main import run_bot

schedule.every().day.at("08:00").do(run_bot)

print("Scheduler started. Running daily at 08:00 AM.")
while True:
    schedule.run_pending()
    time.sleep(60)
