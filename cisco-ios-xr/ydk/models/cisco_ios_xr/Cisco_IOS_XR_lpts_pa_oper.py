""" Cisco_IOS_XR_lpts_pa_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pa package operational data.

This module contains definitions
for the following management objects\:
  lpts\-pa\: lpts pre\-ifib data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LptsPa(Entity):
    """
    lpts pre\-ifib data
    
    .. attribute:: entry_xr
    
    	lpts pa bindings
    	**type**\:  :py:class:`EntryXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr>`
    
    .. attribute:: entries
    
    	lpts pa clients
    	**type**\:  :py:class:`Entries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.Entries>`
    
    

    """

    _prefix = 'lpts-pa-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(LptsPa, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts-pa"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-pa-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"entry-xr" : ("entry_xr", LptsPa.EntryXr), "entries" : ("entries", LptsPa.Entries)}
        self._child_list_classes = {}

        self.entry_xr = LptsPa.EntryXr()
        self.entry_xr.parent = self
        self._children_name_map["entry_xr"] = "entry-xr"
        self._children_yang_names.add("entry-xr")

        self.entries = LptsPa.Entries()
        self.entries.parent = self
        self._children_name_map["entries"] = "entries"
        self._children_yang_names.add("entries")
        self._segment_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa"


    class EntryXr(Entity):
        """
        lpts pa bindings
        
        .. attribute:: entry
        
        	Data for single PA Binding
        	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr.Entry>`
        
        

        """

        _prefix = 'lpts-pa-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(LptsPa.EntryXr, self).__init__()

            self.yang_name = "entry-xr"
            self.yang_parent_name = "lpts-pa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"entry" : ("entry", LptsPa.EntryXr.Entry)}

            self.entry = YList(self)
            self._segment_path = lambda: "entry-xr"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LptsPa.EntryXr, [], name, value)


        class Entry(Entity):
            """
            Data for single PA Binding
            
            .. attribute:: entry  <key>
            
            	Single Binding entry
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: ctime
            
            	Creation Time
            	**type**\:  :py:class:`Ctime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr.Entry.Ctime>`
            
            .. attribute:: utime
            
            	Update Time
            	**type**\:  :py:class:`Utime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.EntryXr.Entry.Utime>`
            
            .. attribute:: location
            
            	Rack/slot/instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_id
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vid
            
            	VR/VRF ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cookie
            
            	Cookie
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l3protocol
            
            	Layer 3 protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: l4protocol
            
            	Layer 4 protocol
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: smask
            
            	Filter operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ifs
            
            	Ifhandle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ptype
            
            	Packet type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ip
            
            	Local address
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: remote_ip
            
            	Remote address
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            .. attribute:: local_len
            
            	Local address length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: remote_len
            
            	Remote address length
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: local_port
            
            	Local port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: remote_port
            
            	Remote port
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: packet_misc
            
            	L5 info
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: scope
            
            	Scope
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_flags
            
            	Client flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: min_ttl
            
            	Minimum TTL
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: lazy_bindq_delay
            
            	 lazy binding queue delay
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ptq_delay
            
            	 pending transactions queue delay
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'lpts-pa-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(LptsPa.EntryXr.Entry, self).__init__()

                self.yang_name = "entry"
                self.yang_parent_name = "entry-xr"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ctime" : ("ctime", LptsPa.EntryXr.Entry.Ctime), "utime" : ("utime", LptsPa.EntryXr.Entry.Utime)}
                self._child_list_classes = {}

                self.entry = YLeaf(YType.str, "entry")

                self.location = YLeaf(YType.uint32, "location")

                self.client_id = YLeaf(YType.uint32, "client-id")

                self.vid = YLeaf(YType.uint32, "vid")

                self.cookie = YLeaf(YType.uint32, "cookie")

                self.l3protocol = YLeaf(YType.uint32, "l3protocol")

                self.l4protocol = YLeaf(YType.uint32, "l4protocol")

                self.smask = YLeaf(YType.uint32, "smask")

                self.ifs = YLeaf(YType.uint32, "ifs")

                self.ptype = YLeaf(YType.uint32, "ptype")

                self.local_ip = YLeaf(YType.str, "local-ip")

                self.remote_ip = YLeaf(YType.str, "remote-ip")

                self.local_len = YLeaf(YType.uint8, "local-len")

                self.remote_len = YLeaf(YType.uint8, "remote-len")

                self.local_port = YLeaf(YType.uint16, "local-port")

                self.remote_port = YLeaf(YType.uint16, "remote-port")

                self.packet_misc = YLeaf(YType.uint32, "packet-misc")

                self.scope = YLeaf(YType.uint32, "scope")

                self.client_flags = YLeaf(YType.uint32, "client-flags")

                self.min_ttl = YLeaf(YType.uint8, "min-ttl")

                self.lazy_bindq_delay = YLeaf(YType.uint32, "lazy-bindq-delay")

                self.ptq_delay = YLeaf(YType.uint32, "ptq-delay")

                self.ctime = LptsPa.EntryXr.Entry.Ctime()
                self.ctime.parent = self
                self._children_name_map["ctime"] = "ctime"
                self._children_yang_names.add("ctime")

                self.utime = LptsPa.EntryXr.Entry.Utime()
                self.utime.parent = self
                self._children_name_map["utime"] = "utime"
                self._children_yang_names.add("utime")
                self._segment_path = lambda: "entry" + "[entry='" + self.entry.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/entry-xr/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LptsPa.EntryXr.Entry, ['entry', 'location', 'client_id', 'vid', 'cookie', 'l3protocol', 'l4protocol', 'smask', 'ifs', 'ptype', 'local_ip', 'remote_ip', 'local_len', 'remote_len', 'local_port', 'remote_port', 'packet_misc', 'scope', 'client_flags', 'min_ttl', 'lazy_bindq_delay', 'ptq_delay'], name, value)


            class Ctime(Entity):
                """
                Creation Time
                
                .. attribute:: tv_sec
                
                	Time Sec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tv_nsec
                
                	Time Nanosec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lpts-pa-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(LptsPa.EntryXr.Entry.Ctime, self).__init__()

                    self.yang_name = "ctime"
                    self.yang_parent_name = "entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.tv_sec = YLeaf(YType.uint32, "tv-sec")

                    self.tv_nsec = YLeaf(YType.uint32, "tv-nsec")
                    self._segment_path = lambda: "ctime"

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPa.EntryXr.Entry.Ctime, ['tv_sec', 'tv_nsec'], name, value)


            class Utime(Entity):
                """
                Update Time
                
                .. attribute:: tv_sec
                
                	Time Sec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: tv_nsec
                
                	Time Nanosec
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'lpts-pa-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(LptsPa.EntryXr.Entry.Utime, self).__init__()

                    self.yang_name = "utime"
                    self.yang_parent_name = "entry"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.tv_sec = YLeaf(YType.uint32, "tv-sec")

                    self.tv_nsec = YLeaf(YType.uint32, "tv-nsec")
                    self._segment_path = lambda: "utime"

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPa.EntryXr.Entry.Utime, ['tv_sec', 'tv_nsec'], name, value)


    class Entries(Entity):
        """
        lpts pa clients
        
        .. attribute:: entry
        
        	Data for single PA Client
        	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pa_oper.LptsPa.Entries.Entry>`
        
        

        """

        _prefix = 'lpts-pa-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(LptsPa.Entries, self).__init__()

            self.yang_name = "entries"
            self.yang_parent_name = "lpts-pa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"entry" : ("entry", LptsPa.Entries.Entry)}

            self.entry = YList(self)
            self._segment_path = lambda: "entries"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LptsPa.Entries, [], name, value)


        class Entry(Entity):
            """
            Data for single PA Client
            
            .. attribute:: entry  <key>
            
            	Single Client entry
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: flags
            
            	Client flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: open_flags
            
            	Open flags
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: location
            
            	Rack/slot/instance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: client_id
            
            	Client ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: times
            
            	Transaction statisitics
            	**type**\: str
            
            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
            
            

            """

            _prefix = 'lpts-pa-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(LptsPa.Entries.Entry, self).__init__()

                self.yang_name = "entry"
                self.yang_parent_name = "entries"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.entry = YLeaf(YType.str, "entry")

                self.flags = YLeaf(YType.uint32, "flags")

                self.open_flags = YLeaf(YType.uint32, "open-flags")

                self.location = YLeaf(YType.uint32, "location")

                self.client_id = YLeaf(YType.uint32, "client-id")

                self.times = YLeaf(YType.str, "times")
                self._segment_path = lambda: "entry" + "[entry='" + self.entry.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pa-oper:lpts-pa/entries/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LptsPa.Entries.Entry, ['entry', 'flags', 'open_flags', 'location', 'client_id', 'times'], name, value)

    def clone_ptr(self):
        self._top_entity = LptsPa()
        return self._top_entity

