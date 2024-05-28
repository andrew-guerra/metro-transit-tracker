import requests

apiURL = "https://svc.metrotransit.org/nextrip"

def generateUrlQuery(queryParams):
    """Generates a api query URL with associated parameters."""
    formatStr = apiURL + "/{}" * len(queryParams)
    
    return formatStr.format(queryParams)

def fetchJson(url):
    """Retrieves response to GET request with query URL."""
    response = requests.get(url)

    if(response.status_code != 200):
        return None
    
    return response.json()

def getAgencies():
    """Retrieves agencies in transit system."""
    return fetchJson("https://svc.metrotransit.org/nextrip/agencies")

def getRoutes():
    """Retrieves routes in transit system."""
    return fetchJson("https://svc.metrotransit.org/nextrip/routes")

def getRouteIDFromLabel(routeLabel):
    """Retrieves route ID based on route label."""
    routes = getRoutes()

    for route in routes:
        if route["route_label"] == routeLabel:
            return route["route_id"]
        
    return None
 
def getDirections(routeID):
    """Retrieves route directions based on route ID."""
    return fetchJson("https://svc.metrotransit.org/nextrip/directions/{}".format(routeID))

def getDirectionIDFromName(routeID, directionName):
    """Retrieves direction ID based on route ID and direction name."""
    directions = getDirections(routeID)

    for directionID in directions:
        if directionID["direction_name"] == directionName:
            return directionID["direction_id"]
        
    return None

def getStops(routeID, directionID):
    """Retrieves stops on route with route ID and direction ID."""
    return fetchJson("https://svc.metrotransit.org/nextrip/stops/{}/{}".format(routeID, directionID))

def getPlaceCodeFromStopDescription(routeID, directionID, stopDescription):
    """Retrieves place code for a stop based on route ID, direction ID, and stop description (stop name)."""
    stops = getStops(routeID, directionID)

    for stop in stops:
        if stop["description"] == stopDescription:
            return stop["place_code"]
    
    return None

def getStopInfo(stopID):
    """Retrieve stop information based on stop ID."""
    return fetchJson("https://svc.metrotransit.org/nextrip/{}".format(stopID))

def getPlaceInfo(routeID, directionID, placeName):
    """Retrieve place information based on route ID, direction ID, and place name."""
    return fetchJson("https://svc.metrotransit.org/nextrip/{}/{}/{}".format(routeID, directionID, placeName))

def getVehicles(routeID):
    """Retrieve vehicle information for all vehicals on route with route ID."""
    return fetchJson("https://svc.metrotransit.org/nextrip/vehicles/{}}".format(routeID))
