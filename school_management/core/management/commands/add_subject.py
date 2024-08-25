from django.core.management.base import BaseCommand
from core.models import Subject


class Command(BaseCommand):
    help = 'Add a New Subject'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name of new Subject')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        if Subject.objects.filter(name=name).exists():
            self.stdout.write(self.style.ERROR('Subject already exists'))
        else:
            subject = Subject.objects.create(name=name)
            subject.save()
            self.stdout.write(self.style.SUCCESS('Subject added successfully'))
