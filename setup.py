from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='nicebytes',
    author='Philipp Ploder',
    url='https://github.com/Fylipp/nicebytes',
    description='human-readable data quantities',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    py_modules=['nicebytes'],
    scripts=['nicebytes', 'nicebytes.py'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "Topic :: System"
    ]
)
