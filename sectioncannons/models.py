from django.db import models
from django.utils.text import slugify
from sectionranks.models import Rank


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
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Пушка"
        verbose_name_plural = "Пушки"

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name, allow_unicode=True)
        super(Cannon, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


M_LIST = [
    ("M0", "M0"),
    ("M1", "M1"),
    ("M2", "M2"),
    ("M3", "M3")
]


class CannonCommonInfo(models.Model):
    """ Родительский класс, содержащий несколько общих полей, которые будут во всех дочерних """
    cannon = models.ForeignKey(Cannon, on_delete=models.DO_NOTHING, verbose_name="Пушка")
    modification = models.CharField(verbose_name="Модификация", max_length=2, choices=M_LIST)
    rank_required = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, verbose_name="Требуемое звание")
    cost = models.IntegerField(verbose_name="Стоимость")

    class Meta:
        abstract = True


class Smoki(CannonCommonInfo):
    image = models.ImageField(upload_to="Cannons-Smoki", verbose_name="Изображение")
    damage_min = models.SmallIntegerField(verbose_name="Урон (мин)")
    damage_max = models.SmallIntegerField(verbose_name="Урон (макс)")
    impact_force = models.DecimalField(verbose_name="Сила удара", max_digits=5, decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=3)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=5, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=5, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")
    critical_chance = models.SmallIntegerField(verbose_name="Шанс критического урона")
    critical_damage = models.SmallIntegerField(verbose_name="Критический урон")

    class Meta:
        verbose_name = "Смоки"
        verbose_name_plural = "Смоки"

    def __str__(self):
        return f"{self.cannon.name} {self.modification}"


class Firebird(CannonCommonInfo):
    image = models.ImageField(upload_to="Cannons-Firebird", verbose_name="Изображение")
    damage_hp_sec = models.SmallIntegerField(verbose_name="Урон (хп/сек)")
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=2)
    attack_duration = models.DecimalField(verbose_name="Длительность атаки", max_digits=3, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=4, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")
    burning_time = models.DecimalField(verbose_name="Время горения", max_digits=3, decimal_places=1)

    class Meta:
        verbose_name = "Огнемёт"
        verbose_name_plural = "Огнемёт"

    def __str__(self):
        return f"{self.cannon.name} {self.modification}"
