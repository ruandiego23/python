

import urllib.request
import json


def manipuleJSON():
    address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen(address)
    if (webURL.getcode() == 200):
        data = webURL.read()
        oJSON = json.loads(data)

        count = oJSON["metadata"]["count"]
        print("Contage: " + str(count))

        for local in oJSON["features"]:
            if local["properties"]["place"] == "167 km SSE of Sand Point, Alaska":
                print("****Encontrado registro especial****")
            else:
                print(local["properties"]["place"])


manipuleJSON()

