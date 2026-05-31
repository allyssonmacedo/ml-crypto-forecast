# 🚀 Crypto Forecast - Machine Learning for Cryptocurrency Price Prediction

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive machine learning framework for cryptocurrency technical analysis, forecasting, and backtesting. This project combines deep technical analysis with modern machine learning algorithms to predict cryptocurrency price movements.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Modules](#modules)
- [Models](#models)
- [Data Pipeline](#data-pipeline)
- [Backtesting](#backtesting)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### 📊 Data Collection & Management
- **Automated Data Ingestion**: Fetch historical cryptocurrency data from Yahoo Finance
- **Data Validation**: Automatic filtering of stable and actively traded cryptocurrencies
- **Multi-Symbol Support**: Analyze 10+ major cryptocurrencies (BTC, ETH, BNB, SOL, XRP, etc.)

### 🔧 Feature Engineering
- **60+ Technical Indicators**: Volume-based, trend-based, momentum, and volatility indicators
- **Advanced Preprocessing**: Data normalization, balancing with SMOTE/RandomUnderSampler
- **Target Engineering**: Multiple prediction targets (7d, 15d, 30d windows)

### 🤖 Machine Learning
- **Multiple Algorithms**: Random Forest, XGBoost, and Logistic Regression
- **Binary Classification**: Predict price increase/decrease patterns
- **Model Evaluation**: Comprehensive metrics (Accuracy, Precision, Recall, F1-Score, AUC-ROC)
- **Hyperparameter Tuning**: Support for model optimization and versioning

### 📈 Predictions & Signals
- **Historical Backtesting**: Validate model performance on past data
- **Daily Predictions**: Real-time price movement forecasts
- **Trading Signals**: Generate buy/sell signals based on model confidence
- **Probability Scores**: Get confidence levels for each prediction

### 💰 Backtesting & Simulation
- **Strategy Backtesting**: Test trading strategies on historical data
- **Compound Returns**: Calculate cumulative returns with multiple entries
- **Monte Carlo Simulations**: 1,000+ simulations for risk analysis
- **Entry Point Analysis**: Analyze profitable entry points

---

## 📁 Project Structure

```
ml-crypto-forecast/
├── src/
│   ├── crypto_modules/          # Core ML modules
│   │   ├── FileHandle.py        # Data I/O operations
│   │   ├── Ingestion.py         # Data collection from APIs
│   │   ├── Features.py          # Technical indicator calculations
│   │   ├── PrepModels.py        # Data preprocessing
│   │   ├── Train.py             # Model training
│   │   ├── Predict.py           # Predictions and forecasting
│   │   ├── Signals.py           # Signal generation
│   │   ├── Backtesting.py       # Backtesting engine
│   │   └── __init__.py
│   └── constants.py             # Configuration constants
│
├── jobs/                        # Job orchestration
│   ├── enrichment.py            # Main execution pipeline
│   ├── parameters.py            # Configuration parameters
│   └── constants.py             # Job-specific constants
│
├── notebooks/                   # Jupyter analysis notebooks
│   ├── preprocessing.ipynb
│   ├── backtest.ipynb
│   ├── deploy.ipynb
│   ├── LogisticRegressionRaw.ipynb
│   └── compound_proba.ipynb
│
├── data/                        # Data storage (git-ignored)
│   ├── crypto_data_historical.parquet
│   ├── crypto_data_with_indicators.parquet
│   └── crypto_data_prep_models.parquet
│
├── output/                      # Results and outputs (git-ignored)
│   ├── accuracy/                # Model performance logs
│   ├── models/                  # Trained models
│   ├── predict/                 # Prediction results
│   ├── signals/                 # Trading signals
│   ├── backtest/                # Backtest results
│   └── simulations/             # Simulation outputs
│
├── pyproject.toml              # Modern Python project config
├── setup.py                    # Package setup
├── requirements.txt            # Dependencies
└── README.md                   # This file
```

---

## 💾 Installation

### Prerequisites
- Python 3.10 or higher
- pip or conda
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/allyssonmacedo/ml-crypto-forecast.git
cd ml-crypto-forecast
```

### Step 2: Create Virtual Environment
```bash
# Using venv (recommended)
python -m venv venv

# Activate the environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

**Option A: Install as Development Package**
```bash
pip install -e .
```

**Option B: Install from Requirements**
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python -c "import crypto_modules; print('✅ Installation successful!')"
```

---

## 🚀 Quick Start

### 1. Run the Complete Pipeline
```bash
cd jobs
python enrichment.py
```

This will execute:
1. **Data Ingestion**: Fetch historical cryptocurrency data
2. **Feature Engineering**: Calculate 60+ technical indicators
3. **Daily Predictions**: Generate real-time price forecasts
4. **Backtesting**: Validate model performance
5. **Signals**: Generate trading signals

### 2. Configure Execution
Edit `jobs/parameters.py` to control which steps run:

```python
execute_data_ingestion = True        # Fetch new data
execute_data_indicators = True       # Calculate indicators
execute_data_prep_models = False     # Prepare training data
execute_train_models = False         # Train new models
execute_daily_predict = True         # Generate daily forecasts
execute_backtest = False             # Run backtests
execute_signals = False              # Generate signals
```

### 3. Filter Cryptocurrencies
```python
# In jobs/parameters.py
filter_symbols = [
    'BTC-USD', 'ETH-USD', 'BNB-USD', 'SOL-USD', 'XRP-USD',
    'DOGE-USD', 'TRX-USD', 'ADA-USD', 'AVAX-USD', 'SHIB-USD'
]
```

---

## ⚙️ Configuration

### Key Parameters (`jobs/parameters.py`)

#### Data Collection
```python
start_date_ingestion = '2022-01-01'  # Historical data start date
active_date_symbol = '2024-10-01'    # Maximum date to consider crypto active
recent_date_symbol = '2022-10-01'    # Minimum date for crypto viability
```

#### Model Selection
```python
score_metric = 'f1_score'            # Metric: accuracy, precision, recall, auc_roc, f1_score
version_model = 'v2.2.20'            # Model version
num_select_models = 0                # Number of models (0 = all)
min_threshold_models = 0.65          # Minimum model score threshold
```

#### Predictions
```python
melt_daily_predict = True            # Pivot prediction results
min_threshold_signals = 0.55         # Minimum signal confidence
```

#### Backtesting & Simulation
```python
start_date_backtest = '2024-01-01'
numbers_of_simulations = 1_000
numbers_of_entries_day_simulations = 5
```

---

## 🎯 Usage Examples

### Train New Models
```python
# In jobs/parameters.py
execute_train_models = True
execute_data_prep_models = True
version_model = 'v2.3.0'  # New version

# Run
python enrichment.py
```

### Generate Daily Predictions
```python
# In jobs/parameters.py
execute_daily_predict = True
execute_train_models = False  # Use existing models

# Run
python enrichment.py
```

### Run Complete Backtest with Signals
```python
# In jobs/parameters.py
execute_backtest = True
execute_signals = True
execute_daily_predict = True

# Run
python enrichment.py
```

### Monte Carlo Simulations
```python
# In jobs/parameters.py
execute_simulations = True
numbers_of_simulations = 5_000

# Run
python enrichment.py
```

---

## 🧠 Modules

### FileHandle
Data I/O operations, file reading/writing, data validation

### Ingestion
Fetches historical cryptocurrency data from Yahoo Finance API

### Features
Calculates 60+ technical indicators:
- Volume-based indicators
- Trend indicators (Moving Averages, MACD)
- Momentum indicators (RSI, Stochastic)
- Volatility indicators (Bollinger Bands, ATR)

### PrepModels
Data preprocessing:
- Normalization and standardization
- Missing value handling
- Outlier removal
- Data balancing (SMOTE/RandomUnderSampler)

### Train
Machine learning model training:
- Random Forest Classifier
- XGBoost Classifier
- Logistic Regression
- Hyperparameter optimization

### Predict
Price movement predictions:
- Historical predictions (backtesting)
- Daily forecasts (real-time)
- Probability scores
- Confidence levels

### Signals
Trading signal generation based on model predictions and thresholds

### Backtesting
Strategy evaluation:
- Simple backtest (entry at every signal)
- Compound backtest (multiple consecutive entries)
- Performance metrics
- Return calculations

---

## 🤖 Models

### Algorithms Used
1. **Random Forest** - High accuracy, handles non-linear relationships
2. **XGBoost** - Superior performance, handles imbalanced data well
3. **Logistic Regression** - Baseline, interpretable probabilities

### Target Variables
The model predicts binary outcomes:

**Positive Targets** (Price increase)
- `bl_target_10P_7d`: 10% increase in 7 days
- `bl_target_15P_15d`: 15% increase in 15 days
- `bl_target_20P_30d`: 20% increase in 30 days

**Negative Targets** (Price decrease)
- `bl_target_10N_7d`: 10% decrease in 7 days
- `bl_target_20N_30d`: 20% decrease in 30 days

---

## 📊 Data Pipeline

```
Raw Data (Yahoo Finance)
    ↓
[Data Ingestion] → crypto_data_historical.parquet
    ↓
[Feature Engineering] → crypto_data_with_indicators.parquet
    ↓
[Data Preparation] → crypto_data_prep_models.parquet
    ↓
[Model Training] → Trained Models (output/models/)
    ↓
[Predictions] → Forecast Results (output/predict/)
    ↓
[Signal Generation] → Trading Signals (output/signals/)
    ↓
[Backtesting] → Performance Metrics (output/backtest/)
```

---

## 📈 Backtesting

### Output Metrics
- **Total Return**: Cumulative percentage return
- **Win Rate**: Percentage of profitable trades
- **Average Return per Trade**: Mean profit/loss per entry
- **Sharpe Ratio**: Risk-adjusted return
- **Maximum Drawdown**: Largest peak-to-trough decline

### Results Location
```
output/
├── backtest/              # Backtest results
├── accuracy/              # Model performance logs
└── simulations/           # Monte Carlo results
```

---

## 🔄 Workflow Examples

### 1. Initial Setup (First Time)
```bash
# Install dependencies
pip install -e .

# Configure symbols
# Edit jobs/parameters.py - set your target cryptocurrencies

# Run first pipeline
cd jobs
python enrichment.py
```

### 2. Daily Forecasting
```python
# jobs/parameters.py
execute_data_ingestion = True
execute_data_indicators = True
execute_daily_predict = True
execute_train_models = False  # Use existing trained models
```

### 3. Model Retraining
```python
# jobs/parameters.py
execute_data_prep_models = True
execute_train_models = True
version_model = 'v2.3.0'  # Bump version
```

---

## 📓 Jupyter Notebooks

The `notebooks/` directory contains analysis and exploration notebooks:

- **preprocessing.ipynb** - Data exploration and feature analysis
- **backtest.ipynb** - Backtest result analysis
- **deploy.ipynb** - Production deployment examples
- **compound_proba.ipynb** - Probability distribution analysis
- **LogisticRegressionRaw.ipynb** - Logistic regression baseline

To run notebooks:
```bash
jupyter lab notebooks/
```

---

## 🛠️ Development

### Running Tests
```bash
# Add pytest to environment
pip install pytest

# Run tests
pytest tests/
```

### Code Style
```bash
# Format code
black src/ jobs/

# Lint
pylint src/ jobs/
```

### Building Documentation
```bash
pip install sphinx
sphinx-build -b html docs/ docs/_build/
```

---

## 📦 Dependencies

Key dependencies:
- **scikit-learn** - Machine learning algorithms
- **xgboost** - Gradient boosting
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **yfinance** - Financial data API
- **pandas_ta** - Technical analysis indicators
- **plotly** - Interactive visualizations
- **jupyter** - Interactive notebooks

See `requirements.txt` for complete list.

---

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'crypto_modules'"
**Solution**: Install the package in development mode:
```bash
pip install -e .
```

### Issue: "ConnectionError" when fetching data
**Solution**: Check internet connection and Yahoo Finance API availability:
```python
import yfinance as yf
yf.download('BTC-USD', start='2024-01-01', end='2024-01-02')
```

### Issue: "Memory Error" with large datasets
**Solution**: Reduce number of symbols or date range in `parameters.py`:
```python
filter_symbols = ['BTC-USD', 'ETH-USD']  # Use fewer symbols
start_date_ingestion = '2023-01-01'      # More recent data
```

---

## 📚 Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Technical Analysis Library](https://github.com/twopirllc/pandas-ta)

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👤 Author

**Allysson Macedo**
- Email: allyssonvsmacedo@gmail.com
- GitHub: [@allyssonmacedo](https://github.com/allyssonmacedo)

---

## ⚠️ Disclaimer

This project is for educational and research purposes only. Cryptocurrency trading involves substantial risk of loss. Past performance does not guarantee future results. Always do your own research and consult with a financial advisor before making investment decisions.

---

## 🙏 Acknowledgments

- Yahoo Finance for providing free historical data
- Open-source ML community for excellent tools
- Contributors and users for feedback and improvements

---

**Last Updated**: May 2026  
**Version**: 0.1.0
