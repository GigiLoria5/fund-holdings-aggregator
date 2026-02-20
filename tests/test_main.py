from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from src.holdings_pipeline import HoldingsPipeline
from src.main import InputFileRequired, main, parse_arguments


@pytest.mark.parametrize(
    ("args", "expected_input", "expected_output"),
    [
        (
            ["input.xlsx"],
            Path("input.xlsx"),
            Path("aggregated_holdings.xlsx"),
        ),
        (
            ["input.xlsx", "output.xlsx"],
            Path("input.xlsx"),
            Path("output.xlsx"),
        ),
        (
            ["data/holdings.xlsx", "results/aggregated.xlsx"],
            Path("data/holdings.xlsx"),
            Path("results/aggregated.xlsx"),
        ),
        (
            ["/absolute/path/input.xlsx"],
            Path("/absolute/path/input.xlsx"),
            Path("aggregated_holdings.xlsx"),
        ),
    ],
)
def test_parse_arguments_valid(
    args: list[str], expected_input: Path, expected_output: Path
) -> None:
    input_file, output_file = parse_arguments(args)

    assert input_file == expected_input
    assert output_file == expected_output


@pytest.mark.parametrize("args", [[], None])
def test_parse_arguments_invalid(args: list[str] | None) -> None:
    with pytest.raises(InputFileRequired):
        parse_arguments(args)


@pytest.mark.parametrize(
    ("args", "expected_input", "expected_output"),
    [
        (
            ["test_input.xlsx"],
            Path("test_input.xlsx"),
            Path("aggregated_holdings.xlsx"),
        ),
        (
            ["test_input.xlsx", "test_output.xlsx"],
            Path("test_input.xlsx"),
            Path("test_output.xlsx"),
        ),
        (
            ["data/holdings.xlsx", "results/output.xlsx"],
            Path("data/holdings.xlsx"),
            Path("results/output.xlsx"),
        ),
    ],
)
def test_main_success(
    mock_holdings_pipeline_run: MagicMock,
    args: list[str],
    expected_input: Path,
    expected_output: Path,
) -> None:
    exit_code = main(args)

    assert exit_code == 0
    mock_holdings_pipeline_run.assert_called_once_with(expected_input, expected_output)


def _mock_holdings_pipeline_run(mocker: MockerFixture) -> MagicMock:
    return mocker.patch.object(HoldingsPipeline, "run")


@pytest.mark.parametrize(
    "args",
    [[], None],
)
def test_main_no_arguments(args: list[str] | None) -> None:
    exit_code = main(args)

    assert exit_code == 1


@pytest.mark.parametrize(
    ("exception", "error_message"),
    [
        (FileNotFoundError("File not found"), "File not found"),
        (ValueError("Invalid data"), "Invalid data"),
        (KeyError("Missing column"), "Missing column"),
        (Exception("Generic error"), "Generic error"),
    ],
)
def test_main_error_handling(
    mock_holdings_pipeline_run: MagicMock,
    exception: Exception,
    error_message: str,
    capsys: Any,
) -> None:
    mock_holdings_pipeline_run.side_effect = exception

    exit_code = main(["input.xlsx"])

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "✗ Error:" in captured.err
    assert error_message in captured.err


def test_main_default_output_path(mock_holdings_pipeline_run: MagicMock) -> None:
    input_path = "test_input.xlsx"

    main([input_path])

    mock_holdings_pipeline_run.assert_called_once()
    call_args = mock_holdings_pipeline_run.call_args[0]
    assert call_args[0] == Path(input_path)
    assert call_args[1] == Path("aggregated_holdings.xlsx")
