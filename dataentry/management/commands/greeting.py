from django.core.management.base import BaseCommand, CommandParser
# Proposed command =python manage greeting Name
#prposed output = hi {name}
class Command(BaseCommand):
    help = 'Greet the user'
    def add_arguments(self, parser):
        parser.add_argument('name',type=str, help='user name')
        
    def handle(self,*args,**kwargs):
        name =kwargs['name']
        greeting = f'Hi {name}'
        self.stdout.write(self.style.SUCCESS(greeting))  
        # you can change the color by warning or self.style.success/warning