from PIL import Image
import os

for infile in filelist:
	ourfile = os.path.splittext(infile)[0] + '.jpg'
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print "cannot convert", infile

