Project Name : Inventory CatalogItem

This project is used to manage an Inventory items,
it allow to you add, delete, editing current items or its category
after you have login.

Project requirements:
you have to download the following to run the project:
- Python3
- VirtualBox
- Vagrant v2.2.0
- SQLAlchemy

Technologies used in this project:
Flask, HTML, CSS, Bootstrap, google OAuth api

this project contains on 3 tables to store informations :
- Table (User) : columns(id, name, email, picture)
- Table (Category) : columns(id, name, user_id)
- Table (CatalogItem) : columns(name, id, description, price, category_id)


how to run the project :

1 - Install Vagrant and VirtualBox
2 - Clone the Vagrantfile from the Udacity Repo
3 - unzip the project folder
4 - now move Vagrantfile to the project folder
5 - now to instal open command line then cd to project folder and run this commands
    'vagrant up' wait to finish
    then run this command to login to the vm
    'vagrant ssh'
6 - now you have to downlaod any python3 lib required for this Project
for sqlalchemy : 'sudo pip3 install sqlalchemy'
7 - now you are ready to run the project, but first you have to initiate database and add some data, so to make the db tables and fill it with some data run this commands
'python3 database_setup.py'
'python3 dbFillData.py'
8- Last thing is run the project, just run this command
'python3 application.py'

now to see the website open any browser in you computer and go to
'http://localhost:5000'
