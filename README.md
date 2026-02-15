# Fund Holdings Aggregator

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
    git clone https://github.com/GigiLoria5/fund-holdings-aggregator.git
    ```

2. Install dependencies:

    ```bash
    make install
    ```

## Usage

### Using the Makefile (Recommended)

```bash
# View all available commands
make help

# Run with input file (creates aggregated_holdings.xlsx)
make run INPUT=holdings.xlsx

# Specify custom output file
make run INPUT=holdings.xlsx OUTPUT=my_output.xlsx
```

## Input File Format

Your Excel file needs **4 columns** containing these keywords (case-insensitive, partial match):

| Keyword      | Description           | Example Column Names                        |
|--------------|-----------------------|---------------------------------------------|
| **Currency** | Currency code         | "Currency", "Trade Currency", "CURRENCY"    |
| **Percent**  | Weight/percentage     | "Percent of Fund", "Weight %", "percent"    |
| **Country**  | Country name          | "Country", "Trade Country Name", "COUNTRY"  |
| **Sector**   | Sector classification | "Sector", "Sector Classification", "SECTOR" |

**Important:** Each keyword must appear in exactly ONE column (unique match).

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
- Detects the header row by matching columns case-insensitively
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

## Testing

```bash
# Run tests with pytest
make test
```

## Contributing

Contributions are welcome!

```bash
# Fork and clone
git clone https://github.com/yourusername/fund-holdings-aggregator.git

# Create a feature branch
git checkout -b feature/my-feature

# Format code
make lint

# Test changes
make test

# Commit and push
git commit -am "Add feature"
git push origin feature/my-feature
```

## License

MIT License - See [LICENSE](LICENSE) for details.

