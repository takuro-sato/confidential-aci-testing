#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

import json
import subprocess

from c_aci_testing.utils import parse_bicep as parse_bicep_module


def test_parse_bicep_requests_text_output(monkeypatch):
    template = {
        "parameters": {},
        "resources": [],
        "metadata": "contains an en dash \u2013",
    }
    output = {
        "templateJson": json.dumps(template),
        "parametersJson": json.dumps({"parameters": {}}),
    }

    monkeypatch.setattr(
        parse_bicep_module,
        "find_bicep_files",
        lambda target_path: ("main.bicep", "main.bicepparam"),
    )
    monkeypatch.setattr(parse_bicep_module, "aci_param_set", lambda *args, **kwargs: None)

    def fake_run(*args, **kwargs):
        assert kwargs["text"] is True
        return subprocess.CompletedProcess(args[0], 0, stdout=json.dumps(output))

    monkeypatch.setattr(subprocess, "run", fake_run)

    result = parse_bicep_module.parse_bicep(
        "workload",
        "subscription",
        "resource-group",
        "deployment",
        "registry",
        None,
        None,
    )

    assert result == template
