from setuptools import setup, find_packages
setup(
    name='kyokowt',
    version='0.0.1',
    license='MIT',
    description='kyokowt',

    author='kahenteikou',
    author_email='umekoujouhouhan@gmail.com',
    url='None.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)