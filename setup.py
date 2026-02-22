from setuptools import setup

setup(
    name="mashup-generator",
    version="0.0.1",
    py_modules=["102303561"],
    install_requires=[
        "moviepy==1.0.3",
        "pydub"
    ],
    entry_points={
        "console_scripts": [
            "mashup=102303561:main"
        ]
    },
)
