# Agentless

[![GitHub license](https://img.shields.io/badge/license-GNU-green?style=flat)](https://github.com/CastellaniDavide/cpp-agentless/blob/master/LICENSE) ![Author](https://img.shields.io/badge/author-Castellani%20Davide-green?style=flat) ![Version](https://img.shields.io/badge/version-v01.02-blue?style=flat) ![Language Python](https://img.shields.io/badge/language-Python-yellowgreen?style=flat) ![sys.platform supported](https://img.shields.io/badge/OS%20platform%20supported-All-blue?style=flat) [![On GitHub](https://img.shields.io/badge/on%20GitHub-True-green?style=flat&logo=github)](https://github.com/CastellaniDavide/agentless) 

![logo](https://github.com/CastellaniDavide/agentless/blob/main/docs/logo.png?raw=true)

REMEMBER: you can see the same that is into this README in the [Wiki](https://github.com/CastellaniDavide/agentless/wiki).

## Documentation structure
- [Description](#Description)
- Before use it
    - [Requirements](#Requirements)
    - [Installation](#Installation)
    - [Update](#Update)
    - [Delete](#Delete)
- How to use it
    - [Execution examples](#Execution-examples)
    - [Output location](#Output-location)
- Extra
    - [YouTube Playlist](https://www.youtube.com/playlist?list=PLRDpL0F-q5Uvcka25LnMdieazgXU02v1J)
    - [Directories structure](#Directories-structure)
    - [Changelog](https://github.com/CastellaniDavide/agentless/blob/main/docs/CHANGELOG.txt)
    - [Code of conduct](https://github.com/CastellaniDavide/agentless/blob/main/docs/CODE_OF_CONDUCT.md)
    - [Contributing](https://github.com/CastellaniDavide/agentless/blob/main/docs/CONTRIBUTING.md)
- Help
    - [Discussions](https://github.com/CastellaniDavide/agentless/discussions)
    - [Issue](https://github.com/CastellaniDavide/agentless/issues)
    - [help@castellanidavide.it](mailto:help@castellanidavide.it)

## Description

[Agentless tool](https://github.com/CastellaniDavide/agentless) can help you scan the network.

I you wanted something to help you to scan, in a easy way, your network, this tool is for you.

With this tool you can easly scan all the wanted terminals' ports.

After execution you could save the data [csv file](https://en.wikipedia.org/wiki/Comma-separated_values) and/ or into [HarperDB](https://harperdb.io/) DataBase.

The scope of this tool is to make your network more secure.

Seeing the output (csv or DB), you can understand what opened ports are useless. Disabling them you can make the network less avariable for [black hat hacker](https://en.wikipedia.org/wiki/Black_hat_(computer_security)) attacks.

![](https://prod-upp-image-read.ft.com/8fdf7f64-e919-11e9-aefb-a946d2463e4b)

## Before use it

### Requirements
![](https://jeffnielsen.com/wp-content/uploads/2014/06/required-cropped.png)

To install this tools you need some preinstalled softwares.

#### Windows
If you are on Windows you needs to install: choco & VirtualBox into C:\Work\ folder

[![See video](https://img.youtube.com/vi/M_hPZVqirno/0.jpg)](https://www.youtube.com/watch?v=M_hPZVqirno)

#### Linux
If you are on Linux you need to install virtualbox

[![See video](https://img.youtube.com/vi/B597Mi7i8yQ/0.jpg)](https://www.youtube.com/watch?v=B597Mi7i8yQ)

### Installation
![](https://dctacademy.com/wp-content/uploads/2016/12/install.jpeg)

To install this tools after installing prequisites.

#### Windows
If you are on Windows you needs to write into Powershell (as Administrator): ```choco install agentless```

[![See video](https://img.youtube.com/vi/9ek_AuicHQE/0.jpg)](https://www.youtube.com/watch?v=9ek_AuicHQE)

#### Linux
If you are on Linux you need to write into the shell: ```sudo add-apt-repository ppa:castellanidavide/school -y; sudo apt update; sudo apt install agentless -y```

[![See video](https://img.youtube.com/vi/2F2c0wHNHO4/0.jpg)](https://www.youtube.com/watch?v=2F2c0wHNHO4)

### Update
![](https://images.idgesg.net/images/article/2020/07/software_update_by_gocmen_gettyimages-1146311500_2400x1600-100852481-large.jpg)

To update this tools.

#### Windows
If you are on Windows you needs to write into Powershell (as Administrator): ```choco upgrade agentless```

[![See video](https://img.youtube.com/vi/O8fTc2rcJK0/0.jpg)](https://www.youtube.com/watch?v=O8fTc2rcJK0)

#### Linux
If you are on Linux you need to write into the shell: ```sudo apt update; sudo apt upgrade```

[![See video](https://img.youtube.com/vi/ZhLG3Ocw-GE/0.jpg)](https://www.youtube.com/watch?v=ZhLG3Ocw-GE)

### Delate
![](http://cdn.onlinewebfonts.com/svg/img_105952.png)
  - Windows (using choco):
    - ```choco remove agentless```
  - Debian/ Ubuntu using apt:
    - ```sudo apt remove agentless```

## How to use it

### Execution examples

![](https://blog.toadworld.com/hs-fs/hubfs/SQL_tools-8_ways_large.jpg?width=3248&name=SQL_tools-8_ways_large.jpg)

## How to use

Write ```agentsless``` on your shell

ATTENTION: Remember to run this tool as Administrator

## Synopsis
On this tool you can pass this paramers:
 - [--help | -h] -  help istructions
 - [--verbose] - verbose mode
 - [--adresses=...] - Choose adresses, you can use this multiple time (Replace "..." with the value(s))
 - [--csv] - enable csv output
 - [--single] - disanable multitreading
 - [--url=... --token=... --table=...] - enable the upload to HarperDB (Replace "..." with the value(s))

If you are on Ubuntu you can always see the synopsis typing: ```man agentsless```

## Example video

[![See video](https://img.youtube.com/vi/l0e9ZI87Rzo/0.jpg)](https://www.youtube.com/watch?v=l0e9ZI87Rzo)

### Output location
![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpVK6K3kB738m0Jw_Er6hJFyHm7fL28kwj2A&usqp=CAU)

## CSV file
To see the csv file you have to search "ping.csv" file in the same directory where it was runned the code with ```--csv``` param.

### Windows
If you are on Windows you needs to write into Powershell (better if as Administrator): ```type ping.csv```

### Linux
If you are on Linux you need to write into the shell: ```cat ping.csv```

## DB output
To see the DB output you have to open [HarperDB console](https://harperdb.io/).
## Log file
To see the csv file you have to search "C:/Program Files/agentless/trace.log" if you are using Windows as OS.
Otherwise the log file will be into "~/trace.log".

ATTENTION: the log file will be create on first run, if you want to see it run tool at least once.

### Windows
If you are on Windows you needs to write into Powershell (better if as Administrator): ```type "C:/Program Files/agentless/trace.log"```

### Linux
If you are on Linux you need to write into the shell: ```cat ~/trace.log```

## Extra

### Directories structure
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
   
---
Made by [Castellani Davide](https://github.com/CastellaniDavide)

If you have any problem please contact me:
- [help@castellanidavide.it](mailto:help@castellanidavide.it)
- [Discussions](https://github.com/CastellaniDavide/agentless/discussions)
- [Issue](https://github.com/CastellaniDavide/agentless/issues)
