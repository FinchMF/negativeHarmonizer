import sys
import mido
from mido import ( Message, MidiFile, MidiTrack )
from math import ( log2, pow ) 
import argparse
import logging

logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout,
)
logger = logging.getLogger('NegHarm-Log')

from negativeHarmonizer.pitch import * 
from negativeHarmonizer.converter import *