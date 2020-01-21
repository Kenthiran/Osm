import os
import sys

for root, dirs, files in os.walk("/var/www/html"):
    for file in files:
        if file.endswith(".pdf"):
            filename = os.path.join(root, file)
            print (file)
            cmdCompress = 'gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dColorImageResolution=150 -sOutputFile=/var/www/html/san/'+file+ ' '+ file

            os.system(cmdCompress)
    break




