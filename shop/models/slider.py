from django.db import models



class Slider(models.Model):
    photo = models.ImageField(verbose_name="Фотогория слайдера")
    url = models.TextField(verbose_name="Сыллка на акцию", null=True)
    
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'
    
