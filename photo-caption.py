import sys
import glob
from imageutils import ImageCaptioner

def main(argv):
    if '*' in argv[1]:
        allFiles = glob.glob(argv[1])
    else:
        allFiles = argv[1:]

    for idx, filename in enumerate(allFiles):
        imgCaptioner = ImageCaptioner()
        success = imgCaptioner.loadImage(filename)
        if success:
            imgCaptioner.saveCaption()

if __name__ == "__main__":
    main(sys.argv)