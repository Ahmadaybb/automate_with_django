import time

from django.conf import settings
from awd_main.celery import app
from django.core.management import call_command
from .utils import generate_csv_file, send_email_notification
@app.task
def celery_test_task():
    time.sleep(5)
    mail_subject = 'Test Subject'
    message= 'this is a test amil'
   
    to_email=settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
    return 'task done'
@app.task
def import_data_task(file_path,model_name):
    try:
        call_command('importdata',file_path,model_name)
    except Exception as e:
        raise e
    mail_subject = 'Import Data Compelted'
    message= 'Your data import has been successful'
    to_email=settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email)
    return 'data imported successfully'

@app.task
def export_data_task(model_name):
    try:
        call_command('exportdata',model_name)
    except Exception as e:
        raise e
    file_path= generate_csv_file(model_name)
    mail_subject = 'Emport Data Compelted'
    message= 'Export data successful.Please find the attachment'
    to_email=settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject,message,to_email,attachment=file_path)
    return 'Export Data task executed successfully'
    
    