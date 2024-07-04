from django.db import models


class Rank(models.Model):
    rank_name = models.CharField(max_length=20, verbose_name="Звание", unique=True)
    rank_icon = models.ImageField(upload_to="Ranks", verbose_name="Иконка")
    exp_start = models.IntegerField(verbose_name="Опыт")
    exp_next = models.IntegerField(verbose_name="Опыт до следующего звания")
    cry_bonus = models.IntegerField(verbose_name="Награда")

    class Meta:
        verbose_name = "Звание"
        verbose_name_plural = "Звания"

    def __str__(self):
        return f"{self.rank_name}"
