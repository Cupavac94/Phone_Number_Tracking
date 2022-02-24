#!/usr/bin/python3
import phonenumbers
from test import number
from phonenumbers import geocoder
from phonenumbers import carrier

# Phone number geolocation
ch_number =  phonenumbers.parse(number, "CH") # C for country and H for history
print(geocoder.description_for_number(ch_number, "en"))

# service provider name
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))
