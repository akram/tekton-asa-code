# -*- coding: utf-8 -*-
# Author: Chmouel Boudjnah <chmouel@chmouel.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""Constant stuff"""
import os

TEKTON_ASA_CODE_DIR = os.environ.get("TEKTON_ASA_CODE_DIR", ".tekton")

REPOSITORY_DIR = "/tmp/repository"

GITHUB_RAW_URL = "https://raw.githubusercontent.com/tektoncd/catalog/main/task"
GITHUB_API_URL = "https://api.github.com"

COMMENT_ALLOWED_STRING = "/ok-to-test"
COMMENT_RETEST_STRING = "/retest"

TEKTON_CATALOG_REPOSITORY = "tektoncd/catalog"

ALLOW_PRERUNS_CMD = False
