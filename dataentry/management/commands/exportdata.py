from django.core.management.base import BaseCommand, CommandParser
import csv

from django.apps import apps
import datetime

#python manage.py exportdata model_name

class Command(BaseCommand):
    help = 'Export data from database model to the csv file'
    def add_arguments(self, parser):
        parser.add_argument('model_name',type=str,help='model name')
        
    
    def handle(self, *args, **kwargs):
        model_name=kwargs['model_name'].capitalize()
        #serach through all the installed app for the model
        model =None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name)
                break
            except LookupError:
                continue
        if not model:
            self.stderr.write(f'Model {model_name} could not found')
            return
                
        #feth the data from database
        data=model.objects.all()

        #generate the timestamp of current time
        timestamp= datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        
        
        #define the csv file name/path
        file_path=f'exported_{model_name}_data_{timestamp}.csv'
        print(file_path)
        #open the csv file write the data
        with open(file_path, 'w' ,newline='') as file:
            writer = csv.writer(file)
            #write the CSV header
            #we want tp print the fiels name of the model
            writer.writerow([field.name for field in model._meta.fields])
            #write data rows
            for dt in data:
                writer.writerow([getattr(dt,field.name) for field in model._meta.fields])
        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))
               
             