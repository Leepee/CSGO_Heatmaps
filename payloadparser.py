import _thread
import json
import pickle
import csv

import matplotlib.pyplot as plt
import numpy as np
import math
import time

locationNumber = 0
locationDict = dict()

class PayloadParser:
    global locationDict
    @staticmethod
    def parse_payload(payload, gamestate):

        global locationNumber

        # Full data dump for debugging:
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(payload, f, ensure_ascii=False, indent=4)

        dump = json.dumps(payload)
        data = json.loads(dump)

        # print(data)

        # locationNumber = 0


        if data.get("player").get("activity") == "playing":

            for player in data.get('allplayers'):
                location = data.get('allplayers').get(player).get('position').split(', ')
                locationNumber = locationNumber + 1
                with open(data.get('allplayers').get(player).get('name')
                          + '_' + data.get('map').get('name') + '.csv',
                          mode='a', newline='', encoding='utf-8') as locations_file:
                    locations_writer = csv.writer(locations_file, delimiter=',', quotechar='"',
                                                  quoting=csv.QUOTE_MINIMAL)

                    locations_writer.writerow([location[0], location[1]])
                    print(location[0] + location[1])
                    location = None

        # if locationNumber % 100 == 0:
        #     print('Saving File')
        #
        #     with open('locations.csv', mode='a', newline='', encoding='utf-8') as locations_file:
        #         locations_writer = csv.writer(locations_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #
        #         for entry in locationDict:
        #             locations_writer.writerow([locationDict[entry][0], locationDict[entry][1]])
        #             print(entry)
        #
        #     locationDict.clear()

            # with open('saved_dictionary.pkl', 'wb') as f:
            #     pickle.dump(locationDict, f)

