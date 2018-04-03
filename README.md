# Django Highcharts.js Example

[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.0-brightgreen.svg)](https://djangoproject.com)

Code sample from the blog post [How to Integrate Highcharts.js with Django](https://simpleisbetterthancomplex.com/tutorial/2018/04/03/how-to-integrate-highcharts-js-with-django.html).

![Highcharts.js Screen Shot](https://simpleisbetterthancomplex.com/media/2018/04/survivors-by-class.png)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/sibtc/django-highcharts-example.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Migrate the database:

```bash
python manage.py migrate
```

The migration will also populate the database.

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/sibtc/dependent-dropdown-example/blob/master/LICENSE).
