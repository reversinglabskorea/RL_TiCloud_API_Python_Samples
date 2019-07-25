#!/usr/bin/python
#-*- coding: euc-kr -*-

# This Code is from Titanium Cloud API User Guide Document
#
# TiCloud API Examples
#
# Copyright (c) 2019 ReversingLabs Korea
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.

import argparse
import hashlib
import sys
import os
import io
import json
import urllib.request
import auth

default_metadata_template = \
"""<?xml version="1.0" encoding="UTF-8"?>
<rl>
<properties>
<property>
<name>file_name</name>
<value>{0}</value>
</property>
</properties>
<domain></domain>
</rl>"""

# put server url
sample_service = ''

class file_stream(io.FileIO):
    def __init__(self, file_name):
        super(file_stream, self).__init__(file_name, mode='rb')
        sha1 = hashlib.sha1()
        self.size = 0
        while True:
            data = self.read(8192)
            sha1.update(data)
            self.size += len(data)
            if len(data) != 8192:
                break

        self.seek(0)
        self.sha1 = sha1.hexdigest()

    def __len__(self):
        return self.size

def check(sha1):
    try:
        if len(sha1.decode('hex')) != 20:
            raise ValueError('invalid sha1 hash')
    except TypeError:
        raise ValueError('invalid sha1 hash')

def upload_sample(user, password, sha1, data):
    url = '%s/upload/%s' % (sample_service, sha1)

    headers = auth.generate_headers(user, password)
    headers['Content-Type'] = 'application/octet-stream'

    r = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(r)

    print('upload sample status code:', response.status)

def upload_meta(user, password, sha1, data):
    url = '%s/upload/%s/meta' % (sample_service, sha1)

    headers = auth.generate_headers(user, password)
    headers['Content-Type'] = 'application/octet-stream'

    r = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(r)

    print('upload sample status code:', response.status)

def upload_meta_from_file(user, password, sha1, path):
    data = file(path, 'rb').read()

    upload_meta(user, password, sha1, data)

def upload_default_meta(user, password, sha1, sample):
    file_name = os.path.basename(sample)

    data = default_metadata_template.format(file_name).encode('utf-8')

    upload_meta(user, password, sha1, data)

def upload(user, password, sample_path, meta):
    data = file_stream(sample_path)
    sha1 = data.sha1

    upload_sample(user, password, sha1, data)

    if meta != None:
        upload_meta_from_file(user, password, sha1, meta)
    else:
        upload_default_meta(user, password, sha1, sample_path)

def main():
    global sample_service
    parser = argparse.ArgumentParser(description='ReversingLabs sample upload utility')
    parser.add_argument('--user', metavar='USER', required=True, help='user name')
    parser.add_argument('--password', metavar='PASSWORD', required=True, help='user password')
    parser.add_argument('--service', metavar='SERVICE', required=sample_service, help='service url')

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-u', '--upload', metavar='SAMPLE', help='upload a sample')
    parser.add_argument('-m', '--meta', metavar='META', default=None, help='meta file')

    args = vars(parser.parse_args())

    user = args['user']
    password = args['password']
    sample_service = args['service']

    if args['upload'] != None:
        sample = args['upload']
        meta = args['meta']
        upload(user, password, sample, meta)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Error: ', sys.stderr, str(e))
    sys.exit(0)
