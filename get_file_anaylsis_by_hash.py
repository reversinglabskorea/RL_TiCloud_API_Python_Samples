#-*- coding: euc-kr -*-

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
import requests
import os
import auth

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='ReversingLabs file analysis by hash')
    parser.add_argument('--user', metavar='USER', required=True, help='user name')
    parser.add_argument('--password', metavar='PASSWORD', required=True, help='user password')
    parser.add_argument('--service', metavar='SERVICE', required=True, help='service url')

    args = vars(parser.parse_args())

    username = args['user']
    password = args['password']
    addr = args['service']

    hd = auth.generate_headers(username, password)

    hash_code = input('put Hash Value you want to analyze: ')
    result_format = 'json' # json or xml

    # TCA0104 - File Analysis
    response = requests.get('%s/api/databrowser/rldata/query/sha1/%s?format=%s' % (addr, hash_code, result_format),
                           headers = hd)

    print('Response status code:', response.status_code)

    # Save the result > depends on a format type
    file_name = 'fileanalyze_%s.%s' % (hash_code, result_format)
    with open(file_name, "w", encoding='UTF8') as fp:
        fp.write(response.text)
        print(os.getcwd()+"\\"+file_name+" SAVED")
