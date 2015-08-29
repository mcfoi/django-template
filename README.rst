A basic GeoDjango Project template for usage in LiClipse environments.

- Checkout the project.

- Edit in the two files named activate_venv.bat and deactivate_venv.bat the

    <virtualenv_root>
with the actual path (e.g.: c:\Users\mcfoi\Dropbox\PythonVirtualEnv\Django\pma\ )

- Create a virtualenv with:

    virtualenv <project_name>
- Activate it by calling:

    activate_venv.bat
- Install GDAL libraries (in Windows use OSGEO4Win.exe with Easy WebGIS Install)
- Install Postgresql

    easy_install psycopg2-2.6.1.win32-py2.7-pg9.4.4-release
- Start server with:
 
    python manage.py runserver 8000 --settings=config.settings.local