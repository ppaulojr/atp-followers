from twython import Twython
import datetime
print datetime.datetime.now()
players = ["fabiofogna",
          "richardgasquet1",
          "JohnIsner",
          "keinishikori",
          "andy_murray",
          "milosraonic",
          "GrigorDimitrov",
          "delpotrojuan",
          "DavidFerrer87",
          "tomasberdych",
          "stanwawrinka",
          "RafaelNadal",
          "rogerfederer",
          "DjokerNole"]
APIKEY = "REGISTER_AN_API_KEY"
APISEC = "GRAB_YOUR_API_SECRET"
twitter = Twython(APIKEY,APISEC)
for p in players:
     followers = twitter.show_user(screen_name = p)
     print (p,followers['followers_count'])
