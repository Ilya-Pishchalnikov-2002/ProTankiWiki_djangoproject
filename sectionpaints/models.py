from django.db import models
from django.utils.text import slugify
from sectionranks.models import Rank


class Paint(models.Model):
    name = models.CharField(verbose_name="Название", max_length=20, unique=True)
    slug_name = models.SlugField(max_length=20, blank=True)
    image_icon = models.ImageField(upload_to="Paints", verbose_name="Иконка в гараже")
    image_view = models.ImageField(upload_to="Paints", verbose_name="Вид на танке")
    rank_required = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, verbose_name="Требуемое звание")
    cost = models.IntegerField(verbose_name="Стоимость")
    description = models.TextField(verbose_name="Описание в гараже", null=True, blank=True)

    have_resist = models.BooleanField(verbose_name="Имеет защиту от пушек")
    resist_smoky = models.SmallIntegerField(verbose_name="Зашита от Смоки", null=True, blank=True)
    resist_firebird = models.SmallIntegerField(verbose_name="Зашита от Огнемёта", null=True, blank=True)
    resist_twins = models.SmallIntegerField(verbose_name="Зашита от Твинса", null=True, blank=True)
    resist_hammer = models.SmallIntegerField(verbose_name="Зашита от Молота", null=True, blank=True)
    resist_railgun = models.SmallIntegerField(verbose_name="Зашита от Рельсы", null=True, blank=True)
    resist_isida = models.SmallIntegerField(verbose_name="Зашита от Изиды", null=True, blank=True)
    resist_vulcan = models.SmallIntegerField(verbose_name="Зашита от Вулкана", null=True, blank=True)
    resist_thunder = models.SmallIntegerField(verbose_name="Зашита от Грома", null=True, blank=True)
    resist_freeze = models.SmallIntegerField(verbose_name="Зашита от Фриза", null=True, blank=True)
    resist_ricochet = models.SmallIntegerField(verbose_name="Зашита от Рикошета", null=True, blank=True)
    resist_shaft = models.SmallIntegerField(verbose_name="Зашита от Шафта", null=True, blank=True)
    resist_mines = models.SmallIntegerField(verbose_name="Зашита от мин", null=True, blank=True)
    resist_all = models.SmallIntegerField(verbose_name="Зашита от всех пушек и мин", null=True, blank=True)

    class Meta:
        verbose_name = "Краска"
        verbose_name_plural = "Краски"

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, allow_unicode=True)
        super(Paint, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
