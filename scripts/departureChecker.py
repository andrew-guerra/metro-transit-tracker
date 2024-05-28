from transitAPIQuery import *
import datetime

def getDepatures(routeID, directionID, placeName):
    """Retrieves all depatures on the route ID, with direction ID, at place name."""
    placeInfo = getPlaceInfo(routeID, directionID, placeName)

    return placeInfo["departures"]

def getNextDepature(routeID, directionID, placeName):
    """Retrieves the next depatures on the route ID, with direction ID, at place name."""
    depatures = getDepatures(routeID, directionID, placeName)

    return depatures[0]

def getDepatureTime(depature):
    """Returns the datetime depature time for the depature."""
    depatureTimestamp = depature["departure_time"]

    return datetime.datetime.fromtimestamp(depatureTimestamp)

def getDepaturesBeforeTime(depatures, time, delta=0):
    """Returns all depatures in depatures that are before the given time, with depature times within delta
       of time not included."""
    before = []

    for depature in depatures:
        depatureTime = getDepatureTime(depature)
        bufferedDepatureTime = depatureTime + datetime.timedelta(minutes=delta)

        if bufferedDepatureTime < time:
            before.append(depature)
    
    return before