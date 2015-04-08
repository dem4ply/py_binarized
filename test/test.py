import cv2
import numpy as np

def convert_grf( img ):
	rows = len( img )
	tmp = img[0]
	for i in range( 1, rows ):
		tmp = np.concatenate( [tmp, img[i]] )
	l = len( tmp )
	r = l % 8
	if r != 0:
		tmp = np.concatenate( tmp, np.zeros( r ) )
	r = l / 8;
	tmp = np.split( tmp, r )
	result = ""
	for x in tmp:
		byte = 0
		for y in x:
			if y != 255:
				byte <<= 1
				byte += 1
		h = hex(byte)[2:]
		if len( h ) == 1:
			h = '0' + h
		result += h
	return result


lenna_png = cv2.imread( 'Lenna.png' )
lenna_jpg = cv2.imread( 'Lenna.jpg' )

lenna_png = cv2.medianBlur( lenna_png, 5 )
lenna_jpg = cv2.medianBlur( lenna_jpg, 5 )

lenna_png = cv2.cvtColor( lenna_png, cv2.COLOR_BGR2GRAY )
lenna_jpg = cv2.cvtColor( lenna_jpg, cv2.COLOR_BGR2GRAY )

lenna_png = cv2.adaptiveThreshold( lenna_png, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2 )
lenna_jpg = cv2.adaptiveThreshold( lenna_jpg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2 )

write = cv2.imwrite( 'lenna_b.png', lenna_png )
if write:
	print "ok png"
else:
	print "no escribio la imagen en png"

write = cv2.imwrite( 'lenna_b.jpg', lenna_png )
if write:
	print "ok jpg"
else:
	print "no escribio la imagen en jpg"

grf = convert_grf( lenna_png )
print len( grf )
print grf.upper()
print "______________________"
print "______________________"
print "______________________"
print "______________________"
print "______________________"
grf = convert_grf( lenna_jpg )
print len( grf )
print grf.upper()
