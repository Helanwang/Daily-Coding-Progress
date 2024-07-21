import phonenumbers
from myphone import number

from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Parse the phone number to get location description
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, 'en')
print(f"Location: {location}")

# Get the carrier name
service_pro = phonenumbers.parse(number)
carrier_name = carrier.name_for_number(service_pro, 'en')
print(f"Carrier: {carrier_name}")

# OpenCage API key`
key = "3da5d526c3ba45ffbd290bffff3f4493"`
geocoder = OpenCageGeocode(key)

# Geocode the location
query = str(location)
results = geocoder.geocode(query)

# Check if results were returned and extract latitude and longitude
if results and len(results) > 0:
    lat = results[0]["geometry"]["lat"]
    lng = results[0]["geometry"]["lng"]
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map with the location
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker(location=[lat, lng], popup=location).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("myMap.html")
else:
    print("Geocoding failed. No results found.")