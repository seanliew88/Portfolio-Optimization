# Portfolio Optimization

A Python-based portfolio optimization tool that uses Monte Carlo simulation to find optimal asset allocation strategies. This project helps investors identify portfolios with maximum Sharpe ratio and minimum volatility by analyzing historical stock data.

## Features

- **Data Collection**: Fetch historical stock data using Yahoo Finance API
- **Data Preprocessing**: Calculate log returns and percentage changes from stock prices
- **Monte Carlo Simulation**: Generate thousands of random portfolio combinations to explore the efficient frontier
- **Portfolio Metrics**: Calculate expected returns, volatility, and Sharpe ratio for each portfolio
- **Optimization**: Identify portfolios with:
  - Maximum Sharpe Ratio (best risk-adjusted returns)
  - Minimum Volatility (lowest risk)

## Project Structure

```
Portfolio Optimization/
├── scripts/
│   ├── grab_data.py          # Functions to fetch and collect stock data
│   ├── preprocess.py          # Data preprocessing utilities
│   └── data_analysis.ipynb   # Main analysis notebook
├── data/
│   └── stock_data_test.csv   # Sample stock data
└── source/                    # Additional source files
```

## Requirements

- Python 3.7+
- pandas
- numpy
- yfinance
- matplotlib
- scipy

## Installation

### Option 1: Using Anaconda (Recommended)

1. Clone the repository:
```bash
git clone <repository-url>
cd Portfolio-Optimization
```

2. Create and activate the conda environment:
```bash
conda env create -f environment.yml
conda activate portfolio-optimization
```

3. Launch Jupyter Notebook:
```bash
jupyter notebook
```

### Option 2: Using pip

1. Clone the repository:
```bash
git clone <repository-url>
cd Portfolio-Optimization
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Create a virtual environment:
```bash
python -m venv portfolio_optimization
source portfolio_optimization/bin/activate  # On Windows: portfolio_optimization\Scripts\activate
pip install -r requirements.txt
```

## Usage

1. Open the Jupyter notebook:
```bash
jupyter notebook scripts/data_analysis.ipynb
```

2. Modify the stock symbols and date range in the notebook:
```python
stock_symbol = ["AAPL", "MSFT", "AMZN"]
start_date = "2023-03-15"
end_date = "2025-08-22"
```

3. Run the cells to:
   - Fetch stock data
   - Calculate returns
   - Run Monte Carlo simulation
   - Find optimal portfolios

## How It Works

1. **Data Collection**: The `grab_data.py` module fetches historical stock prices from Yahoo Finance
2. **Returns Calculation**: Converts stock prices to log returns for portfolio analysis
3. **Monte Carlo Simulation**: Generates random portfolio weight combinations and calculates:
   - Expected annualized returns
   - Expected annualized volatility
   - Sharpe ratio (assuming a risk-free rate)
4. **Optimization**: Identifies the portfolio with the highest Sharpe ratio and the one with the lowest volatility

## Example Output

The analysis provides:
- Portfolio weights for each asset
- Expected portfolio returns and volatility
- Sharpe ratio for risk-adjusted performance evaluation
- Optimal portfolios (maximum Sharpe ratio and minimum volatility)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational and research purposes only. It should not be used as the sole basis for investment decisions. Always consult with a qualified financial advisor before making investment decisions.

