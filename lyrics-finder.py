import urllib.request, urllib.error, urllib.parse
import json
import socket
from Auth import apikey_musixmatch
from tabulate import tabulate

apiurl_musixmatch = 'http://api.musixmatch.com/ws/1.1/'

def find_my_song(query_name):
	'''
	This function receives a users querry be it an artist, track_name or words in the
	songs database and returns songs that matches with the querry accompanied by a 
	unique ID and Artist Name.

	'''

	querystring = (("{0} track.search?q={1} &apikey={2} &format=json&f_has_lyrics=1") 

		.format(apiurl_musixmatch, urllib.parse.quote(query_name), apikey_musixmatch))

	request = urllib.request.Request(querystring)

	request.add_header("Authorization", "Bearer " + apikey_musixmatch)

	'''
	Must include user agent of some sort, otherwise 403 returned
	It is thus we add a user agent of some sort.
	'''

	request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu)"\

		"libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")

	try:

		response = urllib.request.urlopen(request, timeout=30) #timeout set to 30 seconds

		raw = response.read()

	except socket.timeout:

		print("Timeout raised and caught")

	json_obj = json.loads(raw.decode('utf-8'))

	body = json_obj["message"]["body"]["track_list"]

	'''

	A reminder on how to access track_list objects >>>[0]["track"]["track_id"] #["track_name"]
	>>>>>
	print (len(body)) Testing Why The Code only printed 10 objects, I found out the trial version
	only allowed for 10 objects per search.

	'''

	i = 0

	songs_data = [] #Empty list to use with tabulate for proper display of content

	while i < len(body):

		song_data = [] #A nested list to suit the working of tabulate

		songs = body[i]

		track_id = (songs["track"]["track_id"]) 
		
		'''
		This is the Unique Track Id for every particular song, It will
		Be necessary when searching for a songs lyrics.

		'''

		track_name = (songs["track"]["track_name"])

		artist_name = (songs["track"]["artist_name"])

		i += 1

		song_data.append(track_id)

		song_data.append(track_name)

		song_data.append(artist_name)

		songs_data.append(song_data)

	return tabulate(songs_data, headers=["Track ID", "Track Name", "Artist"]) 
	#Returns Data in A Tabular Way

query_name = input("Search Your Song Here: ") #prompts user to input their querryname

if query_name == "":

	print ('"Sorry, You did not input a search parameter!"')

else:

	print(find_my_song(query_name))
