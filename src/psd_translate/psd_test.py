import os
import sys
from os import listdir
from os.path import isfile, join

from psd_tools import PSDImage

currentdir = os.getcwd()
print(currentdir)
onlyfiles = [f for f in listdir(currentdir) if isfile(join(currentdir, f))]


def layerdebug(layer):
    if layer.has_clip_layers():
        print(layer.name + " has clip layers")
        for cliplayer in layer.clip_layers:
            layerdebug(cliplayer)

    if layer.has_mask():
        print(layer.name + " has mask")

    # psd-tools only gives has_fill() to the layer types that can carry one,
    # so a Group raises AttributeError on it.
    if hasattr(layer, "has_fill") and layer.has_fill():
        print(layer.name + " has fill")

    if layer.has_effects():
        print(layer.name + " has effects")

    if layer.is_group():
        print(layer.name + " is group")
        for sublayer in layer:
            layerdebug(sublayer)


for i in onlyfiles:
    if i.endswith(".psd"):
        psd = PSDImage.open(i)

        for layer in psd:
            layerdebug(layer)

# Keep the double-click-on-Windows convenience without hanging CI.
if os.name == "nt" and sys.stdin.isatty():
    os.system("pause")
