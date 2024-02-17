
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
