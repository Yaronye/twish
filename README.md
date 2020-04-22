# Twish for Zerebra
##Description
Project Twish is a simple application to send links with a secret message, such as a password or a public ssh-key, that only can be viewed a specified number of times, default should be one view. In order to achieve this a recommended way is to generate unique links that needs a secret to view the content, when the secret has been showed the content of the link is supposed to be deleted. The project is to be built with the Django Framework and should follow best practices. It is recommended that you follow the book Two Scoops of Django 1.11 with its cookiecutter template.
In order to achieve a good development environment we also recommend that the project is dockerized.
It is only necessary to build the application in such a manner that it can be run in a local environment.
A project that mimics this functionality is onetimesecret.com. 

###Specifications:
Page that creates a link with a field to paste the content
Automatic generation of secret to open the message with
The linkpage that prompts for the secret and then shows the content
Estimated time: 40 hours
