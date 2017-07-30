import sys
import os
from os import path

import Tkinter as tk 
import tkFileDialog
from imageutils import ImageCaptioner

def setupTk():
    root = tk.Tk()
    root.withdraw()

def checkDirectory(dir):
    if not path.exists(dir):
        print "|  Error: Directory does not exist"
        return False   
    elif not path.isdir(dir):
        print "|  Error: Path is not a directory"
        return False

    return True

def captionFiles(allFiles):
    print "Captioning", len(allFiles), "files..."
    for idx, filename in enumerate(allFiles):
        imgCaptioner = ImageCaptioner()
        success = imgCaptioner.loadImage(filename)
        if success:
            imgCaptioner.saveCaption()

def main(argv):
    setupTk()

    if len(argv) > 1:
        srcPath = argv[1]
    else:
        srcPath = tkFileDialog.askdirectory()

    srcPath = path.abspath(srcPath)
    print "Using source srcPath:", srcPath
    if checkDirectory(srcPath):
        allFiles = os.listdir(srcPath)
        allFiles = [path.join(srcPath,file) for file in allFiles]
        allFiles = [file for file in allFiles if path.isfile(file)] #Filter out directories
        captionFiles(allFiles)

if __name__ == "__main__":
    main(sys.argv)