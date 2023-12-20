from django import forms
from .models import Person, Image, File, VideoFile, AudioFile


class Form(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']


class UploadFileForm(forms.Form):
    file_path = forms.FilePathField(label="Выберите файл",
                                    path="templates", allow_files="True", allow_folders="True")


class InputNumForm(forms.Form):
    num = forms.IntegerField(label="Введите число", help_text="Не юзай буковы молю")


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = '__all__'


class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = '__all__'


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = '__all__'
