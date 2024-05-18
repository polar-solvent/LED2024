from setuptools import setup

def requirements_txt_read(path):
    return open(path).read().splitlines()

setup(
    name='led2024',
    version="1.0.0",
    author='polar_solvent',
    url='https://github.com/polar-solvent/LED2024',
    license="MIT",
    package_dir={"": "src"}, #srcをルートとする=何も書かなかった場合srcが自動で適応される
    entry_points={
        "console_scripts": [
            "ledmaking=main:main", #"ledmaking"とターミナルに入力することで(src).main内のmainという関数を実行できる
            "ledshowing=show:main" #同様
        ]
    },
    install_requires = requirements_txt_read("requirements.txt"),
    python_requires='>=3.11'
)
