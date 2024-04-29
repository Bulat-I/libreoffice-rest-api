# Libreoffice REST API

Features
========
This is a very simple implementation of the Libreoffice REST API that listens for incoming requests with a file name and runs the Libreoffice converter to convert that file to PDF.
The goal of this project is to move the Libreoffice converter into a separate Docker container from my Telegram bot.
Both containers communicate via HTTP and use the same storage connected to both containers to process files.

Under the hood
========
This project is written on Python and utilizes the following: 
* Libreoffice v7.1.8.1 package for converting files to PDF format
* Flask async v2.0.1 web framework for handling web requests
* Gunicorn v20.1.0 web server

Settings:
* Default port: 2002
* Default directory to search for incoming files: /var/lib/telegram-bot/input/

Usage
========
* Docker run command: docker run -d --name libreoffice_api -v /var/lib/telegram-bot/:/var/lib/telegram-bot/ -p 2002:2002 lo7api
