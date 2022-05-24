from django.db import models
from django.utils import timezone
from utils.constants import BOOK_GENRES, JOURNAL_TYPES
from auth_.models import AuthUser

# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=30, null=True)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(default=timezone.now)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.SmallIntegerField(choices=BOOK_GENRES, default=2)
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self) -> str:
        return self.name


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=JOURNAL_TYPES)
    # one to many
    publisher = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
    
    def __str__(self) -> str:
        return self.name
    