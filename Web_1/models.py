from django.db import models
from django.contrib.auth.models import User

def get_user_credentials(username):
    try:
        user = User.objects.get(username=username)
        password = user.password
        return username, password
    except User.DoesNotExist:
        return None, None

class Person(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="Имя клиента")
    age = models.IntegerField(verbose_name="Возраст клиента")
    object_person = models.Manager()
    DoesNotExist = models.Manager


class Image(models.Model):
    title = models.CharField(max_length=100, null=False, verbose_name="Описание изображения")
    image = models.ImageField(upload_to='images', verbose_name="Файл с изображением", null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Описание файла", )
    file = models.FileField(upload_to='files',
                            verbose_name="Файл PDF",
                            null=True, blank=True)

    def __str__(self):
        return self.title


class VideoFile(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Описание файла", )
    file = models.FileField(upload_to='videos',
                            verbose_name="Видео файл",
                            null=True, blank=True)
    obj_video = models.Manager()

    def __str__(self):
        return self.title


# Загрузка аудио файлов
class AudioFile(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Описание файла", )
    file = models.FileField(upload_to='audios',
                            verbose_name="Аудио файл",
                            null=True, blank=True)
    obj_audio = models.Manager()

    def __str__(self):
        return self.title
