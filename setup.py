from setuptools import setup

def requirements_txt_read(path):
    return open(path).read().splitlines()

setup(
    name='led2024',
    version="0.1.0",
    description="",
    long_description="",
    author='polar_solvent',
    url='https://github.com/polar-solvent/LED2024',
    license="MIT",
    package_dir={"ledmaking": "src"}, #"ledmaking"が"src"として認識され、インストールしたファイルにはsrcがledmakingになっている
    packages=["ledmaking"], #"ledmaking"というパッケージがある(中身はsrc)
    entry_points={
        "console_scripts": [
            "ledmaking=ledmaking.main:main" #"ledmaking"とターミナルに入力することでledmaking.main内のmainという関数を実行できる
        ]
    },
    install_requires = requirements_txt_read("requirements.txt"),
    python_requires='>=3.11'
)