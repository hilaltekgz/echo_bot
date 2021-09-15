#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "e034aaf3-8fd6-4828-9918-5262a56e713e")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "SVF7Q~y-v~yIoXIbIukwvhxRZgDx76Z4beWxm")


