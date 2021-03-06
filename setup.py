from setuptools import setup

setup(
    name='ricknmorty',
    version='',
    packages=['config', 'config.connection_details', 'scripts', 'scripts.read_from_api'],
    url='',
    license='',
    author='ronot',
    author_email='',
    description='The home assignment from HiredScore',
    install_requires=['certifi==2021.5.30',
                      'charset-normalizer==2.0.3',
                      'greenlet==1.1.0',
                      'idna==3.2',
                      'importlib-metadata==4.6.1',
                      'numpy==1.21.0',
                      'pandas==1.3.0',
                      'psycopg2==2.9.1',
                      'python-dateutil==2.8.2',
                      'pytz==2021.1',
                      'requests==2.26.0',
                      'six==1.16.0',
                      'SQLAlchemy==1.4.21',
                      'typing-extensions==3.10.0.0',
                      'urllib3==1.26.6',
                      'zipp==3.5.0']
)
