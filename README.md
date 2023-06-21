# Django Project with Gunicorn, Nginx, and PostgreSQL

This is a Django project template that demonstrates how to deploy a Django application using Gunicorn as the application server, Nginx as the reverse proxy server, and PostgreSQL as the database backend.

## Project Structure

The project structure is as follows:

myproject/
├── myapp/
│ ├── ...
│ ├── ...
├── myproject/
│ ├── settings/
│ │ ├── init.py
│ │ ├── base.py
│ │ ├── dev.py
│ │ ├── prod.py
│ │ └── test.py
│ ├── init.py
│ ├── urls.py
│ └── wsgi.py
├── gunicorn.conf.py
└── nginx/
└── myproject.conf
pip install -r requirements.txt
- `myapp/`: Contains your Django app code.
- `myproject/`: Contains the project-level code and settings.
- `myproject/settings/`: Contains environment-specific settings files.
- `gunicorn.conf.py`: Gunicorn server configuration file.
- `nginx/`: Contains Nginx configuration file(s).

## Usage

### Development

1. Create and activate a virtual environment (optional).

2. Install the project dependencies:

3. Start the Django development server:
python manage.py runserver --settings=myproject.settings.dev

4. Access the application at `http://localhost:8000/hello/`.

### Production

1. Install Gunicorn and Nginx (if not installed).

2. Create and activate a virtual environment (optional).

3. Install the project dependencies:
pip install -r requirements.txt

4. Configure PostgreSQL:
- Create a PostgreSQL database and update the database settings in `myproject/settings/prod.py`.

5. Update the Nginx configuration:
- Update the IP address and domain in `myproject.conf` inside the `nginx/` directory.
- Copy the `myproject.conf` file to the appropriate Nginx configuration directory (e.g., `/etc/nginx/conf.d/`).

6. Start the Gunicorn server:
gunicorn myproject.wsgi:application -c gunicorn.conf.py --settings=myproject.settings.prod

7. Restart Nginx:
sudo service nginx restart

8. Access the application at `http://your_domain.com/hello/`.

### Testing

1. Create and activate a virtual environment (optional).

2. Install the project dependencies:
python manage.py test --settings=myproject.settings.test

## Configuration

- Database: PostgreSQL is used as the database backend. Update the database settings in the respective environment-specific settings file (`myproject/settings/dev.py`, `myproject/settings/prod.py`, `myproject/settings/test.py`).

- Gunicorn: The Gunicorn server configuration is defined in `gunicorn.conf.py`.

- Nginx: The Nginx server block configuration is defined in `myproject.conf` inside the `nginx/` directory.




