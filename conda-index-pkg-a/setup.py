from setuptools import setup

setup(
    name = "conda-index-pkg-a",
    version = "1.0",
    author = "Kale Franz",
    author_email = "kale@franz.io",
    license = "BSD",
    packages=[
        'conda_index_pkg_a',
    ],
    entry_points={
        'console_scripts': [
            "conda-index-pkg-a=conda_index_pkg_a:main",
            "conda-index-pkg-a-helper = conda_index_pkg_a:helper",
        ],
    },
    zip_safe=False,
)
