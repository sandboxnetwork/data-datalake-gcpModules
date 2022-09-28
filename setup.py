from setuptools import setup, find_packages

install_requires = [
    'google-api-core>=2.10.1',
    'google-auth>=2.11.1',
    'google-cloud-bigquery>=3.3.2',
    'google-cloud-bigquery-storage>=2.16.0',
    'google-cloud-core>=2.3.2',
    'google-cloud-storage>=2.5.0',
]

setup(name='gcpModules',

    version='1.0.0',

    url='',

    license='MIT',

    author='jungsup lee',

    author_email='jungsup@sandbox.co.kr',

    description='easy use of google cloud platform modules',

    packages=['gcpModules'],

    long_description=open('README.md').read(),

    install_requires=install_requires,

    zip_safe=False,

    setup_requires=[]
)