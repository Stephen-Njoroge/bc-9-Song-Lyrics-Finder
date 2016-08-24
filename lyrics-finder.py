import urllib.request, urllib.error, urllib.parse
import json
import socket
import musixmatch
from tabulate import tabulate
apikey_musixmatch = "0f608f8ccf875fcdd9b26cb6d0da8284"

apiurl_musixmatch = 'http://api.musixmatch.com/ws/1.1/'

def find_my_song(query_name):
	'''
	This function receives a users querry be it an artist, track_name or words in the
	songs database and returns songs that matches with the querry accompanied by a 
	unique ID and Artist Name.
	'''

	querystring = (apiurl_musixmatch + "track.search?q=" + (urllib.parse.quote(query_name)) + "&apikey=" + apikey_musixmatch + "&format=plain" + "&f_has_lyrics=1")

	request = urllib.request.Request(querystring)

	request.add_header("Authorization", "Bearer " + apikey_musixmatch)

	'''
	Must include user agent of some sort, otherwise 403 returned
	It is thus we add a user agent of some sort.
	'''

	request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu)libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")

	try:

		response = urllib.request.urlopen(request, timeout=3600) #timeout set to 3600 seconds

		raw = response.read()

	except socket.timeout:

		print("Timeout raised and caught")

	json_obj = json.loads(raw.decode('utf-8'))
	#print (json_obj)

	body = json_obj["message"]["body"]["track_list"]
	#print (body)
	'''
	A reminder on how to access track_list objects >>>[0]["track"]["track_id"] or ["track_name"]
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

def get_lyrics(track_id):
	querystring = (apiurl_musixmatch + "track.lyrics.get?track_id=" + (urllib.parse.quote(track_id)) + "&apikey=" + apikey_musixmatch + "&format=json" + "&f_has_lyrics=1")

	request = urllib.request.Request(querystring)

	request.add_header("Authorization", "Bearer " + apikey_musixmatch)

	'''
	Must include user agent of some sort, otherwise 403 returned
	It is thus we add a user agent of some sort.
	'''

	request.add_header("User-Agent", "curl/7.9.8 (i686-pc-linux-gnu)libcurl 7.9.8 (OpenSSL 0.9.6b) (ipv6 enabled)")

	try:

		response = urllib.request.urlopen(request, timeout=3600) #timeout set to 3600 seconds

		raw = response.read()

	except socket.timeout:

		print("Timeout raised and caught")

	json_obj = json.loads(raw.decode('utf-8'))
	#print (json_obj)

	body = json_obj["message"]["body"]["lyrics"]["lyrics_body"]
	copyright = json_obj["message"]["body"]["lyrics"]["lyrics_copyright"]
	lyrics = (body + "\n\n" +copyright)
	return lyrics
print("="*70)
track_id = input("Paste your Song's Track ID to get lyrics: ")
print("="*50)
print ("Enjoy Your Tune")
print("="*40)
print (get_lyrics(track_id))