#!/usr/bin/python
# Copyright 2021 Dell Inc. or its subsidiaries. All Rights Reserved


# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: dellemc_vxrail_export_cvs_compliance_report

short_description: Export CVS compliance report

description:
- Export the CVS compliance report that is generated using the provided parameters.
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

  group_by:
    description:
      Group by parameter
    required: False
    type: str

  format:
    description:
      The report's format
    required: False
    type: str

  ids:
    description:
      ID list for the report
    required: False
    type: str

  output_file_path:
    description:
      Specifies the path to save the downloaded file. For example, '/path/to/output_file' indicates the file will be downloaded successfully to that location.
    required: True
    type: str    

  api_version_number:
    description:
      A specific version number to use for the API call. If not included, will use the highest version by default
    required: False
    type: int

  timeout:
    description:
      Time out value for cancelling the host shutdown, the default value is 60 seconds
    required: False
    type: int
    default: 1800

author:
    - VxRail Development Team(@VxRailDevTeam) <ansible.team@dell.com>

'''

EXAMPLES = r'''
    - name: Start to export cvs compliance report
      dellemc_vxrail_export_cvs_compliance_report:
        vxmip: "{{ vxmip }}"
        vcadmin: "{{ vcadmin }}"
        vcpasswd: "{{ vcpasswd }}"
        output_file_path: "{{ output_file_path }}"
'''

RETURN = r'''
changed:
  description: Whether or not the resource has changed
  returned: always
  type: bool
message:
  description: Returns a success message with the downloaded file's name
  returned: always
  type: str
  sample: '/path/to/output_file downloaded successfully'
'''

import logging
import urllib3
from ansible.module_utils.basic import AnsibleModule
import vxrail_ansible_utility
from vxrail_ansible_utility.rest import ApiException
from ansible_collections.dellemc.vxrail.plugins.module_utils import dellemc_vxrail_ansible_utils as utils

# Defining global variables
API = "/cvs-compliance/report"
MODULE = "dellemc_vxrail_export_cvs_compliance_report"
LOG_FILE_PATH = "/tmp/vxrail_ansible_export_cvs_compliance_report.log"

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
        self.group_by = module.params.get('group_by')
        self.format = module.params.get('format')
        self.ids = module.params.get('ids')
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

        # Calls versioned method as attribute (ex: v1_cvs_compliance_report_get)
        call_string = self.api_version_string + '_cvs_compliance_report_get'
        # call_string = 'cvs_compliance_report_get'
        LOGGER.info("Using utility method: %s\n", call_string)
        api_cvs_compliance_report_get = getattr(api_instance, call_string)
        # get the parameters
        params = self.getRequestParams()
        LOGGER.info(f"params: {params}")
        return api_cvs_compliance_report_get(**params)
    
    def getRequestParams(self):
        params = {
            # if you don't set the _preload_content to False, the response will become a string.
            '_preload_content': False,
        }
        if self.group_by:
            params['group_by'] = self.group_by
    
        if self.format:
            params['format'] = self.format
    
        if self.ids:
            params['ids'] = self.ids

        return params            

    def export_cvs_compliance_report(self):
        # create an instance of the API class
        api_instance = vxrail_ansible_utility.CVSPublicApi(vxrail_ansible_utility.ApiClient(self.configuration))
        try:
            # export compliance report
            return self.get_versioned_response(api_instance, "Get /v1/cvs-compliance/report")
        except ApiException as e:
            LOGGER.error("Exception when calling CVSPublicApi->%s_cvs_compliance_report_get: %s\n", self.api_version_string, e)
            return 'error'         


def main():
    ''' Entry point into execution flow '''     
    global module
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        vxmip=dict(required=True),
        vcadmin=dict(required=True),
        vcpasswd=dict(required=True, no_log=True),
        group_by=dict(required=False),
        format=dict(required=False),
        ids=dict(required=False),
        output_file_path=dict(required=True),
        api_version_number=dict(type='int', required=False),
        timeout=dict(type='int', default=1800)
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )
     
    LOGGER.info('----Start to export cvs compliance report: ----')
    response = VxRailCluster().export_cvs_compliance_report()
    if response == "error":
        module.fail_json(
            msg=f"Call {API} API failed, please see log file {LOG_FILE_PATH} for more error details.")

    LOGGER.info(f"Http Result: Status code - {response.status}, URL - {response.geturl()}, Headers - {response.headers}")
    output_file_path = module.params.get('output_file_path')
    LOGGER.info('Outputfile Path: %s\n', output_file_path)
    with open(output_file_path, 'wb') as file:
        file.write(response.data)         
        module.exit_json(changed=True, message=f'{output_file_path} downloaded successfully')


if __name__ == "__main__":
    main()
