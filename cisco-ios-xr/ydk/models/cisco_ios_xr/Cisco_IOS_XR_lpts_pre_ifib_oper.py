""" Cisco_IOS_XR_lpts_pre_ifib_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pre\-ifib package operational data.

This module contains definitions
for the following management objects\:
  lpts\-pifib\: lpts pre\-ifib data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LptsPifib(Enum):
    """
    LptsPifib

    Lpts pifib

    .. data:: isis = 0

    	ISIS packets

    .. data:: ipv4_frag = 1

    	IPv4 fragmented packets

    .. data:: ipv4_echo = 2

    	IPv4 ICMP Echo packets

    .. data:: ipv4_any = 3

    	All IPv4 packets

    .. data:: ipv6_frag = 4

    	IPv6 fragmented packets

    .. data:: ipv6_echo = 5

    	IPv6 ICMP Echo packets

    .. data:: ipv6_nd = 6

    	IPv6 ND packets

    .. data:: ipv6_any = 7

    	All IPv6 packets

    .. data:: bfd_any = 8

    	BFD packets

    .. data:: all = 9

    	All packets

    """

    isis = Enum.YLeaf(0, "isis")

    ipv4_frag = Enum.YLeaf(1, "ipv4-frag")

    ipv4_echo = Enum.YLeaf(2, "ipv4-echo")

    ipv4_any = Enum.YLeaf(3, "ipv4-any")

    ipv6_frag = Enum.YLeaf(4, "ipv6-frag")

    ipv6_echo = Enum.YLeaf(5, "ipv6-echo")

    ipv6_nd = Enum.YLeaf(6, "ipv6-nd")

    ipv6_any = Enum.YLeaf(7, "ipv6-any")

    bfd_any = Enum.YLeaf(8, "bfd-any")

    all = Enum.YLeaf(9, "all")



class LptsPifib_(Entity):
    """
    lpts pre\-ifib data
    
    .. attribute:: nodes
    
    	List of Pre\-ifib Nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes>`
    
    

    """

    _prefix = 'lpts-pre-ifib-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(LptsPifib_, self).__init__()
        self._top_entity = None

        self.yang_name = "lpts-pifib"
        self.yang_parent_name = "Cisco-IOS-XR-lpts-pre-ifib-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"nodes" : ("nodes", LptsPifib_.Nodes)}
        self._child_list_classes = {}

        self.nodes = LptsPifib_.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib"


    class Nodes(Entity):
        """
        List of Pre\-ifib Nodes
        
        .. attribute:: node
        
        	Pre\-ifib data for particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node>`
        
        

        """

        _prefix = 'lpts-pre-ifib-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(LptsPifib_.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "lpts-pifib"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", LptsPifib_.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LptsPifib_.Nodes, [], name, value)


        class Node(Entity):
            """
            Pre\-ifib data for particular node
            
            .. attribute:: node_name  <key>
            
            	The node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: type_values
            
            	Type specific
            	**type**\:  :py:class:`TypeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues>`
            
            .. attribute:: dynamic_flows_stats
            
            	Dynamic Flows Statistics
            	**type**\:  :py:class:`DynamicFlowsStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.DynamicFlowsStats>`
            
            .. attribute:: hardware
            
            	Hardware specific
            	**type**\:  :py:class:`Hardware <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware>`
            
            

            """

            _prefix = 'lpts-pre-ifib-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(LptsPifib_.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"type-values" : ("type_values", LptsPifib_.Nodes.Node.TypeValues), "dynamic-flows-stats" : ("dynamic_flows_stats", LptsPifib_.Nodes.Node.DynamicFlowsStats), "Cisco-IOS-XR-platform-pifib-oper:hardware" : ("hardware", LptsPifib_.Nodes.Node.Hardware)}
                self._child_list_classes = {}

                self.node_name = YLeaf(YType.str, "node-name")

                self.type_values = LptsPifib_.Nodes.Node.TypeValues()
                self.type_values.parent = self
                self._children_name_map["type_values"] = "type-values"
                self._children_yang_names.add("type-values")

                self.dynamic_flows_stats = LptsPifib_.Nodes.Node.DynamicFlowsStats()
                self.dynamic_flows_stats.parent = self
                self._children_name_map["dynamic_flows_stats"] = "dynamic-flows-stats"
                self._children_yang_names.add("dynamic-flows-stats")

                self.hardware = LptsPifib_.Nodes.Node.Hardware()
                self.hardware.parent = self
                self._children_name_map["hardware"] = "hardware"
                self._children_yang_names.add("hardware")
                self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-lpts-pre-ifib-oper:lpts-pifib/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(LptsPifib_.Nodes.Node, ['node_name'], name, value)


            class TypeValues(Entity):
                """
                Type specific
                
                .. attribute:: type_value
                
                	pifib types
                	**type**\: list of  		 :py:class:`TypeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues.TypeValue>`
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(LptsPifib_.Nodes.Node.TypeValues, self).__init__()

                    self.yang_name = "type-values"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"type-value" : ("type_value", LptsPifib_.Nodes.Node.TypeValues.TypeValue)}

                    self.type_value = YList(self)
                    self._segment_path = lambda: "type-values"

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.TypeValues, [], name, value)


                class TypeValue(Entity):
                    """
                    pifib types
                    
                    .. attribute:: pifib_type  <key>
                    
                    	Type value
                    	**type**\:  :py:class:`LptsPifib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib>`
                    
                    .. attribute:: entry
                    
                    	Data for single pre\-ifib entry
                    	**type**\: list of  		 :py:class:`Entry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry>`
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.TypeValues.TypeValue, self).__init__()

                        self.yang_name = "type-value"
                        self.yang_parent_name = "type-values"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"entry" : ("entry", LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry)}

                        self.pifib_type = YLeaf(YType.enumeration, "pifib-type")

                        self.entry = YList(self)
                        self._segment_path = lambda: "type-value" + "[pifib-type='" + self.pifib_type.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.TypeValues.TypeValue, ['pifib_type'], name, value)


                    class Entry(Entity):
                        """
                        Data for single pre\-ifib entry
                        
                        .. attribute:: entry  <key>
                        
                        	Single Pre\-ifib entry
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: vrf_name
                        
                        	VRF Name
                        	**type**\: str
                        
                        .. attribute:: vid
                        
                        	VRF ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: destination_addr
                        
                        	Destination IP Address
                        	**type**\: str
                        
                        .. attribute:: source_addr
                        
                        	Source IP Address
                        	**type**\: str
                        
                        .. attribute:: destination_type
                        
                        	Destination Key Type
                        	**type**\: str
                        
                        .. attribute:: destination_value
                        
                        	Destination Port/ICMP Type/IGMP Type
                        	**type**\: str
                        
                        .. attribute:: source_port
                        
                        	Source port
                        	**type**\: str
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: opcode
                        
                        	Opcode
                        	**type**\: str
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\: str
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\: str
                        
                        .. attribute:: local_flag
                        
                        	Local Flag
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: deliver_list_short
                        
                        	Deliver List Short Format
                        	**type**\: str
                        
                        .. attribute:: deliver_list_long
                        
                        	Deliver List Long Format
                        	**type**\: str
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: accepts
                        
                        	Packets matched to accept
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: drops
                        
                        	Packets matched for drop
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: stale
                        
                        	Is Stale
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: pifib_type
                        
                        	sub Pre\-IFIB type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: pifib_program_time
                        
                        	Creation or Update Time
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'lpts-pre-ifib-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry, self).__init__()

                            self.yang_name = "entry"
                            self.yang_parent_name = "type-value"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.entry = YLeaf(YType.str, "entry")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.vid = YLeaf(YType.uint32, "vid")

                            self.l3protocol = YLeaf(YType.uint32, "l3protocol")

                            self.l4protocol = YLeaf(YType.uint32, "l4protocol")

                            self.intf_name = YLeaf(YType.str, "intf-name")

                            self.intf_handle = YLeaf(YType.uint32, "intf-handle")

                            self.destination_addr = YLeaf(YType.str, "destination-addr")

                            self.source_addr = YLeaf(YType.str, "source-addr")

                            self.destination_type = YLeaf(YType.str, "destination-type")

                            self.destination_value = YLeaf(YType.str, "destination-value")

                            self.source_port = YLeaf(YType.str, "source-port")

                            self.is_frag = YLeaf(YType.uint8, "is-frag")

                            self.is_syn = YLeaf(YType.uint8, "is-syn")

                            self.opcode = YLeaf(YType.str, "opcode")

                            self.flow_type = YLeaf(YType.str, "flow-type")

                            self.listener_tag = YLeaf(YType.str, "listener-tag")

                            self.local_flag = YLeaf(YType.uint8, "local-flag")

                            self.is_fgid = YLeaf(YType.uint8, "is-fgid")

                            self.deliver_list_short = YLeaf(YType.str, "deliver-list-short")

                            self.deliver_list_long = YLeaf(YType.str, "deliver-list-long")

                            self.min_ttl = YLeaf(YType.uint8, "min-ttl")

                            self.accepts = YLeaf(YType.uint64, "accepts")

                            self.drops = YLeaf(YType.uint64, "drops")

                            self.stale = YLeaf(YType.uint8, "stale")

                            self.pifib_type = YLeaf(YType.uint8, "pifib-type")

                            self.pifib_program_time = YLeaf(YType.str, "pifib-program-time")
                            self._segment_path = lambda: "entry" + "[entry='" + self.entry.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.TypeValues.TypeValue.Entry, ['entry', 'vrf_name', 'vid', 'l3protocol', 'l4protocol', 'intf_name', 'intf_handle', 'destination_addr', 'source_addr', 'destination_type', 'destination_value', 'source_port', 'is_frag', 'is_syn', 'opcode', 'flow_type', 'listener_tag', 'local_flag', 'is_fgid', 'deliver_list_short', 'deliver_list_long', 'min_ttl', 'accepts', 'drops', 'stale', 'pifib_type', 'pifib_program_time'], name, value)


            class DynamicFlowsStats(Entity):
                """
                Dynamic Flows Statistics
                
                .. attribute:: dynamic_flows_enabled
                
                	Dynamic Flows Enabled
                	**type**\: bool
                
                .. attribute:: platform_supported_max
                
                	Platform Max
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: platform_configured_max
                
                	Platform Config Limit
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: platform_total_configured
                
                	Platform Total Configured
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_hw_entries
                
                	Total HW Entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_sw_entries
                
                	Total SW Entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: flow
                
                	Flow Datalist
                	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow>`
                
                

                """

                _prefix = 'lpts-pre-ifib-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(LptsPifib_.Nodes.Node.DynamicFlowsStats, self).__init__()

                    self.yang_name = "dynamic-flows-stats"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"flow" : ("flow", LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow)}

                    self.dynamic_flows_enabled = YLeaf(YType.boolean, "dynamic-flows-enabled")

                    self.platform_supported_max = YLeaf(YType.uint32, "platform-supported-max")

                    self.platform_configured_max = YLeaf(YType.uint32, "platform-configured-max")

                    self.platform_total_configured = YLeaf(YType.uint32, "platform-total-configured")

                    self.total_hw_entries = YLeaf(YType.uint32, "total-hw-entries")

                    self.total_sw_entries = YLeaf(YType.uint32, "total-sw-entries")

                    self.flow = YList(self)
                    self._segment_path = lambda: "dynamic-flows-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(LptsPifib_.Nodes.Node.DynamicFlowsStats, ['dynamic_flows_enabled', 'platform_supported_max', 'platform_configured_max', 'platform_total_configured', 'total_hw_entries', 'total_sw_entries'], name, value)


                class Flow(Entity):
                    """
                    Flow Datalist
                    
                    .. attribute:: flow_name
                    
                    	Flow Name
                    	**type**\: str
                    
                    .. attribute:: configurable
                    
                    	Is Configurable
                    	**type**\: bool
                    
                    .. attribute:: configured
                    
                    	Is Configured
                    	**type**\: bool
                    
                    .. attribute:: default_max
                    
                    	Default Max
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: configured_max
                    
                    	Configured Max
                    	**type**\: str
                    
                    .. attribute:: active_max
                    
                    	Active Max
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hardware_count
                    
                    	Hardware Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: software_count
                    
                    	Software Count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pending_software_entries
                    
                    	Pending Software Entries
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'lpts-pre-ifib-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "dynamic-flows-stats"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.flow_name = YLeaf(YType.str, "flow-name")

                        self.configurable = YLeaf(YType.boolean, "configurable")

                        self.configured = YLeaf(YType.boolean, "configured")

                        self.default_max = YLeaf(YType.uint32, "default-max")

                        self.configured_max = YLeaf(YType.str, "configured-max")

                        self.active_max = YLeaf(YType.uint32, "active-max")

                        self.hardware_count = YLeaf(YType.uint32, "hardware-count")

                        self.software_count = YLeaf(YType.uint32, "software-count")

                        self.pending_software_entries = YLeaf(YType.boolean, "pending-software-entries")
                        self._segment_path = lambda: "flow"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.DynamicFlowsStats.Flow, ['flow_name', 'configurable', 'configured', 'default_max', 'configured_max', 'active_max', 'hardware_count', 'software_count', 'pending_software_entries'], name, value)


            class Hardware(Entity):
                """
                Hardware specific
                
                .. attribute:: usage_entries
                
                	Usage Table options
                	**type**\:  :py:class:`UsageEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries>`
                
                .. attribute:: police
                
                	Police details
                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Police>`
                
                .. attribute:: static_police
                
                	Static Police details
                	**type**\:  :py:class:`StaticPolice <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.StaticPolice>`
                
                .. attribute:: bfd
                
                	Bfd details
                	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Bfd>`
                
                .. attribute:: statistics
                
                	Hardware Entry type
                	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Statistics>`
                
                .. attribute:: index_entries
                
                	Hardware Entry options
                	**type**\:  :py:class:`IndexEntries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries>`
                
                

                """

                _prefix = 'platform-pifib-oper'
                _revision = '2016-02-22'

                def __init__(self):
                    super(LptsPifib_.Nodes.Node.Hardware, self).__init__()

                    self.yang_name = "hardware"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"usage-entries" : ("usage_entries", LptsPifib_.Nodes.Node.Hardware.UsageEntries), "police" : ("police", LptsPifib_.Nodes.Node.Hardware.Police), "static-police" : ("static_police", LptsPifib_.Nodes.Node.Hardware.StaticPolice), "bfd" : ("bfd", LptsPifib_.Nodes.Node.Hardware.Bfd), "statistics" : ("statistics", LptsPifib_.Nodes.Node.Hardware.Statistics), "index-entries" : ("index_entries", LptsPifib_.Nodes.Node.Hardware.IndexEntries)}
                    self._child_list_classes = {}

                    self.usage_entries = LptsPifib_.Nodes.Node.Hardware.UsageEntries()
                    self.usage_entries.parent = self
                    self._children_name_map["usage_entries"] = "usage-entries"
                    self._children_yang_names.add("usage-entries")

                    self.police = LptsPifib_.Nodes.Node.Hardware.Police()
                    self.police.parent = self
                    self._children_name_map["police"] = "police"
                    self._children_yang_names.add("police")

                    self.static_police = LptsPifib_.Nodes.Node.Hardware.StaticPolice()
                    self.static_police.parent = self
                    self._children_name_map["static_police"] = "static-police"
                    self._children_yang_names.add("static-police")

                    self.bfd = LptsPifib_.Nodes.Node.Hardware.Bfd()
                    self.bfd.parent = self
                    self._children_name_map["bfd"] = "bfd"
                    self._children_yang_names.add("bfd")

                    self.statistics = LptsPifib_.Nodes.Node.Hardware.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                    self._children_yang_names.add("statistics")

                    self.index_entries = LptsPifib_.Nodes.Node.Hardware.IndexEntries()
                    self.index_entries.parent = self
                    self._children_name_map["index_entries"] = "index-entries"
                    self._children_yang_names.add("index-entries")
                    self._segment_path = lambda: "Cisco-IOS-XR-platform-pifib-oper:hardware"


                class UsageEntries(Entity):
                    """
                    Usage Table options
                    
                    .. attribute:: usage_entry
                    
                    	Usage details
                    	**type**\: list of  		 :py:class:`UsageEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.UsageEntries, self).__init__()

                        self.yang_name = "usage-entries"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"usage-entry" : ("usage_entry", LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry)}

                        self.usage_entry = YList(self)
                        self._segment_path = lambda: "usage-entries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.UsageEntries, [], name, value)


                    class UsageEntry(Entity):
                        """
                        Usage details
                        
                        .. attribute:: region_id  <key>
                        
                        	Region ID
                        	**type**\:  :py:class:`UsageAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_platform_pifib_oper.UsageAddressFamily>`
                        
                        .. attribute:: usage_info
                        
                        	Per TCAM type usage info
                        	**type**\: list of  		 :py:class:`UsageInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo>`
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry, self).__init__()

                            self.yang_name = "usage-entry"
                            self.yang_parent_name = "usage-entries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"usage-info" : ("usage_info", LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo)}

                            self.region_id = YLeaf(YType.enumeration, "region-id")

                            self.usage_info = YList(self)
                            self._segment_path = lambda: "usage-entry" + "[region-id='" + self.region_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry, ['region_id'], name, value)


                        class UsageInfo(Entity):
                            """
                            Per TCAM type usage info
                            
                            .. attribute:: pipe_id
                            
                            	Pipe ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: region
                            
                            	Region Type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: region_id
                            
                            	Region ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: size
                            
                            	Maximum Number of Entries in the Region
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: used
                            
                            	Used Number of Entries in the Region
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo, self).__init__()

                                self.yang_name = "usage-info"
                                self.yang_parent_name = "usage-entry"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.pipe_id = YLeaf(YType.uint8, "pipe-id")

                                self.region = YLeaf(YType.uint8, "region")

                                self.region_id = YLeaf(YType.uint8, "region-id")

                                self.size = YLeaf(YType.uint32, "size")

                                self.used = YLeaf(YType.uint32, "used")
                                self._segment_path = lambda: "usage-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo, ['pipe_id', 'region', 'region_id', 'size', 'used'], name, value)


                class Police(Entity):
                    """
                    Police details
                    
                    .. attribute:: police_info
                    
                    	Per flow type police info
                    	**type**\: list of  		 :py:class:`PoliceInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.Police, self).__init__()

                        self.yang_name = "police"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"police-info" : ("police_info", LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo)}

                        self.police_info = YList(self)
                        self._segment_path = lambda: "police"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Police, [], name, value)


                    class PoliceInfo(Entity):
                        """
                        Per flow type police info
                        
                        .. attribute:: avgrate
                        
                        	avgrate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: burst
                        
                        	burst
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: static_avgrate
                        
                        	static avgrate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: avgrate_type
                        
                        	avgrate type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: accepted_stats
                        
                        	accepted stats
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped_stats
                        
                        	dropped stats
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: policer
                        
                        	policer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: iptos_value
                        
                        	iptos value
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: change_type
                        
                        	change type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: acl_config
                        
                        	acl config
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: acl_str
                        
                        	acl str
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo, self).__init__()

                            self.yang_name = "police-info"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.avgrate = YLeaf(YType.uint32, "avgrate")

                            self.burst = YLeaf(YType.uint32, "burst")

                            self.static_avgrate = YLeaf(YType.uint32, "static-avgrate")

                            self.avgrate_type = YLeaf(YType.uint32, "avgrate-type")

                            self.accepted_stats = YLeaf(YType.uint64, "accepted-stats")

                            self.dropped_stats = YLeaf(YType.uint64, "dropped-stats")

                            self.policer = YLeaf(YType.uint32, "policer")

                            self.iptos_value = YLeaf(YType.uint8, "iptos-value")

                            self.change_type = YLeaf(YType.uint8, "change-type")

                            self.acl_config = YLeaf(YType.uint8, "acl-config")

                            self.acl_str = YLeaf(YType.str, "acl-str")
                            self._segment_path = lambda: "police-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Police.PoliceInfo, ['avgrate', 'burst', 'static_avgrate', 'avgrate_type', 'accepted_stats', 'dropped_stats', 'policer', 'iptos_value', 'change_type', 'acl_config', 'acl_str'], name, value)


                class StaticPolice(Entity):
                    """
                    Static Police details
                    
                    .. attribute:: static_info
                    
                    	Per punt reason info
                    	**type**\: list of  		 :py:class:`StaticInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.StaticPolice, self).__init__()

                        self.yang_name = "static-police"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"static-info" : ("static_info", LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo)}

                        self.static_info = YList(self)
                        self._segment_path = lambda: "static-police"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.StaticPolice, [], name, value)


                    class StaticInfo(Entity):
                        """
                        Per punt reason info
                        
                        .. attribute:: punt_reason
                        
                        	punt reason
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sid
                        
                        	sid
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_rate
                        
                        	flow rate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: burst_rate
                        
                        	burst rate
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: accepted
                        
                        	accepted
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: dropped
                        
                        	dropped
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: punt_reason_string
                        
                        	punt reason string
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: change_type
                        
                        	change type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo, self).__init__()

                            self.yang_name = "static-info"
                            self.yang_parent_name = "static-police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.punt_reason = YLeaf(YType.uint32, "punt-reason")

                            self.sid = YLeaf(YType.uint32, "sid")

                            self.flow_rate = YLeaf(YType.uint32, "flow-rate")

                            self.burst_rate = YLeaf(YType.uint32, "burst-rate")

                            self.accepted = YLeaf(YType.uint64, "accepted")

                            self.dropped = YLeaf(YType.uint64, "dropped")

                            self.punt_reason_string = YLeaf(YType.str, "punt-reason-string")

                            self.change_type = YLeaf(YType.uint8, "change-type")
                            self._segment_path = lambda: "static-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.StaticPolice.StaticInfo, ['punt_reason', 'sid', 'flow_rate', 'burst_rate', 'accepted', 'dropped', 'punt_reason_string', 'change_type'], name, value)


                class Bfd(Entity):
                    """
                    Bfd details
                    
                    .. attribute:: bfd_entry_info
                    
                    	Per bfd disc entry info
                    	**type**\: list of  		 :py:class:`BfdEntryInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.Bfd, self).__init__()

                        self.yang_name = "bfd"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"bfd-entry-info" : ("bfd_entry_info", LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo)}

                        self.bfd_entry_info = YList(self)
                        self._segment_path = lambda: "bfd"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Bfd, [], name, value)


                    class BfdEntryInfo(Entity):
                        """
                        Per bfd disc entry info
                        
                        .. attribute:: index
                        
                        	index
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_mcast
                        
                        	is mcast
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: fgid_or_vqi
                        
                        	fgid or vqi
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_valid
                        
                        	is valid
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: policer_id
                        
                        	policer id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo, self).__init__()

                            self.yang_name = "bfd-entry-info"
                            self.yang_parent_name = "bfd"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.index = YLeaf(YType.uint8, "index")

                            self.is_mcast = YLeaf(YType.uint8, "is-mcast")

                            self.fgid_or_vqi = YLeaf(YType.uint32, "fgid-or-vqi")

                            self.is_valid = YLeaf(YType.uint8, "is-valid")

                            self.policer_id = YLeaf(YType.uint32, "policer-id")
                            self._segment_path = lambda: "bfd-entry-info"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Bfd.BfdEntryInfo, ['index', 'is_mcast', 'fgid_or_vqi', 'is_valid', 'policer_id'], name, value)


                class Statistics(Entity):
                    """
                    Hardware Entry type
                    
                    .. attribute:: accepted
                    
                    	Deleted\-entry accepted packets counter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dropped
                    
                    	Deleted\-entry dropped packets counter
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: clear_ts
                    
                    	Statistics clear timestamp
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: no_stats_mem_err
                    
                    	No statistics memory error
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.Statistics, self).__init__()

                        self.yang_name = "statistics"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.accepted = YLeaf(YType.uint64, "accepted")

                        self.dropped = YLeaf(YType.uint64, "dropped")

                        self.clear_ts = YLeaf(YType.uint64, "clear-ts")

                        self.no_stats_mem_err = YLeaf(YType.uint64, "no-stats-mem-err")
                        self._segment_path = lambda: "statistics"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.Statistics, ['accepted', 'dropped', 'clear_ts', 'no_stats_mem_err'], name, value)


                class IndexEntries(Entity):
                    """
                    Hardware Entry options
                    
                    .. attribute:: index_entry
                    
                    	Entry options
                    	**type**\: list of  		 :py:class:`IndexEntry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry>`
                    
                    

                    """

                    _prefix = 'platform-pifib-oper'
                    _revision = '2016-02-22'

                    def __init__(self):
                        super(LptsPifib_.Nodes.Node.Hardware.IndexEntries, self).__init__()

                        self.yang_name = "index-entries"
                        self.yang_parent_name = "hardware"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"index-entry" : ("index_entry", LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry)}

                        self.index_entry = YList(self)
                        self._segment_path = lambda: "index-entries"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.IndexEntries, [], name, value)


                    class IndexEntry(Entity):
                        """
                        Entry options
                        
                        .. attribute:: index  <key>
                        
                        	Index
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: l3protocol
                        
                        	Layer 3 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: l4protocol
                        
                        	Layer 4 Protocol
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: intf_handle
                        
                        	Interface Handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: intf_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        .. attribute:: uidb_index
                        
                        	Interface uidb index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_addr
                        
                        	Local IP Address
                        	**type**\: str
                        
                        .. attribute:: local_prefix_len
                        
                        	Local Prefix Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_addr
                        
                        	Remote IP Address
                        	**type**\: str
                        
                        .. attribute:: remote_prefix_len
                        
                        	Remote Prefix Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: u_value
                        
                        	Remote Port/ICMP Type/IGMP Type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: u_len
                        
                        	Union Key Length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_port
                        
                        	Local port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_frag
                        
                        	Is Fragment
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_syn
                        
                        	Is SYN
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: action
                        
                        	Action
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: action_string
                        
                        	Action String
                        	**type**\: str
                        
                        .. attribute:: listener_tag
                        
                        	Listener Tag
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_fgid
                        
                        	Is FGID or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_vrf
                        
                        	Is VRF or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_optimized
                        
                        	Is optimized or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: is_uidb_opt_bit
                        
                        	Is uidb set for optimized entry or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: fgid_or_sfp
                        
                        	fabric group id or swith fabric port
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_rack
                        
                        	Is entry remote or not
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rack_id
                        
                        	Remote racknum if remote
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: rslot
                        
                        	Remote slotnum if remote
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cir
                        
                        	Committed Information Rate
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: flow_type
                        
                        	Flow type
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: priority
                        
                        	Flow priority or COS
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sid
                        
                        	Stream ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policer_avgrate
                        
                        	Policer avg. rate limit
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: policer_burst
                        
                        	Policer burst
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: lookup_priority
                        
                        	Lookup priority
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: storage_priority
                        
                        	Storage priority
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: num_tm_entries
                        
                        	Number of TCAM entries used
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: entry_ptr
                        
                        	ptr to ifib\_entry\_st
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: entry_shadow_ptr
                        
                        	ptr to ifib\_entry\_shadow\_st
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: list_node_ptr
                        
                        	ptr to dlqueue list node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: state
                        
                        	state of pifib entry
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: retry_fail_cause
                        
                        	failure cause
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: num_retries
                        
                        	retries count
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: min_ttl
                        
                        	Minimum TTL
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: u_type
                        
                        	Union Key Type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: remote_fgid
                        
                        	Remote FGID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: acl_str
                        
                        	Acl name
                        	**type**\: str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: no_stats
                        
                        	Stats not available
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: hw_info
                        
                        	Per pipe type hardware info
                        	**type**\: list of  		 :py:class:`HwInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper.LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo>`
                        
                        

                        """

                        _prefix = 'platform-pifib-oper'
                        _revision = '2016-02-22'

                        def __init__(self):
                            super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry, self).__init__()

                            self.yang_name = "index-entry"
                            self.yang_parent_name = "index-entries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"hw-info" : ("hw_info", LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo)}

                            self.index = YLeaf(YType.int32, "index")

                            self.l3protocol = YLeaf(YType.uint32, "l3protocol")

                            self.l4protocol = YLeaf(YType.uint32, "l4protocol")

                            self.intf_handle = YLeaf(YType.uint32, "intf-handle")

                            self.intf_name = YLeaf(YType.str, "intf-name")

                            self.uidb_index = YLeaf(YType.uint32, "uidb-index")

                            self.local_addr = YLeaf(YType.str, "local-addr")

                            self.local_prefix_len = YLeaf(YType.uint32, "local-prefix-len")

                            self.remote_addr = YLeaf(YType.str, "remote-addr")

                            self.remote_prefix_len = YLeaf(YType.uint32, "remote-prefix-len")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                            self.u_value = YLeaf(YType.uint32, "u-value")

                            self.u_len = YLeaf(YType.uint32, "u-len")

                            self.local_port = YLeaf(YType.uint32, "local-port")

                            self.is_frag = YLeaf(YType.uint8, "is-frag")

                            self.is_syn = YLeaf(YType.uint8, "is-syn")

                            self.action = YLeaf(YType.uint8, "action")

                            self.action_string = YLeaf(YType.str, "action-string")

                            self.listener_tag = YLeaf(YType.uint8, "listener-tag")

                            self.is_fgid = YLeaf(YType.uint8, "is-fgid")

                            self.is_vrf = YLeaf(YType.uint8, "is-vrf")

                            self.is_optimized = YLeaf(YType.uint8, "is-optimized")

                            self.is_uidb_opt_bit = YLeaf(YType.uint8, "is-uidb-opt-bit")

                            self.fgid_or_sfp = YLeaf(YType.uint32, "fgid-or-sfp")

                            self.remote_rack = YLeaf(YType.uint8, "remote-rack")

                            self.rack_id = YLeaf(YType.uint32, "rack-id")

                            self.rslot = YLeaf(YType.uint32, "rslot")

                            self.cir = YLeaf(YType.uint64, "cir")

                            self.flow_type = YLeaf(YType.uint32, "flow-type")

                            self.priority = YLeaf(YType.uint32, "priority")

                            self.sid = YLeaf(YType.uint32, "sid")

                            self.policer_avgrate = YLeaf(YType.uint32, "policer-avgrate")

                            self.policer_burst = YLeaf(YType.uint32, "policer-burst")

                            self.lookup_priority = YLeaf(YType.int32, "lookup-priority")

                            self.storage_priority = YLeaf(YType.int32, "storage-priority")

                            self.num_tm_entries = YLeaf(YType.int32, "num-tm-entries")

                            self.entry_ptr = YLeaf(YType.uint32, "entry-ptr")

                            self.entry_shadow_ptr = YLeaf(YType.uint32, "entry-shadow-ptr")

                            self.list_node_ptr = YLeaf(YType.uint32, "list-node-ptr")

                            self.state = YLeaf(YType.uint8, "state")

                            self.retry_fail_cause = YLeaf(YType.uint8, "retry-fail-cause")

                            self.num_retries = YLeaf(YType.uint8, "num-retries")

                            self.min_ttl = YLeaf(YType.uint8, "min-ttl")

                            self.u_type = YLeaf(YType.uint8, "u-type")

                            self.remote_fgid = YLeaf(YType.uint32, "remote-fgid")

                            self.acl_str = YLeaf(YType.str, "acl-str")

                            self.no_stats = YLeaf(YType.uint8, "no-stats")

                            self.hw_info = YList(self)
                            self._segment_path = lambda: "index-entry" + "[index='" + self.index.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry, ['index', 'l3protocol', 'l4protocol', 'intf_handle', 'intf_name', 'uidb_index', 'local_addr', 'local_prefix_len', 'remote_addr', 'remote_prefix_len', 'vrf_id', 'u_value', 'u_len', 'local_port', 'is_frag', 'is_syn', 'action', 'action_string', 'listener_tag', 'is_fgid', 'is_vrf', 'is_optimized', 'is_uidb_opt_bit', 'fgid_or_sfp', 'remote_rack', 'rack_id', 'rslot', 'cir', 'flow_type', 'priority', 'sid', 'policer_avgrate', 'policer_burst', 'lookup_priority', 'storage_priority', 'num_tm_entries', 'entry_ptr', 'entry_shadow_ptr', 'list_node_ptr', 'state', 'retry_fail_cause', 'num_retries', 'min_ttl', 'u_type', 'remote_fgid', 'acl_str', 'no_stats'], name, value)


                        class HwInfo(Entity):
                            """
                            Per pipe type hardware info
                            
                            .. attribute:: policer
                            
                            	Policer Pointer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: stats_ptr
                            
                            	Stats Pointer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accepted
                            
                            	Accepted Packets Counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: dropped
                            
                            	Dropped Packets Counter
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sort_start_offset
                            
                            	Relative position in sorting order
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: tm_start_offset
                            
                            	Relative position in TCAM
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'platform-pifib-oper'
                            _revision = '2016-02-22'

                            def __init__(self):
                                super(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo, self).__init__()

                                self.yang_name = "hw-info"
                                self.yang_parent_name = "index-entry"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.policer = YLeaf(YType.uint32, "policer")

                                self.stats_ptr = YLeaf(YType.uint32, "stats-ptr")

                                self.accepted = YLeaf(YType.uint64, "accepted")

                                self.dropped = YLeaf(YType.uint64, "dropped")

                                self.sort_start_offset = YLeaf(YType.int32, "sort-start-offset")

                                self.tm_start_offset = YLeaf(YType.int32, "tm-start-offset")
                                self._segment_path = lambda: "hw-info"

                            def __setattr__(self, name, value):
                                self._perform_setattr(LptsPifib_.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo, ['policer', 'stats_ptr', 'accepted', 'dropped', 'sort_start_offset', 'tm_start_offset'], name, value)

    def clone_ptr(self):
        self._top_entity = LptsPifib_()
        return self._top_entity

