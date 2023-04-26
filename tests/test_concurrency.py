# SPDX-FileCopyrightText: 2022 James R. Barlow
# SPDX-License-Identifier: MPL-2.0

from __future__ import annotations

import os

import pytest

from ocrmypdf import ExitCode

from .conftest import run_ocrmypdf_api


@pytest.mark.skipif(True, reason="--use-threads is currently default")
@pytest.mark.skipif(os.name == 'nt', reason="Windows doesn't have SIGKILL")
def test_simulate_oom_killer(multipage, no_outpdf):
    exitcode = run_ocrmypdf_api(
        multipage,
        no_outpdf,
        '--force-ocr',
        '--plugin',
        'tests/plugins/tesseract_simulate_oom_killer.py',
    )
    assert exitcode == ExitCode.child_process_error
