#!/usr/bin/python

#
# Verlihub Python Plugin v.1.0
#
# Created by Aayush Ahuja, N Hari Prasad
#
#
# Script to give imdb info on movie/series in DC++ hubchat
# Currently doesnt handle foreign language characters
#

import vh, sys, re, string, random,httplib,json

# Not able to parse french characters - Eg: dexter
def imdbdata(name,nick):
	h = httplib.HTTPConnection("www.omdbapi.com")
	h.request("GET","/?t="+name+"&r=json")
	jdata = h.getresponse()
	data = json.load(jdata)
	
	#vh.usermc(data["Actors"],nick)
	neededinfo = ["Title", "Year", "Genre", "Actors", "Plot", "imdbRating"]
	
	if data["Response"] == "False":
		return "\nNot found. For getting imdb info use +imdb <movie/series name> \n"
	else:
		#vh.usermc("Entered",nick)
		output = "\n"
		for i in neededinfo:
			output = output + i + ": " + str(data[i]) + "\n"
		return str(output)
	
def OnUserCommand (nick, data):
	d = data.split()
	if d[0] == "+imdb":
		# vh.usermc(' '.join(d[1:]),nick)
		data = imdbdata('%20'.join(d[1:]),nick)
		vh.usermc(str(data),nick)
		return 0
	elif d[0] == "+help" and d[1] == "imdb":
		vh.usermc("\nFor getting imdb info use +imdb <movie/series name> \n",nick)
		return 0
		
