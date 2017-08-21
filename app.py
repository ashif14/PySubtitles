import os
import app #import PySubTime
from collections import OrderedDict

subtitles = []
movies = []

subtitlesDict = {} # Subtitles sorted with duration
videoDict = OrderedDict(sorted(({2:'abc.mp4', 5: 'bcd.mp4', 23: 'def.mp4'}).items()))  # video sorted with duration

subtitleFormats = {'srt'}
videoFormats = {'mkv', 'mp4', 'flv',}


currDir = os.path.dirname(os.path.abspath(__file__))

# Separating movie files with  subtitles
for filename in os.listdir(currDir):
	# print (filename)
	fileFormat = filename.split('.')[-1]
	if fileFormat in videoFormats:
		movies.append(filename)
	elif fileFormat in subtitleFormats:
		srtTime = app.getSubtitleTime(filename)
		subtitlesDict[srtTime] = filename
	else:
		continue;

subtitlesDict = OrderedDict(sorted(subtitlesDict.items())) # Sorted wrt subtitle duration inseconds

subtitles = list((subtitlesDict.values()))
movies = list(videoDict.values())

# print(subtitles)
# print(movies)
# Rename Module: videos is a collection of videos you have in directory and same for subtitles
def renameSub(videos, subtitles):
	i = 0
	for movie in videos:
		mname = movie.split('.')[0]
		os.rename(subtitles[i],mname+'.'+subtitles[i].split('.')[-1])
		i += 1

# Calling renameSub module
renameSub(movies, subtitles)
