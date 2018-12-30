from distutils.core import setup

setup(
    name='py-synsurveillance',
    version='0.2.1',
    packages=['synology'],
    url='https://github.com/johnruemker/py-synsurveillance',
    license='MIT',
    author='jrummy',
    author_email='john.ruemker@gmail.com',
    description='Python API for Synology Surveillance Station',
    requires=['requests']
)
