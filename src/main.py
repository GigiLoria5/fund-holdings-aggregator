import sys
from pathlib import Path

from src.holdings_pipeline import HoldingsPipeline


def main(args: list[str] | None = None) -> int:
    if args is None:
        args = sys.argv[1:]
    if not args:
        _print_usage()
        return 1
    try:
        input_file, output_file = parse_arguments(args)
        HoldingsPipeline.run(input_file, output_file)
        return 0
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        return 1


def _print_usage() -> None:
    print("Usage: python -m src.main <input_file.xlsx> [output_file.xlsx]")
    print("Example: python -m src.main holdings.xlsx aggregated.xlsx")


def parse_arguments(args: list[str]) -> tuple[Path, Path]:
    if len(args) < 1:
        raise ValueError("Input file path is required")
    input_file = Path(args[0])
    output_file = Path(args[1]) if len(args) > 1 else Path("aggregated_holdings.xlsx")
    return input_file, output_file


if __name__ == "__main__":
    main()
