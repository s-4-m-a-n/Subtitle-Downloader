import argparse
import downloader


def main():
	
	parser = argparse.ArgumentParser(description= "subtitle Downloader")

	parser.add_argument("-v","--version",help="display version",action="store_true")

	parser.add_argument("-t","--title",default=None,type=str.lower,help="Enter the movie title")
	parser.add_argument("-y","--year",default=' ',type=str,help="Enter the released year")
	parser.add_argument("-lang","--language",type=str.lower,default="english",choices=["english","arabic","albanian","arabic","bengali","turkish","spanish","swedish","thai","slovenian","russian","portuguese","malay","farsi/persian"],help="Enter any language from choices, default value ='english'")
	parser.add_argument("-l","--limit",type=str.lower,default="1",help="No of files you want to download , default value = 1")
	parser.add_argument("-r","--resolution",type=str.lower,default="all",help="Filter subtitles on resolution\nSelect any resolution from choices",choices=['360p','480p','720p','1080p','1440p'])
	parser.add_argument("-p","--path",type=str.lower,default="PWD",help='Select path for save subtitles, default value is current path (PWD)')
	args = parser.parse_args()

	if args.version:
		print("subtitle-Downloader 0.1")

	else:
		#info = {'Title' : args.title ,'Year':args.year,'Language':args.language,'limit':args.limit }
		#print("{}".format(info))
		
		print("Connecting......")
		print(f"Searching for {args.title + '  ' + args.year}")
		print("Please wait...")


		downloader.main(title=args.title,year=args.year,language=args.language,limit=args.limit,resolution=args.resolution,path_to_save=args.path)

if __name__ == "__main__":
	main()