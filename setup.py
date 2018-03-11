from setuptools import setup, find_packages

setup(
    name='data_analysis',
    version='0.0.1',
    url = 'https://github.com/ymunemasa/PythonPractice',
    license='BSD',
    author='Yumiko Munemasa',
    packages=find_packages(),
    install_requires=['PyQt5',
                    'pandas',
                    'sqlalchemy',
                    'nltk',
                    'numpy',
                    'jupyter',
                    'python-twitter'],
    entry_points={},
    extras_require={'dev': ['flake8',]},
)
