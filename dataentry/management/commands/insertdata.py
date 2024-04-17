from django.core.management.base import BaseCommand

from dataentry.models import Student

#I want to add some data  to the database uing the custom command

class Command(BaseCommand):
    help = 'Insert data to data base'
    def handle(self, *argd,**kwargs):
        #logic
        #add 1 data
        #Student.objects.create(roll_no=1001,name='Ahmad',age='20')
        #add many data
        dataset=[
            {'roll_no': 1007, 'name':'carla','age':24},
            {'roll_no': 1003, 'name':'mahmoud','age':36},
            {'roll_no': 1004, 'name':'Fadi','age':34},
            {'roll_no': 1006, 'name':'Fadi','age':33},
            {'roll_no': 1005, 'name':'Rania','age':34},
        ]
        for data in dataset:
            roll_no =data['roll_no']
            exisiting_record= Student.objects.filter(roll_no=roll_no).exists()
            if not exisiting_record:
              Student.objects.create(roll_no=data['roll_no'],name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll number {roll_no} already exists!'))
            
        self.stdout.write(self.style.SUCCESS('Data insert successfully!'))