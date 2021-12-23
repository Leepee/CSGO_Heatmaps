import json

class PayloadParser:

    @staticmethod
    def parse_payload(payload, gamestate):


        # Full data dump for debugging:
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     json.dump(payload, f, ensure_ascii=False, indent=4)

        dump = json.dumps(payload)
        data = json.loads(dump)

        # print(data)

        if data.get("player").get("activity") == "playing":
            pass

            # Get a load of general data
            # dataDict['Phase'] = data.get('phase_countdowns').get('phase')
            # dataDict['PhaseTimer'] = round(float(data.get('phase_countdowns').get('phase_ends_in')))
            # dataDict['RoundNumber'] = data.get('map').get('round')
            #
            # dataDict['TWins'] = data.get('map').get('team_t').get('score')
            # dataDict['CTWins'] = data.get('map').get('team_ct').get('score')
            #
            # dataDict['bombPhase'] = data.get('bomb').get('state')
            # dataDict['bombTimer'] = data.get('bomb').get('countdown')
            #
            # # Get a load of observed player data
            # dataDict['obsPlayerName'] = data.get('player').get('name')
            # dataDict['obsPlayerHealth'] = data.get('player').get('state').get('health')
            # dataDict['obsPlayerMoney'] = data.get('player').get('state').get('money')
            # dataDict['obsPlayerKills'] = data.get('player').get('match_stats').get('kills')
            # dataDict['obsPlayerDeaths'] = data.get('player').get('match_stats').get('deaths')


