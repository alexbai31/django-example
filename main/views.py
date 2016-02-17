import tablib
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


from main.models import Person
from main.resources import PersonResource


def import_from_file(request):
    file = request.FILES.get('file')

    if file is not None:
        ds = tablib.Dataset()
        ds.csv = open(file.temporary_file_path()).read()

        person_resource = PersonResource()
        result = person_resource.import_data(ds, dry_run=True)

        if not result.has_errors():
            result = person_resource.import_data(ds, dry_run=False)
    else:
        return HttpResponse("Missing file")

    return HttpResponseRedirect("/")


def view_people(request, page=None):
    persons = Person.objects.all()
    request_copy = request.GET.copy()
    order = request.GET.getlist('order')
    q = request.GET.get("q", False)

    if len(order) > 0:
        persons = persons.order_by(order[0])
        if len(order) > 1:
            request_copy.pop('order')
            request_copy.setlist('order', [order[0]])

    if q:
        persons = persons.filter(name__startswith=q)

    paginator = Paginator(persons, 50)  # Show 25 contacts per page

    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        persons = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        persons = paginator.page(paginator.num_pages)

    return render(request, "main.html", context={"persons": persons, "request": request_copy})


def export_to_excel(request, type=None):
    if type is not None:
        resource = PersonResource().export(queryset=Person.objects.filter(type=type))
    else:
        resource = PersonResource().export()

    response = HttpResponse(resource.xls,
                            content_type='application/vnd.ms-excel')

    if type is None:
        response['Content-Disposition'] = 'attachment; filename="all.xls"'
        return response

    return response
