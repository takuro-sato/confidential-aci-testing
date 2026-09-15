#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

from __future__ import annotations


def parse_prerelease_policy_api(parser):
    parser.add_argument(
        "--prerelease-policy-api",
        help="Generate Linux policies with confcom's prerelease policy API and framework",
        action="store_true",
    )
