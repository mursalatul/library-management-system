# Contributing to Library Management System Project

Welcome! We're glad you're interested in contributing to Library Management System. Here are a few guidelines to help you get started. Please take a moment to review this document before submitting any contributions.

## Getting Started
<b>We are assuming the contributer already know about the basics of python virtual environment and git</b>
1. Fork the repository to your GitHub account.
2. Clone the forked repository to your local machine.
   
   `git clone https://github.com/mursalatul/library-management-system.git`
4. Create a python virtual environment. We recommend to use conda environment.

   Makesure you are using python verion 3.7 to 3.9. Upper python versions dont support
   pyqt5.
5. Create a seperated branch `$ git checkout -b new_feature` and make your changes here.
   After adding all your features marge it with master branch and create a pull request.

## Coding Style
* Use OOP style.
* Methods must follow camelCaseStyle
```
def thisIsAMethod():
  pass
```
* Variable name may follow snake_case_style
```
snake_case_style_variable = 1E10
```
* User proper comments, describing what is the code doing. But dont use
  irrelevent or unneunnecessary comments. Using proper comments will help the
  future developers to understand your purpose of the code.
* Include docstring in your method. The following docstring format is recommanded.
```
"""This is a docstring format. Docstring basically describe the purpos of the method,
what type of data it will take, what type of operation it will perform, and what type
of output will generate or return sortly.
Args:
  argument1 (type): short description
  argument1 (type): short description
Returns:
  return type: short description
"""
```
* Dont include any data as inline format or in the class or class file. 
  Use the data directory to store the data and load it from your class.
  It will make the insert/delete/update the date later more easy.
* Try to use build-in methods and packages for performance.
* If its possible then dont install a 3rd party package for a task. Try to create it own.
* Follow the already created directory structure. Here,
  - <b>ui</b>: user interface .ui files created by qt5 designer tool.
  - <b>src</b>: contain all the source codes which make the project live
      - core: handle all the functionality and operations.
      - ui: load the .ui files and create inter connections from ui directory.
  - <b>data</b>: store information for other modules.
* If your changes is about ui then at first try to implement it in qt5 designer.
  If it is impossible to do it in the designer then do it with row code. When you 
  are doing it with qt5 designer, make sure in your commit message add a sub  commit
  and indicate what you have changed or added. This is necessary cause we can not observe
  the .ui file's content to understand the changes.
## NOTE
Dont feel low if your pull request is rejected or asked for any changes. Even your gf
wont accept you if you suddently come and ask for a relationship.

<h3>Thanks Again For Your Effort</h3>
<H2>ALL THE BEST</H2>