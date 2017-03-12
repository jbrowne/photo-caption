import sys
from imageutils import ImageCaptioner
def main(argv):
    allFiles = argv[1:]
    allCaptioners = []

    for idx, filename in enumerate(allFiles):
        imgCaptioner = ImageCaptioner()
        success = imgCaptioner.loadImage(filename)
        if success:
            imgCaptioner.saveCaption()
            allCaptioners.append(imgCaptioner)

if __name__ == "__main__":
    main(sys.argv)