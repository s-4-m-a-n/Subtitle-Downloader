from subsceneAPI import subtitle
import tkinter as tk
from tkinter import filedialog
from zipfile import ZipFile
import os
import re
import requests




class downloader:

	def selectMovie(self):
		root = tk.Tk()
		root.title("subtitle downloader")
		root.withdraw()
		return os.path.normpath(filedialog.askopenfilename())


	def downloadFile(self,path,listData,name,limit): ## main ## limit < 6
		scorelist =self.__likenessChecker(listData,name)
		for i in range(int(limit)):
			
			highestScoreIndex = scorelist.index(max(scorelist))
	   
			scorelist[highestScoreIndex] = -1 ## replacing greaterScore by negative value in the scorelist so that second highest index will be the highest one for next iteration
			link = listData[highestScoreIndex][1]
			self.getZIPfile(link,path)
			print(link)
			print("download successful..............")



	def __likenessChecker(self,listData,name):
		likeness = [ self.__getScore(item[0],name) for item in listData ] 
		return likeness  


	def __Normalization(self,string): ## string normilazition, removes spaces and dots and returns the list of the words of the string  
		string = re.sub("[\s]+|-",'.',string.lower())
		return re.split("[\.]+",string) #return list 

	def __getScore(self,item,name): ## returns the number of common words between the subtitle name  and file name of the movie  
		availableName = self.__Normalization(item)
		searchedName = self.__Normalization(name)
		
		commonElements = (set(availableName)).intersection(set(searchedName))
		return len(commonElements)


	def getZIPfile(self,downloadlink,dirName):
		response = requests.get(downloadlink)
		zipFileName = "temp.zip"
		fullName= os.path.join(os.path.abspath(dirName),zipFileName)
		
		with open(fullName,"wb") as downloadFile:
				downloadFile.write(response.content)
	### extract downloaded file:       
		with ZipFile(fullName,"r") as file:
			file.printdir()
			print("\nExtracting zip file ............(!! please wait !!)\n")
			file.extractall(os.path.dirname(fullName))
			print("\n Extraction successfull ........ \n****!!!! enjoy the movie , have fun  !!!****\n ")
		os.remove(fullName)    



def main(title,year='',language="english",limit=1):
	try:
		if title == None:
			raise Exception(" 'title' cannot be blank ")
	
	except ValueError as e :
		print("value Error :" + repr(e))
	

	obj = downloader()
	path = obj.selectMovie() #return file path , on cancel returns '.'

	if path != '.':
		fileName = os.path.splitext(os.path.basename(path))[0] #video title
		dirName = os.path.dirname(path) # directory name 

		subtitleList = subtitle.search(title=title,year=year,language=language,limit='all')
		linklist = subtitleList.ZIPlinks  # list of all the available subtitle along with download links

		obj.downloadFile(dirName,linklist,fileName,limit)

	else:
		print("!! closing subtitle downloader!!")

# 	# print(subtitleList.ZIPlinks) ## convert subtitle object into a python list


if __name__ == "__main__":
	main(title="R-point")
