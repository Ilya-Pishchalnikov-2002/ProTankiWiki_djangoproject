from django.db import models
from django.utils.text import slugify
from sectionranks.models import Rank

__all__ = [
    "Cannon", "Smoki", "Firebird", "Twins", "Hammer", "Railgun", "Isida", "Vulcan", "Thunder", "Freeze",
    "Ricochet", "Shaft"]


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


class CannonCommonInfo(models.Model):
    """ Родительский класс, содержащий несколько общих полей, которые будут во всех дочерних """

    M_LIST = [
        ("M0", "M0"),
        ("M1", "M1"),
        ("M2", "M2"),
        ("M3", "M3")
    ]

    cannon = models.ForeignKey(Cannon, on_delete=models.DO_NOTHING, verbose_name="Пушка")
    modification = models.CharField(verbose_name="Модификация", max_length=2, choices=M_LIST)
    image = models.ImageField(upload_to="Cannons", verbose_name="Изображение", null=True)
    rank_required = models.ForeignKey(Rank, on_delete=models.DO_NOTHING, verbose_name="Требуемое звание")
    cost = models.IntegerField(verbose_name="Стоимость")

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.cannon.name} {self.modification}"


class Smoki(CannonCommonInfo):
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


class Firebird(CannonCommonInfo):
    damage_hp_sec = models.SmallIntegerField(verbose_name="Урон (хп/сек)")
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=2)
    attack_duration = models.DecimalField(verbose_name="Длительность атаки", max_digits=3, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=4, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")
    burning_damage = models.DecimalField(verbose_name="Урон от горения", max_digits=3, decimal_places=1)

    class Meta:
        verbose_name = "Огнемёт"
        verbose_name_plural = "Огнемёт"


class Twins(CannonCommonInfo):
    damage_min = models.DecimalField(verbose_name="Урон (мин)", max_digits=3, decimal_places=1)
    damage_max = models.DecimalField(verbose_name="Урон (макс)", max_digits=3, decimal_places=1)
    impact_force = models.DecimalField(verbose_name="Сила удара", max_digits=5, decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=3, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    projectile_speed = models.DecimalField(verbose_name="Скорость снаряда", max_digits=4, decimal_places=2)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=4, decimal_places=2)
    weak_dmg_percent = models.DecimalField(verbose_name="Процент слабого поражения", max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = "Твинс"
        verbose_name_plural = "Твинс"


class Hammer(CannonCommonInfo):
    damage_shot = models.DecimalField(verbose_name="Урон выстрела", max_digits=4, decimal_places=1)
    damage_pellet = models.DecimalField(verbose_name="Урон дробинки", max_digits=3, decimal_places=1)
    impact_force_shot = models.DecimalField(verbose_name="Сила удара выстрела", max_digits=5, decimal_places=2)
    impact_force_pellet = models.DecimalField(verbose_name="Сила удара дробинки", max_digits=4, decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=3)
    reload_speed_clip = models.DecimalField(verbose_name="Зарядка обоймы", max_digits=4, decimal_places=3)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=4, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")
    pellet_count = models.SmallIntegerField(verbose_name="Количество дробинок")
    spread_angle_vertical = models.SmallIntegerField(verbose_name="Угол разброса (вертикальный)")
    spread_angle_horizonatal = models.SmallIntegerField(verbose_name="Угол разброса (горизонтальный)")

    class Meta:
        verbose_name = "Молот"
        verbose_name_plural = "Молот"


class Railgun(CannonCommonInfo):
    damage_min = models.SmallIntegerField(verbose_name="Урон (мин)")
    damage_max = models.SmallIntegerField(verbose_name="Урон (макс)")
    impact_force = models.DecimalField(verbose_name="Сила удара", max_digits=5, decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=3)
    shot_delay = models.DecimalField(verbose_name="Задержка перед выстрелом", max_digits=4, decimal_places=3)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    penetration_percent = models.DecimalField(verbose_name="Процент прострела", max_digits=4, decimal_places=1)

    class Meta:
        verbose_name = "Рельса"
        verbose_name_plural = "Рельса"


class Isida(CannonCommonInfo):
    damage_hp_sec = models.SmallIntegerField(verbose_name="Урон (хп/сек)")
    healing_hp_sec = models.SmallIntegerField(verbose_name="Лечение (хп/сек)")
    selfhealing_percent = models.DecimalField(verbose_name="Процент самолечения", max_digits=3, decimal_places=1)
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=2)
    attack_duration = models.DecimalField(verbose_name="Длительность атаки", max_digits=3, decimal_places=2)
    healing_idle_duration = models.DecimalField(verbose_name="Длительность лечения/холостой атаки",
                                                max_digits=4, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    attack_range = models.DecimalField(verbose_name="Дальность атаки", max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = "Изида"
        verbose_name_plural = "Изида"


class Vulcan(CannonCommonInfo):
    damage_hp_sec = models.SmallIntegerField(verbose_name="Урон (хп/сек)")
    impact_force = models.DecimalField(verbose_name="Сила удара", max_digits=5, decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    overheating_time = models.DecimalField(verbose_name="Время до перегрева", max_digits=4, decimal_places=3)
    self_heating = models.DecimalField(verbose_name="Самонагрев", max_digits=3, decimal_places=2)
    self_heat_limit = models.DecimalField(verbose_name="Ограничение на температуру", max_digits=3, decimal_places=2)
    barrel_spin_up_time = models.DecimalField(verbose_name="Раскрутка стволов", max_digits=3, decimal_places=2)
    barrel_spin_down_time = models.DecimalField(verbose_name="Остановка стволов", max_digits=3, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    rotation_deceleration = models.DecimalField(verbose_name="Замедление поворта при стрельбе",
                                                max_digits=4, decimal_places=1)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=5, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")

    class Meta:
        verbose_name = "Вулкан"
        verbose_name_plural = "Вулкан"


class Thunder(CannonCommonInfo):
    damage_min = models.SmallIntegerField(verbose_name="Урон (мин)")
    damage_max = models.SmallIntegerField(verbose_name="Урон (макс)")
    impact_force = models.DecimalField(verbose_name="Сила удара", max_digits=5, decimal_places=2)
    impact_force_splash = models.DecimalField(verbose_name="Сила удара сплеша", max_digits=5, decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=3)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=5, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")
    max_dmg_radius = models.DecimalField(verbose_name="Радиус макс поражения", max_digits=4, decimal_places=2)
    min_dmg_radius = models.DecimalField(verbose_name="Радиус мин поражения", max_digits=4, decimal_places=2)
    weak_splash_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения сплешом")

    class Meta:
        verbose_name = "Гром"
        verbose_name_plural = "Гром"


class Freeze(CannonCommonInfo):
    damage_hp_sec = models.SmallIntegerField(verbose_name="Урон (хп/сек)")
    reload_speed = models.DecimalField(verbose_name="Перезарядка", max_digits=4, decimal_places=2)
    attack_duration = models.DecimalField(verbose_name="Длительность атаки", max_digits=3, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=4, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")

    class Meta:
        verbose_name = "Фриз"
        verbose_name_plural = "Фриз"


class Ricochet(CannonCommonInfo):
    damage_min = models.SmallIntegerField(verbose_name="Урон (мин)")
    damage_max = models.SmallIntegerField(verbose_name="Урон (макс)")
    impact_force = models.DecimalField(verbose_name="Сила удара", max_digits=5, decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    reload_speed = models.DecimalField(verbose_name="Перезарядка выстрелов", max_digits=4, decimal_places=3)
    energy_consumption = models.DecimalField(verbose_name="Процент энергии на выстрел", max_digits=4, decimal_places=2)
    charging_speed = models.DecimalField(verbose_name="Перезарядка всего баллона", max_digits=4, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    projectile_speed = models.DecimalField(verbose_name="Скорость снаряда", max_digits=5, decimal_places=2)
    max_dmg_range = models.DecimalField(verbose_name="Дальность макс поражения", max_digits=4, decimal_places=2)
    min_dmg_range = models.DecimalField(verbose_name="Дальность мин поражения", max_digits=5, decimal_places=2)
    weak_dmg_percent = models.SmallIntegerField(verbose_name="Процент слабого поражения")

    class Meta:
        verbose_name = "Рикошет"
        verbose_name_plural = "Рикошет"


class Shaft(CannonCommonInfo):
    damage_sniper_min = models.SmallIntegerField(verbose_name="Урон прицельный(мин)")
    damage_sniper_max = models.SmallIntegerField(verbose_name="Урон прицельный(макс)")
    damage_arcade_min = models.SmallIntegerField(verbose_name="Урон навскидку(мин)")
    damage_arcade_max = models.SmallIntegerField(verbose_name="Урон навскидку(макс)")
    impact_force_sniper = models.DecimalField(verbose_name="Сила удара прицельного выстрела", max_digits=5,
                                              decimal_places=2)
    impact_force_arcade = models.DecimalField(verbose_name="Сила удара выстрела навскидку", max_digits=5,
                                              decimal_places=2)
    recoil_force = models.DecimalField(verbose_name="Отдача", max_digits=5, decimal_places=2)
    reload_speed_arcade = models.DecimalField(verbose_name="Перезарядка выстрелов навскидку", max_digits=4,
                                              decimal_places=3)
    energy_consumption = models.DecimalField(verbose_name="Процент энергии на выстрел навскидку", max_digits=4,
                                             decimal_places=2)
    sniper_loading_time = models.DecimalField(verbose_name="Время зарядки прицельного выстрела", max_digits=3,
                                              decimal_places=2)
    charging_speed = models.DecimalField(verbose_name="Перезарядка всего баллона", max_digits=4, decimal_places=2)
    rotation_speed = models.DecimalField(verbose_name="Скорость поворота", max_digits=4, decimal_places=1)
    aiming_speed_horiz = models.DecimalField(verbose_name="Скорость прицеливания по горизонтали", max_digits=4,
                                             decimal_places=2)
    aiming_speed_vertic = models.DecimalField(verbose_name="Скорость прицеливания по вертикали", max_digits=4,
                                              decimal_places=2)
    penetration_percent = models.DecimalField(verbose_name="Процент прострела", max_digits=4, decimal_places=1)

    class Meta:
        verbose_name = "Шафт"
        verbose_name_plural = "Шафт"
