import json
import random
import string


class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    Token = ""
    Name = "Brawler"
    Registered = True
    Thumbnail = 0
    Namecolor = 0
    Region = "CA"
    ContentCreator = "LEGACY"

    Coins = 0
    Gems = 0
    StarPoints = 0
    Trophies = 0
    HighestTrophies = 0
    TrophyRoadTier = 0
    Experience = 0
    Level = 1
    Tokens = 200
    TokensDoubler = 0

    SelectedSkins = {}
    SelectedBrawlers = [0, 0, 0]
    RandomizerSelectedSkins = []
    OwnedPins = list(range(688))
    OwnedThumbnails = [60, 61, 63, 64, 69, 70, 72, 73, 76, 77, 78, 79, 83, 84]
    OwnedBrawlers = {
        0: {'CardID': 0, 'Skins': [29, 52, 122, 158, 194, 195, 319, 320, 321, 358], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 and lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'Registered': self.Registered,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensDoubler': self.TokensDoubler,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
