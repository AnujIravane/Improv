#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Custom Search.
Command-line application that does a search.
"""

import pprint

from googleapiclient.discovery import build

def googleSearcher(query): 
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  service = build("customsearch", "v1",
            developerKey="AIzaSyBKGScWW0awDoSM9Lgpc_XOgWZiwnLAaDk")

  # API request
  res = service.cse().list(
      q = query,
      cx = '006195875810839919877:rkqpdr9nkyg',
    ).execute()

  # Extract snippets from the query searh results
  results = []
  removedChars = ["\n", "<b>", "</b>"]
  links = res[u'items']

  for link in links:
  	snippet = link[u'snippet']#.replace("xb7", " - ").replace("\xb7", " - ")
  	snippet = snippet[2 : ]
  	for char in removedChars:
		snippet = snippet.replace(char, "")
	results.append(snippet)

  pprint.pprint(results)

def main():
	googleSearcher('lamb')

if __name__ == '__main__':
  main()
