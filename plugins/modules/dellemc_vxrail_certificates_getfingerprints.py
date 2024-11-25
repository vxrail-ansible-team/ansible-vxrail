#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_certificates_getfingerprints

short_description: Return a fingerprint list of the certificates that stored in VXM trust store.

description:
- This module will return a fingerprint list.
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

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for getting system information, the default value is 60 seconds
    required: false
    type: int
    default: 60

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
  - name: Get a fingerprint list
    dellemc_vxrail_certificates_getfingerprints:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
'''

RETURN = r'''
Fingerprint_List:
  description: a fingerprint list of the certificates that stored in VXM trust store.
  returned: always
  type: dict
  sample: >-
    {
        "fingerprint": [
                "E1:47:2B:51:DB:49:2D:93:D8:51:91:8A:5E:B6:E4:19:8F:91:66:A1"
        ]
    }
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

RESULT = "Fingerprint_List"
API = "/trust-store/certificates/fingerprints"
LOG_FILE_PATH = "/tmp/vxrail_ansible_getfingerprints.log"
MODULE = "dellemc_vxrail_certificates_getfingerprints"

LOGGER = utils.get_logger(MODULE, LOG_FILE_PATH, log_devel=logging.DEBUG)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class VxrailSystemUrls():
    cluster_url = 'https://{}/rest/vxm'

    def __init__(self, vxm_ip):
        self.vxm_ip = vxm_ip

    def set_host(self):
        return VxrailSystemUrls.cluster_url.format(self.vxm_ip)


class VxRailSystem():
    def __init__(self):
        self.vxm_ip = module.params.get('vxmip')
        self.timeout = module.params.get('timeout')
        self.vc_admin = module.params.get('vcadmin')
        self.vc_password = module.params.get('vcpasswd')
        self.system_url = VxrailSystemUrls(self.vxm_ip)
        self.api_version_number = module.params.get('api_version_number')
        # Configure HTTP basic authorization: basicAuth
        self.configuration = vxrail_ansible_utility.Configuration()
        self.configuration.username = self.vc_admin
        self.configuration.password = self.vc_password
        self.configuration.verify_ssl = False
        self.configuration.host = self.system_url.set_host()
        self.api_version_string = "v?"

    # Obtains the response for the given module path with specified api_version_number or highest found version
    def get_versioned_response(self, api_instance, module_path):
        # Set api version string and version number if not defined
        if self.api_version_number is None:
            self.api_version_string = utils.get_highest_api_version_string(self.vxm_ip, module_path, LOGGER)
            self.api_version_number = int(self.api_version_string.split('v')[1])
        else:
            self.api_version_string = utils.get_api_version_string(self.vxm_ip, self.api_version_number, module_path, LOGGER)

        # Calls versioned method as attribute (ex: v1_trust_store_certificates_fingerprints_get)
        call_string = self.api_version_string + '_trust_store_certificates_fingerprints_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        trust_store_certificates_get = getattr(api_instance, call_string)
        return trust_store_certificates_get()

    def invoke_public_api(self) -> dict:
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CertificatesApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # Invoke api
            response = self.get_versioned_response(api_instance, "GET /trust-store/certificates/fingerprints")
        except ApiException as e:
            LOGGER.error("Exception when calling CertificatesApi->%_trust_store_certificates_fingerprints_get: %s\n", str(self.api_version_string), e)
            return 'error'
        information = (f"{API} api response: %s\n", response)
        LOGGER.info(information)
        fingerprints_info = {'fingerprint': response.fingerprint}
        return fingerprints_info


def main():
    ''' Entry point into execution flow '''
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        api_version_number=dict(type='int'),
        timeout=dict(type='int', default=60)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
    result = VxRailSystem().invoke_public_api()
    if result == 'error':
        module.fail_json(
            msg=f"Call {API} API failed,please see log file {LOG_FILE_PATH} for more error details.")
    vx_facts = {RESULT: result}
    vx_facts_result = dict(changed=False, API_Facts=vx_facts)
    module.exit_json(**vx_facts_result)


if __name__ == "__main__":
    main()
