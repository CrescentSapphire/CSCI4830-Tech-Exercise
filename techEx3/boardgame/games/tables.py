from .models import Boardgame
import django_tables2 as tables

class BoardgameTable(tables.Table):
    class Meta:
        model = Boardgame
        fields = ("name", "owner", "type")