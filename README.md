# Image Metadata Toolkit
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- [About](#about)
- [Getting started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Environment Variables](#environment-variables)
- [Running locally](#running-locally)
  * [Keyword Generator](#keyword-generator)
  * [Image Meta Tagger](#image-meta-tagger)
  * [Image Format Converter](#image-format-converter)
  * [Image Describer](#image-describer)
  * [Image Keyword Recognizer](#image-keyword-recognizer)
- [License](#license)

## About
Welcome to the *Image Metadata Toolkit*! This project is a collection of tools that allow users to edit and manipulate image metadata. With these tools, users can generate keywords for their images, attach those keywords to the EXIF metadata, and even convert between different image formats.

**Technologies**\
This project utilizes a combination of *Python* and *JavaScript* as its primary technologies. In addition to these core technologies, we also integrated the Microsoft Azure API and the Adobe Stock API to enhance the functionality and capabilities of the project. 

**Challenges**\
During the development of this project, we encountered several challenges. One such challenge was that EXIF data is stored in the metadata of an image file, and certain operating systems or software programs do not support the editing or modification of metadata. This led to conflicts and errors when attempting to import images whose EXIF data had been edited.

Additionally, it's worth noting that some image file formats do not support the storage of EXIF data. In these cases, it was not possible to edit the EXIF data of an image, regardless of the operating system or software being used.

## Toolkit

### Keyword Generator

### Image Meta Tagger

### Image Format Converter

### Image Describer


## Getting started

### Prerequisites
You need to have a machine with [Python](https://www.python.org/) > 3.10.6 and [Node.js](https://nodejs.org/en/) > 18.12.1.
```
$ python -V
Python 3.10.6

$ node -v
v18.12.1
```
You will also need to setup the following:
* [Adobe Stock API](https://developer.adobe.com/stock/docs/getting-started/): This API is used by KeywordGenerator.js to generate keyword lists.
* [Microsoft Azure Cognitive Service](https://learn.microsoft.com/en-us/azure/cognitive-services/cognitive-services-apis-create-account?tabs=multiservice%2Canomaly-detector%2Clanguage-service%2Ccomputer-vision%2Cwindows): This API is used by ImageDescriber.py to describe images with AI.

To install the packages used by Python and JavaScript, run the following commands using [PyPi](https://pypi.org/) and [npm](https://www.npmjs.com/).
```
pip install azure-cognitiveservices-vision-computervision msrest Pillow exif python-dotenv
```
```
npm i random-words request dotenv
```

### Environment Variables

## Running locally


## License
MIT License

Copyright (c) 2023 Henrik Mårtensson Etverk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.