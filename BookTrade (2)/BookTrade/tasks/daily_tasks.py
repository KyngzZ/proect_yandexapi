import schedule
import time

def send_daily_email():
    print("Отправка ежедневного письма... (Заглушка)")

schedule.every().day.at("08:00").do(send_daily_email)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
