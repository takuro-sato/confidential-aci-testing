#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

from pathlib import Path

from c_aci_testing.tools.policies_gen import (
    PRERELEASE_POLICY_API_ENV,
    _az_command,
    _prerelease_policy_api_enabled,
    _write_policy_file,
)


def test_prerelease_policy_api_explicitly_enabled(monkeypatch):
    monkeypatch.delenv(PRERELEASE_POLICY_API_ENV, raising=False)

    assert _prerelease_policy_api_enabled(True)


def test_prerelease_policy_api_enabled_by_environment(monkeypatch):
    monkeypatch.setenv(PRERELEASE_POLICY_API_ENV, "true")

    assert _prerelease_policy_api_enabled(False)


def test_prerelease_policy_api_disabled_by_default(monkeypatch):
    monkeypatch.delenv(PRERELEASE_POLICY_API_ENV, raising=False)

    assert not _prerelease_policy_api_enabled(False)


def test_az_command_matches_platform():
    assert _az_command() in ("az", "az.bat")


def test_policy_file_write_preserves_crlf(tmp_path):
    policy = "package policy\r\n\r\napi_version := \"0.12.0\"\r\n"
    policy_path = Path(tmp_path) / "policy_test.rego"

    _write_policy_file(str(policy_path), policy)

    assert policy_path.read_bytes() == policy.encode("utf-8")
