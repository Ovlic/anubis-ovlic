from distutils.core import setup

packages = [
    'O_anubis',
]

setup(
    name = "anubis-ovlic",
    version = "0.0.1",
    packages = packages,
    author = "Ovlic",
    description = "My copy of 0sir1ss Anubis for my school encryption project.",
    url = "https://github.com/ovlic/anubis-ovlic",
    project_urls = {
        "Bug Tracker": "https://github.com/ovlic/anubis-ovlic/issues",
    },
    classifiers = {
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    },
    include_package_data=True,
    python_requires = '>=3.6',
)