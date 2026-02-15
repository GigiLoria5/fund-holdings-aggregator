# Portfolio Holdings Aggregator

Transforms detailed fund holdings into aggregated data grouped by:

- Country (e.g., United States, Japan)
- Market Type (Developed/Emerging/Frontier) - automatically classified based on MSCI definition
- Currency (USD, EUR, JPY, etc.)
- Sector (Technology, Financials, etc.)
- Aggregated Weight (summed percentages)

## Installation

### Prerequisites

- Python 3.12 or higher
- uv

### Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/GigiLoria5/portfolio-holdings-aggregator.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Basic Usage

```bash
  python portfolio_aggregator.py input_file.xlsx
```

This creates `aggregated_holdings.xlsx` in the current directory.

### Specify Output File

```bash
  python portfolio_aggregator.py holdings.xlsx output.xlsx
```

### Example

```bash
  python portfolio_aggregator.py holdings-daily-emea-en-spyy-gy.xlsx my_aggregated_data.xlsx
```

## Input File Format

The tool expects Excel files with the following columns (header row auto-detected):

| Column                    | Description                      |
|---------------------------|----------------------------------|
| **Security Name**         | Name of the security (required)  |
| **Currency**              | Currency code (USD, EUR, etc.)   |
| **Percent of Fund**       | Weight in the fund as percentage |
| **Trade Country Name**    | Country of the security          |
| **Sector Classification** | Sector name                      |

### Example Input

```
Fund Name: SPDR MSCI All Country World UCITS ETF
ISIN: IE00B44Z5B48
Holdings As Of: 12-Feb-2026

ISIN          | Security Name           | Currency | Percent of Fund | Trade Country Name | Sector Classification
US67066G1040  | NVIDIA Corporation      | USD      | 4.760762        | United States      | Information Technology
US0378331005  | Apple Inc.              | USD      | 4.065740        | United States      | Information Technology
US5949181045  | Microsoft Corporation   | USD      | 2.955187        | United States      | Information Technology
```

The tool automatically:

- Skips metadata rows at the top
- Detects the header row
- Handles missing or malformed data
- Removes empty rows

## Output Format

The output Excel file contains aggregated data with these columns:

| Column          | Description                 | Format             |
|-----------------|-----------------------------|--------------------|
| **Country**     | Country name                | Text               |
| **Market Type** | Developed/Emerging/Frontier | Text               |
| **Currency**    | Currency code               | Text               |
| **Sector**      | Sector classification       | Text               |
| **Weight**      | Aggregated weight           | Percentage (0.00%) |

### Example Output

| Country        | Market Type | Currency | Sector                 | Weight |
|----------------|-------------|----------|------------------------|--------|
| United States  | Developed   | USD      | Health Care            | 9.00%  |
| United States  | Developed   | USD      | Consumer Discretionary | 8.00%  |
| Japan          | Developed   | JPY      | Industrials            | 5.00%  |
| United Kingdom | Developed   | GBP      | Financials             | 3.39%  |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
