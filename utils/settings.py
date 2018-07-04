from os.path import abspath, dirname, join
import os

PROJ_DIR = join(abspath(dirname(__file__)), '..')
DATA_DIR = join(PROJ_DIR, 'data')
OUT_DIR = join(PROJ_DIR, 'out')
EMB_DIR = join(DATA_DIR, 'emb')
GLOBAL_DIR = join(DATA_DIR, 'global')
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(EMB_DIR, exist_ok=True)
