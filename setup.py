from setuptools import setup, find_packages

setup(
    name="crypto-ml-forecast",
    version="1.2.0",
    description="Machine Learning for crypto forecast",
    author="Allysson Macedo",
    author_email="allyssonvsmacedo@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
    "numpy>=1.26",
    "pandas>=2.2",
    "matplotlib>=3.8",
    "scikit-learn>=1.4",
    "scipy>=1.11",
    "xgboost>=2.0",
    "yfinance>=0.2",
    "plotly>=5.20",
    "pandas-ta",
    "numba>=0.59",
    "requests>=2.31",
    "pyarrow>=20.0.0",
    "vectorbt==0.27.3",
    "imbalanced-learn==0.13.0",
    ],
    python_requires=">=3.12",
)

# Execute in terminal
# pip install -e .