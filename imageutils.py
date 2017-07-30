from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from os import path
from os import mkdir
import platform

class ImageCaptioner():
    def __init__(self, viewWindowSize=(1024,768), captionPath="Captions"):
        # Class settings
        self.captionPath = captionPath
        self.viewWindowSize = viewWindowSize

        # Member fields
        self.image = None
        self.filename = None
        self.caption = None
        self.imageWithCaption = None


    def loadImage(self, filename):
        print "Loading", path.basename(filename), "..."
        try:
            self.image = Image.open(filename)
        except:
            print " | Error: Could not load."
            return False

        self.filename = filename
        return self.processImage()

    def showImage(self):
        if self.image:
            resizeToFit(self.image, self.viewWindowSize).show()

    def showCaption(self):
        if self.imageWithCaption:
            resizeToFit(self.imageWithCaption, self.viewWindowSize).show()

    def processImage(self):
        if not self.image:
            return False

        print "Processing", '"' + self.filename + '"'
        self.caption = path.splitext(path.basename(self.filename))[0]
        #Split the caption at semi-colons
        self.caption = "\n".join([line.strip() for line in self.caption.split(";")])
        print " | Caption:", self.caption
        self.imageWithCaption = addCaptionToImage(self.image, self.caption)
        return True

    def saveCaption(self):
        #Create the out path
        outDir, outFilename = path.split(self.filename)
        outDir = path.join(outDir, self.captionPath)
        outPath = path.join(outDir, outFilename)
        print " | Saving to", '"' + outPath + '"'

        if not path.exists(outDir):
            print " | Creating directory", outPath
            mkdir(outDir)

        #Save the file
        if path.exists(outPath):
            print " | Overwriting file!"
        self.imageWithCaption.save(outPath)



def resizeToFit(image, size):
    w,h = image.size
    outW, outH = size
    outImage = image
    if w > outW or h > outH:
        scale = min (outW / float(w), outH / float(h))
        scaleSize = (int(scale * w), int(scale * h))
        outImage = image.resize(scaleSize)
    return outImage

def addCaptionToImage(image, caption, margin=10):
    w,h = image.size
    #Figure out how much space the caption needs
    fontSize = max(h / 36, 10)
    if platform.system() == "Linux":
        font = ImageFont.truetype("LiberationSans-Regular.ttf", fontSize)
    elif platform.system() == "Windows":
        font = ImageFont.truetype("arial.ttf", fontSize)

    textSize = font.getsize(caption)

    # Add black border for the caption
    numLines = len(caption.split("\n"))
    newHeight = h + 2 * margin + textSize[1] * numLines
    newWidth = max (w, textSize[0])
    captionImg = Image.new("RGB", (newWidth ,newHeight,))
    pasteBox = (0,0, w, h)
    captionImg.paste(image, pasteBox)

    #Write the caption
    draw = ImageDraw.Draw(captionImg)
    textPos = (margin, h + margin)
    draw.text(textPos, caption, font=font)

    return captionImg
