from django.forms import Form, CharField, TextInput


class SearchBarForm(Form):
    search = CharField(
        widget=TextInput(
            attrs={
                "type": "search",
                "name": "search",
                "class": "form-control mr-sm-2 mx-1",
                "id": "search",
                "placeholder": "Realizar búsqueda",
                "aria-label": "Search"
            }
        )
    )

    class Meta:
        fields = ('search',)
