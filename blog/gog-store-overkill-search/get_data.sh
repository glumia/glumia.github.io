# Get games JSON data through GOG API
# See https://gogapidocs.readthedocs.io/en/latest/listing.html for info
# about the API interface


for i in {1..12}; do curl -H "Accept: application/json" -H "Content-Type: application/json" "https://embed.gog.com/games/ajax/filtered?mediaType=game&price=u5&sort=bestselling&page=$i" > games$i.json ; done
