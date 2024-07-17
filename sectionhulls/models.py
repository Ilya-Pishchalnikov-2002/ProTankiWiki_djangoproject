from django.db import models
from django.utils.text import slugify
from sectionranks.models import Rank


class Hull(models.Model):
    CATEGORY_LIST = [
        ("Лёгкий", "Лёгкий"),
        ("Средний", "Средний"),
        ("Тяжёлый", "Тяжёлый")
    ]

    name = models.CharField(verbose_name="Название", max_length=10, unique=True)
    slug_name = models.SlugField(max_length=10, unique=True, blank=True)
    image = models.ImageField(upload_to="Hulls", verbose_name="Изображение")
    category = models.CharField(verbose_name="Категория", max_length=7, choices=CATEGORY_LIST)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Корпус"
        verbose_name_plural = "Корпуса"

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, allow_unicode=True)
        super(Hull, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class HullCommonInfo(models.Model):
    """ Родительский класс, содержащий несколько общих полей, которые будут во всех дочерних """

    M_LIST = [
        ("M0", "M0"),
        ("M1", "M1"),
        ("M2", "M2"),
        ("M3", "M3")
    ]

    hull = models.ForeignKey(Hull, on_delete=models.DO_NOTHING, verbose_name="Корпус")
    modification = models.CharField(verbose_name="Модификация", max_length=2, choices=M_LIST)
    image = models.ImageField(upload_to="Hulls", verbose_name="Изображение", null=True)
    rank_required = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, verbose_name="Требуемое звание")
    cost = models.IntegerField(verbose_name="Стоимость")

    armor = models.SmallIntegerField(verbose_name="Броня")
    max_speed = models.DecimalField(verbose_name="Максимальная скорость", max_digits=3, decimal_places=1)
    turning_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    weight = models.SmallIntegerField(verbose_name="Масса")
    power = models.SmallIntegerField(verbose_name="Мощность")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.hull.name} {self.modification}"


class Hunter(HullCommonInfo):
    class Meta:
        verbose_name = "Хантер"
        verbose_name_plural = "Хантер"


class Vasp(HullCommonInfo):
    class Meta:
        verbose_name = "Васп"
        verbose_name_plural = "Васп"


class Titan(HullCommonInfo):
    class Meta:
        verbose_name = "Титан"
        verbose_name_plural = "Титан"


class Dictator(HullCommonInfo):
    class Meta:
        verbose_name = "Диктатор"
        verbose_name_plural = "Диктатор"


class Hornet(HullCommonInfo):
    class Meta:
        verbose_name = "Хорнет"
        verbose_name_plural = "Хорнет"


class Mammoth(HullCommonInfo):
    class Meta:
        verbose_name = "Мамонт"
        verbose_name_plural = "Мамонт"


class Viking(HullCommonInfo):
    class Meta:
        verbose_name = "Викинг"
        verbose_name_plural = "Викинг"
