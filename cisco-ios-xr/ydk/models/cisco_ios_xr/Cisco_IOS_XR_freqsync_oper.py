""" Cisco_IOS_XR_freqsync_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR freqsync package operational data.

This module contains definitions
for the following management objects\:
  frequency\-synchronization\: Frequency Synchronization
    operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class FsyncBagClockIntfClass(Enum):
    """
    FsyncBagClockIntfClass

    Clock\-interface class

    .. data:: clock_class_bitst1 = 0

    	BITS T1

    .. data:: clock_class_bitse1 = 1

    	BITS E1

    .. data:: clock_class_bits2m = 2

    	BITS 2M

    .. data:: clock_class_bits6m = 3

    	BITS 6M

    .. data:: clock_class_bits64k = 4

    	BITS 64K

    .. data:: clock_class_dti = 5

    	DTI

    .. data:: clock_class_gps = 6

    	GPS

    .. data:: clock_class_chassis_sync = 7

    	Inter-Chassis Sync

    .. data:: clock_class_bitsj1 = 8

    	Bits J1

    """

    clock_class_bitst1 = Enum.YLeaf(0, "clock-class-bitst1")

    clock_class_bitse1 = Enum.YLeaf(1, "clock-class-bitse1")

    clock_class_bits2m = Enum.YLeaf(2, "clock-class-bits2m")

    clock_class_bits6m = Enum.YLeaf(3, "clock-class-bits6m")

    clock_class_bits64k = Enum.YLeaf(4, "clock-class-bits64k")

    clock_class_dti = Enum.YLeaf(5, "clock-class-dti")

    clock_class_gps = Enum.YLeaf(6, "clock-class-gps")

    clock_class_chassis_sync = Enum.YLeaf(7, "clock-class-chassis-sync")

    clock_class_bitsj1 = Enum.YLeaf(8, "clock-class-bitsj1")


class FsyncBagDampingState(Enum):
    """
    FsyncBagDampingState

    Damping state

    .. data:: damping_state_down = 0

    	Down

    .. data:: damping_state_coming_up = 1

    	Coming up

    .. data:: damping_state_up = 2

    	Up

    .. data:: damping_state_going_down = 3

    	Going down

    """

    damping_state_down = Enum.YLeaf(0, "damping-state-down")

    damping_state_coming_up = Enum.YLeaf(1, "damping-state-coming-up")

    damping_state_up = Enum.YLeaf(2, "damping-state-up")

    damping_state_going_down = Enum.YLeaf(3, "damping-state-going-down")


class FsyncBagEsmcPeerState(Enum):
    """
    FsyncBagEsmcPeerState

    ESMC peer state

    .. data:: peer_down = 1808240398

    	Peer state down

    .. data:: peer_up = 1808240399

    	Peer state up

    .. data:: peer_timed_out = 1808240400

    	Peer state timed out

    .. data:: peer_unknown = 1808240401

    	Peer state unknown

    """

    peer_down = Enum.YLeaf(1808240398, "peer-down")

    peer_up = Enum.YLeaf(1808240399, "peer-up")

    peer_timed_out = Enum.YLeaf(1808240400, "peer-timed-out")

    peer_unknown = Enum.YLeaf(1808240401, "peer-unknown")


class FsyncBagForwardtraceNode(Enum):
    """
    FsyncBagForwardtraceNode

    Selection forwardtrace node information

    .. data:: forward_trace_node_selection_point = 0

    	A selection point forwardtrace node

    .. data:: forward_trace_node_source = 1

    	A timing source forwardtrace node

    """

    forward_trace_node_selection_point = Enum.YLeaf(0, "forward-trace-node-selection-point")

    forward_trace_node_source = Enum.YLeaf(1, "forward-trace-node-source")


class FsyncBagQlO1Value(Enum):
    """
    FsyncBagQlO1Value

    Quality level option 1 values

    .. data:: option1_invalid = 0

    	Invalid

    .. data:: option1_do_not_use = 1

    	Do not use

    .. data:: option1_failed = 2

    	Failed

    .. data:: option1_none = 3

    	None

    .. data:: option1prc = 10

    	Primary reference clock

    .. data:: option1ssu_a = 11

    	Type I or V slave clock

    .. data:: option1ssu_b = 12

    	Type VI slave clock

    .. data:: option1sec = 13

    	SONET equipment clock

    """

    option1_invalid = Enum.YLeaf(0, "option1-invalid")

    option1_do_not_use = Enum.YLeaf(1, "option1-do-not-use")

    option1_failed = Enum.YLeaf(2, "option1-failed")

    option1_none = Enum.YLeaf(3, "option1-none")

    option1prc = Enum.YLeaf(10, "option1prc")

    option1ssu_a = Enum.YLeaf(11, "option1ssu-a")

    option1ssu_b = Enum.YLeaf(12, "option1ssu-b")

    option1sec = Enum.YLeaf(13, "option1sec")


class FsyncBagQlO2G1Value(Enum):
    """
    FsyncBagQlO2G1Value

    Quality level option 2, generation 1 values

    .. data:: option2_generation1_invalid = 0

    	Invalid

    .. data:: option2_generation1_do_not_use = 1

    	Do not use

    .. data:: option2_generation1_failed = 2

    	Failed

    .. data:: option2_generation1_none = 3

    	None

    .. data:: option2_generation1prs = 20

    	Primary reference source

    .. data:: option2_generation1stu = 21

    	Synchronized - traceability unknown

    .. data:: option2_generation1_stratum2 = 22

    	Stratum 2

    .. data:: option2_generation1_stratum3 = 23

    	Stratum 3

    .. data:: option2_generation1smc = 24

    	SONET clock self timed

    .. data:: option2_generation1_stratum4 = 25

    	Stratum 4 freerun

    """

    option2_generation1_invalid = Enum.YLeaf(0, "option2-generation1-invalid")

    option2_generation1_do_not_use = Enum.YLeaf(1, "option2-generation1-do-not-use")

    option2_generation1_failed = Enum.YLeaf(2, "option2-generation1-failed")

    option2_generation1_none = Enum.YLeaf(3, "option2-generation1-none")

    option2_generation1prs = Enum.YLeaf(20, "option2-generation1prs")

    option2_generation1stu = Enum.YLeaf(21, "option2-generation1stu")

    option2_generation1_stratum2 = Enum.YLeaf(22, "option2-generation1-stratum2")

    option2_generation1_stratum3 = Enum.YLeaf(23, "option2-generation1-stratum3")

    option2_generation1smc = Enum.YLeaf(24, "option2-generation1smc")

    option2_generation1_stratum4 = Enum.YLeaf(25, "option2-generation1-stratum4")


class FsyncBagQlO2G2Value(Enum):
    """
    FsyncBagQlO2G2Value

    Quality level option 2, generation 2 values

    .. data:: option2_generation2_invalid = 0

    	Invalid

    .. data:: option2_generation2_do_not_use = 1

    	Do not use

    .. data:: option2_generation2_failed = 2

    	Failed

    .. data:: option2_generation2_none = 3

    	None

    .. data:: option2_generation2prs = 30

    	Primary reference source

    .. data:: option2_generation2stu = 31

    	Synchronized - traceability unknown

    .. data:: option2_generation2_stratum2 = 32

    	Stratum 2

    .. data:: option2_generation2_stratum3 = 33

    	Stratum 3

    .. data:: option2_generation2tnc = 34

    	Transit node clock

    .. data:: option2_generation2_stratum3e = 35

    	Stratum 3E

    .. data:: option2_generation2smc = 36

    	SONET clock self timed

    .. data:: option2_generation2_stratum4 = 37

    	Stratum 4 freerun

    """

    option2_generation2_invalid = Enum.YLeaf(0, "option2-generation2-invalid")

    option2_generation2_do_not_use = Enum.YLeaf(1, "option2-generation2-do-not-use")

    option2_generation2_failed = Enum.YLeaf(2, "option2-generation2-failed")

    option2_generation2_none = Enum.YLeaf(3, "option2-generation2-none")

    option2_generation2prs = Enum.YLeaf(30, "option2-generation2prs")

    option2_generation2stu = Enum.YLeaf(31, "option2-generation2stu")

    option2_generation2_stratum2 = Enum.YLeaf(32, "option2-generation2-stratum2")

    option2_generation2_stratum3 = Enum.YLeaf(33, "option2-generation2-stratum3")

    option2_generation2tnc = Enum.YLeaf(34, "option2-generation2tnc")

    option2_generation2_stratum3e = Enum.YLeaf(35, "option2-generation2-stratum3e")

    option2_generation2smc = Enum.YLeaf(36, "option2-generation2smc")

    option2_generation2_stratum4 = Enum.YLeaf(37, "option2-generation2-stratum4")


class FsyncBagQlOption(Enum):
    """
    FsyncBagQlOption

    Quality level option

    .. data:: no_quality_level_option = 0

    	No quality level option

    .. data:: option1 = 1

    	ITU-T Quality level option 1

    .. data:: option2_generation1 = 2

    	ITU-T Quality level option 2, generation 1

    .. data:: option2_generation2 = 3

    	ITU-T Quality level option 2, generation 2

    .. data:: invalid_quality_level_option = 4

    	Invalid quality level option

    """

    no_quality_level_option = Enum.YLeaf(0, "no-quality-level-option")

    option1 = Enum.YLeaf(1, "option1")

    option2_generation1 = Enum.YLeaf(2, "option2-generation1")

    option2_generation2 = Enum.YLeaf(3, "option2-generation2")

    invalid_quality_level_option = Enum.YLeaf(4, "invalid-quality-level-option")


class FsyncBagSourceClass(Enum):
    """
    FsyncBagSourceClass

    Source class

    .. data:: invalid_source = 0

    	Invalid source class

    .. data:: ethernet_interface_source = 1

    	Ethernet interface

    .. data:: sonet_interface_source = 2

    	SONET interface

    .. data:: clock_interface_source = 3

    	Clock interface

    .. data:: internal_clock_source = 4

    	Internal clock

    .. data:: ptp_source = 5

    	PTP clock

    .. data:: satellite_access_interface_source = 6

    	Satellite Access Interface

    .. data:: ntp_source = 7

    	NTP clock

    """

    invalid_source = Enum.YLeaf(0, "invalid-source")

    ethernet_interface_source = Enum.YLeaf(1, "ethernet-interface-source")

    sonet_interface_source = Enum.YLeaf(2, "sonet-interface-source")

    clock_interface_source = Enum.YLeaf(3, "clock-interface-source")

    internal_clock_source = Enum.YLeaf(4, "internal-clock-source")

    ptp_source = Enum.YLeaf(5, "ptp-source")

    satellite_access_interface_source = Enum.YLeaf(6, "satellite-access-interface-source")

    ntp_source = Enum.YLeaf(7, "ntp-source")


class FsyncBagSourceState(Enum):
    """
    FsyncBagSourceState

    Source state

    .. data:: source_state_unknown = 0

    	Unknown

    .. data:: source_state_up = 1

    	Up

    .. data:: source_state_down = 2

    	Down

    """

    source_state_unknown = Enum.YLeaf(0, "source-state-unknown")

    source_state_up = Enum.YLeaf(1, "source-state-up")

    source_state_down = Enum.YLeaf(2, "source-state-down")


class FsyncBagStreamInput(Enum):
    """
    FsyncBagStreamInput

    Stream input type

    .. data:: invalid_input = 0

    	Invalid stream input

    .. data:: source_input = 1

    	Source stream input

    .. data:: selection_point_input = 2

    	Selection point stream input

    """

    invalid_input = Enum.YLeaf(0, "invalid-input")

    source_input = Enum.YLeaf(1, "source-input")

    selection_point_input = Enum.YLeaf(2, "selection-point-input")


class FsyncBagStreamState(Enum):
    """
    FsyncBagStreamState

    Platform stream status

    .. data:: stream_invalid = 0

    	Invalid stream

    .. data:: stream_available = 2

    	Stream available

    .. data:: stream_locked = 4

    	Stream locked

    .. data:: stream_holdover = 5

    	Stream in holdover

    .. data:: stream_freerun = 6

    	Stream free running

    .. data:: stream_failed = 7

    	Stream failed

    .. data:: stream_unmonitored = 8

    	Unmonitored stream

    .. data:: stream_error = 9

    	Stream error

    """

    stream_invalid = Enum.YLeaf(0, "stream-invalid")

    stream_available = Enum.YLeaf(2, "stream-available")

    stream_locked = Enum.YLeaf(4, "stream-locked")

    stream_holdover = Enum.YLeaf(5, "stream-holdover")

    stream_freerun = Enum.YLeaf(6, "stream-freerun")

    stream_failed = Enum.YLeaf(7, "stream-failed")

    stream_unmonitored = Enum.YLeaf(8, "stream-unmonitored")

    stream_error = Enum.YLeaf(9, "stream-error")


class FsyncSource(Enum):
    """
    FsyncSource

    Fsync source

    .. data:: ethernet = 1

    	An ethernet interface

    .. data:: sonet = 2

    	A SONET interface

    .. data:: clock = 3

    	A clock interface

    .. data:: internal = 4

    	An internal clock

    .. data:: ptp = 5

    	A PTP clock

    .. data:: satellite_access = 6

    	A satellite access interface clock

    .. data:: ntp = 7

    	An NTP clock

    """

    ethernet = Enum.YLeaf(1, "ethernet")

    sonet = Enum.YLeaf(2, "sonet")

    clock = Enum.YLeaf(3, "clock")

    internal = Enum.YLeaf(4, "internal")

    ptp = Enum.YLeaf(5, "ptp")

    satellite_access = Enum.YLeaf(6, "satellite-access")

    ntp = Enum.YLeaf(7, "ntp")


class FsyncStream(Enum):
    """
    FsyncStream

    Fsync stream

    .. data:: local = 1

    	Stream input from a local source

    .. data:: selection_point = 2

    	Stream input from a selection point on a remote

    	node

    """

    local = Enum.YLeaf(1, "local")

    selection_point = Enum.YLeaf(2, "selection-point")


class ImStateEnum(Enum):
    """
    ImStateEnum

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = Enum.YLeaf(0, "im-state-not-ready")

    im_state_admin_down = Enum.YLeaf(1, "im-state-admin-down")

    im_state_down = Enum.YLeaf(2, "im-state-down")

    im_state_up = Enum.YLeaf(3, "im-state-up")

    im_state_shutdown = Enum.YLeaf(4, "im-state-shutdown")

    im_state_err_disable = Enum.YLeaf(5, "im-state-err-disable")

    im_state_down_immediate = Enum.YLeaf(6, "im-state-down-immediate")

    im_state_down_immediate_admin = Enum.YLeaf(7, "im-state-down-immediate-admin")

    im_state_down_graceful = Enum.YLeaf(8, "im-state-down-graceful")

    im_state_begin_shutdown = Enum.YLeaf(9, "im-state-begin-shutdown")

    im_state_end_shutdown = Enum.YLeaf(10, "im-state-end-shutdown")

    im_state_begin_error_disable = Enum.YLeaf(11, "im-state-begin-error-disable")

    im_state_end_error_disable = Enum.YLeaf(12, "im-state-end-error-disable")

    im_state_begin_down_graceful = Enum.YLeaf(13, "im-state-begin-down-graceful")

    im_state_reset = Enum.YLeaf(14, "im-state-reset")

    im_state_operational = Enum.YLeaf(15, "im-state-operational")

    im_state_not_operational = Enum.YLeaf(16, "im-state-not-operational")

    im_state_unknown = Enum.YLeaf(17, "im-state-unknown")

    im_state_last = Enum.YLeaf(18, "im-state-last")



class FrequencySynchronization(Entity):
    """
    Frequency Synchronization operational data
    
    .. attribute:: global_nodes
    
    	Table for global node\-specific operational data
    	**type**\:  :py:class:`GlobalNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes>`
    
    .. attribute:: global_interfaces
    
    	Table for global interface operational data
    	**type**\:  :py:class:`GlobalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces>`
    
    .. attribute:: summary
    
    	Summary operational data
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary>`
    
    .. attribute:: interfaces
    
    	Table for interface operational data
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces>`
    
    .. attribute:: nodes
    
    	Table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes>`
    
    

    """

    _prefix = 'freqsync-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(FrequencySynchronization, self).__init__()
        self._top_entity = None

        self.yang_name = "frequency-synchronization"
        self.yang_parent_name = "Cisco-IOS-XR-freqsync-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"global-nodes" : ("global_nodes", FrequencySynchronization.GlobalNodes), "global-interfaces" : ("global_interfaces", FrequencySynchronization.GlobalInterfaces), "summary" : ("summary", FrequencySynchronization.Summary), "interfaces" : ("interfaces", FrequencySynchronization.Interfaces), "nodes" : ("nodes", FrequencySynchronization.Nodes)}
        self._child_list_classes = {}

        self.global_nodes = FrequencySynchronization.GlobalNodes()
        self.global_nodes.parent = self
        self._children_name_map["global_nodes"] = "global-nodes"
        self._children_yang_names.add("global-nodes")

        self.global_interfaces = FrequencySynchronization.GlobalInterfaces()
        self.global_interfaces.parent = self
        self._children_name_map["global_interfaces"] = "global-interfaces"
        self._children_yang_names.add("global-interfaces")

        self.summary = FrequencySynchronization.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")

        self.interfaces = FrequencySynchronization.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.nodes = FrequencySynchronization.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization"


    class GlobalNodes(Entity):
        """
        Table for global node\-specific operational data
        
        .. attribute:: global_node
        
        	Global node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`GlobalNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FrequencySynchronization.GlobalNodes, self).__init__()

            self.yang_name = "global-nodes"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"global-node" : ("global_node", FrequencySynchronization.GlobalNodes.GlobalNode)}

            self.global_node = YList(self)
            self._segment_path = lambda: "global-nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.GlobalNodes, [], name, value)


        class GlobalNode(Entity):
            """
            Global node\-specific data for a particular node
            
            .. attribute:: node  <key>
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: clock_interface_selection_back_traces
            
            	Selection backtrace operational data for clock\-interfaces
            	**type**\:  :py:class:`ClockInterfaceSelectionBackTraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces>`
            
            .. attribute:: clock_interface_selection_forward_traces
            
            	Selection forwardtrace operational data for clock\-interfaces
            	**type**\:  :py:class:`ClockInterfaceSelectionForwardTraces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces>`
            
            .. attribute:: time_of_day_back_trace
            
            	Selection backtrace operational data for time\-of\-day on a particular node
            	**type**\:  :py:class:`TimeOfDayBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace>`
            
            .. attribute:: ntp_selection_forward_trace
            
            	Selection forwardtrace operational data for a NTP clock
            	**type**\:  :py:class:`NtpSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace>`
            
            .. attribute:: ptp_selection_forward_trace
            
            	Selection forwardtrace operational data for a PTP clock
            	**type**\:  :py:class:`PtpSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace>`
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FrequencySynchronization.GlobalNodes.GlobalNode, self).__init__()

                self.yang_name = "global-node"
                self.yang_parent_name = "global-nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"clock-interface-selection-back-traces" : ("clock_interface_selection_back_traces", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces), "clock-interface-selection-forward-traces" : ("clock_interface_selection_forward_traces", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces), "time-of-day-back-trace" : ("time_of_day_back_trace", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace), "ntp-selection-forward-trace" : ("ntp_selection_forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace), "ptp-selection-forward-trace" : ("ptp_selection_forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace)}
                self._child_list_classes = {}

                self.node = YLeaf(YType.str, "node")

                self.clock_interface_selection_back_traces = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces()
                self.clock_interface_selection_back_traces.parent = self
                self._children_name_map["clock_interface_selection_back_traces"] = "clock-interface-selection-back-traces"
                self._children_yang_names.add("clock-interface-selection-back-traces")

                self.clock_interface_selection_forward_traces = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces()
                self.clock_interface_selection_forward_traces.parent = self
                self._children_name_map["clock_interface_selection_forward_traces"] = "clock-interface-selection-forward-traces"
                self._children_yang_names.add("clock-interface-selection-forward-traces")

                self.time_of_day_back_trace = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace()
                self.time_of_day_back_trace.parent = self
                self._children_name_map["time_of_day_back_trace"] = "time-of-day-back-trace"
                self._children_yang_names.add("time-of-day-back-trace")

                self.ntp_selection_forward_trace = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace()
                self.ntp_selection_forward_trace.parent = self
                self._children_name_map["ntp_selection_forward_trace"] = "ntp-selection-forward-trace"
                self._children_yang_names.add("ntp-selection-forward-trace")

                self.ptp_selection_forward_trace = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace()
                self.ptp_selection_forward_trace.parent = self
                self._children_name_map["ptp_selection_forward_trace"] = "ptp-selection-forward-trace"
                self._children_yang_names.add("ptp-selection-forward-trace")
                self._segment_path = lambda: "global-node" + "[node='" + self.node.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/global-nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode, ['node'], name, value)


            class ClockInterfaceSelectionBackTraces(Entity):
                """
                Selection backtrace operational data for
                clock\-interfaces
                
                .. attribute:: clock_interface_selection_back_trace
                
                	Selection backtrace operational data for a particular clock\-interface
                	**type**\: list of  		 :py:class:`ClockInterfaceSelectionBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces, self).__init__()

                    self.yang_name = "clock-interface-selection-back-traces"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"clock-interface-selection-back-trace" : ("clock_interface_selection_back_trace", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace)}

                    self.clock_interface_selection_back_trace = YList(self)
                    self._segment_path = lambda: "clock-interface-selection-back-traces"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces, [], name, value)


                class ClockInterfaceSelectionBackTrace(Entity):
                    """
                    Selection backtrace operational data for a
                    particular clock\-interface
                    
                    .. attribute:: clock_type  <key>
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  <key>
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: selected_source
                    
                    	Source which has been selected for output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource>`
                    
                    .. attribute:: selection_point
                    
                    	List of selection points in the backtrace
                    	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace, self).__init__()

                        self.yang_name = "clock-interface-selection-back-trace"
                        self.yang_parent_name = "clock-interface-selection-back-traces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"selected-source" : ("selected_source", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource)}
                        self._child_list_classes = {"selection-point" : ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint)}

                        self.clock_type = YLeaf(YType.enumeration, "clock-type")

                        self.port = YLeaf(YType.int32, "port")

                        self.selected_source = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource()
                        self.selected_source.parent = self
                        self._children_name_map["selected_source"] = "selected-source"
                        self._children_yang_names.add("selected-source")

                        self.selection_point = YList(self)
                        self._segment_path = lambda: "clock-interface-selection-back-trace" + "[clock-type='" + self.clock_type.get() + "']" + "[port='" + self.port.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace, ['clock_type', 'port'], name, value)


                    class SelectedSource(Entity):
                        """
                        Source which has been selected for output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "clock-interface-selection-back-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId)}
                            self._child_list_classes = {}

                            self.source_class = YLeaf(YType.enumeration, "source-class")

                            self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                            self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                            self.node = YLeaf(YType.str, "node")

                            self.ptp_node = YLeaf(YType.str, "ptp-node")

                            self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                            self.ntp_node = YLeaf(YType.str, "ntp-node")

                            self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"
                            self._children_yang_names.add("clock-id")
                            self._segment_path = lambda: "selected-source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: port
                            
                            	Port number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.node = YLeaf(YType.str, "node")

                                self.port = YLeaf(YType.uint32, "port")
                                self._segment_path = lambda: "clock-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectedSource.ClockId, ['node', 'port'], name, value)


                    class SelectionPoint(Entity):
                        """
                        List of selection points in the backtrace
                        
                        .. attribute:: selection_point_type
                        
                        	Selection point type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point descrption
                        	**type**\: str
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint, self).__init__()

                            self.yang_name = "selection-point"
                            self.yang_parent_name = "clock-interface-selection-back-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                            self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                            self.node = YLeaf(YType.str, "node")
                            self._segment_path = lambda: "selection-point"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionBackTraces.ClockInterfaceSelectionBackTrace.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


            class ClockInterfaceSelectionForwardTraces(Entity):
                """
                Selection forwardtrace operational data for
                clock\-interfaces
                
                .. attribute:: clock_interface_selection_forward_trace
                
                	Selection forwardtrace operational data for a particular clock\-interface
                	**type**\: list of  		 :py:class:`ClockInterfaceSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces, self).__init__()

                    self.yang_name = "clock-interface-selection-forward-traces"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"clock-interface-selection-forward-trace" : ("clock_interface_selection_forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace)}

                    self.clock_interface_selection_forward_trace = YList(self)
                    self._segment_path = lambda: "clock-interface-selection-forward-traces"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces, [], name, value)


                class ClockInterfaceSelectionForwardTrace(Entity):
                    """
                    Selection forwardtrace operational data for a
                    particular clock\-interface
                    
                    .. attribute:: clock_type  <key>
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  <key>
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: forward_trace
                    
                    	Selection ForwardTrace
                    	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace, self).__init__()

                        self.yang_name = "clock-interface-selection-forward-trace"
                        self.yang_parent_name = "clock-interface-selection-forward-traces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"forward-trace" : ("forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace)}

                        self.clock_type = YLeaf(YType.enumeration, "clock-type")

                        self.port = YLeaf(YType.int32, "port")

                        self.forward_trace = YList(self)
                        self._segment_path = lambda: "clock-interface-selection-forward-trace" + "[clock-type='" + self.clock_type.get() + "']" + "[port='" + self.port.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace, ['clock_type', 'port'], name, value)


                    class ForwardTrace(Entity):
                        """
                        Selection ForwardTrace
                        
                        .. attribute:: forward_trace_node
                        
                        	The source or selection point at this point in the forwardtrace
                        	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace, self).__init__()

                            self.yang_name = "forward-trace"
                            self.yang_parent_name = "clock-interface-selection-forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"forward-trace-node" : ("forward_trace_node", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode)}
                            self._child_list_classes = {}

                            self.forward_trace_node = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                            self.forward_trace_node.parent = self
                            self._children_name_map["forward_trace_node"] = "forward-trace-node"
                            self._children_yang_names.add("forward-trace-node")
                            self._segment_path = lambda: "forward-trace"


                        class ForwardTraceNode(Entity):
                            """
                            The source or selection point at this point in
                            the forwardtrace
                            
                            .. attribute:: selection_point
                            
                            	Selection Point
                            	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                            
                            .. attribute:: source
                            
                            	Timing Source
                            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                            
                            .. attribute:: node_type
                            
                            	NodeType
                            	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                                self.yang_name = "forward-trace-node"
                                self.yang_parent_name = "forward-trace"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"selection-point" : ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint), "source" : ("source", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source)}
                                self._child_list_classes = {}

                                self.node_type = YLeaf(YType.enumeration, "node-type")

                                self.selection_point = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                                self.selection_point.parent = self
                                self._children_name_map["selection_point"] = "selection-point"
                                self._children_yang_names.add("selection-point")

                                self.source = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                                self.source.parent = self
                                self._children_name_map["source"] = "source"
                                self._children_yang_names.add("source")
                                self._segment_path = lambda: "forward-trace-node"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                            class SelectionPoint(Entity):
                                """
                                Selection Point
                                
                                .. attribute:: selection_point_type
                                
                                	Selection point type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: selection_point_description
                                
                                	Selection point descrption
                                	**type**\: str
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                    self.yang_name = "selection-point"
                                    self.yang_parent_name = "forward-trace-node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                                    self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                                    self.node = YLeaf(YType.str, "node")
                                    self._segment_path = lambda: "selection-point"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


                            class Source(Entity):
                                """
                                Timing Source
                                
                                .. attribute:: clock_id
                                
                                	Clock ID
                                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                                
                                .. attribute:: source_class
                                
                                	SourceClass
                                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                                
                                .. attribute:: ethernet_interface
                                
                                	Ethernet interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: sonet_interface
                                
                                	SONET interfaces
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: node
                                
                                	Internal Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: ptp_node
                                
                                	PTP Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: satellite_access_interface
                                
                                	Satellite Access Interface
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: ntp_node
                                
                                	NTP Clock Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                    self.yang_name = "source"
                                    self.yang_parent_name = "forward-trace-node"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)}
                                    self._child_list_classes = {}

                                    self.source_class = YLeaf(YType.enumeration, "source-class")

                                    self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                                    self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                                    self.node = YLeaf(YType.str, "node")

                                    self.ptp_node = YLeaf(YType.str, "ptp-node")

                                    self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                                    self.ntp_node = YLeaf(YType.str, "ntp-node")

                                    self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                    self.clock_id.parent = self
                                    self._children_name_map["clock_id"] = "clock-id"
                                    self._children_yang_names.add("clock-id")
                                    self._segment_path = lambda: "source"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                                class ClockId(Entity):
                                    """
                                    Clock ID
                                    
                                    .. attribute:: node
                                    
                                    	Node
                                    	**type**\: str
                                    
                                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                    
                                    .. attribute:: port
                                    
                                    	Port number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'freqsync-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                        self.yang_name = "clock-id"
                                        self.yang_parent_name = "source"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.node = YLeaf(YType.str, "node")

                                        self.port = YLeaf(YType.uint32, "port")
                                        self._segment_path = lambda: "clock-id"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.ClockInterfaceSelectionForwardTraces.ClockInterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'port'], name, value)


            class TimeOfDayBackTrace(Entity):
                """
                Selection backtrace operational data for
                time\-of\-day on a particular node
                
                .. attribute:: selected_source
                
                	Source which has been selected for output
                	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource>`
                
                .. attribute:: selection_point
                
                	List of selection points in the backtrace
                	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace, self).__init__()

                    self.yang_name = "time-of-day-back-trace"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"selected-source" : ("selected_source", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource)}
                    self._child_list_classes = {"selection-point" : ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint)}

                    self.selected_source = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource()
                    self.selected_source.parent = self
                    self._children_name_map["selected_source"] = "selected-source"
                    self._children_yang_names.add("selected-source")

                    self.selection_point = YList(self)
                    self._segment_path = lambda: "time-of-day-back-trace"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace, [], name, value)


                class SelectedSource(Entity):
                    """
                    Source which has been selected for output
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId>`
                    
                    .. attribute:: source_class
                    
                    	SourceClass
                    	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                    
                    .. attribute:: ethernet_interface
                    
                    	Ethernet interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: sonet_interface
                    
                    	SONET interfaces
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: node
                    
                    	Internal Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: ptp_node
                    
                    	PTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: satellite_access_interface
                    
                    	Satellite Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: ntp_node
                    
                    	NTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource, self).__init__()

                        self.yang_name = "selected-source"
                        self.yang_parent_name = "time-of-day-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId)}
                        self._child_list_classes = {}

                        self.source_class = YLeaf(YType.enumeration, "source-class")

                        self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                        self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                        self.node = YLeaf(YType.str, "node")

                        self.ptp_node = YLeaf(YType.str, "ptp-node")

                        self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                        self.ntp_node = YLeaf(YType.str, "ntp-node")

                        self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId()
                        self.clock_id.parent = self
                        self._children_name_map["clock_id"] = "clock-id"
                        self._children_yang_names.add("clock-id")
                        self._segment_path = lambda: "selected-source"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                    class ClockId(Entity):
                        """
                        Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId, self).__init__()

                            self.yang_name = "clock-id"
                            self.yang_parent_name = "selected-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.node = YLeaf(YType.str, "node")

                            self.port = YLeaf(YType.uint32, "port")
                            self._segment_path = lambda: "clock-id"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectedSource.ClockId, ['node', 'port'], name, value)


                class SelectionPoint(Entity):
                    """
                    List of selection points in the backtrace
                    
                    .. attribute:: selection_point_type
                    
                    	Selection point type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point descrption
                    	**type**\: str
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint, self).__init__()

                        self.yang_name = "selection-point"
                        self.yang_parent_name = "time-of-day-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                        self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                        self.node = YLeaf(YType.str, "node")
                        self._segment_path = lambda: "selection-point"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.TimeOfDayBackTrace.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


            class NtpSelectionForwardTrace(Entity):
                """
                Selection forwardtrace operational data for a
                NTP clock
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace, self).__init__()

                    self.yang_name = "ntp-selection-forward-trace"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"forward-trace" : ("forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace)}

                    self.forward_trace = YList(self)
                    self._segment_path = lambda: "ntp-selection-forward-trace"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace, [], name, value)


                class ForwardTrace(Entity):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace, self).__init__()

                        self.yang_name = "forward-trace"
                        self.yang_parent_name = "ntp-selection-forward-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"forward-trace-node" : ("forward_trace_node", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode)}
                        self._child_list_classes = {}

                        self.forward_trace_node = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                        self.forward_trace_node.parent = self
                        self._children_name_map["forward_trace_node"] = "forward-trace-node"
                        self._children_yang_names.add("forward-trace-node")
                        self._segment_path = lambda: "forward-trace"


                    class ForwardTraceNode(Entity):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                            self.yang_name = "forward-trace-node"
                            self.yang_parent_name = "forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"selection-point" : ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint), "source" : ("source", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source)}
                            self._child_list_classes = {}

                            self.node_type = YLeaf(YType.enumeration, "node-type")

                            self.selection_point = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                            self.selection_point.parent = self
                            self._children_name_map["selection_point"] = "selection-point"
                            self._children_yang_names.add("selection-point")

                            self.source = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                            self.source.parent = self
                            self._children_name_map["source"] = "source"
                            self._children_yang_names.add("source")
                            self._segment_path = lambda: "forward-trace-node"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                        class SelectionPoint(Entity):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                self.yang_name = "selection-point"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                                self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                                self.node = YLeaf(YType.str, "node")
                                self._segment_path = lambda: "selection-point"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


                        class Source(Entity):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)}
                                self._child_list_classes = {}

                                self.source_class = YLeaf(YType.enumeration, "source-class")

                                self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                                self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                                self.node = YLeaf(YType.str, "node")

                                self.ptp_node = YLeaf(YType.str, "ptp-node")

                                self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                                self.ntp_node = YLeaf(YType.str, "ntp-node")

                                self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"
                                self._children_yang_names.add("clock-id")
                                self._segment_path = lambda: "source"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: port
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.node = YLeaf(YType.str, "node")

                                    self.port = YLeaf(YType.uint32, "port")
                                    self._segment_path = lambda: "clock-id"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.NtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'port'], name, value)


            class PtpSelectionForwardTrace(Entity):
                """
                Selection forwardtrace operational data for a
                PTP clock
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace, self).__init__()

                    self.yang_name = "ptp-selection-forward-trace"
                    self.yang_parent_name = "global-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"forward-trace" : ("forward_trace", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace)}

                    self.forward_trace = YList(self)
                    self._segment_path = lambda: "ptp-selection-forward-trace"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace, [], name, value)


                class ForwardTrace(Entity):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace, self).__init__()

                        self.yang_name = "forward-trace"
                        self.yang_parent_name = "ptp-selection-forward-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"forward-trace-node" : ("forward_trace_node", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode)}
                        self._child_list_classes = {}

                        self.forward_trace_node = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                        self.forward_trace_node.parent = self
                        self._children_name_map["forward_trace_node"] = "forward-trace-node"
                        self._children_yang_names.add("forward-trace-node")
                        self._segment_path = lambda: "forward-trace"


                    class ForwardTraceNode(Entity):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                            self.yang_name = "forward-trace-node"
                            self.yang_parent_name = "forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"selection-point" : ("selection_point", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint), "source" : ("source", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source)}
                            self._child_list_classes = {}

                            self.node_type = YLeaf(YType.enumeration, "node-type")

                            self.selection_point = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                            self.selection_point.parent = self
                            self._children_name_map["selection_point"] = "selection-point"
                            self._children_yang_names.add("selection-point")

                            self.source = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                            self.source.parent = self
                            self._children_name_map["source"] = "source"
                            self._children_yang_names.add("source")
                            self._segment_path = lambda: "forward-trace-node"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                        class SelectionPoint(Entity):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                self.yang_name = "selection-point"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                                self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                                self.node = YLeaf(YType.str, "node")
                                self._segment_path = lambda: "selection-point"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


                        class Source(Entity):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)}
                                self._child_list_classes = {}

                                self.source_class = YLeaf(YType.enumeration, "source-class")

                                self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                                self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                                self.node = YLeaf(YType.str, "node")

                                self.ptp_node = YLeaf(YType.str, "ptp-node")

                                self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                                self.ntp_node = YLeaf(YType.str, "ntp-node")

                                self.clock_id = FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"
                                self._children_yang_names.add("clock-id")
                                self._segment_path = lambda: "source"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: port
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.node = YLeaf(YType.str, "node")

                                    self.port = YLeaf(YType.uint32, "port")
                                    self._segment_path = lambda: "clock-id"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalNodes.GlobalNode.PtpSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'port'], name, value)


    class GlobalInterfaces(Entity):
        """
        Table for global interface operational data
        
        .. attribute:: global_interface
        
        	Global interface information for a particular interface
        	**type**\: list of  		 :py:class:`GlobalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FrequencySynchronization.GlobalInterfaces, self).__init__()

            self.yang_name = "global-interfaces"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"global-interface" : ("global_interface", FrequencySynchronization.GlobalInterfaces.GlobalInterface)}

            self.global_interface = YList(self)
            self._segment_path = lambda: "global-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.GlobalInterfaces, [], name, value)


        class GlobalInterface(Entity):
            """
            Global interface information for a particular
            interface
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: interface_selection_forward_trace
            
            	Selection forwardtrace operational data for a particular interface
            	**type**\:  :py:class:`InterfaceSelectionForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace>`
            
            .. attribute:: interface_selection_back_trace
            
            	Selection backtrace operational data for a particular interface
            	**type**\:  :py:class:`InterfaceSelectionBackTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace>`
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FrequencySynchronization.GlobalInterfaces.GlobalInterface, self).__init__()

                self.yang_name = "global-interface"
                self.yang_parent_name = "global-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"interface-selection-forward-trace" : ("interface_selection_forward_trace", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace), "interface-selection-back-trace" : ("interface_selection_back_trace", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.interface_selection_forward_trace = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace()
                self.interface_selection_forward_trace.parent = self
                self._children_name_map["interface_selection_forward_trace"] = "interface-selection-forward-trace"
                self._children_yang_names.add("interface-selection-forward-trace")

                self.interface_selection_back_trace = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace()
                self.interface_selection_back_trace.parent = self
                self._children_name_map["interface_selection_back_trace"] = "interface-selection-back-trace"
                self._children_yang_names.add("interface-selection-back-trace")
                self._segment_path = lambda: "global-interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/global-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface, ['interface_name'], name, value)


            class InterfaceSelectionForwardTrace(Entity):
                """
                Selection forwardtrace operational data for a
                particular interface
                
                .. attribute:: forward_trace
                
                	Selection ForwardTrace
                	**type**\: list of  		 :py:class:`ForwardTrace <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace, self).__init__()

                    self.yang_name = "interface-selection-forward-trace"
                    self.yang_parent_name = "global-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"forward-trace" : ("forward_trace", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace)}

                    self.forward_trace = YList(self)
                    self._segment_path = lambda: "interface-selection-forward-trace"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace, [], name, value)


                class ForwardTrace(Entity):
                    """
                    Selection ForwardTrace
                    
                    .. attribute:: forward_trace_node
                    
                    	The source or selection point at this point in the forwardtrace
                    	**type**\:  :py:class:`ForwardTraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace, self).__init__()

                        self.yang_name = "forward-trace"
                        self.yang_parent_name = "interface-selection-forward-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"forward-trace-node" : ("forward_trace_node", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode)}
                        self._child_list_classes = {}

                        self.forward_trace_node = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode()
                        self.forward_trace_node.parent = self
                        self._children_name_map["forward_trace_node"] = "forward-trace-node"
                        self._children_yang_names.add("forward-trace-node")
                        self._segment_path = lambda: "forward-trace"


                    class ForwardTraceNode(Entity):
                        """
                        The source or selection point at this point in
                        the forwardtrace
                        
                        .. attribute:: selection_point
                        
                        	Selection Point
                        	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint>`
                        
                        .. attribute:: source
                        
                        	Timing Source
                        	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source>`
                        
                        .. attribute:: node_type
                        
                        	NodeType
                        	**type**\:  :py:class:`FsyncBagForwardtraceNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagForwardtraceNode>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, self).__init__()

                            self.yang_name = "forward-trace-node"
                            self.yang_parent_name = "forward-trace"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"selection-point" : ("selection_point", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint), "source" : ("source", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source)}
                            self._child_list_classes = {}

                            self.node_type = YLeaf(YType.enumeration, "node-type")

                            self.selection_point = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint()
                            self.selection_point.parent = self
                            self._children_name_map["selection_point"] = "selection-point"
                            self._children_yang_names.add("selection-point")

                            self.source = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source()
                            self.source.parent = self
                            self._children_name_map["source"] = "source"
                            self._children_yang_names.add("source")
                            self._segment_path = lambda: "forward-trace-node"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode, ['node_type'], name, value)


                        class SelectionPoint(Entity):
                            """
                            Selection Point
                            
                            .. attribute:: selection_point_type
                            
                            	Selection point type
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: selection_point_description
                            
                            	Selection point descrption
                            	**type**\: str
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, self).__init__()

                                self.yang_name = "selection-point"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                                self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                                self.node = YLeaf(YType.str, "node")
                                self._segment_path = lambda: "selection-point"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


                        class Source(Entity):
                            """
                            Timing Source
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, self).__init__()

                                self.yang_name = "source"
                                self.yang_parent_name = "forward-trace-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId)}
                                self._child_list_classes = {}

                                self.source_class = YLeaf(YType.enumeration, "source-class")

                                self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                                self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                                self.node = YLeaf(YType.str, "node")

                                self.ptp_node = YLeaf(YType.str, "ptp-node")

                                self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                                self.ntp_node = YLeaf(YType.str, "ntp-node")

                                self.clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"
                                self._children_yang_names.add("clock-id")
                                self._segment_path = lambda: "source"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: port
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.node = YLeaf(YType.str, "node")

                                    self.port = YLeaf(YType.uint32, "port")
                                    self._segment_path = lambda: "clock-id"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionForwardTrace.ForwardTrace.ForwardTraceNode.Source.ClockId, ['node', 'port'], name, value)


            class InterfaceSelectionBackTrace(Entity):
                """
                Selection backtrace operational data for a
                particular interface
                
                .. attribute:: selected_source
                
                	Source which has been selected for output
                	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource>`
                
                .. attribute:: selection_point
                
                	List of selection points in the backtrace
                	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace, self).__init__()

                    self.yang_name = "interface-selection-back-trace"
                    self.yang_parent_name = "global-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"selected-source" : ("selected_source", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource)}
                    self._child_list_classes = {"selection-point" : ("selection_point", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint)}

                    self.selected_source = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource()
                    self.selected_source.parent = self
                    self._children_name_map["selected_source"] = "selected-source"
                    self._children_yang_names.add("selected-source")

                    self.selection_point = YList(self)
                    self._segment_path = lambda: "interface-selection-back-trace"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace, [], name, value)


                class SelectedSource(Entity):
                    """
                    Source which has been selected for output
                    
                    .. attribute:: clock_id
                    
                    	Clock ID
                    	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId>`
                    
                    .. attribute:: source_class
                    
                    	SourceClass
                    	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                    
                    .. attribute:: ethernet_interface
                    
                    	Ethernet interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: sonet_interface
                    
                    	SONET interfaces
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: node
                    
                    	Internal Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: ptp_node
                    
                    	PTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: satellite_access_interface
                    
                    	Satellite Access Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: ntp_node
                    
                    	NTP Clock Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource, self).__init__()

                        self.yang_name = "selected-source"
                        self.yang_parent_name = "interface-selection-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId)}
                        self._child_list_classes = {}

                        self.source_class = YLeaf(YType.enumeration, "source-class")

                        self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                        self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                        self.node = YLeaf(YType.str, "node")

                        self.ptp_node = YLeaf(YType.str, "ptp-node")

                        self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                        self.ntp_node = YLeaf(YType.str, "ntp-node")

                        self.clock_id = FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId()
                        self.clock_id.parent = self
                        self._children_name_map["clock_id"] = "clock-id"
                        self._children_yang_names.add("clock-id")
                        self._segment_path = lambda: "selected-source"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                    class ClockId(Entity):
                        """
                        Clock ID
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: port
                        
                        	Port number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId, self).__init__()

                            self.yang_name = "clock-id"
                            self.yang_parent_name = "selected-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.node = YLeaf(YType.str, "node")

                            self.port = YLeaf(YType.uint32, "port")
                            self._segment_path = lambda: "clock-id"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectedSource.ClockId, ['node', 'port'], name, value)


                class SelectionPoint(Entity):
                    """
                    List of selection points in the backtrace
                    
                    .. attribute:: selection_point_type
                    
                    	Selection point type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selection_point_description
                    
                    	Selection point descrption
                    	**type**\: str
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint, self).__init__()

                        self.yang_name = "selection-point"
                        self.yang_parent_name = "interface-selection-back-trace"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                        self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                        self.node = YLeaf(YType.str, "node")
                        self._segment_path = lambda: "selection-point"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.GlobalInterfaces.GlobalInterface.InterfaceSelectionBackTrace.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


    class Summary(Entity):
        """
        Summary operational data
        
        .. attribute:: frequency_summary
        
        	Summary of sources selected for frequency
        	**type**\: list of  		 :py:class:`FrequencySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary>`
        
        .. attribute:: time_of_day_summary
        
        	Summary of sources selected for time\-of\-day
        	**type**\: list of  		 :py:class:`TimeOfDaySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FrequencySynchronization.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"frequency-summary" : ("frequency_summary", FrequencySynchronization.Summary.FrequencySummary), "time-of-day-summary" : ("time_of_day_summary", FrequencySynchronization.Summary.TimeOfDaySummary)}

            self.frequency_summary = YList(self)
            self.time_of_day_summary = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.Summary, [], name, value)


        class FrequencySummary(Entity):
            """
            Summary of sources selected for frequency
            
            .. attribute:: source
            
            	The source associated with this summary information
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source>`
            
            .. attribute:: clock_count
            
            	The number of clock\-interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ethernet_count
            
            	The number of Ethernet interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: sonet_count
            
            	The number of SONET/SDH interfaces being driven by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FrequencySynchronization.Summary.FrequencySummary, self).__init__()

                self.yang_name = "frequency-summary"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"source" : ("source", FrequencySynchronization.Summary.FrequencySummary.Source)}
                self._child_list_classes = {}

                self.clock_count = YLeaf(YType.uint32, "clock-count")

                self.ethernet_count = YLeaf(YType.uint32, "ethernet-count")

                self.sonet_count = YLeaf(YType.uint32, "sonet-count")

                self.source = FrequencySynchronization.Summary.FrequencySummary.Source()
                self.source.parent = self
                self._children_name_map["source"] = "source"
                self._children_yang_names.add("source")
                self._segment_path = lambda: "frequency-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary, ['clock_count', 'ethernet_count', 'sonet_count'], name, value)


            class Source(Entity):
                """
                The source associated with this summary
                information
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.FrequencySummary.Source.ClockId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Summary.FrequencySummary.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "frequency-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Summary.FrequencySummary.Source.ClockId)}
                    self._child_list_classes = {}

                    self.source_class = YLeaf(YType.enumeration, "source-class")

                    self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                    self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                    self.node = YLeaf(YType.str, "node")

                    self.ptp_node = YLeaf(YType.str, "ptp-node")

                    self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                    self.ntp_node = YLeaf(YType.str, "ntp-node")

                    self.clock_id = FrequencySynchronization.Summary.FrequencySummary.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"
                    self._children_yang_names.add("clock-id")
                    self._segment_path = lambda: "source"
                    self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/frequency-summary/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: port
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Summary.FrequencySummary.Source.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.node = YLeaf(YType.str, "node")

                        self.port = YLeaf(YType.uint32, "port")
                        self._segment_path = lambda: "clock-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/frequency-summary/source/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.FrequencySummary.Source.ClockId, ['node', 'port'], name, value)


        class TimeOfDaySummary(Entity):
            """
            Summary of sources selected for time\-of\-day
            
            .. attribute:: source
            
            	The source associated with this summary information
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source>`
            
            .. attribute:: node_count
            
            	The number of cards having their time\-of\-day set by the source
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FrequencySynchronization.Summary.TimeOfDaySummary, self).__init__()

                self.yang_name = "time-of-day-summary"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"source" : ("source", FrequencySynchronization.Summary.TimeOfDaySummary.Source)}
                self._child_list_classes = {}

                self.node_count = YLeaf(YType.uint32, "node-count")

                self.source = FrequencySynchronization.Summary.TimeOfDaySummary.Source()
                self.source.parent = self
                self._children_name_map["source"] = "source"
                self._children_yang_names.add("source")
                self._segment_path = lambda: "time-of-day-summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary, ['node_count'], name, value)


            class Source(Entity):
                """
                The source associated with this summary
                information
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Summary.TimeOfDaySummary.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "time-of-day-summary"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId)}
                    self._child_list_classes = {}

                    self.source_class = YLeaf(YType.enumeration, "source-class")

                    self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                    self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                    self.node = YLeaf(YType.str, "node")

                    self.ptp_node = YLeaf(YType.str, "ptp-node")

                    self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                    self.ntp_node = YLeaf(YType.str, "ntp-node")

                    self.clock_id = FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"
                    self._children_yang_names.add("clock-id")
                    self._segment_path = lambda: "source"
                    self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/time-of-day-summary/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: port
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.node = YLeaf(YType.str, "node")

                        self.port = YLeaf(YType.uint32, "port")
                        self._segment_path = lambda: "clock-id"
                        self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/summary/time-of-day-summary/source/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Summary.TimeOfDaySummary.Source.ClockId, ['node', 'port'], name, value)


    class Interfaces(Entity):
        """
        Table for interface operational data
        
        .. attribute:: interface
        
        	Operational data for a particular interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FrequencySynchronization.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", FrequencySynchronization.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Operational data for a particular interface
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: source
            
            	The source ID for the interface
            	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.Source>`
            
            .. attribute:: selected_source
            
            	Timing source selected for interface output
            	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.SelectedSource>`
            
            .. attribute:: quality_level_received
            
            	Received quality level
            	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.QualityLevelReceived>`
            
            .. attribute:: quality_level_damped
            
            	Quality level after damping has been applied
            	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.QualityLevelDamped>`
            
            .. attribute:: quality_level_effective_input
            
            	The effective input quality level
            	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveInput>`
            
            .. attribute:: quality_level_effective_output
            
            	The effective output quality level
            	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveOutput>`
            
            .. attribute:: quality_level_selected_source
            
            	The quality level of the source driving this interface
            	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.QualityLevelSelectedSource>`
            
            .. attribute:: ethernet_peer_information
            
            	Ethernet peer information
            	**type**\:  :py:class:`EthernetPeerInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation>`
            
            .. attribute:: esmc_statistics
            
            	ESMC Statistics
            	**type**\:  :py:class:`EsmcStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.EsmcStatistics>`
            
            .. attribute:: name
            
            	Interface name
            	**type**\: str
            
            .. attribute:: state
            
            	Interface state
            	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.ImStateEnum>`
            
            .. attribute:: ssm_enabled
            
            	SSM is enabled on the interface
            	**type**\: bool
            
            .. attribute:: squelched
            
            	The interface output is squelched
            	**type**\: bool
            
            .. attribute:: selection_input
            
            	The interface is an input for selection
            	**type**\: bool
            
            .. attribute:: priority
            
            	Priority
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: time_of_day_priority
            
            	Time\-of\-day priority
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: damping_state
            
            	Damping state
            	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
            
            .. attribute:: damping_time
            
            	Time until damping state changes in ms
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: wait_to_restore_time
            
            	Wait\-to\-restore time for the interface
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: supports_frequency
            
            	The PTP clock supports frequency
            	**type**\: bool
            
            .. attribute:: supports_time_of_day
            
            	The PTP clock supports time
            	**type**\: bool
            
            .. attribute:: spa_selection_point
            
            	Spa selection points
            	**type**\: list of int
            
            	**range:** 0..255
            
            .. attribute:: spa_selection_points_description
            
            	Spa selection points descrption
            	**type**\: list of str
            
            .. attribute:: node_selection_point
            
            	Node selection points
            	**type**\: list of int
            
            	**range:** 0..255
            
            .. attribute:: node_selection_points_description
            
            	Node selection points descrption
            	**type**\: list of str
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FrequencySynchronization.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"source" : ("source", FrequencySynchronization.Interfaces.Interface.Source), "selected-source" : ("selected_source", FrequencySynchronization.Interfaces.Interface.SelectedSource), "quality-level-received" : ("quality_level_received", FrequencySynchronization.Interfaces.Interface.QualityLevelReceived), "quality-level-damped" : ("quality_level_damped", FrequencySynchronization.Interfaces.Interface.QualityLevelDamped), "quality-level-effective-input" : ("quality_level_effective_input", FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveInput), "quality-level-effective-output" : ("quality_level_effective_output", FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveOutput), "quality-level-selected-source" : ("quality_level_selected_source", FrequencySynchronization.Interfaces.Interface.QualityLevelSelectedSource), "ethernet-peer-information" : ("ethernet_peer_information", FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation), "esmc-statistics" : ("esmc_statistics", FrequencySynchronization.Interfaces.Interface.EsmcStatistics)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.name = YLeaf(YType.str, "name")

                self.state = YLeaf(YType.enumeration, "state")

                self.ssm_enabled = YLeaf(YType.boolean, "ssm-enabled")

                self.squelched = YLeaf(YType.boolean, "squelched")

                self.selection_input = YLeaf(YType.boolean, "selection-input")

                self.priority = YLeaf(YType.uint8, "priority")

                self.time_of_day_priority = YLeaf(YType.uint8, "time-of-day-priority")

                self.damping_state = YLeaf(YType.enumeration, "damping-state")

                self.damping_time = YLeaf(YType.uint32, "damping-time")

                self.wait_to_restore_time = YLeaf(YType.uint16, "wait-to-restore-time")

                self.supports_frequency = YLeaf(YType.boolean, "supports-frequency")

                self.supports_time_of_day = YLeaf(YType.boolean, "supports-time-of-day")

                self.spa_selection_point = YLeafList(YType.uint8, "spa-selection-point")

                self.spa_selection_points_description = YLeafList(YType.str, "spa-selection-points-description")

                self.node_selection_point = YLeafList(YType.uint8, "node-selection-point")

                self.node_selection_points_description = YLeafList(YType.str, "node-selection-points-description")

                self.source = FrequencySynchronization.Interfaces.Interface.Source()
                self.source.parent = self
                self._children_name_map["source"] = "source"
                self._children_yang_names.add("source")

                self.selected_source = FrequencySynchronization.Interfaces.Interface.SelectedSource()
                self.selected_source.parent = self
                self._children_name_map["selected_source"] = "selected-source"
                self._children_yang_names.add("selected-source")

                self.quality_level_received = FrequencySynchronization.Interfaces.Interface.QualityLevelReceived()
                self.quality_level_received.parent = self
                self._children_name_map["quality_level_received"] = "quality-level-received"
                self._children_yang_names.add("quality-level-received")

                self.quality_level_damped = FrequencySynchronization.Interfaces.Interface.QualityLevelDamped()
                self.quality_level_damped.parent = self
                self._children_name_map["quality_level_damped"] = "quality-level-damped"
                self._children_yang_names.add("quality-level-damped")

                self.quality_level_effective_input = FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveInput()
                self.quality_level_effective_input.parent = self
                self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"
                self._children_yang_names.add("quality-level-effective-input")

                self.quality_level_effective_output = FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveOutput()
                self.quality_level_effective_output.parent = self
                self._children_name_map["quality_level_effective_output"] = "quality-level-effective-output"
                self._children_yang_names.add("quality-level-effective-output")

                self.quality_level_selected_source = FrequencySynchronization.Interfaces.Interface.QualityLevelSelectedSource()
                self.quality_level_selected_source.parent = self
                self._children_name_map["quality_level_selected_source"] = "quality-level-selected-source"
                self._children_yang_names.add("quality-level-selected-source")

                self.ethernet_peer_information = FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation()
                self.ethernet_peer_information.parent = self
                self._children_name_map["ethernet_peer_information"] = "ethernet-peer-information"
                self._children_yang_names.add("ethernet-peer-information")

                self.esmc_statistics = FrequencySynchronization.Interfaces.Interface.EsmcStatistics()
                self.esmc_statistics.parent = self
                self._children_name_map["esmc_statistics"] = "esmc-statistics"
                self._children_yang_names.add("esmc-statistics")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.Interfaces.Interface, ['interface_name', 'name', 'state', 'ssm_enabled', 'squelched', 'selection_input', 'priority', 'time_of_day_priority', 'damping_state', 'damping_time', 'wait_to_restore_time', 'supports_frequency', 'supports_time_of_day', 'spa_selection_point', 'spa_selection_points_description', 'node_selection_point', 'node_selection_points_description'], name, value)


            class Source(Entity):
                """
                The source ID for the interface
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.Source.ClockId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.Source, self).__init__()

                    self.yang_name = "source"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Interfaces.Interface.Source.ClockId)}
                    self._child_list_classes = {}

                    self.source_class = YLeaf(YType.enumeration, "source-class")

                    self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                    self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                    self.node = YLeaf(YType.str, "node")

                    self.ptp_node = YLeaf(YType.str, "ptp-node")

                    self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                    self.ntp_node = YLeaf(YType.str, "ntp-node")

                    self.clock_id = FrequencySynchronization.Interfaces.Interface.Source.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"
                    self._children_yang_names.add("clock-id")
                    self._segment_path = lambda: "source"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: port
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Interfaces.Interface.Source.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.node = YLeaf(YType.str, "node")

                        self.port = YLeaf(YType.uint32, "port")
                        self._segment_path = lambda: "clock-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Interfaces.Interface.Source.ClockId, ['node', 'port'], name, value)


            class SelectedSource(Entity):
                """
                Timing source selected for interface output
                
                .. attribute:: clock_id
                
                	Clock ID
                	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.SelectedSource.ClockId>`
                
                .. attribute:: source_class
                
                	SourceClass
                	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                
                .. attribute:: ethernet_interface
                
                	Ethernet interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: sonet_interface
                
                	SONET interfaces
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: node
                
                	Internal Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: ptp_node
                
                	PTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: satellite_access_interface
                
                	Satellite Access Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: ntp_node
                
                	NTP Clock Node
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.SelectedSource, self).__init__()

                    self.yang_name = "selected-source"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Interfaces.Interface.SelectedSource.ClockId)}
                    self._child_list_classes = {}

                    self.source_class = YLeaf(YType.enumeration, "source-class")

                    self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                    self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                    self.node = YLeaf(YType.str, "node")

                    self.ptp_node = YLeaf(YType.str, "ptp-node")

                    self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                    self.ntp_node = YLeaf(YType.str, "ntp-node")

                    self.clock_id = FrequencySynchronization.Interfaces.Interface.SelectedSource.ClockId()
                    self.clock_id.parent = self
                    self._children_name_map["clock_id"] = "clock-id"
                    self._children_yang_names.add("clock-id")
                    self._segment_path = lambda: "selected-source"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                class ClockId(Entity):
                    """
                    Clock ID
                    
                    .. attribute:: node
                    
                    	Node
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: port
                    
                    	Port number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Interfaces.Interface.SelectedSource.ClockId, self).__init__()

                        self.yang_name = "clock-id"
                        self.yang_parent_name = "selected-source"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.node = YLeaf(YType.str, "node")

                        self.port = YLeaf(YType.uint32, "port")
                        self._segment_path = lambda: "clock-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Interfaces.Interface.SelectedSource.ClockId, ['node', 'port'], name, value)


            class QualityLevelReceived(Entity):
                """
                Received quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.QualityLevelReceived, self).__init__()

                    self.yang_name = "quality-level-received"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                    self.option1_value = YLeaf(YType.enumeration, "option1-value")

                    self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                    self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                    self._segment_path = lambda: "quality-level-received"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.QualityLevelReceived, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class QualityLevelDamped(Entity):
                """
                Quality level after damping has been applied
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.QualityLevelDamped, self).__init__()

                    self.yang_name = "quality-level-damped"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                    self.option1_value = YLeaf(YType.enumeration, "option1-value")

                    self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                    self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                    self._segment_path = lambda: "quality-level-damped"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.QualityLevelDamped, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class QualityLevelEffectiveInput(Entity):
                """
                The effective input quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveInput, self).__init__()

                    self.yang_name = "quality-level-effective-input"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                    self.option1_value = YLeaf(YType.enumeration, "option1-value")

                    self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                    self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                    self._segment_path = lambda: "quality-level-effective-input"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class QualityLevelEffectiveOutput(Entity):
                """
                The effective output quality level
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveOutput, self).__init__()

                    self.yang_name = "quality-level-effective-output"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                    self.option1_value = YLeaf(YType.enumeration, "option1-value")

                    self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                    self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                    self._segment_path = lambda: "quality-level-effective-output"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.QualityLevelEffectiveOutput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class QualityLevelSelectedSource(Entity):
                """
                The quality level of the source driving this
                interface
                
                .. attribute:: quality_level_option
                
                	QualityLevelOption
                	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                
                .. attribute:: option1_value
                
                	ITU\-T Option 1 QL value
                	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                
                .. attribute:: option2_generation1_value
                
                	ITU\-T Option 2, generation 1 value
                	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                
                .. attribute:: option2_generation2_value
                
                	ITU\-T Option 2, generation 2 value
                	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.QualityLevelSelectedSource, self).__init__()

                    self.yang_name = "quality-level-selected-source"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                    self.option1_value = YLeaf(YType.enumeration, "option1-value")

                    self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                    self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                    self._segment_path = lambda: "quality-level-selected-source"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.QualityLevelSelectedSource, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class EthernetPeerInformation(Entity):
                """
                Ethernet peer information
                
                .. attribute:: peer_state_time
                
                	Time of last peer state transition
                	**type**\:  :py:class:`PeerStateTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.PeerStateTime>`
                
                .. attribute:: last_ssm
                
                	Time of last SSM received
                	**type**\:  :py:class:`LastSsm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.LastSsm>`
                
                .. attribute:: peer_state
                
                	Peer state
                	**type**\:  :py:class:`FsyncBagEsmcPeerState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagEsmcPeerState>`
                
                .. attribute:: peer_up_count
                
                	Number of times the peer has come up
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: peer_timeout_count
                
                	Number of times the peer has timed out
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation, self).__init__()

                    self.yang_name = "ethernet-peer-information"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"peer-state-time" : ("peer_state_time", FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.PeerStateTime), "last-ssm" : ("last_ssm", FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.LastSsm)}
                    self._child_list_classes = {}

                    self.peer_state = YLeaf(YType.enumeration, "peer-state")

                    self.peer_up_count = YLeaf(YType.uint16, "peer-up-count")

                    self.peer_timeout_count = YLeaf(YType.uint16, "peer-timeout-count")

                    self.peer_state_time = FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.PeerStateTime()
                    self.peer_state_time.parent = self
                    self._children_name_map["peer_state_time"] = "peer-state-time"
                    self._children_yang_names.add("peer-state-time")

                    self.last_ssm = FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.LastSsm()
                    self.last_ssm.parent = self
                    self._children_name_map["last_ssm"] = "last-ssm"
                    self._children_yang_names.add("last-ssm")
                    self._segment_path = lambda: "ethernet-peer-information"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation, ['peer_state', 'peer_up_count', 'peer_timeout_count'], name, value)


                class PeerStateTime(Entity):
                    """
                    Time of last peer state transition
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.PeerStateTime, self).__init__()

                        self.yang_name = "peer-state-time"
                        self.yang_parent_name = "ethernet-peer-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "peer-state-time"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.PeerStateTime, ['seconds', 'nanoseconds'], name, value)


                class LastSsm(Entity):
                    """
                    Time of last SSM received
                    
                    .. attribute:: seconds
                    
                    	Seconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: nanoseconds
                    
                    	Nanoseconds
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: nanosecond
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.LastSsm, self).__init__()

                        self.yang_name = "last-ssm"
                        self.yang_parent_name = "ethernet-peer-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.seconds = YLeaf(YType.uint32, "seconds")

                        self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                        self._segment_path = lambda: "last-ssm"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Interfaces.Interface.EthernetPeerInformation.LastSsm, ['seconds', 'nanoseconds'], name, value)


            class EsmcStatistics(Entity):
                """
                ESMC Statistics
                
                .. attribute:: esmc_events_sent
                
                	Number of event SSMs sent
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: esmc_events_received
                
                	Number of event SSMs received
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: esmc_infos_sent
                
                	Number of info SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_infos_received
                
                	Number of info SSms received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_dn_us_sent
                
                	Number of SSMs with DNU QL sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_dn_us_received
                
                	Number of SSMs with DNU QL received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esmc_malformed_received
                
                	Number of malformed packets received
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: esmc_received_error
                
                	Number of received packets that failed to be handled
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Interfaces.Interface.EsmcStatistics, self).__init__()

                    self.yang_name = "esmc-statistics"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.esmc_events_sent = YLeaf(YType.uint16, "esmc-events-sent")

                    self.esmc_events_received = YLeaf(YType.uint16, "esmc-events-received")

                    self.esmc_infos_sent = YLeaf(YType.uint32, "esmc-infos-sent")

                    self.esmc_infos_received = YLeaf(YType.uint32, "esmc-infos-received")

                    self.esmc_dn_us_sent = YLeaf(YType.uint32, "esmc-dn-us-sent")

                    self.esmc_dn_us_received = YLeaf(YType.uint32, "esmc-dn-us-received")

                    self.esmc_malformed_received = YLeaf(YType.uint16, "esmc-malformed-received")

                    self.esmc_received_error = YLeaf(YType.uint16, "esmc-received-error")
                    self._segment_path = lambda: "esmc-statistics"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Interfaces.Interface.EsmcStatistics, ['esmc_events_sent', 'esmc_events_received', 'esmc_infos_sent', 'esmc_infos_received', 'esmc_dn_us_sent', 'esmc_dn_us_received', 'esmc_malformed_received', 'esmc_received_error'], name, value)


    class Nodes(Entity):
        """
        Table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node>`
        
        

        """

        _prefix = 'freqsync-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(FrequencySynchronization.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "frequency-synchronization"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", FrequencySynchronization.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FrequencySynchronization.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  <key>
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: ntp
            
            	NTP operational data
            	**type**\:  :py:class:`Ntp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Ntp>`
            
            .. attribute:: clocks
            
            	Table for clock operational data
            	**type**\:  :py:class:`Clocks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks>`
            
            .. attribute:: configuration_errors
            
            	Configuration error operational data
            	**type**\:  :py:class:`ConfigurationErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors>`
            
            .. attribute:: ptp
            
            	PTP operational data
            	**type**\:  :py:class:`Ptp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Ptp>`
            
            .. attribute:: ssm_summary
            
            	SSM operational data
            	**type**\:  :py:class:`SsmSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SsmSummary>`
            
            .. attribute:: selection_points
            
            	Selection point table
            	**type**\:  :py:class:`SelectionPoints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPoints>`
            
            .. attribute:: selection_point_inputs
            
            	Table for selection point input operational data
            	**type**\:  :py:class:`SelectionPointInputs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs>`
            
            

            """

            _prefix = 'freqsync-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(FrequencySynchronization.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ntp" : ("ntp", FrequencySynchronization.Nodes.Node.Ntp), "clocks" : ("clocks", FrequencySynchronization.Nodes.Node.Clocks), "configuration-errors" : ("configuration_errors", FrequencySynchronization.Nodes.Node.ConfigurationErrors), "ptp" : ("ptp", FrequencySynchronization.Nodes.Node.Ptp), "ssm-summary" : ("ssm_summary", FrequencySynchronization.Nodes.Node.SsmSummary), "selection-points" : ("selection_points", FrequencySynchronization.Nodes.Node.SelectionPoints), "selection-point-inputs" : ("selection_point_inputs", FrequencySynchronization.Nodes.Node.SelectionPointInputs)}
                self._child_list_classes = {}

                self.node = YLeaf(YType.str, "node")

                self.ntp = FrequencySynchronization.Nodes.Node.Ntp()
                self.ntp.parent = self
                self._children_name_map["ntp"] = "ntp"
                self._children_yang_names.add("ntp")

                self.clocks = FrequencySynchronization.Nodes.Node.Clocks()
                self.clocks.parent = self
                self._children_name_map["clocks"] = "clocks"
                self._children_yang_names.add("clocks")

                self.configuration_errors = FrequencySynchronization.Nodes.Node.ConfigurationErrors()
                self.configuration_errors.parent = self
                self._children_name_map["configuration_errors"] = "configuration-errors"
                self._children_yang_names.add("configuration-errors")

                self.ptp = FrequencySynchronization.Nodes.Node.Ptp()
                self.ptp.parent = self
                self._children_name_map["ptp"] = "ptp"
                self._children_yang_names.add("ptp")

                self.ssm_summary = FrequencySynchronization.Nodes.Node.SsmSummary()
                self.ssm_summary.parent = self
                self._children_name_map["ssm_summary"] = "ssm-summary"
                self._children_yang_names.add("ssm-summary")

                self.selection_points = FrequencySynchronization.Nodes.Node.SelectionPoints()
                self.selection_points.parent = self
                self._children_name_map["selection_points"] = "selection-points"
                self._children_yang_names.add("selection-points")

                self.selection_point_inputs = FrequencySynchronization.Nodes.Node.SelectionPointInputs()
                self.selection_point_inputs.parent = self
                self._children_name_map["selection_point_inputs"] = "selection-point-inputs"
                self._children_yang_names.add("selection-point-inputs")
                self._segment_path = lambda: "node" + "[node='" + self.node.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-freqsync-oper:frequency-synchronization/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(FrequencySynchronization.Nodes.Node, ['node'], name, value)


            class Ntp(Entity):
                """
                NTP operational data
                
                .. attribute:: quality_level_effective_input
                
                	The effective input quality level
                	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Ntp.QualityLevelEffectiveInput>`
                
                .. attribute:: state
                
                	NTP state
                	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                
                .. attribute:: supports_frequency
                
                	The NTP clock supports frequency
                	**type**\: bool
                
                .. attribute:: supports_time_of_day
                
                	The NTP clock supports time
                	**type**\: bool
                
                .. attribute:: frequency_priority
                
                	The priority of the NTP clock when selected between frequency sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: time_of_day_priority
                
                	The priority of the NTP clock when selecting between time\-of\-day sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: spa_selection_point
                
                	Spa selection points
                	**type**\: list of int
                
                	**range:** 0..255
                
                .. attribute:: spa_selection_points_description
                
                	Spa selection points descrption
                	**type**\: list of str
                
                .. attribute:: node_selection_point
                
                	Node selection points
                	**type**\: list of int
                
                	**range:** 0..255
                
                .. attribute:: node_selection_points_description
                
                	Node selection points descrption
                	**type**\: list of str
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.Ntp, self).__init__()

                    self.yang_name = "ntp"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"quality-level-effective-input" : ("quality_level_effective_input", FrequencySynchronization.Nodes.Node.Ntp.QualityLevelEffectiveInput)}
                    self._child_list_classes = {}

                    self.state = YLeaf(YType.enumeration, "state")

                    self.supports_frequency = YLeaf(YType.boolean, "supports-frequency")

                    self.supports_time_of_day = YLeaf(YType.boolean, "supports-time-of-day")

                    self.frequency_priority = YLeaf(YType.uint8, "frequency-priority")

                    self.time_of_day_priority = YLeaf(YType.uint8, "time-of-day-priority")

                    self.spa_selection_point = YLeafList(YType.uint8, "spa-selection-point")

                    self.spa_selection_points_description = YLeafList(YType.str, "spa-selection-points-description")

                    self.node_selection_point = YLeafList(YType.uint8, "node-selection-point")

                    self.node_selection_points_description = YLeafList(YType.str, "node-selection-points-description")

                    self.quality_level_effective_input = FrequencySynchronization.Nodes.Node.Ntp.QualityLevelEffectiveInput()
                    self.quality_level_effective_input.parent = self
                    self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"
                    self._children_yang_names.add("quality-level-effective-input")
                    self._segment_path = lambda: "ntp"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.Ntp, ['state', 'supports_frequency', 'supports_time_of_day', 'frequency_priority', 'time_of_day_priority', 'spa_selection_point', 'spa_selection_points_description', 'node_selection_point', 'node_selection_points_description'], name, value)


                class QualityLevelEffectiveInput(Entity):
                    """
                    The effective input quality level
                    
                    .. attribute:: quality_level_option
                    
                    	QualityLevelOption
                    	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                    
                    .. attribute:: option1_value
                    
                    	ITU\-T Option 1 QL value
                    	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                    
                    .. attribute:: option2_generation1_value
                    
                    	ITU\-T Option 2, generation 1 value
                    	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                    
                    .. attribute:: option2_generation2_value
                    
                    	ITU\-T Option 2, generation 2 value
                    	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.Ntp.QualityLevelEffectiveInput, self).__init__()

                        self.yang_name = "quality-level-effective-input"
                        self.yang_parent_name = "ntp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                        self.option1_value = YLeaf(YType.enumeration, "option1-value")

                        self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                        self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                        self._segment_path = lambda: "quality-level-effective-input"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.Ntp.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class Clocks(Entity):
                """
                Table for clock operational data
                
                .. attribute:: clock
                
                	Operational data for a particular clock
                	**type**\: list of  		 :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.Clocks, self).__init__()

                    self.yang_name = "clocks"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"clock" : ("clock", FrequencySynchronization.Nodes.Node.Clocks.Clock)}

                    self.clock = YList(self)
                    self._segment_path = lambda: "clocks"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks, [], name, value)


                class Clock(Entity):
                    """
                    Operational data for a particular clock
                    
                    .. attribute:: clock_type  <key>
                    
                    	Clock type
                    	**type**\:  :py:class:`FsyncClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_datatypes.FsyncClock>`
                    
                    .. attribute:: port  <key>
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: source
                    
                    	The source ID for the clock
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.Source>`
                    
                    .. attribute:: selected_source
                    
                    	Timing source selected for clock output
                    	**type**\:  :py:class:`SelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource>`
                    
                    .. attribute:: quality_level_received
                    
                    	Received quality level
                    	**type**\:  :py:class:`QualityLevelReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelReceived>`
                    
                    .. attribute:: quality_level_damped
                    
                    	Quality level after damping has been applied
                    	**type**\:  :py:class:`QualityLevelDamped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelDamped>`
                    
                    .. attribute:: quality_level_effective_input
                    
                    	The effective input quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveInput>`
                    
                    .. attribute:: quality_level_effective_output
                    
                    	The effective output quality level
                    	**type**\:  :py:class:`QualityLevelEffectiveOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveOutput>`
                    
                    .. attribute:: quality_level_selected_source
                    
                    	The quality level of the source driving this interface
                    	**type**\:  :py:class:`QualityLevelSelectedSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelSelectedSource>`
                    
                    .. attribute:: state
                    
                    	Clock state
                    	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                    
                    .. attribute:: down_reason
                    
                    	Why the clock is down
                    	**type**\: str
                    
                    .. attribute:: description
                    
                    	Clock description
                    	**type**\: str
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: ssm_support
                    
                    	The clock supports SSMs
                    	**type**\: bool
                    
                    .. attribute:: ssm_enabled
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    .. attribute:: loopback
                    
                    	The clock is looped back
                    	**type**\: bool
                    
                    .. attribute:: selection_input
                    
                    	The clock is an input for selection
                    	**type**\: bool
                    
                    .. attribute:: squelched
                    
                    	The clock output is squelched
                    	**type**\: bool
                    
                    .. attribute:: damping_state
                    
                    	Damping state
                    	**type**\:  :py:class:`FsyncBagDampingState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagDampingState>`
                    
                    .. attribute:: damping_time
                    
                    	Time until damping state changes in ms
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_disabled
                    
                    	Timing input is disabled
                    	**type**\: bool
                    
                    .. attribute:: output_disabled
                    
                    	Timing output is disabled
                    	**type**\: bool
                    
                    .. attribute:: wait_to_restore_time
                    
                    	Wait\-to\-restore time for the clock
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: clock_type_xr
                    
                    	The type of clock
                    	**type**\:  :py:class:`FsyncBagClockIntfClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagClockIntfClass>`
                    
                    .. attribute:: supports_frequency
                    
                    	The PTP clock supports frequency
                    	**type**\: bool
                    
                    .. attribute:: supports_time_of_day
                    
                    	The PTP clock supports time
                    	**type**\: bool
                    
                    .. attribute:: spa_selection_point
                    
                    	Spa selection points
                    	**type**\: list of int
                    
                    	**range:** 0..255
                    
                    .. attribute:: spa_selection_points_description
                    
                    	Spa selection points descrption
                    	**type**\: list of str
                    
                    .. attribute:: node_selection_point
                    
                    	Node selection points
                    	**type**\: list of int
                    
                    	**range:** 0..255
                    
                    .. attribute:: node_selection_points_description
                    
                    	Node selection points descrption
                    	**type**\: list of str
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.Clocks.Clock, self).__init__()

                        self.yang_name = "clock"
                        self.yang_parent_name = "clocks"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"source" : ("source", FrequencySynchronization.Nodes.Node.Clocks.Clock.Source), "selected-source" : ("selected_source", FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource), "quality-level-received" : ("quality_level_received", FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelReceived), "quality-level-damped" : ("quality_level_damped", FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelDamped), "quality-level-effective-input" : ("quality_level_effective_input", FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveInput), "quality-level-effective-output" : ("quality_level_effective_output", FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveOutput), "quality-level-selected-source" : ("quality_level_selected_source", FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelSelectedSource)}
                        self._child_list_classes = {}

                        self.clock_type = YLeaf(YType.enumeration, "clock-type")

                        self.port = YLeaf(YType.int32, "port")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.down_reason = YLeaf(YType.str, "down-reason")

                        self.description = YLeaf(YType.str, "description")

                        self.priority = YLeaf(YType.uint8, "priority")

                        self.time_of_day_priority = YLeaf(YType.uint8, "time-of-day-priority")

                        self.ssm_support = YLeaf(YType.boolean, "ssm-support")

                        self.ssm_enabled = YLeaf(YType.boolean, "ssm-enabled")

                        self.loopback = YLeaf(YType.boolean, "loopback")

                        self.selection_input = YLeaf(YType.boolean, "selection-input")

                        self.squelched = YLeaf(YType.boolean, "squelched")

                        self.damping_state = YLeaf(YType.enumeration, "damping-state")

                        self.damping_time = YLeaf(YType.uint32, "damping-time")

                        self.input_disabled = YLeaf(YType.boolean, "input-disabled")

                        self.output_disabled = YLeaf(YType.boolean, "output-disabled")

                        self.wait_to_restore_time = YLeaf(YType.uint16, "wait-to-restore-time")

                        self.clock_type_xr = YLeaf(YType.enumeration, "clock-type-xr")

                        self.supports_frequency = YLeaf(YType.boolean, "supports-frequency")

                        self.supports_time_of_day = YLeaf(YType.boolean, "supports-time-of-day")

                        self.spa_selection_point = YLeafList(YType.uint8, "spa-selection-point")

                        self.spa_selection_points_description = YLeafList(YType.str, "spa-selection-points-description")

                        self.node_selection_point = YLeafList(YType.uint8, "node-selection-point")

                        self.node_selection_points_description = YLeafList(YType.str, "node-selection-points-description")

                        self.source = FrequencySynchronization.Nodes.Node.Clocks.Clock.Source()
                        self.source.parent = self
                        self._children_name_map["source"] = "source"
                        self._children_yang_names.add("source")

                        self.selected_source = FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource()
                        self.selected_source.parent = self
                        self._children_name_map["selected_source"] = "selected-source"
                        self._children_yang_names.add("selected-source")

                        self.quality_level_received = FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelReceived()
                        self.quality_level_received.parent = self
                        self._children_name_map["quality_level_received"] = "quality-level-received"
                        self._children_yang_names.add("quality-level-received")

                        self.quality_level_damped = FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelDamped()
                        self.quality_level_damped.parent = self
                        self._children_name_map["quality_level_damped"] = "quality-level-damped"
                        self._children_yang_names.add("quality-level-damped")

                        self.quality_level_effective_input = FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveInput()
                        self.quality_level_effective_input.parent = self
                        self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"
                        self._children_yang_names.add("quality-level-effective-input")

                        self.quality_level_effective_output = FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveOutput()
                        self.quality_level_effective_output.parent = self
                        self._children_name_map["quality_level_effective_output"] = "quality-level-effective-output"
                        self._children_yang_names.add("quality-level-effective-output")

                        self.quality_level_selected_source = FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelSelectedSource()
                        self.quality_level_selected_source.parent = self
                        self._children_name_map["quality_level_selected_source"] = "quality-level-selected-source"
                        self._children_yang_names.add("quality-level-selected-source")
                        self._segment_path = lambda: "clock" + "[clock-type='" + self.clock_type.get() + "']" + "[port='" + self.port.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock, ['clock_type', 'port', 'state', 'down_reason', 'description', 'priority', 'time_of_day_priority', 'ssm_support', 'ssm_enabled', 'loopback', 'selection_input', 'squelched', 'damping_state', 'damping_time', 'input_disabled', 'output_disabled', 'wait_to_restore_time', 'clock_type_xr', 'supports_frequency', 'supports_time_of_day', 'spa_selection_point', 'spa_selection_points_description', 'node_selection_point', 'node_selection_points_description'], name, value)


                    class Source(Entity):
                        """
                        The source ID for the clock
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.Source.ClockId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.Clocks.Clock.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Nodes.Node.Clocks.Clock.Source.ClockId)}
                            self._child_list_classes = {}

                            self.source_class = YLeaf(YType.enumeration, "source-class")

                            self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                            self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                            self.node = YLeaf(YType.str, "node")

                            self.ptp_node = YLeaf(YType.str, "ptp-node")

                            self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                            self.ntp_node = YLeaf(YType.str, "ntp-node")

                            self.clock_id = FrequencySynchronization.Nodes.Node.Clocks.Clock.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"
                            self._children_yang_names.add("clock-id")
                            self._segment_path = lambda: "source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: port
                            
                            	Port number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.Clocks.Clock.Source.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.node = YLeaf(YType.str, "node")

                                self.port = YLeaf(YType.uint32, "port")
                                self._segment_path = lambda: "clock-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.Source.ClockId, ['node', 'port'], name, value)


                    class SelectedSource(Entity):
                        """
                        Timing source selected for clock output
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource.ClockId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource, self).__init__()

                            self.yang_name = "selected-source"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource.ClockId)}
                            self._child_list_classes = {}

                            self.source_class = YLeaf(YType.enumeration, "source-class")

                            self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                            self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                            self.node = YLeaf(YType.str, "node")

                            self.ptp_node = YLeaf(YType.str, "ptp-node")

                            self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                            self.ntp_node = YLeaf(YType.str, "ntp-node")

                            self.clock_id = FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"
                            self._children_yang_names.add("clock-id")
                            self._segment_path = lambda: "selected-source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: port
                            
                            	Port number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "selected-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.node = YLeaf(YType.str, "node")

                                self.port = YLeaf(YType.uint32, "port")
                                self._segment_path = lambda: "clock-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.SelectedSource.ClockId, ['node', 'port'], name, value)


                    class QualityLevelReceived(Entity):
                        """
                        Received quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelReceived, self).__init__()

                            self.yang_name = "quality-level-received"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "quality-level-received"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelReceived, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class QualityLevelDamped(Entity):
                        """
                        Quality level after damping has been applied
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelDamped, self).__init__()

                            self.yang_name = "quality-level-damped"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "quality-level-damped"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelDamped, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class QualityLevelEffectiveInput(Entity):
                        """
                        The effective input quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveInput, self).__init__()

                            self.yang_name = "quality-level-effective-input"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "quality-level-effective-input"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class QualityLevelEffectiveOutput(Entity):
                        """
                        The effective output quality level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveOutput, self).__init__()

                            self.yang_name = "quality-level-effective-output"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "quality-level-effective-output"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelEffectiveOutput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class QualityLevelSelectedSource(Entity):
                        """
                        The quality level of the source driving this
                        interface
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelSelectedSource, self).__init__()

                            self.yang_name = "quality-level-selected-source"
                            self.yang_parent_name = "clock"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "quality-level-selected-source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.Clocks.Clock.QualityLevelSelectedSource, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class ConfigurationErrors(Entity):
                """
                Configuration error operational data
                
                .. attribute:: error_source
                
                	Configuration errors
                	**type**\: list of  		 :py:class:`ErrorSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.ConfigurationErrors, self).__init__()

                    self.yang_name = "configuration-errors"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"error-source" : ("error_source", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource)}

                    self.error_source = YList(self)
                    self._segment_path = lambda: "configuration-errors"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors, [], name, value)


                class ErrorSource(Entity):
                    """
                    Configuration errors
                    
                    .. attribute:: source
                    
                    	Source
                    	**type**\:  :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source>`
                    
                    .. attribute:: input_min_ql
                    
                    	Configured minimum input QL
                    	**type**\:  :py:class:`InputMinQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl>`
                    
                    .. attribute:: input_exact_ql
                    
                    	Configured exact input QL
                    	**type**\:  :py:class:`InputExactQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl>`
                    
                    .. attribute:: input_max_ql
                    
                    	Configured maximum input QL
                    	**type**\:  :py:class:`InputMaxQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl>`
                    
                    .. attribute:: output_min_ql
                    
                    	Configured mininum output QL
                    	**type**\:  :py:class:`OutputMinQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl>`
                    
                    .. attribute:: output_exact_ql
                    
                    	Configured exact output QL
                    	**type**\:  :py:class:`OutputExactQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl>`
                    
                    .. attribute:: output_max_ql
                    
                    	Configured exact maximum QL
                    	**type**\:  :py:class:`OutputMaxQl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl>`
                    
                    .. attribute:: enable_error
                    
                    	Frequency Synchronization enable error
                    	**type**\: bool
                    
                    .. attribute:: input_min_error
                    
                    	Minimum input QL config error
                    	**type**\: bool
                    
                    .. attribute:: input_exact_error
                    
                    	Exact input QL config error
                    	**type**\: bool
                    
                    .. attribute:: input_max_error
                    
                    	Maximum input Ql config error
                    	**type**\: bool
                    
                    .. attribute:: ouput_min_error
                    
                    	Minimum output QL config error
                    	**type**\: bool
                    
                    .. attribute:: output_exact_error
                    
                    	Exact output QL config error
                    	**type**\: bool
                    
                    .. attribute:: output_max_error
                    
                    	Maximum output QL config error
                    	**type**\: bool
                    
                    .. attribute:: input_output_mismatch
                    
                    	Input/Output mismatch error
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource, self).__init__()

                        self.yang_name = "error-source"
                        self.yang_parent_name = "configuration-errors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"source" : ("source", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source), "input-min-ql" : ("input_min_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl), "input-exact-ql" : ("input_exact_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl), "input-max-ql" : ("input_max_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl), "output-min-ql" : ("output_min_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl), "output-exact-ql" : ("output_exact_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl), "output-max-ql" : ("output_max_ql", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl)}
                        self._child_list_classes = {}

                        self.enable_error = YLeaf(YType.boolean, "enable-error")

                        self.input_min_error = YLeaf(YType.boolean, "input-min-error")

                        self.input_exact_error = YLeaf(YType.boolean, "input-exact-error")

                        self.input_max_error = YLeaf(YType.boolean, "input-max-error")

                        self.ouput_min_error = YLeaf(YType.boolean, "ouput-min-error")

                        self.output_exact_error = YLeaf(YType.boolean, "output-exact-error")

                        self.output_max_error = YLeaf(YType.boolean, "output-max-error")

                        self.input_output_mismatch = YLeaf(YType.boolean, "input-output-mismatch")

                        self.source = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source()
                        self.source.parent = self
                        self._children_name_map["source"] = "source"
                        self._children_yang_names.add("source")

                        self.input_min_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl()
                        self.input_min_ql.parent = self
                        self._children_name_map["input_min_ql"] = "input-min-ql"
                        self._children_yang_names.add("input-min-ql")

                        self.input_exact_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl()
                        self.input_exact_ql.parent = self
                        self._children_name_map["input_exact_ql"] = "input-exact-ql"
                        self._children_yang_names.add("input-exact-ql")

                        self.input_max_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl()
                        self.input_max_ql.parent = self
                        self._children_name_map["input_max_ql"] = "input-max-ql"
                        self._children_yang_names.add("input-max-ql")

                        self.output_min_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl()
                        self.output_min_ql.parent = self
                        self._children_name_map["output_min_ql"] = "output-min-ql"
                        self._children_yang_names.add("output-min-ql")

                        self.output_exact_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl()
                        self.output_exact_ql.parent = self
                        self._children_name_map["output_exact_ql"] = "output-exact-ql"
                        self._children_yang_names.add("output-exact-ql")

                        self.output_max_ql = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl()
                        self.output_max_ql.parent = self
                        self._children_name_map["output_max_ql"] = "output-max-ql"
                        self._children_yang_names.add("output-max-ql")
                        self._segment_path = lambda: "error-source"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource, ['enable_error', 'input_min_error', 'input_exact_error', 'input_max_error', 'ouput_min_error', 'output_exact_error', 'output_max_error', 'input_output_mismatch'], name, value)


                    class Source(Entity):
                        """
                        Source
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source, self).__init__()

                            self.yang_name = "source"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId)}
                            self._child_list_classes = {}

                            self.source_class = YLeaf(YType.enumeration, "source-class")

                            self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                            self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                            self.node = YLeaf(YType.str, "node")

                            self.ptp_node = YLeaf(YType.str, "ptp-node")

                            self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                            self.ntp_node = YLeaf(YType.str, "ntp-node")

                            self.clock_id = FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"
                            self._children_yang_names.add("clock-id")
                            self._segment_path = lambda: "source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: port
                            
                            	Port number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.node = YLeaf(YType.str, "node")

                                self.port = YLeaf(YType.uint32, "port")
                                self._segment_path = lambda: "clock-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.Source.ClockId, ['node', 'port'], name, value)


                    class InputMinQl(Entity):
                        """
                        Configured minimum input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl, self).__init__()

                            self.yang_name = "input-min-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "input-min-ql"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMinQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class InputExactQl(Entity):
                        """
                        Configured exact input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl, self).__init__()

                            self.yang_name = "input-exact-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "input-exact-ql"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputExactQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class InputMaxQl(Entity):
                        """
                        Configured maximum input QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl, self).__init__()

                            self.yang_name = "input-max-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "input-max-ql"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.InputMaxQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class OutputMinQl(Entity):
                        """
                        Configured mininum output QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl, self).__init__()

                            self.yang_name = "output-min-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "output-min-ql"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMinQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class OutputExactQl(Entity):
                        """
                        Configured exact output QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl, self).__init__()

                            self.yang_name = "output-exact-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "output-exact-ql"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputExactQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


                    class OutputMaxQl(Entity):
                        """
                        Configured exact maximum QL
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl, self).__init__()

                            self.yang_name = "output-max-ql"
                            self.yang_parent_name = "error-source"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "output-max-ql"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.ConfigurationErrors.ErrorSource.OutputMaxQl, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class Ptp(Entity):
                """
                PTP operational data
                
                .. attribute:: quality_level_effective_input
                
                	The effective input quality level
                	**type**\:  :py:class:`QualityLevelEffectiveInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.Ptp.QualityLevelEffectiveInput>`
                
                .. attribute:: state
                
                	PTP state
                	**type**\:  :py:class:`FsyncBagSourceState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceState>`
                
                .. attribute:: supports_frequency
                
                	The PTP clock supports frequency
                	**type**\: bool
                
                .. attribute:: supports_time_of_day
                
                	The PTP clock supports time
                	**type**\: bool
                
                .. attribute:: frequency_priority
                
                	The priority of the PTP clock when selected between frequency sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: time_of_day_priority
                
                	The priority of the PTP clock when selecting between time\-of\-day sources
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: spa_selection_point
                
                	Spa selection points
                	**type**\: list of int
                
                	**range:** 0..255
                
                .. attribute:: spa_selection_points_description
                
                	Spa selection points descrption
                	**type**\: list of str
                
                .. attribute:: node_selection_point
                
                	Node selection points
                	**type**\: list of int
                
                	**range:** 0..255
                
                .. attribute:: node_selection_points_description
                
                	Node selection points descrption
                	**type**\: list of str
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.Ptp, self).__init__()

                    self.yang_name = "ptp"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"quality-level-effective-input" : ("quality_level_effective_input", FrequencySynchronization.Nodes.Node.Ptp.QualityLevelEffectiveInput)}
                    self._child_list_classes = {}

                    self.state = YLeaf(YType.enumeration, "state")

                    self.supports_frequency = YLeaf(YType.boolean, "supports-frequency")

                    self.supports_time_of_day = YLeaf(YType.boolean, "supports-time-of-day")

                    self.frequency_priority = YLeaf(YType.uint8, "frequency-priority")

                    self.time_of_day_priority = YLeaf(YType.uint8, "time-of-day-priority")

                    self.spa_selection_point = YLeafList(YType.uint8, "spa-selection-point")

                    self.spa_selection_points_description = YLeafList(YType.str, "spa-selection-points-description")

                    self.node_selection_point = YLeafList(YType.uint8, "node-selection-point")

                    self.node_selection_points_description = YLeafList(YType.str, "node-selection-points-description")

                    self.quality_level_effective_input = FrequencySynchronization.Nodes.Node.Ptp.QualityLevelEffectiveInput()
                    self.quality_level_effective_input.parent = self
                    self._children_name_map["quality_level_effective_input"] = "quality-level-effective-input"
                    self._children_yang_names.add("quality-level-effective-input")
                    self._segment_path = lambda: "ptp"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.Ptp, ['state', 'supports_frequency', 'supports_time_of_day', 'frequency_priority', 'time_of_day_priority', 'spa_selection_point', 'spa_selection_points_description', 'node_selection_point', 'node_selection_points_description'], name, value)


                class QualityLevelEffectiveInput(Entity):
                    """
                    The effective input quality level
                    
                    .. attribute:: quality_level_option
                    
                    	QualityLevelOption
                    	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                    
                    .. attribute:: option1_value
                    
                    	ITU\-T Option 1 QL value
                    	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                    
                    .. attribute:: option2_generation1_value
                    
                    	ITU\-T Option 2, generation 1 value
                    	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                    
                    .. attribute:: option2_generation2_value
                    
                    	ITU\-T Option 2, generation 2 value
                    	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.Ptp.QualityLevelEffectiveInput, self).__init__()

                        self.yang_name = "quality-level-effective-input"
                        self.yang_parent_name = "ptp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                        self.option1_value = YLeaf(YType.enumeration, "option1-value")

                        self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                        self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                        self._segment_path = lambda: "quality-level-effective-input"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.Ptp.QualityLevelEffectiveInput, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)


            class SsmSummary(Entity):
                """
                SSM operational data
                
                .. attribute:: ethernet_sources
                
                	Number of ethernet interfaces in synchronous mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_sources_select
                
                	Number of ethernet interfaces assigned for selection
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_sources_enabled
                
                	Number of ethernet interfaces with SSM enabled
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sonet_sources
                
                	Number of SONET interfaces in synchronous mode
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sonet_sources_select
                
                	Number of SONET interfaces assigned for selection
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sonet_sources_enabled
                
                	Number of SONET interfaces with SSM enabled
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: events_sent
                
                	Total event SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: events_received
                
                	Total event SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: infos_sent
                
                	Total information SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: infos_received
                
                	Total information SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dn_us_sent
                
                	Total DNU SSMs sent
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: dn_us_received
                
                	Total DNU SSMs received
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.SsmSummary, self).__init__()

                    self.yang_name = "ssm-summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ethernet_sources = YLeaf(YType.uint32, "ethernet-sources")

                    self.ethernet_sources_select = YLeaf(YType.uint32, "ethernet-sources-select")

                    self.ethernet_sources_enabled = YLeaf(YType.uint32, "ethernet-sources-enabled")

                    self.sonet_sources = YLeaf(YType.uint32, "sonet-sources")

                    self.sonet_sources_select = YLeaf(YType.uint32, "sonet-sources-select")

                    self.sonet_sources_enabled = YLeaf(YType.uint32, "sonet-sources-enabled")

                    self.events_sent = YLeaf(YType.uint32, "events-sent")

                    self.events_received = YLeaf(YType.uint32, "events-received")

                    self.infos_sent = YLeaf(YType.uint32, "infos-sent")

                    self.infos_received = YLeaf(YType.uint32, "infos-received")

                    self.dn_us_sent = YLeaf(YType.uint32, "dn-us-sent")

                    self.dn_us_received = YLeaf(YType.uint32, "dn-us-received")
                    self._segment_path = lambda: "ssm-summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SsmSummary, ['ethernet_sources', 'ethernet_sources_select', 'ethernet_sources_enabled', 'sonet_sources', 'sonet_sources_select', 'sonet_sources_enabled', 'events_sent', 'events_received', 'infos_sent', 'infos_received', 'dn_us_sent', 'dn_us_received'], name, value)


            class SelectionPoints(Entity):
                """
                Selection point table
                
                .. attribute:: selection_point
                
                	Operational data for a given selection point
                	**type**\: list of  		 :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.SelectionPoints, self).__init__()

                    self.yang_name = "selection-points"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"selection-point" : ("selection_point", FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint)}

                    self.selection_point = YList(self)
                    self._segment_path = lambda: "selection-points"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPoints, [], name, value)


                class SelectionPoint(Entity):
                    """
                    Operational data for a given selection point
                    
                    .. attribute:: selection_point  <key>
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: output
                    
                    	Information about the output of the selection point
                    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.Output>`
                    
                    .. attribute:: last_programmed
                    
                    	Time the SP was last programmed
                    	**type**\:  :py:class:`LastProgrammed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastProgrammed>`
                    
                    .. attribute:: last_selection
                    
                    	Time the last selection was made
                    	**type**\:  :py:class:`LastSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastSelection>`
                    
                    .. attribute:: selection_point_type
                    
                    	Selection Point Type
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: description
                    
                    	Description
                    	**type**\: str
                    
                    .. attribute:: inputs
                    
                    	Number of inputs
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inputs_selected
                    
                    	Number of inputs that are selected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_of_day_selection
                    
                    	The selection point is a time\-of\-day selection point
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint, self).__init__()

                        self.yang_name = "selection-point"
                        self.yang_parent_name = "selection-points"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"output" : ("output", FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.Output), "last-programmed" : ("last_programmed", FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastProgrammed), "last-selection" : ("last_selection", FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastSelection)}
                        self._child_list_classes = {}

                        self.selection_point = YLeaf(YType.int32, "selection-point")

                        self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                        self.description = YLeaf(YType.str, "description")

                        self.inputs = YLeaf(YType.uint32, "inputs")

                        self.inputs_selected = YLeaf(YType.uint32, "inputs-selected")

                        self.time_of_day_selection = YLeaf(YType.boolean, "time-of-day-selection")

                        self.output = FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.Output()
                        self.output.parent = self
                        self._children_name_map["output"] = "output"
                        self._children_yang_names.add("output")

                        self.last_programmed = FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastProgrammed()
                        self.last_programmed.parent = self
                        self._children_name_map["last_programmed"] = "last-programmed"
                        self._children_yang_names.add("last-programmed")

                        self.last_selection = FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastSelection()
                        self.last_selection.parent = self
                        self._children_name_map["last_selection"] = "last-selection"
                        self._children_yang_names.add("last-selection")
                        self._segment_path = lambda: "selection-point" + "[selection-point='" + self.selection_point.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint, ['selection_point', 'selection_point_type', 'description', 'inputs', 'inputs_selected', 'time_of_day_selection'], name, value)


                    class Output(Entity):
                        """
                        Information about the output of the selection
                        point
                        
                        .. attribute:: local_clock_ouput
                        
                        	Used for local clock output
                        	**type**\: bool
                        
                        .. attribute:: local_line_output
                        
                        	Used for local line interface output
                        	**type**\: bool
                        
                        .. attribute:: local_time_of_day_output
                        
                        	Used for local time\-of\-day output
                        	**type**\: bool
                        
                        .. attribute:: spa_selection_point
                        
                        	SPA selection points
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: spa_selection_points_description
                        
                        	SPA selection points descrption
                        	**type**\: list of str
                        
                        .. attribute:: node_selection_point
                        
                        	Node selection points
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: node_selection_points_description
                        
                        	Node selection points descrption
                        	**type**\: list of str
                        
                        .. attribute:: chassis_selection_point
                        
                        	Chassis selection points
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: chassis_selection_points_description
                        
                        	Chassis selection points descrption
                        	**type**\: list of str
                        
                        .. attribute:: router_selection_point
                        
                        	Router selection points
                        	**type**\: list of int
                        
                        	**range:** 0..255
                        
                        .. attribute:: router_selection_points_description
                        
                        	Router selection points descrption
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.Output, self).__init__()

                            self.yang_name = "output"
                            self.yang_parent_name = "selection-point"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.local_clock_ouput = YLeaf(YType.boolean, "local-clock-ouput")

                            self.local_line_output = YLeaf(YType.boolean, "local-line-output")

                            self.local_time_of_day_output = YLeaf(YType.boolean, "local-time-of-day-output")

                            self.spa_selection_point = YLeafList(YType.uint8, "spa-selection-point")

                            self.spa_selection_points_description = YLeafList(YType.str, "spa-selection-points-description")

                            self.node_selection_point = YLeafList(YType.uint8, "node-selection-point")

                            self.node_selection_points_description = YLeafList(YType.str, "node-selection-points-description")

                            self.chassis_selection_point = YLeafList(YType.uint8, "chassis-selection-point")

                            self.chassis_selection_points_description = YLeafList(YType.str, "chassis-selection-points-description")

                            self.router_selection_point = YLeafList(YType.uint8, "router-selection-point")

                            self.router_selection_points_description = YLeafList(YType.str, "router-selection-points-description")
                            self._segment_path = lambda: "output"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.Output, ['local_clock_ouput', 'local_line_output', 'local_time_of_day_output', 'spa_selection_point', 'spa_selection_points_description', 'node_selection_point', 'node_selection_points_description', 'chassis_selection_point', 'chassis_selection_points_description', 'router_selection_point', 'router_selection_points_description'], name, value)


                    class LastProgrammed(Entity):
                        """
                        Time the SP was last programmed
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastProgrammed, self).__init__()

                            self.yang_name = "last-programmed"
                            self.yang_parent_name = "selection-point"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.seconds = YLeaf(YType.uint32, "seconds")

                            self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                            self._segment_path = lambda: "last-programmed"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastProgrammed, ['seconds', 'nanoseconds'], name, value)


                    class LastSelection(Entity):
                        """
                        Time the last selection was made
                        
                        .. attribute:: seconds
                        
                        	Seconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nanoseconds
                        
                        	Nanoseconds
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: nanosecond
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastSelection, self).__init__()

                            self.yang_name = "last-selection"
                            self.yang_parent_name = "selection-point"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.seconds = YLeaf(YType.uint32, "seconds")

                            self.nanoseconds = YLeaf(YType.uint32, "nanoseconds")
                            self._segment_path = lambda: "last-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPoints.SelectionPoint.LastSelection, ['seconds', 'nanoseconds'], name, value)


            class SelectionPointInputs(Entity):
                """
                Table for selection point input operational
                data
                
                .. attribute:: selection_point_input
                
                	Operational data for a particular selection point input
                	**type**\: list of  		 :py:class:`SelectionPointInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput>`
                
                

                """

                _prefix = 'freqsync-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs, self).__init__()

                    self.yang_name = "selection-point-inputs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"selection-point-input" : ("selection_point_input", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput)}

                    self.selection_point_input = YList(self)
                    self._segment_path = lambda: "selection-point-inputs"

                def __setattr__(self, name, value):
                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs, [], name, value)


                class SelectionPointInput(Entity):
                    """
                    Operational data for a particular selection
                    point input
                    
                    .. attribute:: selection_point
                    
                    	Selection point ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: stream_type
                    
                    	Type of stream
                    	**type**\:  :py:class:`FsyncStream <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncStream>`
                    
                    .. attribute:: source_type
                    
                    	Type of source
                    	**type**\:  :py:class:`FsyncSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncSource>`
                    
                    .. attribute:: interface
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: clock_port
                    
                    	Clock port
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: last_node
                    
                    	Last node for a selection point stream
                    	**type**\: str
                    
                    	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                    
                    .. attribute:: last_selection_point
                    
                    	Last selection point for a selection point stream
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: output_id
                    
                    	Output ID for a selection point stream
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: input_selection_point
                    
                    	The selection point the input is for
                    	**type**\:  :py:class:`InputSelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint>`
                    
                    .. attribute:: stream
                    
                    	Stream
                    	**type**\:  :py:class:`Stream <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream>`
                    
                    .. attribute:: original_source
                    
                    	Original source
                    	**type**\:  :py:class:`OriginalSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource>`
                    
                    .. attribute:: quality_level
                    
                    	Quality Level
                    	**type**\:  :py:class:`QualityLevel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel>`
                    
                    .. attribute:: supports_frequency
                    
                    	The selection point input supports frequency
                    	**type**\: bool
                    
                    .. attribute:: supports_time_of_day
                    
                    	The selection point input supports time\-of\-day
                    	**type**\: bool
                    
                    .. attribute:: priority
                    
                    	Priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: time_of_day_priority
                    
                    	Time\-of\-day priority
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: selected
                    
                    	The selection point input is selected
                    	**type**\: bool
                    
                    .. attribute:: output_id_xr
                    
                    	Platform output ID, if the input is selected
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: platform_status
                    
                    	Platform status
                    	**type**\:  :py:class:`FsyncBagStreamState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagStreamState>`
                    
                    .. attribute:: platform_failed_reason
                    
                    	Why the stream has failed
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'freqsync-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput, self).__init__()

                        self.yang_name = "selection-point-input"
                        self.yang_parent_name = "selection-point-inputs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"input-selection-point" : ("input_selection_point", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint), "stream" : ("stream", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream), "original-source" : ("original_source", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource), "quality-level" : ("quality_level", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel)}
                        self._child_list_classes = {}

                        self.selection_point = YLeaf(YType.int32, "selection-point")

                        self.stream_type = YLeaf(YType.enumeration, "stream-type")

                        self.source_type = YLeaf(YType.enumeration, "source-type")

                        self.interface = YLeaf(YType.str, "interface")

                        self.clock_port = YLeaf(YType.int32, "clock-port")

                        self.last_node = YLeaf(YType.str, "last-node")

                        self.last_selection_point = YLeaf(YType.int32, "last-selection-point")

                        self.output_id = YLeaf(YType.int32, "output-id")

                        self.supports_frequency = YLeaf(YType.boolean, "supports-frequency")

                        self.supports_time_of_day = YLeaf(YType.boolean, "supports-time-of-day")

                        self.priority = YLeaf(YType.uint8, "priority")

                        self.time_of_day_priority = YLeaf(YType.uint8, "time-of-day-priority")

                        self.selected = YLeaf(YType.boolean, "selected")

                        self.output_id_xr = YLeaf(YType.uint8, "output-id-xr")

                        self.platform_status = YLeaf(YType.enumeration, "platform-status")

                        self.platform_failed_reason = YLeaf(YType.str, "platform-failed-reason")

                        self.input_selection_point = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint()
                        self.input_selection_point.parent = self
                        self._children_name_map["input_selection_point"] = "input-selection-point"
                        self._children_yang_names.add("input-selection-point")

                        self.stream = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream()
                        self.stream.parent = self
                        self._children_name_map["stream"] = "stream"
                        self._children_yang_names.add("stream")

                        self.original_source = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource()
                        self.original_source.parent = self
                        self._children_name_map["original_source"] = "original-source"
                        self._children_yang_names.add("original-source")

                        self.quality_level = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel()
                        self.quality_level.parent = self
                        self._children_name_map["quality_level"] = "quality-level"
                        self._children_yang_names.add("quality-level")
                        self._segment_path = lambda: "selection-point-input"

                    def __setattr__(self, name, value):
                        self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput, ['selection_point', 'stream_type', 'source_type', 'interface', 'clock_port', 'last_node', 'last_selection_point', 'output_id', 'supports_frequency', 'supports_time_of_day', 'priority', 'time_of_day_priority', 'selected', 'output_id_xr', 'platform_status', 'platform_failed_reason'], name, value)


                    class InputSelectionPoint(Entity):
                        """
                        The selection point the input is for
                        
                        .. attribute:: selection_point_type
                        
                        	Selection point type
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: selection_point_description
                        
                        	Selection point descrption
                        	**type**\: str
                        
                        .. attribute:: node
                        
                        	Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint, self).__init__()

                            self.yang_name = "input-selection-point"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                            self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                            self.node = YLeaf(YType.str, "node")
                            self._segment_path = lambda: "input-selection-point"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.InputSelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


                    class Stream(Entity):
                        """
                        Stream
                        
                        .. attribute:: source_id
                        
                        	Source ID
                        	**type**\:  :py:class:`SourceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId>`
                        
                        .. attribute:: selection_point_id
                        
                        	Selection point ID
                        	**type**\:  :py:class:`SelectionPointId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId>`
                        
                        .. attribute:: stream_input
                        
                        	StreamInput
                        	**type**\:  :py:class:`FsyncBagStreamInput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagStreamInput>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream, self).__init__()

                            self.yang_name = "stream"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"source-id" : ("source_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId), "selection-point-id" : ("selection_point_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId)}
                            self._child_list_classes = {}

                            self.stream_input = YLeaf(YType.enumeration, "stream-input")

                            self.source_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId()
                            self.source_id.parent = self
                            self._children_name_map["source_id"] = "source-id"
                            self._children_yang_names.add("source-id")

                            self.selection_point_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId()
                            self.selection_point_id.parent = self
                            self._children_name_map["selection_point_id"] = "selection-point-id"
                            self._children_yang_names.add("selection-point-id")
                            self._segment_path = lambda: "stream"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream, ['stream_input'], name, value)


                        class SourceId(Entity):
                            """
                            Source ID
                            
                            .. attribute:: clock_id
                            
                            	Clock ID
                            	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId>`
                            
                            .. attribute:: source_class
                            
                            	SourceClass
                            	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                            
                            .. attribute:: ethernet_interface
                            
                            	Ethernet interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: sonet_interface
                            
                            	SONET interfaces
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: node
                            
                            	Internal Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: ptp_node
                            
                            	PTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: satellite_access_interface
                            
                            	Satellite Access Interface
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: ntp_node
                            
                            	NTP Clock Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId, self).__init__()

                                self.yang_name = "source-id"
                                self.yang_parent_name = "stream"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId)}
                                self._child_list_classes = {}

                                self.source_class = YLeaf(YType.enumeration, "source-class")

                                self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                                self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                                self.node = YLeaf(YType.str, "node")

                                self.ptp_node = YLeaf(YType.str, "ptp-node")

                                self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                                self.ntp_node = YLeaf(YType.str, "ntp-node")

                                self.clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId()
                                self.clock_id.parent = self
                                self._children_name_map["clock_id"] = "clock-id"
                                self._children_yang_names.add("clock-id")
                                self._segment_path = lambda: "source-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                            class ClockId(Entity):
                                """
                                Clock ID
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                .. attribute:: port
                                
                                	Port number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId, self).__init__()

                                    self.yang_name = "clock-id"
                                    self.yang_parent_name = "source-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.node = YLeaf(YType.str, "node")

                                    self.port = YLeaf(YType.uint32, "port")
                                    self._segment_path = lambda: "clock-id"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SourceId.ClockId, ['node', 'port'], name, value)


                        class SelectionPointId(Entity):
                            """
                            Selection point ID
                            
                            .. attribute:: selection_point
                            
                            	Last selection point
                            	**type**\:  :py:class:`SelectionPoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint>`
                            
                            .. attribute:: output_id
                            
                            	Output ID
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId, self).__init__()

                                self.yang_name = "selection-point-id"
                                self.yang_parent_name = "stream"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"selection-point" : ("selection_point", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint)}
                                self._child_list_classes = {}

                                self.output_id = YLeaf(YType.uint8, "output-id")

                                self.selection_point = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint()
                                self.selection_point.parent = self
                                self._children_name_map["selection_point"] = "selection-point"
                                self._children_yang_names.add("selection-point")
                                self._segment_path = lambda: "selection-point-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId, ['output_id'], name, value)


                            class SelectionPoint(Entity):
                                """
                                Last selection point
                                
                                .. attribute:: selection_point_type
                                
                                	Selection point type
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: selection_point_description
                                
                                	Selection point descrption
                                	**type**\: str
                                
                                .. attribute:: node
                                
                                	Node
                                	**type**\: str
                                
                                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                                
                                

                                """

                                _prefix = 'freqsync-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint, self).__init__()

                                    self.yang_name = "selection-point"
                                    self.yang_parent_name = "selection-point-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.selection_point_type = YLeaf(YType.uint8, "selection-point-type")

                                    self.selection_point_description = YLeaf(YType.str, "selection-point-description")

                                    self.node = YLeaf(YType.str, "node")
                                    self._segment_path = lambda: "selection-point"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.Stream.SelectionPointId.SelectionPoint, ['selection_point_type', 'selection_point_description', 'node'], name, value)


                    class OriginalSource(Entity):
                        """
                        Original source
                        
                        .. attribute:: clock_id
                        
                        	Clock ID
                        	**type**\:  :py:class:`ClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId>`
                        
                        .. attribute:: source_class
                        
                        	SourceClass
                        	**type**\:  :py:class:`FsyncBagSourceClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagSourceClass>`
                        
                        .. attribute:: ethernet_interface
                        
                        	Ethernet interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: sonet_interface
                        
                        	SONET interfaces
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: node
                        
                        	Internal Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: ptp_node
                        
                        	PTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: satellite_access_interface
                        
                        	Satellite Access Interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: ntp_node
                        
                        	NTP Clock Node
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource, self).__init__()

                            self.yang_name = "original-source"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"clock-id" : ("clock_id", FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId)}
                            self._child_list_classes = {}

                            self.source_class = YLeaf(YType.enumeration, "source-class")

                            self.ethernet_interface = YLeaf(YType.str, "ethernet-interface")

                            self.sonet_interface = YLeaf(YType.str, "sonet-interface")

                            self.node = YLeaf(YType.str, "node")

                            self.ptp_node = YLeaf(YType.str, "ptp-node")

                            self.satellite_access_interface = YLeaf(YType.str, "satellite-access-interface")

                            self.ntp_node = YLeaf(YType.str, "ntp-node")

                            self.clock_id = FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId()
                            self.clock_id.parent = self
                            self._children_name_map["clock_id"] = "clock-id"
                            self._children_yang_names.add("clock-id")
                            self._segment_path = lambda: "original-source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource, ['source_class', 'ethernet_interface', 'sonet_interface', 'node', 'ptp_node', 'satellite_access_interface', 'ntp_node'], name, value)


                        class ClockId(Entity):
                            """
                            Clock ID
                            
                            .. attribute:: node
                            
                            	Node
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: port
                            
                            	Port number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'freqsync-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId, self).__init__()

                                self.yang_name = "clock-id"
                                self.yang_parent_name = "original-source"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.node = YLeaf(YType.str, "node")

                                self.port = YLeaf(YType.uint32, "port")
                                self._segment_path = lambda: "clock-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.OriginalSource.ClockId, ['node', 'port'], name, value)


                    class QualityLevel(Entity):
                        """
                        Quality Level
                        
                        .. attribute:: quality_level_option
                        
                        	QualityLevelOption
                        	**type**\:  :py:class:`FsyncBagQlOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlOption>`
                        
                        .. attribute:: option1_value
                        
                        	ITU\-T Option 1 QL value
                        	**type**\:  :py:class:`FsyncBagQlO1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO1Value>`
                        
                        .. attribute:: option2_generation1_value
                        
                        	ITU\-T Option 2, generation 1 value
                        	**type**\:  :py:class:`FsyncBagQlO2G1Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G1Value>`
                        
                        .. attribute:: option2_generation2_value
                        
                        	ITU\-T Option 2, generation 2 value
                        	**type**\:  :py:class:`FsyncBagQlO2G2Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_freqsync_oper.FsyncBagQlO2G2Value>`
                        
                        

                        """

                        _prefix = 'freqsync-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel, self).__init__()

                            self.yang_name = "quality-level"
                            self.yang_parent_name = "selection-point-input"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.quality_level_option = YLeaf(YType.enumeration, "quality-level-option")

                            self.option1_value = YLeaf(YType.enumeration, "option1-value")

                            self.option2_generation1_value = YLeaf(YType.enumeration, "option2-generation1-value")

                            self.option2_generation2_value = YLeaf(YType.enumeration, "option2-generation2-value")
                            self._segment_path = lambda: "quality-level"

                        def __setattr__(self, name, value):
                            self._perform_setattr(FrequencySynchronization.Nodes.Node.SelectionPointInputs.SelectionPointInput.QualityLevel, ['quality_level_option', 'option1_value', 'option2_generation1_value', 'option2_generation2_value'], name, value)

    def clone_ptr(self):
        self._top_entity = FrequencySynchronization()
        return self._top_entity

