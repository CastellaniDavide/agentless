# agentless
[![GitHub license](https://img.shields.io/badge/license-GNU-green?style=flat)](https://github.com/CastellaniDavide/cpp-agentless/blob/master/LICENSE) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v01.01-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-All-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/agentless) 

## Description
This tool can help you scan the network

## Required
![](http://jeffnielsen.com/wp-content/uploads/2014/06/required-cropped.png)
 - choco/ snap
 - virtualbox (C:\Work\* if you are on windows)

## Installation
![](https://dctacademy.com/wp-content/uploads/2016/12/install.jpeg)
 - choco (Windows) (as Administartor)
   - ```choco install agentless=01.01```
 - Ubuntu using apt:
    - ```sudo add-apt-repository ppa:castellanidavide/school -y; sudo apt update; sudo apt install agentless -y```

### Update
![](https://images.idgesg.net/images/article/2020/07/software_update_by_gocmen_gettyimages-1146311500_2400x1600-100852481-large.jpg)
  - Windows (using choco):
    - ```choco upgrade agentless```
  - Ubuntu using apt:
    - ```sudo apt update; sudo apt upgrade```

### Delate
![](http://cdn.onlinewebfonts.com/svg/img_105952.png)
  - Windows (using choco):
    - ```choco remove agentless```
  - Debian/ Ubuntu using apt:
    - ```sudo apt remove agentless```

## Directories structure
![](https://cdn.analyticsvidhya.com/wp-content/uploads/2019/05/data-science-framework.png)
 - .gitignore
 - setup.py
 - LICENSE.md
 - .github
   - ISSUE_TEMPLATE
     - bug_report.md
     - feature-request.md
   - workflows
     - on-push.yml
     - on-release.yml
 - choco
   - ReadMe.md
   - set.txt
   - agentless.nuspec
   - tools
     - chocolateyinstall.ps1
     - chocolateyuninstall.ps1
     - LICENSE.txt
     - VERIFICATION.txt
     - agentless-install.c
     - agentless-install.exe
     - agentless-install.o
     - agentless.c
     - agentless.exe
     - agentless.o
 - debian
   - agentless.1
   - agentless.c
   - Makefile
   - requirements.in
   - debian
     - changelog
     - compat
     - control
     - copyright
     - postinst
     - postrm
     - preinst
     - rules
     - source
 - docs
   - logo.png
   - \*.md
 - flussi (example output(s))
   - net.csv
   - OS.csv
 - log (example log(s))
   - trace.log
 - requirements
   - requirements.txt
 - agentless
   - \_\_init\_\_.py
   
### Execution examples  
![](https://blog.toadworld.com/hs-fs/hubfs/SQL_tools-8_ways_large.jpg?width=3248&name=SQL_tools-8_ways_large.jpg)
 - agentless
   
### Output location
![](https://www.macroeconomia.it/wp-content/uploads/2018/03/input-output-650x364.png)
 - *.csv (if enabled) in the location where the code was lauched
 - *.log
   - C:/Program Files/agentless/* on Windows
   - ~/* on linux
   - current location (if you didn't lauch the code with the correct rights)

# Changelog
![](https://www.ashoka.org/sites/default/files/styles/medium_1600x1000/public/old_way_new_way.jpg?itok=3JnbJz4O)
 - [Version_01.01_2021-3-22](#Version_0101_2021-3-22)

## Version_01.01_2021-3-22
 - Initial version

---
Made by Castellani Davide 
If you have any problem please contact me:
- help@castellanidavide.it
- [Issue](https://github.com/CastellaniDavide/agentless/issues)
