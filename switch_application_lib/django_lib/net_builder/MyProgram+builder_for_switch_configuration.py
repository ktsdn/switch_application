#! /bin/env python

import os,re,copy
from net_builder.MyProgram.commons_utils import commons_utils as COMMONS_UTILS
from ip_manager.models import switch_configuration_urls, switch_network_usages, mgmt_network_ip_pools_for_cstack, mgmt_network_ip_pools_for_ostack, srv_network_ip_pools_for_cstack, srv_network_ip_pools_for_ostack


from TEST_SAMPLE_7124_MLAG import TEST_SAMPLE_7124_MLAG
from TEST_SAMPLE_7124_SINGLE_MGMT_ONLY import TEST_SAMPLE_7124_SINGLE_MGMT_ONLY
from KR1B_CS_T2_7050S_NEX import KR1B_CS_T2_7050S_NEX
from KR1B_CS_T2_7050S_DELL import KR1B_CS_T2_7050S_DELL
from KR1B_CS_T2_7050S_NETAPP import KR1B_CS_T2_7050S_NETAPP



