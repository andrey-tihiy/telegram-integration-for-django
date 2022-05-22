from django.core.management.base import BaseCommand, CommandError
from apps.property_bot.service import dp
from aiogram import executor


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        executor.start_polling(dp, skip_updates=True)
