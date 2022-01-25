import os
import re
import sys
from os import listdir
from os.path import isfile, join

from external_tools.google_trans_new.google_trans_new import google_translator
from external_tools.psd_tools.src.psd_tools import PSDImage

# destination language
lang = 'en'  # change this line to adjust output language

# source language
jp = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf]+'

cn = u'[\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD]+'
# Chinese Unicode Extension characters
# these aren't included because I don't know how to use them, they are just here for safekeeping
# cnExt = u'[\u20000-\u215FF\u21600-\u230FF\u23100-\u245FF\u24600-\u260FF\u26100-\u275FF\u27600-\u290FF\u29100-\u2A6DF\u2A700-\u2B734\u2B740-\u2B81D]+'

kr = u'[\uac00-\ud7a3]+'

regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD\uac00-\ud7a3]+'

translator = google_translator()

filetouched = False
layerindent = 0


def printindent(printstr):
    global layerindent

    for x in range(layerindent):
        printstr = '	' + printstr

    print(printstr)


def translate_layer(layer):
    global filetouched
    global layerindent
    layerindent += 1

    if layer.is_group():
        for sublayer in layer:
            translate_layer(sublayer)

    if layer.has_clip_layers():
        for cliplayer in layer._clip_layers:
            translate_layer(cliplayer)

    if len(re.findall(regex, layer.name)) > 0:
        layer.name = translator.translate(layer.name, lang)
        filetouched = True
        printindent('translated layer: ' + layer.name)

    layerindent -= 1


if len(sys.argv) > 1:
    for i in sys.argv:
        if i.endswith(".psd"):

            psd = PSDImage.open(i)
            filetouched = False
            print()
            print(i + " opened")

            for layer in psd:
                translate_layer(layer)

            if filetouched:
                psd.save(i)
                print(i + " saved")

else:
    print('No input file specified.')
    print('translating all .psd files in directory.')
    currentdir = os.getcwd()
    print(currentdir)
    onlyfiles = [f for f in listdir(currentdir) if isfile(join(currentdir, f))]

    for i in onlyfiles:
        if i.endswith(".psd"):

            psd = PSDImage.open(i)
            filetouched = False
            print(i + " opened")

            for layer in psd:
                translate_layer(layer)

            if filetouched:
                psd.save(i)
                print(i + " saved")
                print()
os.system('pause')
