#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_callhome_change_mode

short_description: Change the call home mode.

description:
- This module will change the call home mode.
options:

  vxmip:
    description:
      The IP address of the VxRail Manager System
    required: True
    type: str

  vcadmin:
    description:
      Administrative account of the vCenter Server the VxRail Manager is registered to
    required: True
    type: str

  vcpasswd:
    description:
      The password for the administrator account provided in vcadmin
    required: True
    type: str

  is_muted:
    description:
      Whether call home mode is muted or unmuted. Supported values are true and false. True indicates that call home is muted.
    required: True
    type: bool

  timeout:
    description:
      Time out value for changing Callhome mode, the default value is 60 seconds
    required: false
    type: int
    default: 60

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: false
    type: int

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Change callhome mode information
    dellemc_vxrail_callhome_change_mode:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        is_muted: "{{ is_muted }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
CallHome_Mode_Change:
  description: Change callhome mode
  returned: always
  type: dict
  sample: >-
        {
                "Result": "Call home mode is changed successfully"
            }

'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

LOGGER = utils.get_logger("dellemc_vxrail_callhome_change_mode", "/tmp/vxrail_ansible_callhome_change_mode.log",
                          log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailClusterUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailClusterUrls.cluster_url.format(self.vxm_ip)


class VxRailCluster():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.is_muted = module.params.get('is_muted')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        callhome_info = {}
        callhome_info['is_muted'] = self.is_muted

        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path,
                                                                   LOGGER)

        # Calls versioned method as attribute (ex: v1_calhome_mode_put)
        call_string = self.api_version_string + "_callhome_mode_put"
        LOGGER.info("Using utility method: %s\n", call_string)
        callhome_mode_change = getattr(api_instance, call_string)
        return callhome_mode_change(callhome_info)

    def put_callhome_mode(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CallHomeModeApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Change CallHome Mode
            response = self.get_versioned_response(api_instance, "Put /callhome/mode")
        except ApiException as e:
            LOGGER.error("Exception when calling CallHomeModeApi->%s_calhome_mode_put: %s\n", self.api_version_string,
                         e)
            return 'error'
        LOGGER.info("%s/callhome/mode api response: %s\n", self.api_version_string, response)
        return response


def main():
    ''' Entry point into execution flow '''
    result = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        is_muted=dict(required=True, type='bool'),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailCluster().put_callhome_mode()
    if result == 'error':
        module.fail_json(msg="Call PUT /callhome/mode API failed,"
                             "please see log file /tmp/vxrail_ansible_callhome_change_mode.log for more error details.")
    vx_facts = {'Result': 'Call home mode is changed successfully'}
    vx_facts_result = dict(changed=True, CallHome_Mode_Change=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
