from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)
    pseudo_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class BookModel(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        AuthorModel,
        on_delete=models.CASCADE,
        related_name='books'
    )
    short_description = models.CharField(max_length=255)
    long_description = models.TextField()
    price = models.PositiveIntegerField()
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='books/')

    def __str__(self):
        return self.title

    def get_price(self):
        if self.discount:
            return self.price - self.price / 100 * self.discount
        else:
            return self.price

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
