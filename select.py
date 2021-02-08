import json as JS
import xml.etree.ElementTree as ET
from os import listdir, remove, rename
from PIL import Image

IMAGE_DIR = "DATASET4_2/images"
ANNOT_DIR = "DATASET4_2/annotations"

for annot_name in listdir(ANNOT_DIR):
    file = ANNOT_DIR + "/" + annot_name
    tree = ET.parse(file)
    root = tree.getroot()
    delete = False

    img_path = IMAGE_DIR + "/" + root.find("filename").text
    objs = root.findall('.//object')
    '''if len(objs)==1 and objs[0].find("name").text == "with_mask":
        remove(img_path)
        remove(file)
    elif len(objs) == 2 and objs[0].find("name").text == "with_mask" and objs[1].find("name").text == "with_mask":
        remove(img_path)
        remove(file)'''

    if len(objs) >= 0:
        delete = False
        n = len(objs)
        for i in range(n):
            if objs[i].find("name").text != "mask_weared_incorrect":
                delete = True
        if delete:
            remove(img_path)
            remove(file)
