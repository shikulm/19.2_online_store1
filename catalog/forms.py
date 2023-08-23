from django import forms

from catalog.models import Product, Version

class StyleFormMixtin:
    def __init__(self, *args, **kwargs):
        """Стилизация формы"""
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name.lower()!='is_actual':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixtin, forms.ModelForm):
    class Meta:
        model = Product
        fields ="__all__"
        exclude = ('owner',)
        # fields = ('name_product',)
        # exclude = ('changed_at',)

    forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


    def clean_name_product(self):
        '''Проверяет название и описание товара на наличие запрещенных слов'''

        cleaned_data = self.cleaned_data.get('name_product')
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Название продукта содержит запрещенные слова')
        return cleaned_data

    def clean_description(self):
        '''Проверяет название и описание товара на наличие запрещенных слов'''

        cleaned_data = self.cleaned_data.get('description')
        for word in self.forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Описание продукта содержит запрещенные слова')
        return cleaned_data


class VersionForm(StyleFormMixtin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        

        



