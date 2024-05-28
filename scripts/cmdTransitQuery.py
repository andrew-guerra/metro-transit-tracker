from transitAPIQuery import *
import sys

def transitQuery():
    if(len(sys.argv) < 2):
        print("Flag is required")
        return None
    
    flag = sys.argv[1]

    match flag:
        case "-a":
            print(getAgencies())
        case "-r":
            print(getRoutes())
        case "-rid":
            print(getRouteIDFromLabel(sys.argv[2]))
        case "-d":
            print(getDirections(sys.argv[2]))
        case "-s":
            print(getStops(sys.argv[2], sys.argv[3]))
        case "-pc":
            print(getPlaceCodeFromStopDescription(sys.argv[2], sys.argv[3], sys.argv[4]))
        case "-si":
            print(getStopInfo(sys.argv[2]))
        case "-pi":
            print(getPlaceInfo(sys.argv[2], sys.argv[3], sys.argv[4]))
        case "-v":
            print(getVehicles(sys.argv[2]))

if __name__ == "__main__":
    transitQuery()