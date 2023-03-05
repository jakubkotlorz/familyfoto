from django import forms
from .models import Foto

class FotoAddForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('image', 'title', 'description')

    def clean_image(self):
        image = self.cleaned_data['image']
        valid_extensions = ['jpg', 'jpeg']
        extension = image.name.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('Wrong extension')
        return image

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == '':
            title = self.cleaned_data['image']
        return title
