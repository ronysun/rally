# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally.common import cfg

OPTS = {"openstack": [
    cfg.FloatOpt("vm_ping_poll_interval",
                 default=1.0,
                 deprecated_group="benchmark",
                 help="Interval between checks when waiting for a VM to "
                 "become pingable"),
    cfg.FloatOpt("vm_ping_timeout",
                 default=120.0,
                 deprecated_group="benchmark",
                 help="Time to wait for a VM to become pingable")
]}
