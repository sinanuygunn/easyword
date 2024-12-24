from setuptools import setup, find_packages

setup(
    name='easyword', 
    version='1.0.0', 
    description='Learn words easily with a simple word management tool',
    author='Sinan Uygun',
    author_email='sinanuygun00125@gmail.com',  
    url='https://github.com/sinanuygunn/easyword',  
    packages=['easyword', 'commands', 'components'], 
    include_package_data=True, 
    install_requires=[
        'wheel',
        'colorama', 
        'argparse',
        'googletrans==3.1.0a0',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'easyword=easyword:run',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
