import urllib.request
import json
from selenium import webdriver
import time
import pip
def look_for_new_video():
  api_key = "AIzaSyDyvvjmsbKEni1i12o71_cwnrDhbluSlQg"
  channel_id = "UCmSp4bDxS9R0jpeZEvkut2g"
  base_video_url = 'https://www.youtube.com/watch?v='
  base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
  url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(api_key, channel_id)
  inp = urllib.request.urlopen(url)
  resp = json.load(inp)
  vidID = resp['items'][0]['id']['videoId']
  with open('videoid.json', 'r') as json_file:
    data = json.load(json_file)
    if data['videoId'] != vidID:
      driver = webdriver.Chrome()
      driver.get(base_video_url + vidID)
      video_exists = True
  if video_exists:
    with open('videoid.json', 'w') as json_file:
      data = {'videoId' : vidID}
      json.dump(data, json_file)
try:
  while True:
    look_for_new_video()
    time.sleep(10)
except KeyboardInterrupt:
  print('Stopping')