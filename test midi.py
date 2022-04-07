import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
from copy import deepcopy
from PIL import Image
from midiutil.MidiFile import MIDIFile

from best_match import match
from box import BoundingBox
from staff import Staff
from primitive import Primitive
from bar import Bar

mary = "C:\Users\chuml\PycharmProjects\MusicImage\mary.mid"