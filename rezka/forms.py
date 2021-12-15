from django import forms

from rezka import parser, models

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('Films', 'Films'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'Films':
            films_data = parser.films_parser()
            for i in films_data:
                models.Films.objects.create(**i)
