from phones import settings
from twilio.rest import TwilioLookupsClient


def parse_row(person):
    if person.type is None or person.type == "":
        account_sid = settings.ACCOUNT_SID
        auth_token = settings.AUTH_TOKEN
        client = TwilioLookupsClient(account_sid, auth_token)
        number_one = False
        number_two = False

        if person.phone_one != "":
            try:
                number_one = client.phone_numbers.get(person.phone_one, include_carrier_info=True)
            except Exception as e:
                number_one = False
        if person.phone_two != "":
            try:
                number_two = client.phone_numbers.get(person.phone_two, include_carrier_info=True)
            except Exception as e:
                number_two = False

        if number_one:
            person.type = "{0}".format(number_one.carrier['type'])
        if number_two:
            person.type = "{0}; {1}".format(person.type, number_two.carrier['type'])
        # time.sleep(1)
        person.save()


def parse_data_list(queryset):
    for person in queryset:
        parse_row(person)

    return queryset
