import argparse
from subtitleDownloader import downloader


def main():
	
	parser = argparse.ArgumentParser(description= "subtitle Downloader")

	parser.add_argument("-v","--version",help="display version",action="store_true")

	parser.add_argument("-t","--title",default=None,type=str.lower,help="enter the movie title")
	parser.add_argument("-y","--year",default=' ',type=str,help="enter the released year")
	parser.add_argument("-lng","--language",type=str.lower,default="english",choices=["english","arabic","albanian","arabic","bengali","turkish","spanish","swedish","thai","slovenian","russian","portuguese","malay","farsi/persian"],help="enter any language from choice, default value='english' " )
	parser.add_argument("-l","--limit",type=str.lower,default="1",help="No of files you want to download , default value = 1")
	args = parser.parse_args()

	if args.version:
		print("subtitle-Downloader 0.1")

	elif args.title != None:
		print("connecting......")
		print("searching for ... ")
		info = {'Title' : args.title ,'Year':args.year,'Language':args.language,'limit':args.limit }
		print("{}".format(info))


		downloader.main(title=args.title,year=args.year,language=args.language,limit=args.limit)

if __name__ == "__main__":
	main()