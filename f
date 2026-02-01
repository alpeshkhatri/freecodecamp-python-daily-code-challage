#!/bin/bash
cd freecodecamp
cp template.py $(date +%Y-%m-%d).py
ls -ltr | tail
cd .. 
code .

echo $(date +%Y-%m-%d)
