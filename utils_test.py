# coding: utf-8
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Jeremy Emerson'

import test_utils
import utils


class FakeEntity(object):

    def __init__(self, name, entity_id, ancestor=None, user=None):
        self.__name__ = name
        self.name = name
        self.id = entity_id
        self.key = entity_id
        if ancestor:
            self.ancestor = ancestor
        if user:
            self.user = user
        self.param = True

    def get_by_id(self, query_id):
        if query_id == self.id:
            return self

    def query(self, ancestor=None):
        if not ancestor:
            return self
        if self.ancestor.key == ancestor:
            return self
        return None

    def filter(self, param):
        self.param = param
        return self

    def get(self):
        if self.param:
            return self
        return None


class UtilsTests(test_utils.AppEngineTestBase):
    """Test the exploration model."""

    def test_create_enum_method(self):
        """Test create_enum Method."""
        o = utils.create_enum('first', 'second', 'third')
        self.assertEqual(o.first, 'first')
        self.assertEqual(o.second, 'second')
        self.assertEqual(o.third, 'third')
        with self.assertRaises(AttributeError):
            o.fourth

