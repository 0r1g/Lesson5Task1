from django.core.management.base import BaseCommand
from core.models import Student, Class


class Command(BaseCommand):
    help = 'Add a New Student'

    def add_arguments(self, parser):
        parser.add_argument('first_name', type=str, help='First Name of new Student')
        parser.add_argument('last_name', type=str, help='Last Name of new Student')
        parser.add_argument('student_class', type=int, help='ID of the Class')

    def handle(self, *args, **kwargs):
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        class_id = kwargs['student_class']

        try:
            student_class = Class.objects.get(id=class_id)
        except Class.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Subject with ID {class_id} does not exist'))
            return None

        if Student.objects.filter(first_name=first_name, last_name=last_name, student_class=student_class).exists():
            self.stdout.write(self.style.ERROR('Student already exists'))
        else:
            student = Student.objects.create(first_name=first_name, last_name=last_name, student_class=student_class)
            student.save()
            self.stdout.write(self.style.SUCCESS('Student added successfully'))
