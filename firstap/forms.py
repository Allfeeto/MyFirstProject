from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента' , max_length=20, help_text="Имя не может быть более 20 символов")
    age = forms.IntegerField(label='Возраст клиента' , min_value=0)
    basket = forms.BooleanField(label='Положить товар в корзину?')
    vyb = forms.NullBooleanField(label='Вы зачтете лабораторную работу?')
    email = forms.EmailField(label='Электронная почта')
    RF = forms.RegexField(label='Телефон', regex=r'^\+7\d{10}$')
    url_text = forms.URLField(label='Ссылка на соц сети')
    file_path = forms.FilePathField(label='Выберите файл', path=r"C:\Users\10509\Downloads")
    file = forms.FileField(label='Выберите файл', required=False)
    image = forms.ImageField(label='Выберите изображение', required=False)
    data_field = forms.DateField(label='Выберите дату', input_formats=['%d/%m/%Y'])
    integer_field = forms.IntegerField(label='Выберите целое число', min_value=0)
    choice_field = forms.ChoiceField(label='Выберите целое число', choices=[('1', '1'), ('2', '2'), ('3', '3')])
