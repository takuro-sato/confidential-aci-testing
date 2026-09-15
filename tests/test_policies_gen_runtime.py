#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

from c_aci_testing.tools.policies_gen import (
    PRERELEASE_POLICY_API_ENV,
    _az_command,
    _prerelease_policy_api_enabled,
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
