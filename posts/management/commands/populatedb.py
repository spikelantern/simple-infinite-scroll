from django.core.management.base import BaseCommand, CommandError
from posts.models import Post

class Command(BaseCommand):
    help = 'Populates the database. Deletes old entries'

    def handle(self, *args, **options):
        print("Deleting old entries...")
        Post.objects.all().delete()
        print("Populating...")
        for i in range(300):
            Post.objects.create(text=str(i))
        print("Done.")