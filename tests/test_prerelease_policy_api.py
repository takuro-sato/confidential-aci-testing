#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

import argparse

from c_aci_testing.args.parameters.prerelease_policy_api import (
    parse_prerelease_policy_api,
)


def test_prerelease_policy_api_defaults_to_false():
    parser = argparse.ArgumentParser()
    parse_prerelease_policy_api(parser)

    assert parser.parse_args([]).prerelease_policy_api is False


def test_prerelease_policy_api_can_be_enabled():
    parser = argparse.ArgumentParser()
    parse_prerelease_policy_api(parser)

    assert parser.parse_args(["--prerelease-policy-api"]).prerelease_policy_api is True
