import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TPEBot", # Replace with your own username
    version="0.0.1",
    author="Ester Goh",
    description="A tpe chatbot pakage",
    packages=setuptools.find_packages(),
    package_data={'': ['Data/*.js', 'Data/*.html', 'Data/Default - Learn/*.json', 'Data/Default - Recommended/*.json']},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
