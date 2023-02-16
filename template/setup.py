from setuptools import setup, find_packages

setup(
        name='tweetcounter',
        version='1.0',
        author='class',
        author_email='class@ou.edu',
        packages=find_packages(exclude=('tests', 'docs')),
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
        )
