import setuptools

def readme():
    with open("README.md", "r") as fh:
        README = fh.read()
    return README

setuptools.setup(
    name="subtitleDownloader", 
    version="0.1",
    author="Suman Dhakal",
    author_email="dhakalsumn739@gmail.com",
    keywords="python3 pypi packages subscene api easy subtitle downloader application command line app",
    description ="python3 command line subtitle downloader ",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/s-4-m-a-n/subtitle-Downloader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    # packages = ["subscene_API","subscene_API.cli","subscene_API.subtitle"],
    packages = ["subtitleDownloader"],
    include_package_data = True, 
    install_requires=[
                    'beautifulsoup4==4.9.0',
                    'requests==2.23.0',
                    'tkinter==8.6',
                    'subsceneAPI==0.1'
                        ],
    entry_points = {
        'console_scripts':['subtitleDownloader=subtitleDownloader.cli:main']
    }
)