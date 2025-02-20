import platform
import sys

import shutil
import datetime

from mail import send_smtp_email

def get_info():
    system_os = platform.system()
    python_version = sys.version
    total_disk_space = shutil.disk_usage("/").total / (1024 ** 3)
    free_disk_space = shutil.disk_usage("/").free / (1024 ** 3)

    report = f"""
    System Report:
    ---------------
    Operating System: {system_os}
    Python Version: {python_version}
    Total Disk Space: {total_disk_space:.2f} GB
    Free Disk Space: {free_disk_space:.2f} GB
    """

    return report

def save_text(report):
    now = datetime.datetime.now()
    file_name = f"system_report_{now.strftime('%Y%m%d_%H%M%S')}.txt"
    with open(file_name, 'w') as f:
        f.write(report)
    return file_name

def send_mail(filename, date):
    subject = f'System Report {date}'
    text = f"Attached is the system report {filename}."

    send_smtp_email(subject, text)



if __name__ == "__main__":
    report = get_info()
    print(report)
    filename = save_text(report)
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    send_mail(filename,date)

    print(f"Report generated and sent to email with filename: {filename}")

