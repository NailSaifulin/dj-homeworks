from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Температура')
    date_measurements = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
