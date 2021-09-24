from django.forms.models import BaseInlineFormSet
from django import forms
from django.contrib.auth.models import User
from . import models


# class ProdutoForm(forms.ModelForm):
#   class Meta:
#      model = models.Produto
#     fields = '__all__'


class ProdutoForm(forms.ModelForm):
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usuario = usuario

    class Meta:
        model = models.Produto
        fields = '__all__'
        exclude = ('slug',)


class ProdutoAdminForm(forms.ModelForm):
    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

    class Meta:
        model = models.Variacao
        fields = '__all__'
        exclude = ('produto',)


class VariacaoObrigatoria(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(VariacaoObrigatoria, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form
