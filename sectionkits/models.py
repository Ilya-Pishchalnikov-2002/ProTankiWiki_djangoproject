from django.db import models
from sectionranks.models import Rank
from sectioncannons.models import Cannon
from sectionhulls.models import Hull
from sectionpaints.models import Paint


class KitCommonInfo(models.Model):
    name = models.CharField(verbose_name="Название", max_length=25, unique=True)
    image = models.ImageField(upload_to="Kits", verbose_name="Изображение")
    discount = models.SmallIntegerField(verbose_name="Скидка")
    cost = models.IntegerField(verbose_name="Стоимость по скидке")
    rank_start = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, verbose_name="Требуемое звание (от)",
                                   related_name="%(class)s_rank_start")
    rank_end = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, verbose_name="Требуемое звание (до)",
                                 related_name="%(class)s_rank_end")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name}"


class ArmamentKit(KitCommonInfo):
    content = models.TextField(verbose_name="Содержание")

    class Meta:
        verbose_name = "Комплект вооружений"
        verbose_name_plural = "Комплекты вооружений"


class SupplyKit(KitCommonInfo):
    supply_count = models.SmallIntegerField(verbose_name="Количество припасов каждого вида")

    class Meta:
        verbose_name = "Комплект припасов"
        verbose_name_plural = "Комплекты припасов"


class TankKit(KitCommonInfo):
    M_LIST = [
        ("M0", "M0"),
        ("M1", "M1"),
        ("M2", "M2"),
        ("M3", "M3")
    ]

    cannon = models.ForeignKey(Cannon, on_delete=models.DO_NOTHING, verbose_name="Пушка")
    cannon_modification = models.CharField(verbose_name="Модификация пушки", max_length=2, choices=M_LIST)
    hull = models.ForeignKey(Hull, on_delete=models.DO_NOTHING, verbose_name="Корпус")
    hull_modification = models.CharField(verbose_name="Модификация корпуса", max_length=2, choices=M_LIST)
    paint = models.ForeignKey(Paint, on_delete=models.DO_NOTHING, verbose_name="Краска")

    class Meta:
        verbose_name = "Танковый комплект"
        verbose_name_plural = "Танковые комплекты"
