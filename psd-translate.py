import re
import os
import sys
from external_tools.google_trans_new.google_trans_new import google_translator
from external_tools.psd_tools import PSDImage
from os import listdir
from os.path import isfile, join
# usage: Python translate.py [input_file_path1] [input_file_path2] ...
#
# if a [input_file_path] doesn't end in .psd it will be ignored
# you can specify as many as you want

regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+'
translator = google_translator()
lang = 'en'  # change this line to adjust output language

if len(sys.argv) > 2:
    for i in sys.argv:
        if i.endswith(".psd"):

            psd = PSDImage.open(i)
            print(i + " opened")

            for layer in psd:
                if len(re.findall(regex, layer.name)) > 0:
                    layer.name = translator.translate(layer.name, lang)

                if layer.is_group():
                    for childLayer in layer:
                        if len(re.findall(regex, childLayer.name)) > 0:
                            childLayer.name = translator.translate(
                                childLayer.name, lang)

            psd.save(i)
            print(i + " saved")

else:

    print('No input file specified.')
    print('translating all .psd files in directory.')
    dir = os.getcwd()
    print(dir)
    onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]

    for i in onlyfiles:
        if i.endswith(".psd"):

            psd = PSDImage.open(i)
            print(i + " opened")
            
            for layer in psd:
                if len(re.findall(regex, layer.name)) > 0:
                    layer.name = translator.translate(layer.name, lang)

                if layer.is_group():
                    for childLayer in layer:
                        if len(re.findall(regex, childLayer.name)) > 0:
                            childLayer.name = translator.translate(
                                childLayer.name, lang)

            psd.save(i)
            print(i + " saved")