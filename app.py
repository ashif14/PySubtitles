import os

subtitles = []
movies = []

subtitleFormats = {'srt'}
videoFormats = {'mkv', 'mp4', 'flv',}

currDir = os.path.dirname(os.path.abspath(__file__))

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

# Rename Module: videos is a collection of videos you have in directory and same for subtitles
def renameSub(videos, subtitles):
	for movie in movies:
		mname = movie.split('.')[0]
		mpart = mname.split('_')[-1]
		for subtitle in subtitles:
			spart = subtitle.split('.')[0].split('_')[-1]
			if mpart == spart:
				os.rename(subtitle,mname+'.'+subtitle.split('.')[-1])
				break;


# Calling renameSub module
renameSub(movies, subtitles)
