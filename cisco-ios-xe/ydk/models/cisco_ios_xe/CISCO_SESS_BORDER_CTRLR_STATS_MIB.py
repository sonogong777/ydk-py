""" CISCO_SESS_BORDER_CTRLR_STATS_MIB 

The main purpose of this MIB is to define the statistics
information for Session Border Controller application. This MIB
categorizes the statistics information into following types\:
1. RADIUS Messages Statistics \- Represents statistics of
   various RADIUS messages for RADIUS servers with which the
   client (SBC) shares a secret.

2. Rf Billing Statistics\- Represents Rf billing statistics 
   information which monitors the messages sent per\-realm over
   IMS Rx interface by Rf billing manager(SBC).

3. SIP Statistics \- Represents SIP requests and various SIP
   responses on a SIP adjacency in a given interval.

The Session Border Controller (SBC) enables direct IP\-to\-IP
interconnect between multiple administrative domains for
session\-based services providing protocol inter\-working,
security, and admission control and management. The SBC is a
voice over IP (VoIP) device that sits on the border of a 
network and controls call admission to that network. 

The primary purpose of an SBC is to protect the interior of the
network from excessive call load and malicious traffic.
Additional functions provided by the SBC include media bridging
and billing services. 

Periodic Statistics \- Represents the SBC call statistics 
information for a particular time interval. E.g. you can 
specify that you want to retrieve statistics for a summary 
period of the current or previous 5 minutes, 15 minutes, hour, 
or day. The statistics for 5 minutes are divided into five 
minute intervals past the hour \- that is, at 0 minutes, 5 
minutes, 10 minutes... past the hour.  When you retrieve 
statistics for the current five minute period, you will be 
given statistics from the start of the interval to the current
time. When you retrieve statistics for the previous five 
minutes, you will be given the statistics for the entirety of 
the previous interval. For example, if it is currently 12\:43
\-  the current 5 minute statistics cover 12\:40 \- 12\:43

\-  the previous 5 minute statistics cover 12\:35 \- 12\:40

The other intervals work similarly.  15 minute statistics are 
divided into 15 minute intervals past the hour (0 minutes, 15 
minutes, 30 minutes, 45 minutes).  Hourly statistics are divided
into intervals on the hour. Daily statistics are divided into
intervals at 0\:00 each day. Therefore, if you retrieve the 
statistics at 12\:43 for each of these intervals, the periods
covered are as follows.  
\-     current 15 minutes\: 12\:30 \- 12\:43

\-     previous 15 minutes\: 12\:15 \- 12\:30

\-     current hour\: 12\:00 \- 12\:43

\-     last hour\: 11\:00 \- 12\:00

\-     current day\: 00\:00 \- 12\:43

\-     last day\: 00\:00 (the day before) \- 00\:00.


GLOSSARY
SBC\: Session Border Controller

CSB\: CISCO Session Border Controller

Adjacency\: An adjacency contains the system information to be
transmitted to next HOP.

ACR\: Accounting Request

ACA\: Accounting Accept

AVP\: Attribute\-Value Pairs

REFERENCES
1. CISCO Session Border Controller Documents and FAQ
http\://zed.cisco.com/confluence/display/SBC/SBC

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiscoSbcRadiusClientType(Enum):
    """
    CiscoSbcRadiusClientType

    This textual convention represents the type of RADIUS client.

    .. data:: authentication = 1

    .. data:: accounting = 2

    """

    authentication = Enum.YLeaf(1, "authentication")

    accounting = Enum.YLeaf(2, "accounting")


class CiscoSbcSIPMethod(Enum):
    """
    CiscoSbcSIPMethod

    This textual convention represents the various SIP Methods.

    .. data:: unknown = 1

    .. data:: ack = 2

    .. data:: bye = 3

    .. data:: cancel = 4

    .. data:: info = 5

    .. data:: invite = 6

    .. data:: message = 7

    .. data:: notify = 8

    .. data:: options = 9

    .. data:: prack = 10

    .. data:: refer = 11

    .. data:: register = 12

    .. data:: subscribe = 13

    .. data:: update = 14

    """

    unknown = Enum.YLeaf(1, "unknown")

    ack = Enum.YLeaf(2, "ack")

    bye = Enum.YLeaf(3, "bye")

    cancel = Enum.YLeaf(4, "cancel")

    info = Enum.YLeaf(5, "info")

    invite = Enum.YLeaf(6, "invite")

    message = Enum.YLeaf(7, "message")

    notify = Enum.YLeaf(8, "notify")

    options = Enum.YLeaf(9, "options")

    prack = Enum.YLeaf(10, "prack")

    refer = Enum.YLeaf(11, "refer")

    register = Enum.YLeaf(12, "register")

    subscribe = Enum.YLeaf(13, "subscribe")

    update = Enum.YLeaf(14, "update")



class CISCOSESSBORDERCTRLRSTATSMIB(Entity):
    """
    
    
    .. attribute:: csbradiusstatstable
    
    	This table has the reporting statistics of various RADIUS messages for RADIUS servers with which the client (SBC) shares a secret. Each entry in this table is identified by a  value of csbRadiusStatsEntIndex. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:  :py:class:`Csbradiusstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable>`
    
    .. attribute:: csbrfbillrealmstatstable
    
    	This table describes the Rf billing statistics information which monitors the messages sent per\-realm by Rf billing  manager(SBC). SBC sends Rf billing data using Diameter as a transport protocol. Rf billing uses only ACR and ACA Diameter messages for the transport of billing data. The Accounting\-Record\-Type AVP on the ACR message labels the type  of the accounting request. The following types are used by Rf billing. 1.   For session\-based charging, the types Start (session begins), Interim (session is modified) and Stop (session ends) are used. 2.   For event\-based charging, the type Event is used when a chargeable event occurs outside the scope of a session.  Each row of this table is identified by a value of csbRfBillRealmStatsIndex and csbRfBillRealmStatsRealmName. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and  csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:  :py:class:`Csbrfbillrealmstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable>`
    
    .. attribute:: csbsipmthdcurrentstatstable
    
    	This table reports count of SIP request and various SIP responses  for each SIP method on a SIP adjacency in a given interval. Each entry in this table represents a SIP method, its incoming and outgoing count, individual incoming and outgoing  count of various SIP responses for this method on a SIP adjacency in a given interval. To understand the meaning of  interval please refer <Periodic Statistics> section in  description of ciscoSbcStatsMIB.   This table is indexed on csbSIPMthdCurrentStatsAdjName, csbSIPMthdCurrentStatsMethod and  csbSIPMthdCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:  :py:class:`Csbsipmthdcurrentstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable>`
    
    .. attribute:: csbsipmthdhistorystatstable
    
    	This table provide historical count of SIP request and various SIP responses for each SIP method on a SIP adjacency in various interval length defined by the csbSIPMthdHistoryStatsInterval object. Each entry in this table represents a SIP method, its incoming and outgoing count, individual incoming and outgoing  count of various SIP responses for this method on a SIP adjacency in a given interval. The possible values of interval will be previous 5 minutes, previous 15 minutes, previous 1 hour and previous day. To understand the meaning of interval please refer <Periodic Statistics> description of ciscoSbcStatsMIB. This table is indexed on csbSIPMthdHistoryStatsAdjName, csbSIPMthdHistoryStatsMethod and  csbSIPMthdHistoryStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
    	**type**\:  :py:class:`Csbsipmthdhistorystatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable>`
    
    .. attribute:: csbsipmthdrccurrentstatstable
    
    	This table reports SIP method request and response code statistics for each method and response code combination on given SIP adjacency in a given interval. To understand the  meaning of interval please refer <Periodic Statistics> section in description of ciscoSbcStatsMIB. An exact lookup will return a row only  if \- 1) detailed response code statistics are turned on in SBC 2) response code  messages sent or received is non zero for     given SIP adjacency, method and interval. Also an inexact lookup will only return rows for messages with non\-zero counts, to protect the user from large numbers of rows  for response codes which have not been received or sent
    	**type**\:  :py:class:`Csbsipmthdrccurrentstatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable>`
    
    .. attribute:: csbsipmthdrchistorystatstable
    
    	This table reports historical data for SIP method request and response code statistics for each method and response code  combination in a given past interval. The possible values of  interval will be previous 5 minutes, previous 15 minutes,  previous 1 hour and previous day. To understand the  meaning of interval please refer <Periodic Statistics> section in description of ciscoSbcStatsMIB. An exact lookup will return a row only  if \- 1) detailed response code statistics are turned on in SBC 2) response code  messages sent or received is non zero for     given SIP adjacency, method and interval. Also an inexact lookup will only return rows for messages with non\-zero counts, to protect the user from large numbers of rows for response codes which have not been received or sent
    	**type**\:  :py:class:`Csbsipmthdrchistorystatstable <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable>`
    
    

    """

    _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
    _revision = '2010-09-15'

    def __init__(self):
        super(CISCOSESSBORDERCTRLRSTATSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
        self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"csbRadiusStatsTable" : ("csbradiusstatstable", CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable), "csbRfBillRealmStatsTable" : ("csbrfbillrealmstatstable", CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable), "csbSIPMthdCurrentStatsTable" : ("csbsipmthdcurrentstatstable", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable), "csbSIPMthdHistoryStatsTable" : ("csbsipmthdhistorystatstable", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable), "csbSIPMthdRCCurrentStatsTable" : ("csbsipmthdrccurrentstatstable", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable), "csbSIPMthdRCHistoryStatsTable" : ("csbsipmthdrchistorystatstable", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable)}
        self._child_list_classes = {}

        self.csbradiusstatstable = CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable()
        self.csbradiusstatstable.parent = self
        self._children_name_map["csbradiusstatstable"] = "csbRadiusStatsTable"
        self._children_yang_names.add("csbRadiusStatsTable")

        self.csbrfbillrealmstatstable = CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable()
        self.csbrfbillrealmstatstable.parent = self
        self._children_name_map["csbrfbillrealmstatstable"] = "csbRfBillRealmStatsTable"
        self._children_yang_names.add("csbRfBillRealmStatsTable")

        self.csbsipmthdcurrentstatstable = CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable()
        self.csbsipmthdcurrentstatstable.parent = self
        self._children_name_map["csbsipmthdcurrentstatstable"] = "csbSIPMthdCurrentStatsTable"
        self._children_yang_names.add("csbSIPMthdCurrentStatsTable")

        self.csbsipmthdhistorystatstable = CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable()
        self.csbsipmthdhistorystatstable.parent = self
        self._children_name_map["csbsipmthdhistorystatstable"] = "csbSIPMthdHistoryStatsTable"
        self._children_yang_names.add("csbSIPMthdHistoryStatsTable")

        self.csbsipmthdrccurrentstatstable = CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable()
        self.csbsipmthdrccurrentstatstable.parent = self
        self._children_name_map["csbsipmthdrccurrentstatstable"] = "csbSIPMthdRCCurrentStatsTable"
        self._children_yang_names.add("csbSIPMthdRCCurrentStatsTable")

        self.csbsipmthdrchistorystatstable = CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable()
        self.csbsipmthdrchistorystatstable.parent = self
        self._children_name_map["csbsipmthdrchistorystatstable"] = "csbSIPMthdRCHistoryStatsTable"
        self._children_yang_names.add("csbSIPMthdRCHistoryStatsTable")
        self._segment_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB"


    class Csbradiusstatstable(Entity):
        """
        This table has the reporting statistics of various RADIUS
        messages for RADIUS servers with which the client (SBC) shares a
        secret. Each entry in this table is identified by a 
        value of csbRadiusStatsEntIndex. The other indices of this table
        are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbradiusstatsentry
        
        	A conceptual row in the csbRadiusStatsTable. There is an entry in this table for each RADIUS server, as identified by a  value of csbRadiusStatsEntIndex. The other indices of this  table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbradiusstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable.Csbradiusstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable, self).__init__()

            self.yang_name = "csbRadiusStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"csbRadiusStatsEntry" : ("csbradiusstatsentry", CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable.Csbradiusstatsentry)}

            self.csbradiusstatsentry = YList(self)
            self._segment_path = lambda: "csbRadiusStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable, [], name, value)


        class Csbradiusstatsentry(Entity):
            """
            A conceptual row in the csbRadiusStatsTable. There is an
            entry in this table for each RADIUS server, as identified by a 
            value of csbRadiusStatsEntIndex. The other indices of this 
            table are csbCallStatsInstanceIndex defined in 
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbradiusstatsentindex  <key>
            
            	This object indicates the index of the RADIUS client entity that this server is configured on. This index is assigned  arbitrarily by the engine and is not saved over reboots
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbradiusstatsclientname
            
            	This object indicates the client name of the RADIUS client to which that these statistics apply
            	**type**\: str
            
            .. attribute:: csbradiusstatsclienttype
            
            	This object indicates the type(authentication or accounting) of the RADIUS clients configured on SBC
            	**type**\:  :py:class:`CiscoSbcRadiusClientType <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcRadiusClientType>`
            
            .. attribute:: csbradiusstatssrvrname
            
            	This object indicates the server name of the RADIUS server to which that these statistics apply
            	**type**\: str
            
            .. attribute:: csbradiusstatsacsreqs
            
            	This object indicates the number of RADIUS Access\-Request packets sent to this server.  This does not include retransmissions
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsacsrtrns
            
            	This object indicates the number of RADIUS Access\-Request packets retransmitted to this RADIUS server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsacsaccpts
            
            	This object indicates the number of RADIUS Access\-Accept packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: csbradiusstatsacsrejects
            
            	This object indicates the number of RADIUS Access\-Reject packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsacschalls
            
            	This object indicates the number of RADIUS Access\-Challenge packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsactreqs
            
            	This object indicates the number of RADIUS Accounting\-Request packets sent to this server. This does not include retransmissions
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsactretrans
            
            	This object indicates the number of RADIUS Accounting\-Request packets retransmitted to this RADIUS server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsactrsps
            
            	This object indicates the number of RADIUS Accounting\-Response packets (valid or invalid) received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsmalformedrsps
            
            	This object indicates the number of malformed RADIUS response packets received from this server.  Malformed packets include packets with an invalid length. Bad authenticators, Signature attributes and unknown types are not included as malformed access responses
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsbadauths
            
            	This object indicates the number of RADIUS response packets containing invalid authenticators or Signature attributes received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatspending
            
            	This object indicates the number of RADIUS request packets destined for this server that have not yet timed out or received a response. This variable is incremented when a request is sent and decremented on receipt of the response or on a timeout or retransmission
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatstimeouts
            
            	This object indicates the number of RADIUS request timeouts to this server.  After a timeout the client may retry to a different server or give up. A retry to a different server is counted as a request as well as a timeout
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsunknowntype
            
            	This object indicates the number of RADIUS packets of unknown type which were received from this server
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: csbradiusstatsdropped
            
            	This object indicates the number of RADIUS packets which were received from this server and dropped for some other reason
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable.Csbradiusstatsentry, self).__init__()

                self.yang_name = "csbRadiusStatsEntry"
                self.yang_parent_name = "csbRadiusStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbradiusstatsentindex = YLeaf(YType.uint32, "csbRadiusStatsEntIndex")

                self.csbradiusstatsclientname = YLeaf(YType.str, "csbRadiusStatsClientName")

                self.csbradiusstatsclienttype = YLeaf(YType.enumeration, "csbRadiusStatsClientType")

                self.csbradiusstatssrvrname = YLeaf(YType.str, "csbRadiusStatsSrvrName")

                self.csbradiusstatsacsreqs = YLeaf(YType.uint64, "csbRadiusStatsAcsReqs")

                self.csbradiusstatsacsrtrns = YLeaf(YType.uint64, "csbRadiusStatsAcsRtrns")

                self.csbradiusstatsacsaccpts = YLeaf(YType.uint64, "csbRadiusStatsAcsAccpts")

                self.csbradiusstatsacsrejects = YLeaf(YType.uint64, "csbRadiusStatsAcsRejects")

                self.csbradiusstatsacschalls = YLeaf(YType.uint64, "csbRadiusStatsAcsChalls")

                self.csbradiusstatsactreqs = YLeaf(YType.uint64, "csbRadiusStatsActReqs")

                self.csbradiusstatsactretrans = YLeaf(YType.uint64, "csbRadiusStatsActRetrans")

                self.csbradiusstatsactrsps = YLeaf(YType.uint64, "csbRadiusStatsActRsps")

                self.csbradiusstatsmalformedrsps = YLeaf(YType.uint64, "csbRadiusStatsMalformedRsps")

                self.csbradiusstatsbadauths = YLeaf(YType.uint64, "csbRadiusStatsBadAuths")

                self.csbradiusstatspending = YLeaf(YType.uint32, "csbRadiusStatsPending")

                self.csbradiusstatstimeouts = YLeaf(YType.uint64, "csbRadiusStatsTimeouts")

                self.csbradiusstatsunknowntype = YLeaf(YType.uint64, "csbRadiusStatsUnknownType")

                self.csbradiusstatsdropped = YLeaf(YType.uint64, "csbRadiusStatsDropped")
                self._segment_path = lambda: "csbRadiusStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbRadiusStatsEntIndex='" + self.csbradiusstatsentindex.get() + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbRadiusStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbradiusstatstable.Csbradiusstatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbradiusstatsentindex', 'csbradiusstatsclientname', 'csbradiusstatsclienttype', 'csbradiusstatssrvrname', 'csbradiusstatsacsreqs', 'csbradiusstatsacsrtrns', 'csbradiusstatsacsaccpts', 'csbradiusstatsacsrejects', 'csbradiusstatsacschalls', 'csbradiusstatsactreqs', 'csbradiusstatsactretrans', 'csbradiusstatsactrsps', 'csbradiusstatsmalformedrsps', 'csbradiusstatsbadauths', 'csbradiusstatspending', 'csbradiusstatstimeouts', 'csbradiusstatsunknowntype', 'csbradiusstatsdropped'], name, value)


    class Csbrfbillrealmstatstable(Entity):
        """
        This table describes the Rf billing statistics information
        which monitors the messages sent per\-realm by Rf billing 
        manager(SBC). SBC sends Rf billing data using Diameter as a
        transport protocol. Rf billing uses only ACR and ACA Diameter
        messages for the transport of billing data. The
        Accounting\-Record\-Type AVP on the ACR message labels the type 
        of the accounting request. The following types are used by Rf
        billing.
        1.   For session\-based charging, the types Start (session
        begins), Interim (session is modified) and Stop (session ends)
        are used.
        2.   For event\-based charging, the type Event is used when a
        chargeable event occurs outside the scope of a session.
        
        Each row of this table is identified by a value of
        csbRfBillRealmStatsIndex and csbRfBillRealmStatsRealmName.
        The other indices of this table are csbCallStatsInstanceIndex
        defined in csbCallStatsInstanceTable and 
        csbCallStatsServiceIndex defined in csbCallStatsTable.
        
        .. attribute:: csbrfbillrealmstatsentry
        
        	A conceptual row in the csbRfBillRealmStatsTable. There is an entry in this table for each realm, as identified by a  value of csbRfBillRealmStatsIndex and  csbRfBillRealmStatsRealmName. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbrfbillrealmstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable, self).__init__()

            self.yang_name = "csbRfBillRealmStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"csbRfBillRealmStatsEntry" : ("csbrfbillrealmstatsentry", CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry)}

            self.csbrfbillrealmstatsentry = YList(self)
            self._segment_path = lambda: "csbRfBillRealmStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable, [], name, value)


        class Csbrfbillrealmstatsentry(Entity):
            """
            A conceptual row in the csbRfBillRealmStatsTable. There
            is an entry in this table for each realm, as identified by a 
            value of csbRfBillRealmStatsIndex and 
            csbRfBillRealmStatsRealmName. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbrfbillrealmstatsindex  <key>
            
            	This object indicates the billing method instance index. The range of valid values for this field is 0 \- 31
            	**type**\: int
            
            	**range:** 0..31
            
            .. attribute:: csbrfbillrealmstatsrealmname  <key>
            
            	This object indicates the realm for which these statistics are collected. The length of this object is zero when value is not assigned to it
            	**type**\: str
            
            .. attribute:: csbrfbillrealmstatstotalstartacrs
            
            	This object indicates the combined sum of successful and failed Start ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatstotalinterimacrs
            
            	This object indicates the combined sum of successful and failed Interim ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatstotalstopacrs
            
            	This object indicates the combined sum of successful and failed Stop ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatstotaleventacrs
            
            	This object indicates the combined sum of successful and failed Event ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssuccstartacrs
            
            	This object indicates the total number of successful Start ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssuccinterimacrs
            
            	This object indicates the total number of successful Interim ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssuccstopacrs
            
            	This object indicates the total number of successful Stop ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatssucceventacrs
            
            	This object indicates the total number of successful Event ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatsfailstartacrs
            
            	This object indicates the total number of failed Start ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatsfailinterimacrs
            
            	This object indicates the total number of failed Interim ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatsfailstopacrs
            
            	This object indicates the total number of failed Stop ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            .. attribute:: csbrfbillrealmstatsfaileventacrs
            
            	This object indicates the total number of failed Event ACRs since start of day or the last time the statistics were reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: ACRs
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry, self).__init__()

                self.yang_name = "csbRfBillRealmStatsEntry"
                self.yang_parent_name = "csbRfBillRealmStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbrfbillrealmstatsindex = YLeaf(YType.uint32, "csbRfBillRealmStatsIndex")

                self.csbrfbillrealmstatsrealmname = YLeaf(YType.str, "csbRfBillRealmStatsRealmName")

                self.csbrfbillrealmstatstotalstartacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalStartAcrs")

                self.csbrfbillrealmstatstotalinterimacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalInterimAcrs")

                self.csbrfbillrealmstatstotalstopacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalStopAcrs")

                self.csbrfbillrealmstatstotaleventacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsTotalEventAcrs")

                self.csbrfbillrealmstatssuccstartacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccStartAcrs")

                self.csbrfbillrealmstatssuccinterimacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccInterimAcrs")

                self.csbrfbillrealmstatssuccstopacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccStopAcrs")

                self.csbrfbillrealmstatssucceventacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsSuccEventAcrs")

                self.csbrfbillrealmstatsfailstartacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailStartAcrs")

                self.csbrfbillrealmstatsfailinterimacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailInterimAcrs")

                self.csbrfbillrealmstatsfailstopacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailStopAcrs")

                self.csbrfbillrealmstatsfaileventacrs = YLeaf(YType.uint32, "csbRfBillRealmStatsFailEventAcrs")
                self._segment_path = lambda: "csbRfBillRealmStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbRfBillRealmStatsIndex='" + self.csbrfbillrealmstatsindex.get() + "']" + "[csbRfBillRealmStatsRealmName='" + self.csbrfbillrealmstatsrealmname.get() + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbRfBillRealmStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbrfbillrealmstatstable.Csbrfbillrealmstatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbrfbillrealmstatsindex', 'csbrfbillrealmstatsrealmname', 'csbrfbillrealmstatstotalstartacrs', 'csbrfbillrealmstatstotalinterimacrs', 'csbrfbillrealmstatstotalstopacrs', 'csbrfbillrealmstatstotaleventacrs', 'csbrfbillrealmstatssuccstartacrs', 'csbrfbillrealmstatssuccinterimacrs', 'csbrfbillrealmstatssuccstopacrs', 'csbrfbillrealmstatssucceventacrs', 'csbrfbillrealmstatsfailstartacrs', 'csbrfbillrealmstatsfailinterimacrs', 'csbrfbillrealmstatsfailstopacrs', 'csbrfbillrealmstatsfaileventacrs'], name, value)


    class Csbsipmthdcurrentstatstable(Entity):
        """
        This table reports count of SIP request and various SIP
        responses  for each SIP method on a SIP adjacency in a given
        interval. Each entry in this table represents a SIP method, its
        incoming and outgoing count, individual incoming and outgoing 
        count of various SIP responses for this method on a SIP
        adjacency in a given interval. To understand the meaning of 
        interval please refer <Periodic Statistics> section in 
        description of ciscoSbcStatsMIB.  
        This table is indexed on csbSIPMthdCurrentStatsAdjName,
        csbSIPMthdCurrentStatsMethod and 
        csbSIPMthdCurrentStatsInterval. The other indices of this
        table are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbsipmthdcurrentstatsentry
        
        	A conceptual row in the csbSIPMthdCurrentStatsTable. Each row describes a SIP method and various responses count for this method on a given SIP adjacency and given interval. This table is indexed on csbSIPMthdCurrentStatsAdjName, csbSIPMthdCurrentStatsMethod and  csbSIPMthdCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in  csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbsipmthdcurrentstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable, self).__init__()

            self.yang_name = "csbSIPMthdCurrentStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"csbSIPMthdCurrentStatsEntry" : ("csbsipmthdcurrentstatsentry", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry)}

            self.csbsipmthdcurrentstatsentry = YList(self)
            self._segment_path = lambda: "csbSIPMthdCurrentStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable, [], name, value)


        class Csbsipmthdcurrentstatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdCurrentStatsTable. Each row
            describes a SIP method and various responses count for this
            method on a given SIP adjacency and given interval. This table
            is indexed on csbSIPMthdCurrentStatsAdjName,
            csbSIPMthdCurrentStatsMethod and 
            csbSIPMthdCurrentStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in 
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdcurrentstatsadjname  <key>
            
            	This object indicates the name of the SIP adjacency for which stats related with SIP request and all kind of corresponding SIP responses are reported. The object acts as an index of the table
            	**type**\: str
            
            .. attribute:: csbsipmthdcurrentstatsmethod  <key>
            
            	This object indicates the SIP method Request. The object acts as an index of the table
            	**type**\:  :py:class:`CiscoSbcSIPMethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod>`
            
            .. attribute:: csbsipmthdcurrentstatsinterval  <key>
            
            	This object indicates the interval for which the periodic statistics information is to be displayed. The interval values can be 5 minutes, 15 minutes, 1 hour , 1 Day. This  object acts as an index for the table
            	**type**\:  :py:class:`CiscoSbcPeriodicStatsInterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval>`
            
            .. attribute:: csbsipmthdcurrentstatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            .. attribute:: csbsipmthdcurrentstatsreqin
            
            	This object indicates the total incoming SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdcurrentstatsreqout
            
            	This object indicates the total outgoing SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdcurrentstatsresp1xxin
            
            	This object indicates the total 1xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp1xxout
            
            	This object indicates the total 1xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp2xxin
            
            	This object indicates the total 2xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp2xxout
            
            	This object indicates the total 2xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp3xxin
            
            	This object indicates the total 3xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp3xxout
            
            	This object indicates the total 3xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp4xxin
            
            	This object indicates the total 4xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp4xxout
            
            	This object indicates the total 4xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp5xxin
            
            	This object indicates the total 5xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp5xxout
            
            	This object indicates the total 5xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp6xxin
            
            	This object indicates the total 6xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdcurrentstatsresp6xxout
            
            	This object indicates the total 6xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry, self).__init__()

                self.yang_name = "csbSIPMthdCurrentStatsEntry"
                self.yang_parent_name = "csbSIPMthdCurrentStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdcurrentstatsadjname = YLeaf(YType.str, "csbSIPMthdCurrentStatsAdjName")

                self.csbsipmthdcurrentstatsmethod = YLeaf(YType.enumeration, "csbSIPMthdCurrentStatsMethod")

                self.csbsipmthdcurrentstatsinterval = YLeaf(YType.enumeration, "csbSIPMthdCurrentStatsInterval")

                self.csbsipmthdcurrentstatsmethodname = YLeaf(YType.str, "csbSIPMthdCurrentStatsMethodName")

                self.csbsipmthdcurrentstatsreqin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsReqIn")

                self.csbsipmthdcurrentstatsreqout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsReqOut")

                self.csbsipmthdcurrentstatsresp1xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp1xxIn")

                self.csbsipmthdcurrentstatsresp1xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp1xxOut")

                self.csbsipmthdcurrentstatsresp2xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp2xxIn")

                self.csbsipmthdcurrentstatsresp2xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp2xxOut")

                self.csbsipmthdcurrentstatsresp3xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp3xxIn")

                self.csbsipmthdcurrentstatsresp3xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp3xxOut")

                self.csbsipmthdcurrentstatsresp4xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp4xxIn")

                self.csbsipmthdcurrentstatsresp4xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp4xxOut")

                self.csbsipmthdcurrentstatsresp5xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp5xxIn")

                self.csbsipmthdcurrentstatsresp5xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp5xxOut")

                self.csbsipmthdcurrentstatsresp6xxin = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp6xxIn")

                self.csbsipmthdcurrentstatsresp6xxout = YLeaf(YType.uint32, "csbSIPMthdCurrentStatsResp6xxOut")
                self._segment_path = lambda: "csbSIPMthdCurrentStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdCurrentStatsAdjName='" + self.csbsipmthdcurrentstatsadjname.get() + "']" + "[csbSIPMthdCurrentStatsMethod='" + self.csbsipmthdcurrentstatsmethod.get() + "']" + "[csbSIPMthdCurrentStatsInterval='" + self.csbsipmthdcurrentstatsinterval.get() + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdCurrentStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdcurrentstatstable.Csbsipmthdcurrentstatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbsipmthdcurrentstatsadjname', 'csbsipmthdcurrentstatsmethod', 'csbsipmthdcurrentstatsinterval', 'csbsipmthdcurrentstatsmethodname', 'csbsipmthdcurrentstatsreqin', 'csbsipmthdcurrentstatsreqout', 'csbsipmthdcurrentstatsresp1xxin', 'csbsipmthdcurrentstatsresp1xxout', 'csbsipmthdcurrentstatsresp2xxin', 'csbsipmthdcurrentstatsresp2xxout', 'csbsipmthdcurrentstatsresp3xxin', 'csbsipmthdcurrentstatsresp3xxout', 'csbsipmthdcurrentstatsresp4xxin', 'csbsipmthdcurrentstatsresp4xxout', 'csbsipmthdcurrentstatsresp5xxin', 'csbsipmthdcurrentstatsresp5xxout', 'csbsipmthdcurrentstatsresp6xxin', 'csbsipmthdcurrentstatsresp6xxout'], name, value)


    class Csbsipmthdhistorystatstable(Entity):
        """
        This table provide historical count of SIP request and various
        SIP responses for each SIP method on a SIP adjacency in various
        interval length defined by the csbSIPMthdHistoryStatsInterval
        object. Each entry in this table represents a SIP method, its
        incoming and outgoing count, individual incoming and outgoing 
        count of various SIP responses for this method on a SIP
        adjacency in a given interval. The possible values of interval
        will be previous 5 minutes, previous 15 minutes, previous 1 hour
        and previous day. To understand the meaning of interval please
        refer <Periodic Statistics> description of ciscoSbcStatsMIB.
        This table is indexed on csbSIPMthdHistoryStatsAdjName,
        csbSIPMthdHistoryStatsMethod and 
        csbSIPMthdHistoryStatsInterval. The other indices of this
        table are csbCallStatsInstanceIndex defined in 
        csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
        in csbCallStatsTable.
        
        .. attribute:: csbsipmthdhistorystatsentry
        
        	A conceptual row in the csbSIPMthdHistoryStatsTable. The entries in this table are updated as interval completes in the csbSIPMthdCurrentStatsTable table and the data is  moved from that table to this one. This table is indexed on csbSIPMthdHistoryStatsAdjName, csbSIPMthdHistoryStatsMethod and csbSIPMthdHistoryStatsInterval. The other indices of this  table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbsipmthdhistorystatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable, self).__init__()

            self.yang_name = "csbSIPMthdHistoryStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"csbSIPMthdHistoryStatsEntry" : ("csbsipmthdhistorystatsentry", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry)}

            self.csbsipmthdhistorystatsentry = YList(self)
            self._segment_path = lambda: "csbSIPMthdHistoryStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable, [], name, value)


        class Csbsipmthdhistorystatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdHistoryStatsTable. The
            entries in this table are updated as interval completes in
            the csbSIPMthdCurrentStatsTable table and the data is 
            moved from that table to this one.
            This table is indexed on csbSIPMthdHistoryStatsAdjName,
            csbSIPMthdHistoryStatsMethod and
            csbSIPMthdHistoryStatsInterval. The other indices of this 
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex
            defined in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdhistorystatsadjname  <key>
            
            	This object indicates the name of the SIP adjacency for which stats related with SIP request and all kind of corresponding SIP responses are reported. The object acts as an index of the table
            	**type**\: str
            
            .. attribute:: csbsipmthdhistorystatsmethod  <key>
            
            	This object indicates the SIP method Request. The object acts as an index of the table
            	**type**\:  :py:class:`CiscoSbcSIPMethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod>`
            
            .. attribute:: csbsipmthdhistorystatsinterval  <key>
            
            	This object indicates the interval for which the historical statistics information is to be displayed. The interval values can be previous 5 minutes, previous 15 minutes,  previous 1 hour and previous 1 Day. This object acts as an  index for the table
            	**type**\:  :py:class:`CiscoSbcPeriodicStatsInterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval>`
            
            .. attribute:: csbsipmthdhistorystatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            .. attribute:: csbsipmthdhistorystatsreqin
            
            	This object indicates the total incoming SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdhistorystatsreqout
            
            	This object indicates the total outgoing SIP message requests of this type on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: requests
            
            .. attribute:: csbsipmthdhistorystatsresp1xxin
            
            	This object indicates the total 1xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp1xxout
            
            	This object indicates the total 1xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp2xxin
            
            	This object indicates the total 2xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp2xxout
            
            	This object indicates the total 2xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp3xxin
            
            	This object indicates the total 3xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp3xxout
            
            	This object indicates the total 3xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp4xxin
            
            	This object indicates the total 4xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp4xxout
            
            	This object indicates the total 4xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp5xxin
            
            	This object indicates the total 5xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp5xxout
            
            	This object indicates the total 5xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp6xxin
            
            	This object indicates the total 6xx responses for this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdhistorystatsresp6xxout
            
            	This object indicates the total 6xx responses for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry, self).__init__()

                self.yang_name = "csbSIPMthdHistoryStatsEntry"
                self.yang_parent_name = "csbSIPMthdHistoryStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdhistorystatsadjname = YLeaf(YType.str, "csbSIPMthdHistoryStatsAdjName")

                self.csbsipmthdhistorystatsmethod = YLeaf(YType.enumeration, "csbSIPMthdHistoryStatsMethod")

                self.csbsipmthdhistorystatsinterval = YLeaf(YType.enumeration, "csbSIPMthdHistoryStatsInterval")

                self.csbsipmthdhistorystatsmethodname = YLeaf(YType.str, "csbSIPMthdHistoryStatsMethodName")

                self.csbsipmthdhistorystatsreqin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsReqIn")

                self.csbsipmthdhistorystatsreqout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsReqOut")

                self.csbsipmthdhistorystatsresp1xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp1xxIn")

                self.csbsipmthdhistorystatsresp1xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp1xxOut")

                self.csbsipmthdhistorystatsresp2xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp2xxIn")

                self.csbsipmthdhistorystatsresp2xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp2xxOut")

                self.csbsipmthdhistorystatsresp3xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp3xxIn")

                self.csbsipmthdhistorystatsresp3xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp3xxOut")

                self.csbsipmthdhistorystatsresp4xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp4xxIn")

                self.csbsipmthdhistorystatsresp4xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp4xxOut")

                self.csbsipmthdhistorystatsresp5xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp5xxIn")

                self.csbsipmthdhistorystatsresp5xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp5xxOut")

                self.csbsipmthdhistorystatsresp6xxin = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp6xxIn")

                self.csbsipmthdhistorystatsresp6xxout = YLeaf(YType.uint32, "csbSIPMthdHistoryStatsResp6xxOut")
                self._segment_path = lambda: "csbSIPMthdHistoryStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdHistoryStatsAdjName='" + self.csbsipmthdhistorystatsadjname.get() + "']" + "[csbSIPMthdHistoryStatsMethod='" + self.csbsipmthdhistorystatsmethod.get() + "']" + "[csbSIPMthdHistoryStatsInterval='" + self.csbsipmthdhistorystatsinterval.get() + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdHistoryStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdhistorystatstable.Csbsipmthdhistorystatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbsipmthdhistorystatsadjname', 'csbsipmthdhistorystatsmethod', 'csbsipmthdhistorystatsinterval', 'csbsipmthdhistorystatsmethodname', 'csbsipmthdhistorystatsreqin', 'csbsipmthdhistorystatsreqout', 'csbsipmthdhistorystatsresp1xxin', 'csbsipmthdhistorystatsresp1xxout', 'csbsipmthdhistorystatsresp2xxin', 'csbsipmthdhistorystatsresp2xxout', 'csbsipmthdhistorystatsresp3xxin', 'csbsipmthdhistorystatsresp3xxout', 'csbsipmthdhistorystatsresp4xxin', 'csbsipmthdhistorystatsresp4xxout', 'csbsipmthdhistorystatsresp5xxin', 'csbsipmthdhistorystatsresp5xxout', 'csbsipmthdhistorystatsresp6xxin', 'csbsipmthdhistorystatsresp6xxout'], name, value)


    class Csbsipmthdrccurrentstatstable(Entity):
        """
        This table reports SIP method request and response code
        statistics for each method and response code combination on
        given SIP adjacency in a given interval. To understand the 
        meaning of interval please refer <Periodic Statistics> section
        in description of ciscoSbcStatsMIB. An exact lookup will return
        a row only  if \-
        1) detailed response code statistics are turned on in SBC
        2) response code  messages sent or received is non zero for 
           given SIP adjacency, method and interval.
        Also an inexact lookup will only return rows for messages with
        non\-zero counts, to protect the user from large numbers of rows 
        for response codes which have not been received or sent.
        
        .. attribute:: csbsipmthdrccurrentstatsentry
        
        	A conceptual row in the csbSIPMthdRCCurrentStatsTable. Each entry in this table represents a method and response code combination. Each entry in this table is identified by a value of csbSIPMthdRCCurrentStatsAdjName, csbSIPMthdRCCurrentStatsMethod, csbSIPMthdRCCurrentStatsRespCode and csbSIPMthdRCCurrentStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbsipmthdrccurrentstatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable, self).__init__()

            self.yang_name = "csbSIPMthdRCCurrentStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"csbSIPMthdRCCurrentStatsEntry" : ("csbsipmthdrccurrentstatsentry", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry)}

            self.csbsipmthdrccurrentstatsentry = YList(self)
            self._segment_path = lambda: "csbSIPMthdRCCurrentStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable, [], name, value)


        class Csbsipmthdrccurrentstatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdRCCurrentStatsTable. Each
            entry in this table represents a method and response code
            combination. Each entry in this table is identified by a value
            of csbSIPMthdRCCurrentStatsAdjName,
            csbSIPMthdRCCurrentStatsMethod,
            csbSIPMthdRCCurrentStatsRespCode and
            csbSIPMthdRCCurrentStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdrccurrentstatsadjname  <key>
            
            	This identifies the name of the adjacency for which statistics are reported. This object acts as an index for the table
            	**type**\: str
            
            .. attribute:: csbsipmthdrccurrentstatsmethod  <key>
            
            	This object indicates the SIP method request. This object acts as an index for the table
            	**type**\:  :py:class:`CiscoSbcSIPMethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod>`
            
            .. attribute:: csbsipmthdrccurrentstatsrespcode  <key>
            
            	This object indicates the response code for the SIP message request. The range of valid values for SIP response codes is 100 \- 999. This object acts as an index for the table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrccurrentstatsinterval  <key>
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be 5 min, 15 mins, 1 hour , 1 Day. This object acts as an index for the table
            	**type**\:  :py:class:`CiscoSbcPeriodicStatsInterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval>`
            
            .. attribute:: csbsipmthdrccurrentstatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            .. attribute:: csbsipmthdrccurrentstatsrespin
            
            	This object indicates the total SIP messages with this response code this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdrccurrentstatsrespout
            
            	This object indicates the total SIP messages with this response code for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry, self).__init__()

                self.yang_name = "csbSIPMthdRCCurrentStatsEntry"
                self.yang_parent_name = "csbSIPMthdRCCurrentStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdrccurrentstatsadjname = YLeaf(YType.str, "csbSIPMthdRCCurrentStatsAdjName")

                self.csbsipmthdrccurrentstatsmethod = YLeaf(YType.enumeration, "csbSIPMthdRCCurrentStatsMethod")

                self.csbsipmthdrccurrentstatsrespcode = YLeaf(YType.uint32, "csbSIPMthdRCCurrentStatsRespCode")

                self.csbsipmthdrccurrentstatsinterval = YLeaf(YType.enumeration, "csbSIPMthdRCCurrentStatsInterval")

                self.csbsipmthdrccurrentstatsmethodname = YLeaf(YType.str, "csbSIPMthdRCCurrentStatsMethodName")

                self.csbsipmthdrccurrentstatsrespin = YLeaf(YType.uint32, "csbSIPMthdRCCurrentStatsRespIn")

                self.csbsipmthdrccurrentstatsrespout = YLeaf(YType.uint32, "csbSIPMthdRCCurrentStatsRespOut")
                self._segment_path = lambda: "csbSIPMthdRCCurrentStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdRCCurrentStatsAdjName='" + self.csbsipmthdrccurrentstatsadjname.get() + "']" + "[csbSIPMthdRCCurrentStatsMethod='" + self.csbsipmthdrccurrentstatsmethod.get() + "']" + "[csbSIPMthdRCCurrentStatsRespCode='" + self.csbsipmthdrccurrentstatsrespcode.get() + "']" + "[csbSIPMthdRCCurrentStatsInterval='" + self.csbsipmthdrccurrentstatsinterval.get() + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdRCCurrentStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrccurrentstatstable.Csbsipmthdrccurrentstatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbsipmthdrccurrentstatsadjname', 'csbsipmthdrccurrentstatsmethod', 'csbsipmthdrccurrentstatsrespcode', 'csbsipmthdrccurrentstatsinterval', 'csbsipmthdrccurrentstatsmethodname', 'csbsipmthdrccurrentstatsrespin', 'csbsipmthdrccurrentstatsrespout'], name, value)


    class Csbsipmthdrchistorystatstable(Entity):
        """
        This table reports historical data for SIP method request and
        response code statistics for each method and response code 
        combination in a given past interval. The possible values of 
        interval will be previous 5 minutes, previous 15 minutes, 
        previous 1 hour and previous day. To understand the 
        meaning of interval please refer <Periodic Statistics> section
        in description of ciscoSbcStatsMIB. An exact lookup will return
        a row only  if \-
        1) detailed response code statistics are turned on in SBC
        2) response code  messages sent or received is non zero for 
           given SIP adjacency, method and interval.
        Also an inexact lookup will only return rows for messages with
        non\-zero counts, to protect the user from large numbers of rows
        for response codes which have not been received or sent.
        
        .. attribute:: csbsipmthdrchistorystatsentry
        
        	A conceptual row in the csbSIPMthdRCHistoryStatsTable. The entries in this table are updated as interval completes in the csbSIPMthdRCCurrentStatsTable table and the data is  moved from that table to this one. Each entry in this table  is identified by a value of csbSIPMthdRCHistoryStatsAdjName,  csbSIPMthdRCHistoryStatsMethod, csbSIPMthdRCHistoryStatsRespCode and csbSIPMthdRCHistoryStatsInterval. The other indices of this table are csbCallStatsInstanceIndex defined in csbCallStatsInstanceTable and csbCallStatsServiceIndex defined in csbCallStatsTable
        	**type**\: list of  		 :py:class:`Csbsipmthdrchistorystatsentry <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry>`
        
        

        """

        _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
        _revision = '2010-09-15'

        def __init__(self):
            super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable, self).__init__()

            self.yang_name = "csbSIPMthdRCHistoryStatsTable"
            self.yang_parent_name = "CISCO-SESS-BORDER-CTRLR-STATS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"csbSIPMthdRCHistoryStatsEntry" : ("csbsipmthdrchistorystatsentry", CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry)}

            self.csbsipmthdrchistorystatsentry = YList(self)
            self._segment_path = lambda: "csbSIPMthdRCHistoryStatsTable"
            self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable, [], name, value)


        class Csbsipmthdrchistorystatsentry(Entity):
            """
            A conceptual row in the csbSIPMthdRCHistoryStatsTable. The
            entries in this table are updated as interval completes in
            the csbSIPMthdRCCurrentStatsTable table and the data is 
            moved from that table to this one. Each entry in this table 
            is identified by a value of csbSIPMthdRCHistoryStatsAdjName, 
            csbSIPMthdRCHistoryStatsMethod,
            csbSIPMthdRCHistoryStatsRespCode and
            csbSIPMthdRCHistoryStatsInterval. The other indices of this
            table are csbCallStatsInstanceIndex defined in
            csbCallStatsInstanceTable and csbCallStatsServiceIndex defined
            in csbCallStatsTable.
            
            .. attribute:: csbcallstatsinstanceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsinstanceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatsinstancetable.Csbcallstatsinstanceentry>`
            
            .. attribute:: csbcallstatsserviceindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`csbcallstatsserviceindex <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CISCOSESSBORDERCTRLRCALLSTATSMIB.Csbcallstatstable.Csbcallstatsentry>`
            
            .. attribute:: csbsipmthdrchistorystatsadjname  <key>
            
            	This identifies the name of the adjacency for which statistics are reported. This object acts as an index for the table
            	**type**\: str
            
            .. attribute:: csbsipmthdrchistorystatsmethod  <key>
            
            	This object indicates the SIP method request. This object acts as an index for the table
            	**type**\:  :py:class:`CiscoSbcSIPMethod <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_STATS_MIB.CiscoSbcSIPMethod>`
            
            .. attribute:: csbsipmthdrchistorystatsrespcode  <key>
            
            	This object indicates the response code for the SIP message request. The range of valid values for SIP response codes is 100 \- 999. This object acts as an index for the table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: csbsipmthdrchistorystatsinterval  <key>
            
            	This object identifies the interval for which the periodic statistics information is to be displayed. The interval values can be previous 5 min, previous 15 mins, previous 1  hour , previous 1 Day. This object acts as an index for the table
            	**type**\:  :py:class:`CiscoSbcPeriodicStatsInterval <ydk.models.cisco_ios_xe.CISCO_SESS_BORDER_CTRLR_CALL_STATS_MIB.CiscoSbcPeriodicStatsInterval>`
            
            .. attribute:: csbsipmthdrchistorystatsmethodname
            
            	This object indicates the text representation of the SIP method request. E.g. INVITE, ACK, BYE etc
            	**type**\: str
            
            .. attribute:: csbsipmthdrchistorystatsrespin
            
            	This object indicates the total SIP messages with this response code this method received on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            .. attribute:: csbsipmthdrchistorystatsrespout
            
            	This object indicates the total SIP messages with this response code for this method sent on this SIP adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: responses
            
            

            """

            _prefix = 'CISCO-SESS-BORDER-CTRLR-STATS-MIB'
            _revision = '2010-09-15'

            def __init__(self):
                super(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry, self).__init__()

                self.yang_name = "csbSIPMthdRCHistoryStatsEntry"
                self.yang_parent_name = "csbSIPMthdRCHistoryStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.csbcallstatsinstanceindex = YLeaf(YType.str, "csbCallStatsInstanceIndex")

                self.csbcallstatsserviceindex = YLeaf(YType.str, "csbCallStatsServiceIndex")

                self.csbsipmthdrchistorystatsadjname = YLeaf(YType.str, "csbSIPMthdRCHistoryStatsAdjName")

                self.csbsipmthdrchistorystatsmethod = YLeaf(YType.enumeration, "csbSIPMthdRCHistoryStatsMethod")

                self.csbsipmthdrchistorystatsrespcode = YLeaf(YType.uint32, "csbSIPMthdRCHistoryStatsRespCode")

                self.csbsipmthdrchistorystatsinterval = YLeaf(YType.enumeration, "csbSIPMthdRCHistoryStatsInterval")

                self.csbsipmthdrchistorystatsmethodname = YLeaf(YType.str, "csbSIPMthdRCHistoryStatsMethodName")

                self.csbsipmthdrchistorystatsrespin = YLeaf(YType.uint32, "csbSIPMthdRCHistoryStatsRespIn")

                self.csbsipmthdrchistorystatsrespout = YLeaf(YType.uint32, "csbSIPMthdRCHistoryStatsRespOut")
                self._segment_path = lambda: "csbSIPMthdRCHistoryStatsEntry" + "[csbCallStatsInstanceIndex='" + self.csbcallstatsinstanceindex.get() + "']" + "[csbCallStatsServiceIndex='" + self.csbcallstatsserviceindex.get() + "']" + "[csbSIPMthdRCHistoryStatsAdjName='" + self.csbsipmthdrchistorystatsadjname.get() + "']" + "[csbSIPMthdRCHistoryStatsMethod='" + self.csbsipmthdrchistorystatsmethod.get() + "']" + "[csbSIPMthdRCHistoryStatsRespCode='" + self.csbsipmthdrchistorystatsrespcode.get() + "']" + "[csbSIPMthdRCHistoryStatsInterval='" + self.csbsipmthdrchistorystatsinterval.get() + "']"
                self._absolute_path = lambda: "CISCO-SESS-BORDER-CTRLR-STATS-MIB:CISCO-SESS-BORDER-CTRLR-STATS-MIB/csbSIPMthdRCHistoryStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSESSBORDERCTRLRSTATSMIB.Csbsipmthdrchistorystatstable.Csbsipmthdrchistorystatsentry, ['csbcallstatsinstanceindex', 'csbcallstatsserviceindex', 'csbsipmthdrchistorystatsadjname', 'csbsipmthdrchistorystatsmethod', 'csbsipmthdrchistorystatsrespcode', 'csbsipmthdrchistorystatsinterval', 'csbsipmthdrchistorystatsmethodname', 'csbsipmthdrchistorystatsrespin', 'csbsipmthdrchistorystatsrespout'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOSESSBORDERCTRLRSTATSMIB()
        return self._top_entity

