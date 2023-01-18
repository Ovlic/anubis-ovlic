from distutils.core import setup

packages = [
    'ovlic_anubis',
]

setup(
    name = "ovlic-anubis",
    version = "0.0.1",
    packages = packages,
    install_requires = [
        "pycrypto",
        "requests",
    ],
    author = "Ovlic",
    description = "My copy of 0sir1ss Anubis for my school encryption project.",
    url = "https://github.com/ovlic/ovlic-anubis",
    project_urls = {
        "Bug Tracker": "https://github.com/ovlic/ovlic-anubis/issues",
    },
    classifiers = {
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    },
    include_package_data=True,
    python_requires = '>=3.6',
)
