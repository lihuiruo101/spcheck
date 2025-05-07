from setuptools import setup, find_packages

setup(
    name="spcheck",
    version="0.1",
    packages=find_packages(),
    install_requires=["py-hanspell"],
    entry_points={
        'console_scripts': [
            'spcheck = spcheck.__main__:main',
        ]
    },
    author="lihuiruo101",
    description="한글 맞춤법 검사 CLI 도구",
    python_requires='>=3.7',
)
