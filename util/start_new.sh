#!/bin/bash

python gen_new.py
fname=$(cat tmp.l)
rm tmp.l
subl $fname