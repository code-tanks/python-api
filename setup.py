from setuptools import setup

# setup(
#     name='PackageName',
#     version='0.1.0',
#     author='An Awesome Coder',
#     author_email='aac@example.com',
#     packages=['package_name', 'package_name.test'],
#     scripts=['bin/script1', 'bin/script2'],
#     url='http://pypi.python.org/pypi/PackageName/',
#     license='LICENSE.txt',
#     description='An awesome package that does something',
#     long_description=open('README.md', encoding='utf-8').read(),
#     install_requires=[
#         "Django >= 1.1.1",
#         "pytest",
#     ],
# )

setup(
    name='codetanks',
    version='0.1.3',
    description='The Python API for Code-Tanks',
    url='http://github.com/code-tanks/python-api',
    author='Derrick Liu',
    author_email='me@derrickliu.dev',
    license='Apache Software License 2.0',
    packages=['codetanks'],
    zip_safe=False,
    install_requires=[
        "fastapi==0.91.0",
    ],
)
