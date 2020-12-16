import tweepy
from textstat import flesch_kincaid_grade as fkg
from textstat import flesch_reading_ease as fre
import unicodedata
import numpy as np

"""
Program to generate random coordinates in the contiguous UNited States.
This program will generate a user-specified number of random geographic
coordinates in the contiguous United States, reverse geocode them, then
write them to the specified file.
Example:
    $ python randomcoords.py number_of_points output_file
The following conventions were used to ensure the coordinates were in the
contiguous U.S.
US Geographic Information
Northernmost - (49.384472, -95.153389)
Southernmost - (24.433333, -81.918333)
Easternmost - (44.815278. -65.949722)
Westernmost - (48.164167. -124.733056)
Geographic Center - (39.833333. -98.583333)
"""


import argparse
import os
import random

from pygeocoder import Geocoder, GeocoderError

__version__ = '0.1.0'

NORTHERNMOST = 49.
SOUTHERNMOST = 25.
EASTERNMOST = -66.
WESTERNMOST = -124.

def coord():
    """
    Generate a number of random geographical points and then geocode them.
    :param number_of_points: number of points to generate
    :type number_of_points: int
    :return: list of geographic point tuples
    """

    coordinate_list = []

    geocoder = Geocoder()
    lat = round(random.uniform(SOUTHERNMOST, NORTHERNMOST), 6)
    lng = round(random.uniform(EASTERNMOST, WESTERNMOST), 6)
    return (lat, lng)
    # output_file.write(fullstring.format(gcode.x, gcode.y, gcode.address))     
userDict = {
    "ParkerGames": "2361893610",
    "Donald Trump": "25073877",
    "Aaron Silvera": "942908124373032961",
    "King Grandpa": "1157723407674273792",
    "Hank Green": "61592079"
}

auth = tweepy.OAuthHandler('D0xzAVo6idwxEEmpN6P8i2MN6', 'lgZbw3XS4IN7i1GAyHdoU2w5EzDZFgM401DCCyulYdnCDHWxum')
auth.set_access_token('1302861793732091905-3etPrssiLXkrGtCeqw6SxOzDroilT9', '0lEPeNEZ747qIyvgCGsZDkoH2f8hVJ4mgnorkDRaf1vAO')
api = tweepy.API(auth, wait_on_rate_limit=False)
rng = np.random.default_rng()


range=20
c = coord()
print(c)
place_id = api.reverse_geocode(c[0],c[1],range)[0].id
print(place_id)
tweets = api.search(q="place:%s" % place_id)
print(tweets)
api.update_status("fuck you, @"+tweets[0].user.name)


