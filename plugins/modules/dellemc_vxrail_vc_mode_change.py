#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_vc_mode_change

short_description: Change the VxRail vCenter or Platform Services Controller (PSC) mode

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.6.0"

description:
- This module will change the VxRail vCenter or Platform Services Controller (PSC) mode between embedded mode and external mode.
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

  vc_mode:
    description:
      Target vCenter mode, allowed values is EXTERNAL, EMBEDDED.
    required: True
    type: str

  psc_mode:
    description:
      Target PSC mode, allowed values is EMBEDDED, EXTERNAL.
    required: True
    type: str

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for converting vc, the default value is 60 seconds
    required: false
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
    - name: Start to change the VxRail vCenter mode
      dellemc_vxrail_vc_mode_change:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        vc_mode: "{{ vc_mode }}"
        psc_mode: "{{ psc_mode }}"
        timeout: "{{ timeout }}"
        api_version_number: "{{ api_version_number }}"
'''

RETURN = r'''
Patch_VC_Mode_API:
  description: Returns the request ID and whether the operation was successful.
  returned: always
  type: dict
  sample: >-
        {
            "Request_ID": "SBI_2",
            "Request_Status": "COMPLETED"
        }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
import time
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "/vc/mode"
MODULE = "dellemc_vxrail_vc_mode_change"
LOG_FILE_PATH = "/tmp/vxrail_ansible_vc_mode_change.log"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
CHECK_STATUS_INTERVAL = 30
MAX_CHECK_COUNT = 60


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
        self.vc_mode = module.params.get('vc_mode')
        self.psc_mode = module.params.get('psc_mode')
        self.api_version_number = module.params.get('api_version_number')
        self.system_url = VxrailClusterUrls(self.vxm_ip)
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        # Added for auto-version detection
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if undefined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_vc_vc_mode_patch)
        call_string = self.api_version_string + '_vc_vc_mode_patch'
        LOGGER.info("Using utility method: %s\n", call_string)
        vcmode_info = {}
        vcadmin_spec = {
            "username": self.vc_admin,
            "password": self.vc_password
        }
        vcmode_info['vc_admin_user'] = vcadmin_spec
        vcmode_info['vc_mode'] = self.vc_mode
        vcmode_info['psc_mode'] = self.psc_mode
        LOGGER.info("json: %s\n", vcmode_info)
        api_vc_mode_patch = getattr(api_instance, call_string)
        return api_vc_mode_patch(vcmode_info)

    def patch_vc_mode(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.VCenterServerModeApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # patch vc mode
            response = self.get_versioned_response(api_instance, "Patch /vc/mode")
        except ApiException as e:
            LOGGER.error("Exception when calling VCenterServerModeApi->%s_vc_vc_mode_patch: %s\n", self.api_version_string, e)
            return 'error'
        requestid = response.request_id
        return requestid


def main():
    ''' Entry point into execution flow '''
    result_request_id = ''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        vc_mode=dict(required=True),
        psc_mode=dict(required=True),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=1800)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result_status = 0
    time_out = 0
    initial_timeout = module.params.get('timeout')
    LOGGER.info('----Start to change vc mode: ----')
    result_request_id = VxRailCluster().patch_vc_mode()
    LOGGER.info('ConvertVC task_ID: %s.', result_request_id)
    if result_request_id == "error":
        module.fail_json(
            msg=f"The request id is not returned. Please see the log file {LOG_FILE_PATH} for more details")
    while result_status not in ('COMPLETED', 'FAILED') and time_out < initial_timeout:
        result_response = utils.get_request_status(vxm_ip=module.params.get('vxmip'), vcadmin=module.params.get('vcadmin'),
                                                   vcpasswd=module.params.get('vcpasswd'), logger=LOGGER,
                                                   request_id=result_request_id)
        result_status = result_response.state
        LOGGER.info('ConvertVC_Task: status: %s.', result_status)
        LOGGER.info('ConvertVC_Task: details: %s.', result_response)
        LOGGER.info("ConvertVC_Task: Sleeping %s seconds...", CHECK_STATUS_INTERVAL)
        time.sleep(CHECK_STATUS_INTERVAL)
        time_out = time_out + CHECK_STATUS_INTERVAL
    if result_status == 'COMPLETED':
        LOGGER.info("-------ConvertVC_Task is successful.-----")
    else:
        LOGGER.info("------ConvertVC_Task Failed.-----")
        vc_mode_change = {'request_id': result_request_id}
        vx_facts_result = dict(failed=True, Patch_VC_Mode_API=vc_mode_change,
                               msg=f"Converting VC has failed. Please see the {LOG_FILE_PATH} for more details")
        module.exit_json(**vx_facts_result)
    vc_mode_change = {'request_status': result_status, 'request_id': result_request_id}
    vx_facts_result = dict(changed=True, Patch_VC_Mode_API=vc_mode_change,
                           msg=f"Converting VC is successful. Please see the {LOG_FILE_PATH} for more details")
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()