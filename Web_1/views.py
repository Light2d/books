from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .forms import UploadFileForm, InputNumForm, Form, ImageForm, VideoForm, AudioForm
from .models import Person, Image, File, VideoFile, AudioFile
from .forms import FileForm


def index(request):
    my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->',
             'IV квартал->']
    my_month = ['Январь', 'Февраль', 'Март',
                'Апрель', 'Май', 'Июнь',
                'Июль', 'Август', 'Сентябрь',
                'Октябрь', 'Ноябрь', 'Декабрь']
    context = {'my_month': my_month, 'my_kv': my_kv}
    return render(request, "index.html", context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def form(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            form.save()

    my_text = 'Сведения о клиентах'
    people = Person.object_person.all()
    form = Form()
    context = {'my_text': my_text, "people": people, "form": form}
    return render(request, "my_forms.html", context)


def edit_form(request, id):
    person = Person.object_person.get(id=id)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect('form')

    data = {"person": person}
    return render(request, "edit_form.html", context=data)


def delete(request, id):
    try:
        person = Person.object_person.get(id=id)
        person.delete()
        return redirect('form')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


def form_up_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_text = 'Загруженные изображения'
            my_img = Image.objects.all()
            form = ImageForm()
            context = {'my_text': my_text, "my_img": my_img, "form": form}
            return render(request, 'form_up_img.html', context)
        else:
            return HttpResponse("Форма не валидна.")
    elif request.method == 'GET':
        my_text = 'Загруженные изображения'
        my_img = Image.objects.all()
        form = ImageForm()
        context = {'my_text': my_text, "my_img": my_img, "form": form}
        return render(request, 'form_up_img.html', context)
    else:
        return HttpResponse("Неверный метод запроса.")


def delete_img(request, id):
    try:
        img = Image.objects.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Image.DoesNotExist:
        return HttpResponseNotFound("<h2>Изображение не найдено</h2>")


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = UploadFileForm()

    return render(request, 'upload_form.html', {'form': form})


def input_num(request):
    if request.method == 'POST':
        form = InputNumForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = InputNumForm()

    return render(request, 'input_num.html', {'form': form})

# загрузка файлов pdf
def form_up_pdf(request):
    context = {'my_text': '', "file_obj": File.objects.all(), "form": FileForm()}

    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context['my_text'] = 'Загруженные файлы'
            context['form'] = FileForm()

    return render(request, 'form_up_pdf.html', context)


# удаление файлов из БД
def delete_pdf(request, id):
    try:
        pdf = File.objects.get(id=id)
        pdf.delete()
        return redirect('form_up_pdf.html')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


# загрузка видео файлов
def form_up_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_text = 'Загруженные видео файлы'
            form = VideoForm()
            file_obj = VideoFile.obj_video.all()
            context = {'my_text': my_text, "file_obj": file_obj, "form": form}
            return render(request, 'form_up_video.html', context)
    else:
        form = VideoForm()
        file_obj = VideoFile.obj_video.all()
        context = {'my_text': 'Загруженные видео файлы', "file_obj": file_obj, "form": form}
        return render(request, 'form_up_video.html', context)


# удаление видео файлов из БД
def delete_video(request, id):
    try:
        video = VideoFile.obj_video.get(id=id)
        video.delete()
        return redirect('form_up_video')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")


# загрузка аудио файлов
from django.shortcuts import render

def form_up_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_text = 'Загруженные аудио файлы'
            form = AudioForm()
            file_obj = AudioFile.obj_audio.all()
            context = {'my_text': my_text, "file_obj": file_obj, "form": form}
            return render(request, 'form_up_audio.html', context)
    else:
        form = AudioForm()
        file_obj = AudioFile.obj_audio.all()
        context = {'my_text': 'Загруженные аудио файлы', "file_obj": file_obj, "form": form}
        return render(request, 'form_up_audio.html', context)



# удаление аудио файлов из БД
def delete_audio(request, id):
    try:
        audio = AudioFile.obj_audio.get(id=id)
        audio.delete()
        return redirect('form_up_audio')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
