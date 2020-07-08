#!/usr/bin/env python3

import sys
from core import colors

errorstr = "\033[1;31m[-]\033[0m "
infostr = "\033[1;34m[*]\033[0m "
warningstr = "\033[1;33m[!]\033[0m "
successstr = "\033[1;32m[+]\033[0m "
informstr = "\033[1;77m[i]\033[0m "

def printError(message, start="", end="\n"):
	sys.stdout.write(errorstr+message+end)

def printWarning(message, start="", end="\n"):
	sys.stdout.write(start+warningstr+message+end)

def printInfo(message, start="", end="\n"):
	sys.stdout.write(start+infostr+message+end)

def printSuccess(message, start="", end="\n"):
	sys.stdout.write(start+successstr+message+end)

def printInform(message, start="", end="\n"):
	sys.stdout.write(start+informstr+message+end)