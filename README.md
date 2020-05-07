# Subtitle Downloader (v 0.1)[:link:](https://github.com/s-4-m-a-n/Subtitle-Downloader/)<br/>

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source-150x25.png?v=103)](https://github.com/s-4-m-a-n) 
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br/>
[![Generic badge](https://img.shields.io/badge/python-3.6+-<COLOR>.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/Pypi-v0.1-<COLOR>.svg)](https://pypi.org/project/subtitleDownloader/)
[![Generic badge](https://img.shields.io/badge/Python-Automation-<COLOR>.svg)](https://pypi.org/project/subtitleDownloader//)

subtitle downloader is a light weighted command line app that allows us to download subtitle from the web-site [subscene](https://www.subscene.com) in a most convenient way. 

## [:small_blue_diamond:](https://github.com/s-4-m-a-n)<ins>How to install<ins> ?
#### Dependencies :
  subtitle downloader requires:
   - python (>=3.6)
   - [subsceneAPI (==0.2)](https://pypi.org/project/subsceneAPI/)
      
***don't worry about dependencies, all you need to do is install python and pip on your system(this is a prerequisite)***

***below given code works in both terminal and cmd***:heavy_check_mark:


run the below given code in the terminal(for linux user) or cmd(for windows user) 
```
  $  pip install subsceneAPI==0.2
```
Now, You are ready to download subtitle in any language for any movie. But first, let's check if the subtitle downloader has been installed properly or not. 
Try:
```
  $  subtitleDownloader -v 
    OR
  $  subtitleDownloader --version

```
For successful installation, the expected output is :
```
      $  subtitleDownloader 0.1
``` 

## <ins>Usage<ins>:
  It can be used as an application software or as a python package.
  All the commands for subscene API can be found using ***help*** flag.
```
  $  subtitleDownloader -h
    OR
  $  subtitleDownloader --help
``` 
  To download a subtitle, run the given code:
 ```
  $  subtitleDownloader -t "<movie's title/name>" -y "<release year>" -lng "language" -l <limit>
    OR
  $  subtitleDownloader --title "<movie's title/name>" --year "<release year>" --language "<language>" --limit <limit>
```
   Here, title and release year is mandatory. And the default value for language is "english" and for limit, it is 1 (the number of different subtitles that are going to be downloaded)
      
once you run the above command with appropirate arguments(ie title,year,language and limit value), a pop-up (file) box will be opened and you have to select a movie whose subtitle you want to have.
That's all, now all you need to do is wait till it is successfully downloaded.

#  TIPS 
I will personally recommend you to download both python and subtitleDownloader in the administrative mode(for windows user) or in the sudo mode(for linux user). so that, you just have to open the cmd or terminal and run the command to download any subtitle.


## Developement:
   Contibuters of all experience levels are warmly welcomed to be the part of this subtitleDownloader community.The community goals are to be helpful,welcoming,effective.
   #### important links:
  - official source code  : [https://github.com/s-4-m-a-n/Subtitle-Downloader/tree/master/subtitleDownloader](https://github.com/s-4-m-a-n/Subtitle-Downloader/tree/master/subtitleDownloader)
  - Download release : [https://pypi.org/project/subtitleDownloader/](https://pypi.org/project/subtitleDownloader/)<br/>
   #### <ins>source code:<ins>
   you can check the latest sources with the command :
   ```bash
          git clone https://github.com/s-4-m-a-n/subscene-API.git
   ```





## LICENSE:
  It is an open source project and is being licensed under MIT LICENSE - [click me](https://github.com/s-4-m-a-n/Subtitle-Downloader/blob/master/LICENSE) to get to the license file for more details.
  ***It is not an official [subscene version : 4.0](https://www.subscene.com/) product.***
  
  
 

[![Facebook](https://img.shields.io/static/v1.svg?label=follow&message=@me&color=9cf&logo=facebook&style=flat&logoColor=white&colorA=informational)](https://www.facebook.com/suman.dhakal.39982) 
[![Twitter](https://img.shields.io/static/v1.svg?label=follow&message=@&color=grey&logo=twitter&style=flat&logoColor=white&colorA=critical)](https://twitter.com/s_4_m_A_N)
      




  
  