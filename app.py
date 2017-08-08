import os

subtitles = []
movies = []

subtitleFormats = {'srt','txt'}
videoFormats = {'mkv', 'mp4', 'flv','json'}

currDir = os.path.dirname(os.path.abspath(__file__))
# print currDir

# Separating movie files with  subtitles
for filename in os.listdir(currDir):
	print filename
	fileFormat = filename.split('.')[-1]
	if fileFormat in videoFormats:
		movies.append(filename)
	elif fileFormat in subtitleFormats:
		subtitles.append(filename)
	else:
		break;

print movies;
print subtitles;


def renameSub(videos, subtitles):
	for movie in movies:
		mname = movie.split('.')[0]
		mpart = mname.split('_')[-1]
		for subtitle in subtitles:
			spart = subtitle.split('.')[0].split('_')[-1]
			if mpart == spart:
				os.rename(subtitle,mname+'.'+subtitle.split('.')[-1])
				break;


renameSub(movies, subtitles)