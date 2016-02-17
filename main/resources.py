from import_export import resources
from main.helpers import parse_row
from main.models import Person


class PersonResource(resources.ModelResource):
    class Meta:
        model = Person