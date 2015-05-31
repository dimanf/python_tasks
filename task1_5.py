#!/usr/bin/python

import argparse

class CustomException(Exception):
    pass

if __name__ == '__main__':
	import os
	import sys
	import datetime
	import getpass

	from os import listdir
	from os.path import isfile, join

	parser = argparse.ArgumentParser()
	parser.add_argument('-t', '--datetime', dest='datetime', action='store_true', help='Datetime now')
	parser.add_argument('-d', '--date' , dest='date', action='store_true', help='Date now')
	parser.add_argument('-u', '--uname' , dest='user_name', action='store_true', help='User name')
	parser.add_argument('-v', '--version' , dest='version', action='store_true', help='Python version')
	parser.add_argument('-l', '--tree' , dest='tree', action='store_true', help='Tree catalog')

	args = parser.parse_args()

	if args.datetime:
		print datetime.datetime.now()
	if args.date:
		print datetime.date.today()
	if args.user_name:
		print getpass.getuser()
	if args.version:
		print sys.version
	if args.tree:
		CURRENT_DIR = os.path.abspath(os.path.curdir)		
		print [ file_item for file_item in listdir(CURRENT_DIR) if isfile(join(CURRENT_DIR, file_item))]


