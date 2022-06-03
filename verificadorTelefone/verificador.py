import numbers
import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o número de telefone no formato +55 (DDD) XXXXX-XXXX: ')
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))