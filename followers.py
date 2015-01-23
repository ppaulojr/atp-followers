#!/usr/bin/env python

from twython import Twython
import datetime
print datetime.datetime.now()

# TODO: Update twitter handle of the players
# Wait until the Australian Open Ends, but right now Fognini must go.

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
