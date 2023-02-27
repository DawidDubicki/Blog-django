from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(label="Tytuł", max_length=100)
    text = forms.CharField(label="Treść", widget=forms.Textarea, max_length=500)
    tags = forms.CharField(label="Tagi", max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=150,  widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label='Hasło', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Hasło', 'type': 'password'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label='Nazwa użytkownika', max_length=150,  widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label='Hasło', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Hasło', 'type': 'password'}))
    password_repeat = forms.CharField(label='Powtórz hasło', max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Powtórz hasło', 'type': 'password'}))

