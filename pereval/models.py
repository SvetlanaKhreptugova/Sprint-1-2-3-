from django.db import models

new = 'New'
pending = 'PG'
accepted = 'AD'
rejected = 'RD'

STATUS = [
    (new, "New"),
    (pending, "Pending"),
    (accepted, "Accepted"),
    (rejected, "Rejected")
]


# В данной модели указаны поля для ввода Имени, Фамилии, Отчество, почты, и телефона

class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, null=False)
    surname = models.CharField(max_length=150, null=False)
    email = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=11, null=False)


class Coord(models.Model):  # Указываем координаты (широта, долгота, высота)
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Level(models.Model):  # Уровень сложности по времени года
    winter = models.TextField(blank=True, null=True)
    summer = models.TextField(blank=True, null=True)
    autumn = models.TextField(blank=True, null=True)
    spring = models.TextField(blank=True, null=True)


# В данной модели указываются поля о координатах, времени года...
class Pass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.ForeignKey(Coord, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    status = models.CharField(max_length=150, choices=STATUS, default='New')
    beauty_title = models.CharField(max_length=250, blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    other_titles = models.CharField(max_length=250, blank=True, null=True)
    connect = models.CharField(max_length=250, blank=True, null=True)
    add_time = models.DateTimeField(auto_now_add=True)


class Image(models.Model):
    title = models.CharField(max_length=255)
    data = models.URLField()
    passes = models.ForeignKey(Pass, on_delete=models.CASCADE, related_name='images')
