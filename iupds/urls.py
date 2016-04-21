# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include, url

from iupdsmanager.views import request_token, token_callback,request_authorization, test

urlpatterns = [
    # url(r'^third-party/', include('iupdsmanager.urls')),
    url(r'^api/v1/request_token/$', request_token, name='request_token'),
    url(r'^api/v1/token_callback/$', token_callback, name='token_callback'),
    url(r'^third-party/', include('msg.urls')),
    url(r'^pds/contacts/', request_authorization, name='request_token'),
    url(r'^test/', test, name='test'),
]
