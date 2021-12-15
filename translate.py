import re
import sys

from external_tools.google_trans_new.google_trans_new import google_translator
from external_tools.psd_tools import PSDImage

# usage: Python translate.py [input_file_path1] [input_file_path2] ...
#
# if a [input_file_path] doesn't end in .psd it will be ignored
# you can specify as many as you want

if len(sys.argv) < 2:
    print('No input file specified.')
    input()
    sys.exit()


regex = u'[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]+'

translator = google_translator()

lang = 'en'  # change this line to adjust output language

for i in sys.argv:

    if i.endswith(".psd"):

        psd = PSDImage.open(i)

        for layer in psd:
            if len(re.findall(regex, layer.name)) > 0:
                layer.name = translator.translate(layer.name, lang)

            if layer.is_group():
                for childLayer in layer:
                    if len(re.findall(regex, childLayer.name)) > 0:
                        childLayer.name = translator.translate(
                            childLayer.name, lang)

        psd.save(i)
