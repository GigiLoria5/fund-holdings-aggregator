from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from src.holdings_pipeline import HoldingsPipeline


@pytest.fixture
def mock_holdings_pipeline_run(mocker: MockerFixture) -> MagicMock:
    return mocker.patch.object(HoldingsPipeline, "run")
