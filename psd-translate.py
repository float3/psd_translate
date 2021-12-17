import re
import os
import sys
from external_tools.google_trans_new.google_trans_new import google_translator
from external_tools.psd_tools import PSDImage
from os import listdir
from os.path import isfile, join

jp = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf]+'

cn = u'[\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD\u20000-\u215FF\u21600-\u230FF\u23100-\u245FF\u24600-\u260FF\u26100-\u275FF\u27600-\u290FF\u29100-\u2A6DF\u2A700-\u2B734\u2B740-\u2B81D]+'

kr = u'[\uac00-\ud7a3]+'

regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf\u3400-\u4DB5\u6300-\u77FF\u7800-\u8CFF\u8D00-\u9FCC\u2e80-\u2fd5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD\uac00-\ud7a3]+' #\u20000-\u215FF\u21600-\u230FF\u23100-\u245FF\u24600-\u260FF\u26100-\u275FF\u27600-\u290FF\u29100-\u2A6DF\u2A700-\u2B734\u2B740-\u2B81D

translator = google_translator()
lang = 'en'  # change this line to adjust output language


def translate_layer(layer):
    
    if len(re.findall(regex, layer.name)) > 0:
        layer.name = translator.translate(layer.name, lang)
        print('    translated layer: ' + layer.name)

    if layer.is_group():
        for sublayer in layer:
            translate_layer(sublayer)

if len(sys.argv) > 2:
    for i in sys.argv:
        if i.endswith(".psd"):

            psd = PSDImage.open(i)
            print(i + " opened")

            for layer in psd:
                translate_layer(layer)

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
                translate_layer(layer)

            psd.save(i)
            print(i + " saved")