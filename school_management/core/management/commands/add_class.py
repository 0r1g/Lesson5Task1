from django.core.management.base import BaseCommand
from core.models import Class


class Command(BaseCommand):
    help = 'Add a New Class'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of new Class')
        parser.add_argument('year', type=int, help='Year of new Class')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        year = kwargs['year']

        if Class.objects.filter(name=name, year=year).exists():
            self.stdout.write(self.style.ERROR('Class already exists'))
        else:
            your_class = Class.objects.create(name=name, year=year)
            your_class.save()
            self.stdout.write(self.style.SUCCESS('Class added successfully'))
