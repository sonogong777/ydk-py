""" Cisco_IOS_XR_ppp_ma_syslog_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-syslog package configuration.

This module contains definitions
for the following management objects\:
  ppp\: PPP configuration

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ppp(Entity):
    """
    PPP configuration
    
    .. attribute:: syslog
    
    	syslog option for session status
    	**type**\:  :py:class:`Syslog <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_syslog_cfg.Ppp.Syslog>`
    
    

    """

    _prefix = 'ppp-ma-syslog-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ppp, self).__init__()
        self._top_entity = None

        self.yang_name = "ppp"
        self.yang_parent_name = "Cisco-IOS-XR-ppp-ma-syslog-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"syslog" : ("syslog", Ppp.Syslog)}
        self._child_list_classes = {}

        self.syslog = Ppp.Syslog()
        self.syslog.parent = self
        self._children_name_map["syslog"] = "syslog"
        self._children_yang_names.add("syslog")
        self._segment_path = lambda: "Cisco-IOS-XR-ppp-ma-syslog-cfg:ppp"


    class Syslog(Entity):
        """
        syslog option for session status
        
        .. attribute:: enable_session_status
        
        	Enable syslog for ppp session status
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'ppp-ma-syslog-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ppp.Syslog, self).__init__()

            self.yang_name = "syslog"
            self.yang_parent_name = "ppp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.enable_session_status = YLeaf(YType.empty, "enable-session-status")
            self._segment_path = lambda: "syslog"
            self._absolute_path = lambda: "Cisco-IOS-XR-ppp-ma-syslog-cfg:ppp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ppp.Syslog, ['enable_session_status'], name, value)

    def clone_ptr(self):
        self._top_entity = Ppp()
        return self._top_entity

