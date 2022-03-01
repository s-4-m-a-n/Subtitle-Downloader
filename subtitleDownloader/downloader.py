from requests import exceptions
from subsceneAPI import subtitle
from tkinter import Tk
from tkinter import filedialog
from zipfile import ZipFile
from os import mkdir, remove, path, environ
from re import sub, split
from requests import get
from sys import exit

class Downloader:

    def __init__(self) -> None:
        self.pwd = environ['PWD']

    def selectMovie(self):
        root = Tk()
        root.title('subtitle downloader')
        root.withdraw()
        path = filedialog.askopenfilename()
        if path:
            path = path.normpath(path)
        return path

    def downloadFile(self, title:str, listData:list, save_path=None):
        """this method download and save subtitles"""
        scorelist = self.__likenessChecker(listData, title)
        if save_path is None:
            save_path = self.pwd
        for _ in listData:
            try:
                highestScoreIndex = scorelist.index(max(scorelist))
            except Exception:
                print(' oops !! No result found !! \n  ')
                exit(1)
            else:
                del scorelist[highestScoreIndex]
                subtitle_name, link = listData[highestScoreIndex]
                del listData[highestScoreIndex]
                print(f"\nLink :\n{link}")
                download_status, zip_path = self.getSubtitleZIP(link, save_path, subtitle_name)
                print(f"\n**** Download {'successful (:' if download_status else 'failed ):'} ****\n")
                if not download_status:
                    continue
                extract_status = self.extractSubtitleZIP(zip_path)
                print(f"\n**** Extraction {'successful (:' if extract_status else 'failed ):'} ****\n")

    def __likenessChecker(self, listData:list, name:str):
        likeness = [self.__getScore(item[0], name) for item in listData]
        return likeness

    def __Normalization(self, string:str):
        """string normilazition, removes spaces and dots and returns the list of the words of the string"""
        string = sub('[\\s]+|-', '.', string.lower())
        return split('[\\.]+', string)

    def __getScore(self, item:str, name:str):
        """returns the number of common words between the subtitle name and file name of the movie"""
        availableName = self.__Normalization(item)
        searchedName = self.__Normalization(name)
        commonElements = set(availableName).intersection(set(searchedName))
        return len(commonElements)

    def getSubtitleZIP(self,link:str,save_path:str,subtitle_name:str):
        '''download subtitle from links and save that as a zip file into save_path variable'''
        try:
            response = get(link)
            zipFileName = subtitle_name.strip() + '.zip'
            zip_path= path.join(path.abspath(save_path),zipFileName)
    
            with open(zip_path,"wb") as downloadFile:
                downloadFile.write(response.content)
            return (True,zip_path)
        except:
            return (False,'')


    def extractSubtitleZIP(self,zip_path:str):
        '''create a directory and extract subtitles into that'''
        zip_name = path.splitext(path.basename(zip_path))[0]
        zip_dir = path.dirname(zip_path)
        subtitle_directory_path = zip_dir + '/' + zip_name + '-directory-'
        try:
            with ZipFile(zip_path,'r') as zipfile:
                if not path.isdir(subtitle_directory_path):
                    mkdir(subtitle_directory_path)
                print("Extracting zip file ...\nPlease wait...\n")
                zipfile.extractall(subtitle_directory_path)
                print(f'Subtitles extracted in {subtitle_directory_path}')
            return True
        except:
            return False
        finally:
            remove(zip_path)

def main(title:str, year:str='', language:str='english', resolution:str='all', limit:str=1, path_to_save:str=None):
    """do some works for download subtitle"""
    downloader = Downloader()
    if not title:
        print("\n'title' cannot be empty, so select movie file in window will that opens...")
        movie_path = downloader.selectMovie()
        if not movie_path:
            error = 'Error:\n\tyou must be select a title for search for subtitle.\n\tyou can do that with:\n\tuse "-t" option like -> "-t <you-title-considering>"\n\tor\n\tselect movie file in window will that opens.\n\tfor this work restart program and do not pay attention to \'-t\',leave it alone.'
            print(error)
            exit(1)
        title = path.splitext(path.basename(movie_path))
    try:
        subtitleList = subtitle.search(title=title,
          year=year,
          language=language,
          limit=limit).ZIPlinks
    except:
        raise exceptions.ConnectionError('Please check your internet connection and try again...')
    else:
        if resolution != 'all':
            subtitleList = [sub for sub in subtitleList if resolution in sub[0]]
        downloader.downloadFile(title, subtitleList, path_to_save)


if __name__ == '__main__':
    main(title='spider-man', year='2002', language='persian', limit=20, resolution='1080p', path_to_save='/home/me/sub')
