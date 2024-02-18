
# A Quick Breakdown Of The Project Structure

- ### .idea:
  The contents of this folder are IDE specific settings stored as xml files.
  Additionally, the project's .gitignore file is located in this folder

- ### djangoRechained:
  The contents of this folder are project specific files pertinent to the Django Python library.
  These files are generated automatically when initializing a Django project, and all end with the .py extension

- ### firstDjangoProject:
  The contents of this folder are application specific files pertinent to the Django Python library.
  These files are generated automatically when initializing a Django app, with the exception of
  the contents of the migrations folder (which are generated automatically when making migrations within Django), and
  urls.py (which was added during development to map incoming urls containing "/firstDjangoProject" to proper requests in views.py)

- ### templates:
  The contents of this folder are .html templates used by views.py (located in the firstDjangoProject folder) to render content in the client's browser
  These files were all created during development

- ### db.sqlite3:
  This file represents the database where all content/data is stored for the client

- ### manage.py:
  This file contains code neccessary to run the Django application from the command line

- ### .ebextensions:
  This folder contains necessary information for deployment of project to _AWS Elastic Beanstalk_.

- ### mystaticfiles:
  This folder contains static files such as CSS, JS, and images that are to be rendered with the HTML templates on the client side

- ### prodfiles:
  This folder contains static files that are to be served during production.
  Some of these files are copies from _mystaticfiles_ folder.

- ### static:
  This folder contains more static files meant to be rendered on the client side

- ### djangoRechained.zip:
  This folder contains all other folders and files that will be deployed through _AWS Beanstalk_.
  This folder is uploaded to the web through the AWS console.

- ### requirements.txt:
  This file contains a list of all projects dependencies.
  It is used during deployment to ensure all necessary packages are included.
