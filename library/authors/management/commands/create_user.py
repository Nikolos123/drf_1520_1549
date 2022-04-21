from django.contrib.auth.models import User
from django.core.management import BaseCommand

from authors.models import Author, Book


class Command(BaseCommand):

    def handle(self, *args, **options):

        User.objects.create_superuser(username='nikolay', password='1', email='admin@mail.ru')
        data_author = {
            'first_name': 'Александр',
            'last_name': 'Пушкин',
            'birthday_year': 1789
        }
        author = Author.objects.create(**data_author)
        # data_book = {
        #     'name':'Руслан и Людмила',
        #     'authors':[author.id]
        # }
        book = Book.objects.create(name='Руслан и Людмила')
        book.authors.add(author.id)
