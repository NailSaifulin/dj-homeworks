from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.URLField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f'{self.name}\n {self.image}\n {self.price}\n {self.release_date}\n {self.lte_exists}' \
               f'\n {self.slug}'
