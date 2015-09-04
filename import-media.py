#!/usr/bin/env python
from optparse import OptionParser
# from sortphotos import sortPhotos

parser = OptionParser()
def main():
    usage = "usage: %prog [options] arg"

    parser.add_option("-a", "--all",
                      action="store_true", dest="all",
                      help="Sort both Pictures and Videos")
    parser.add_option("-p", "--pictures",
                      action="store_true", dest="pictures",
                      help="Sort pictures in ~/Pictures/import folder")
    parser.add_option("-v", "--videos",
                      action="store_true", dest="videos",
                      help="Sort videos in ~/Videos/import folder")

    (options, args) = parser.parse_args()

    if options.pictures:
        print "Importing Pictures..."
        python '~/bin/sortphotos/src/sortphotos.py ~/Pictures/import ~/Pictures/ -r --rename %Y_%m_%d_%H%M%S --ignore-tags EXIF:CreateDate'

    print ("_EOF_")

if __name__ == "__main__":
    main()
# sortphotos = 'python ~/bin/sortphotos/src/sortphotos.py'
# sortpictures = 'sortphotos ~/Pictures/import ~/Pictures/ -r --rename %Y_%m_%d_%H%M%S --ignore-tags EXIF:CreateDate'
# sortvideos = 'sortphotos ~/Videos/import ~/Videos/ -r --rename %Y_%m_%d_%H%M%S --ignore-tags EXIF:CreateDate'

