import os
from setuptools import setup

LONG_DESCRIPTION = """
Run RequireJS (r.js) without node.
"""


def parse_markdown_readme():
    """
    Convert README.md to RST via pandoc, and load into memory
    (fallback to LONG_DESCRIPTION on failure)
    """
    # Attempt to run pandoc on markdown file
    import subprocess
    try:
        subprocess.call(
            ['pandoc', '-t', 'rst', '-o', 'README.rst', 'README.md']
        )
    except OSError:
        return LONG_DESCRIPTION

    # Attempt to load output
    try:
        readme = open(os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        ))
    except IOError:
        return LONG_DESCRIPTION
    return readme.read()


setup(
    name='requirejs',
    version='0.1.0',
    author='S. Andrew Sheppard',
    author_email='andrew@wq.io',
    url='https://github.com/wq/python-requirejs',
    license='MIT',
    packages=['requirejs'],
    package_data={
        'requirejs': ["*.js"],
    },
    install_requires=[
        'py-mini-racer',
    ],
    description=LONG_DESCRIPTION.strip(),
    long_description=parse_markdown_readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Pre-processors',
    ],
    test_suite='tests',
    tests_require=[
        'wq.app'
    ],
)
