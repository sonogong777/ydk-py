""" Cisco_IOS_XR_linux_os_reboot_history_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR linux\-os\-reboot\-history package operational data.

This module contains definitions
for the following management objects\:
  reboot\-history\: Reboot History information

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RebootHistory(Entity):
    """
    Reboot History information
    
    .. attribute:: node
    
    	Node ID
    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper.RebootHistory.Node>`
    
    

    """

    _prefix = 'linux-os-reboot-history-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(RebootHistory, self).__init__()
        self._top_entity = None

        self.yang_name = "reboot-history"
        self.yang_parent_name = "Cisco-IOS-XR-linux-os-reboot-history-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"node" : ("node", RebootHistory.Node)}

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-linux-os-reboot-history-oper:reboot-history"

    def __setattr__(self, name, value):
        self._perform_setattr(RebootHistory, [], name, value)


    class Node(Entity):
        """
        Node ID
        
        .. attribute:: node_name  <key>
        
        	Node name
        	**type**\: str
        
        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
        
        .. attribute:: reboot_history
        
        	Last Reboots
        	**type**\: list of  		 :py:class:`RebootHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_linux_os_reboot_history_oper.RebootHistory.Node.RebootHistory>`
        
        

        """

        _prefix = 'linux-os-reboot-history-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(RebootHistory.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "reboot-history"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"reboot-history" : ("reboot_history", RebootHistory.Node.RebootHistory)}

            self.node_name = YLeaf(YType.str, "node-name")

            self.reboot_history = YList(self)
            self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-linux-os-reboot-history-oper:reboot-history/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RebootHistory.Node, ['node_name'], name, value)


        class RebootHistory(Entity):
            """
            Last Reboots
            
            .. attribute:: no
            
            	Number count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: time
            
            	Time of reboot
            	**type**\: str
            
            .. attribute:: cause_code
            
            	Cause code for reboot
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: reason
            
            	Reason for reboot
            	**type**\: str
            
            

            """

            _prefix = 'linux-os-reboot-history-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(RebootHistory.Node.RebootHistory, self).__init__()

                self.yang_name = "reboot-history"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.no = YLeaf(YType.uint32, "no")

                self.time = YLeaf(YType.str, "time")

                self.cause_code = YLeaf(YType.uint32, "cause-code")

                self.reason = YLeaf(YType.str, "reason")
                self._segment_path = lambda: "reboot-history"

            def __setattr__(self, name, value):
                self._perform_setattr(RebootHistory.Node.RebootHistory, ['no', 'time', 'cause_code', 'reason'], name, value)

    def clone_ptr(self):
        self._top_entity = RebootHistory()
        return self._top_entity

