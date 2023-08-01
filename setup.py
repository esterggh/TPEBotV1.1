import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TPEBot", # Replace with your own username
    version="1.5.0",
    author="Ester Goh",
    description="A TPE Chatbot Package",
    packages=setuptools.find_packages(),
    package_data={'': ['Data/*.js', 'Data/*.html', 'Data/Default - Learn/*.json', 'Data/Default - Hot Topics/*.json']},
    include_package_data=True,
    install_requires=[
        'pandas',
        'torch', 
        'openpyxl', 
        'transformers', 
        'sentencepiece', 
        'python-Levenshtein', 
        'sentence-transformers', 
        'fuzzywuzzy', 
        'protobuf==3.20.0'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
