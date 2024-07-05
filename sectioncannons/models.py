from django.db import models
from django.utils.text import slugify


class Cannon(models.Model):
    CATEGORY_LIST = [
        ("Ближний бой", "Ближний бой"),
        ("Малая дальность", "Малая дальность"),
        ("Средняя дальность", "Средняя дальность"),
        ("Большая дальность", "Большая дальность")
    ]

    name = models.CharField(verbose_name="Название", max_length=10, unique=True)
    slug_name = models.SlugField(max_length=10, unique=True, blank=True)
    image = models.ImageField(upload_to="Cannons", verbose_name="Изображение")
    category = models.CharField(verbose_name="Категория", max_length=20, choices=CATEGORY_LIST)

    class Meta:
        verbose_name = "Пушка"
        verbose_name_plural = "Пушки"

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, allow_unicode=True)
        super(Cannon, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
