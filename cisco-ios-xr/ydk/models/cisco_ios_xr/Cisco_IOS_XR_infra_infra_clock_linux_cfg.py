""" Cisco_IOS_XR_infra_infra_clock_linux_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-clock\-linux package configuration.

This module contains definitions
for the following management objects\:
  clock\: Configure time\-of\-day clock

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Clock(Entity):
    """
    Configure time\-of\-day clock
    
    .. attribute:: time_zone
    
    	Configure time zone
    	**type**\:  :py:class:`TimeZone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg.Clock.TimeZone>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'infra-infra-clock-linux-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Clock, self).__init__()
        self._top_entity = None

        self.yang_name = "clock"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-clock-linux-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"time-zone" : ("time_zone", Clock.TimeZone)}
        self._child_list_classes = {}

        self.time_zone = None
        self._children_name_map["time_zone"] = "time-zone"
        self._children_yang_names.add("time-zone")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock"


    class TimeZone(Entity):
        """
        Configure time zone
        
        .. attribute:: time_zone_name
        
        	Name of time zone
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: area_name
        
        	Area File in zoneinfo package
        	**type**\: str
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-linux-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Clock.TimeZone, self).__init__()

            self.yang_name = "time-zone"
            self.yang_parent_name = "clock"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}
            self.is_presence_container = True

            self.time_zone_name = YLeaf(YType.str, "time-zone-name")

            self.area_name = YLeaf(YType.str, "area-name")
            self._segment_path = lambda: "time-zone"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Clock.TimeZone, ['time_zone_name', 'area_name'], name, value)

    def clone_ptr(self):
        self._top_entity = Clock()
        return self._top_entity

