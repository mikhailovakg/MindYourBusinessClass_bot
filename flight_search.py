from amadeus import Client, ResponseError
from config import AMADEUS_API_KEY, AMADEUS_API_SECRET

amadeus = Client(
    client_id=AMADEUS_API_KEY,
    client_secret=AMADEUS_API_SECRET
)

def search_flights(origin, destination, date):
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=1,
            travelClass='BUSINESS',
            currencyCode='USD',
            max=3
        )

        results = []
        for offer in response.data:
            price = offer["price"]["total"]
            itinerary = offer["itineraries"][0]["segments"]
            segments_info = []
            for seg in itinerary:
                dep = seg['departure']['iataCode']
                arr = seg['arrival']['iataCode']
                carrier = seg['carrierCode']
                segments_info.append(f"{carrier} {dep}→{arr}")
            segments = " ➔ ".join(segments_info)
            departure = itinerary[0]["departure"]["at"][:16].replace("T", " ")
            results.append(f" ${price} | {segments} | {departure}")
        return results or ["No flights found."]
    except ResponseError as error:
        return [f"API error: {error}"]
