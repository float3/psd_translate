import re

from google_trans_new import google_translator

# destination language
lang = "en"  # change this line to adjust output language

# source language
jp = "[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf]+"

cn = "[\u3400-\u4db5\u6300-\u77ff\u7800-\u8cff\u8d00-\u9fcc\u2e80-\u2fd5\u3190-\u319f\u3400-\u4dbf\u4e00-\u9fcc\uf900-\ufaad]+"
# Chinese Unicode Extension characters these aren't included because I don't know how to use them, they are just here for safekeeping
# cnExt = u'[\u20000-\u215FF\u21600-\u230FF\u23100-\u245FF\u24600-\u260FF\u26100-\u275FF\u27600-\u290FF\u29100-\u2A6DF\u2A700-\u2B734\u2B740-\u2B81D]+'

kr = "[\uac00-\ud7a3]+"

regex = "[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u3400-\u4dbf\u3400-\u4db5\u6300-\u77ff\u7800-\u8cff\u8d00-\u9fcc\u2e80-\u2fd5\u3190-\u319f\u3400-\u4dbf\u4e00-\u9fcc\uf900-\ufaad\uac00-\ud7a3]+"

translator = google_translator()
with open("tests/test1.txt", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if len(re.findall(regex, line)) > 0:
            print(translator.translate(line, lang))
        else:
            print(line)
