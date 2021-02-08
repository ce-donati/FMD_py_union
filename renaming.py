import xml.etree.ElementTree as ET
from os import listdir, remove, rename

#IMAGE_DIR = "Dataset/test/images"
#ANNOT_DIR = "Dataset/test/annotations"
IMAGE_DIR = "Dataset_7/db_07_full_balanced1/train/images"
ANNOT_DIR = "Dataset_7/db_07_full_balanced1/train/annotations"

index = 0
for filename in listdir(ANNOT_DIR):
    tree = ET.parse(ANNOT_DIR + "/" + filename)
    root = tree.getroot()
    imagename = root.find("filename")

    j = imagename.text.find(".")
    ext = imagename.text[j:]
    if len(ext) < 4:
        ext = ".jpg"

    rename(ANNOT_DIR + "/" + filename, "Dataset_7/db_07_full_balanced/train/annotations" + "/" + str(index) + ".xml")
    rename(IMAGE_DIR + "/" + str(imagename.text), "Dataset_7/db_07_full_balanced/train/images" + "/" + str(index) + ext)

    imagename.text = str(index) + ext
    tree = ET.ElementTree(root)
    tree.write("Dataset_7/db_07_full_balanced/train/annotations" + "/" + str(index) + ".xml")

    index += 1