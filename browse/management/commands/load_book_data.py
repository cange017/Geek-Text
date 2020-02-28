"""
Mod Log:
1/24 Miguel created batch upload proces for CSV files
1/25 Miguel updated process to read multiple comments

"""
from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from browse.models import Book,Author,Comments
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from book_data.csv into our book model"

    def handle(self, *args, **options):
        if Book.objects.exists():#or Author.objects.exists():
            print('Book data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating book data")
        
        print("Loading book data")
        for row in DictReader(open('./book_data.csv')):
            book = Book()
            book.image = row['image']
            book.title = row['title']

            obj, created = Author.objects.get_or_create(name=row['author'],
                  defaults={'bio':"Not available"})
            book.author = obj  
            if row['rating'].isdigit():
                obj = row['rating']
            else:
                obj = None
            book.rating = obj
            book.genre = row['genre']
            book.topSeller = row['top_seller'].lower().capitalize()
            book.price = row['price']
            raw_submission_date = row['release_date']
            # add if statement below for datetime eror when time data = ''
            #if (len(raw_submission_date) != 0):
            submission_date = UTC.localize(datetime.strptime(raw_submission_date, DATETIME_FORMAT))
            book.releaseDate = submission_date
            book.save()
            book.Publisher = row['publisher']
            book.description = row['description']
            comments = row['comments']#gets an array of comments tokenized by pipes "|"
            commentsArr = [name for name in comments.split('| ') if name]
            for newComment in commentsArr:
                book.comments = Comments(text= newComment)
                book.comments.save()
            book.save()
           
           
           
