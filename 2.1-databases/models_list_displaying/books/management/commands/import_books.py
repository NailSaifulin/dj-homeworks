import csv
import json

from django.core.management.base import BaseCommand
from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('fixtures/books.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            for items in json_data:
                Book.objects.create(name=items['fields']['name'], author=items['fields']['author'],
                                    pub_date=items['fields']['pub_date'])
