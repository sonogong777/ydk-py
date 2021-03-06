""" CISCO_OSPF_MIB 

An extension to the MIB module defined in
RFC 1850 for managing OSPF implimentation. 
Most of the MIB definitions are based on
the IETF draft 
< draft\-ietf\-ospf\-mib\-update\-05.txt > . 
Support for OSPF Sham link is also added

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOOSPFMIB(Entity):
    """
    
    
    .. attribute:: cospfgeneralgroup
    
    	
    	**type**\:  :py:class:`Cospfgeneralgroup <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfgeneralgroup>`
    
    .. attribute:: cospflsdbtable
    
    	The OSPF Process's Link State Database. This  table is meant for Opaque LSA's
    	**type**\:  :py:class:`Cospflsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospflsdbtable>`
    
    .. attribute:: cospfshamlinktable
    
    	Information about this router's sham links
    	**type**\:  :py:class:`Cospfshamlinktable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinktable>`
    
    	**status**\: deprecated
    
    .. attribute:: cospflocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for non\-virtual links
    	**type**\:  :py:class:`Cospflocallsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospflocallsdbtable>`
    
    .. attribute:: cospfvirtlocallsdbtable
    
    	The OSPF Process's Link\-Local Link State Database for virtual links
    	**type**\:  :py:class:`Cospfvirtlocallsdbtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfvirtlocallsdbtable>`
    
    .. attribute:: cospfshamlinknbrtable
    
    	A table of sham link neighbor information
    	**type**\:  :py:class:`Cospfshamlinknbrtable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinknbrtable>`
    
    .. attribute:: cospfshamlinkstable
    
    	Information about this router's sham links
    	**type**\:  :py:class:`Cospfshamlinkstable <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinkstable>`
    
    

    """

    _prefix = 'CISCO-OSPF-MIB'
    _revision = '2003-07-18'

    def __init__(self):
        super(CISCOOSPFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-OSPF-MIB"
        self.yang_parent_name = "CISCO-OSPF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cospfGeneralGroup" : ("cospfgeneralgroup", CISCOOSPFMIB.Cospfgeneralgroup), "cospfLsdbTable" : ("cospflsdbtable", CISCOOSPFMIB.Cospflsdbtable), "cospfShamLinkTable" : ("cospfshamlinktable", CISCOOSPFMIB.Cospfshamlinktable), "cospfLocalLsdbTable" : ("cospflocallsdbtable", CISCOOSPFMIB.Cospflocallsdbtable), "cospfVirtLocalLsdbTable" : ("cospfvirtlocallsdbtable", CISCOOSPFMIB.Cospfvirtlocallsdbtable), "cospfShamLinkNbrTable" : ("cospfshamlinknbrtable", CISCOOSPFMIB.Cospfshamlinknbrtable), "cospfShamLinksTable" : ("cospfshamlinkstable", CISCOOSPFMIB.Cospfshamlinkstable)}
        self._child_list_classes = {}

        self.cospfgeneralgroup = CISCOOSPFMIB.Cospfgeneralgroup()
        self.cospfgeneralgroup.parent = self
        self._children_name_map["cospfgeneralgroup"] = "cospfGeneralGroup"
        self._children_yang_names.add("cospfGeneralGroup")

        self.cospflsdbtable = CISCOOSPFMIB.Cospflsdbtable()
        self.cospflsdbtable.parent = self
        self._children_name_map["cospflsdbtable"] = "cospfLsdbTable"
        self._children_yang_names.add("cospfLsdbTable")

        self.cospfshamlinktable = CISCOOSPFMIB.Cospfshamlinktable()
        self.cospfshamlinktable.parent = self
        self._children_name_map["cospfshamlinktable"] = "cospfShamLinkTable"
        self._children_yang_names.add("cospfShamLinkTable")

        self.cospflocallsdbtable = CISCOOSPFMIB.Cospflocallsdbtable()
        self.cospflocallsdbtable.parent = self
        self._children_name_map["cospflocallsdbtable"] = "cospfLocalLsdbTable"
        self._children_yang_names.add("cospfLocalLsdbTable")

        self.cospfvirtlocallsdbtable = CISCOOSPFMIB.Cospfvirtlocallsdbtable()
        self.cospfvirtlocallsdbtable.parent = self
        self._children_name_map["cospfvirtlocallsdbtable"] = "cospfVirtLocalLsdbTable"
        self._children_yang_names.add("cospfVirtLocalLsdbTable")

        self.cospfshamlinknbrtable = CISCOOSPFMIB.Cospfshamlinknbrtable()
        self.cospfshamlinknbrtable.parent = self
        self._children_name_map["cospfshamlinknbrtable"] = "cospfShamLinkNbrTable"
        self._children_yang_names.add("cospfShamLinkNbrTable")

        self.cospfshamlinkstable = CISCOOSPFMIB.Cospfshamlinkstable()
        self.cospfshamlinkstable.parent = self
        self._children_name_map["cospfshamlinkstable"] = "cospfShamLinksTable"
        self._children_yang_names.add("cospfShamLinksTable")
        self._segment_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB"


    class Cospfgeneralgroup(Entity):
        """
        
        
        .. attribute:: cospfrfc1583compatibility
        
        	Indicates metrics used to choose among multiple AS\- external\-LSAs. When cospfRFC1583Compatibility is set to enabled, only cost will be used when choosing among multiple AS\-external\-LSAs advertising the same destination. When cospfRFC1583Compatibility is set to disabled, preference will be driven first by type of path using cost only to break ties
        	**type**\: bool
        
        .. attribute:: cospfopaquelsasupport
        
        	The router's support for Opaque LSA types
        	**type**\: bool
        
        .. attribute:: cospftrafficengineeringsupport
        
        	The router's support for OSPF traffic engineering
        	**type**\: bool
        
        .. attribute:: cospfopaqueaslsacount
        
        	The total number of Opaque AS link\-state advertisements in the link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cospfopaqueaslsacksumsum
        
        	The 32\-bit unsigned sum of the Opaque AS  link\-state advertisements' LS checksums contained link state database
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.Cospfgeneralgroup, self).__init__()

            self.yang_name = "cospfGeneralGroup"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cospfrfc1583compatibility = YLeaf(YType.boolean, "cospfRFC1583Compatibility")

            self.cospfopaquelsasupport = YLeaf(YType.boolean, "cospfOpaqueLsaSupport")

            self.cospftrafficengineeringsupport = YLeaf(YType.boolean, "cospfTrafficEngineeringSupport")

            self.cospfopaqueaslsacount = YLeaf(YType.uint32, "cospfOpaqueASLsaCount")

            self.cospfopaqueaslsacksumsum = YLeaf(YType.uint32, "cospfOpaqueASLsaCksumSum")
            self._segment_path = lambda: "cospfGeneralGroup"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.Cospfgeneralgroup, ['cospfrfc1583compatibility', 'cospfopaquelsasupport', 'cospftrafficengineeringsupport', 'cospfopaqueaslsacount', 'cospfopaqueaslsacksumsum'], name, value)


    class Cospflsdbtable(Entity):
        """
        The OSPF Process's Link State Database. This 
        table is meant for Opaque LSA's
        
        .. attribute:: cospflsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of  		 :py:class:`Cospflsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospflsdbtable.Cospflsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.Cospflsdbtable, self).__init__()

            self.yang_name = "cospfLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cospfLsdbEntry" : ("cospflsdbentry", CISCOOSPFMIB.Cospflsdbtable.Cospflsdbentry)}

            self.cospflsdbentry = YList(self)
            self._segment_path = lambda: "cospfLsdbTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.Cospflsdbtable, [], name, value)


        class Cospflsdbentry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: ospflsdbareaid  <key>
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbareaid <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: cospflsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`Cospflsdbtype <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospflsdbtable.Cospflsdbentry.Cospflsdbtype>`
            
            .. attribute:: ospflsdblsid  <key>
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdblsid <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: ospflsdbrouterid  <key>
            
            	
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ospflsdbrouterid <ydk.models.cisco_ios_xe.OSPF_MIB.OSPFMIB.Ospflsdbtable.Ospflsdbentry>`
            
            .. attribute:: cospflsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer.   It  is used to detect old and duplicate link state advertisements.  The  space  of sequence  numbers  is  linearly  ordered.   The larger the sequence number the more recent  the advertisement
            	**type**\: int
            
            	**range:** 1..147483647
            
            .. attribute:: cospflsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbchecksum
            
            	This field is the  checksum  of  the  complete contents  of  the  advertisement, excepting the age field.  The age field is excepted  so  that an   advertisement's  age  can  be  incremented without updating the  checksum.   The  checksum used  is  the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.Cospflsdbtable.Cospflsdbentry, self).__init__()

                self.yang_name = "cospfLsdbEntry"
                self.yang_parent_name = "cospfLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ospflsdbareaid = YLeaf(YType.str, "ospfLsdbAreaId")

                self.cospflsdbtype = YLeaf(YType.enumeration, "cospfLsdbType")

                self.ospflsdblsid = YLeaf(YType.str, "ospfLsdbLsid")

                self.ospflsdbrouterid = YLeaf(YType.str, "ospfLsdbRouterId")

                self.cospflsdbsequence = YLeaf(YType.int32, "cospfLsdbSequence")

                self.cospflsdbage = YLeaf(YType.int32, "cospfLsdbAge")

                self.cospflsdbchecksum = YLeaf(YType.int32, "cospfLsdbChecksum")

                self.cospflsdbadvertisement = YLeaf(YType.str, "cospfLsdbAdvertisement")
                self._segment_path = lambda: "cospfLsdbEntry" + "[ospfLsdbAreaId='" + self.ospflsdbareaid.get() + "']" + "[cospfLsdbType='" + self.cospflsdbtype.get() + "']" + "[ospfLsdbLsid='" + self.ospflsdblsid.get() + "']" + "[ospfLsdbRouterId='" + self.ospflsdbrouterid.get() + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.Cospflsdbtable.Cospflsdbentry, ['ospflsdbareaid', 'cospflsdbtype', 'ospflsdblsid', 'ospflsdbrouterid', 'cospflsdbsequence', 'cospflsdbage', 'cospflsdbchecksum', 'cospflsdbadvertisement'], name, value)

            class Cospflsdbtype(Enum):
                """
                Cospflsdbtype

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: areaOpaqueLink = 10

                .. data:: asOpaqueLink = 11

                """

                areaOpaqueLink = Enum.YLeaf(10, "areaOpaqueLink")

                asOpaqueLink = Enum.YLeaf(11, "asOpaqueLink")



    class Cospfshamlinktable(Entity):
        """
        Information about this router's sham links
        
        .. attribute:: cospfshamlinkentry
        
        	Information about a single sham link
        	**type**\: list of  		 :py:class:`Cospfshamlinkentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinktable.Cospfshamlinkentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.Cospfshamlinktable, self).__init__()

            self.yang_name = "cospfShamLinkTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cospfShamLinkEntry" : ("cospfshamlinkentry", CISCOOSPFMIB.Cospfshamlinktable.Cospfshamlinkentry)}

            self.cospfshamlinkentry = YList(self)
            self._segment_path = lambda: "cospfShamLinkTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.Cospfshamlinktable, [], name, value)


        class Cospfshamlinkentry(Entity):
            """
            Information about a single sham link
            
            .. attribute:: cospfshamlinkareaid  <key>
            
            	The  Transit  Area  that  the   Virtual   Link traverses.  By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinklocalipaddress  <key>
            
            	The Local IP address of the sham link
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkneighborid  <key>
            
            	The Router ID of the other end router of the sham link
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions,  for  adjacencies belonging to this  link.   This  value  is also used when retransmitting database description   and  link\-state  request  packets. This value   should  be well over the expected round trip time
            	**type**\: int
            
            	**range:** 0..3600
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkhellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\: int
            
            	**range:** 1..65535
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkstate
            
            	OSPF sham link states
            	**type**\:  :py:class:`Cospfshamlinkstate <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinktable.Cospfshamlinkentry.Cospfshamlinkstate>`
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkevents
            
            	The number of state changes or error events on this sham link
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cospfshamlinkmetric
            
            	The Metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.Cospfshamlinktable.Cospfshamlinkentry, self).__init__()

                self.yang_name = "cospfShamLinkEntry"
                self.yang_parent_name = "cospfShamLinkTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cospfshamlinkareaid = YLeaf(YType.str, "cospfShamLinkAreaId")

                self.cospfshamlinklocalipaddress = YLeaf(YType.str, "cospfShamLinkLocalIpAddress")

                self.cospfshamlinkneighborid = YLeaf(YType.str, "cospfShamLinkNeighborId")

                self.cospfshamlinkretransinterval = YLeaf(YType.int32, "cospfShamLinkRetransInterval")

                self.cospfshamlinkhellointerval = YLeaf(YType.int32, "cospfShamLinkHelloInterval")

                self.cospfshamlinkrtrdeadinterval = YLeaf(YType.int32, "cospfShamLinkRtrDeadInterval")

                self.cospfshamlinkstate = YLeaf(YType.enumeration, "cospfShamLinkState")

                self.cospfshamlinkevents = YLeaf(YType.uint32, "cospfShamLinkEvents")

                self.cospfshamlinkmetric = YLeaf(YType.int32, "cospfShamLinkMetric")
                self._segment_path = lambda: "cospfShamLinkEntry" + "[cospfShamLinkAreaId='" + self.cospfshamlinkareaid.get() + "']" + "[cospfShamLinkLocalIpAddress='" + self.cospfshamlinklocalipaddress.get() + "']" + "[cospfShamLinkNeighborId='" + self.cospfshamlinkneighborid.get() + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinkTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.Cospfshamlinktable.Cospfshamlinkentry, ['cospfshamlinkareaid', 'cospfshamlinklocalipaddress', 'cospfshamlinkneighborid', 'cospfshamlinkretransinterval', 'cospfshamlinkhellointerval', 'cospfshamlinkrtrdeadinterval', 'cospfshamlinkstate', 'cospfshamlinkevents', 'cospfshamlinkmetric'], name, value)

            class Cospfshamlinkstate(Enum):
                """
                Cospfshamlinkstate

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")



    class Cospflocallsdbtable(Entity):
        """
        The OSPF Process's Link\-Local Link State Database
        for non\-virtual links.
        
        .. attribute:: cospflocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of  		 :py:class:`Cospflocallsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospflocallsdbtable.Cospflocallsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.Cospflocallsdbtable, self).__init__()

            self.yang_name = "cospfLocalLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cospfLocalLsdbEntry" : ("cospflocallsdbentry", CISCOOSPFMIB.Cospflocallsdbtable.Cospflocallsdbentry)}

            self.cospflocallsdbentry = YList(self)
            self._segment_path = lambda: "cospfLocalLsdbTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.Cospflocallsdbtable, [], name, value)


        class Cospflocallsdbentry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospflocallsdbipaddress  <key>
            
            	The IP Address of the interface from which the LSA was received if the interface is numbered
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbaddresslessif  <key>
            
            	The Interface Index of the interface from which the LSA was received if the interface is unnumbered
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospflocallsdbtype  <key>
            
            	The type of the link state advertisement. Each link state type has a separate advertisement format
            	**type**\:  :py:class:`Cospflocallsdbtype <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospflocallsdbtable.Cospflocallsdbentry.Cospflocallsdbtype>`
            
            .. attribute:: cospflocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbrouterid  <key>
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospflocallsdbsequence
            
            	The sequence number field is a signed 32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483647..2147483647
            
            .. attribute:: cospflocallsdbage
            
            	This field is the age of the link state advertisement  in seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospflocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospflocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.Cospflocallsdbtable.Cospflocallsdbentry, self).__init__()

                self.yang_name = "cospfLocalLsdbEntry"
                self.yang_parent_name = "cospfLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cospflocallsdbipaddress = YLeaf(YType.str, "cospfLocalLsdbIpAddress")

                self.cospflocallsdbaddresslessif = YLeaf(YType.int32, "cospfLocalLsdbAddressLessIf")

                self.cospflocallsdbtype = YLeaf(YType.enumeration, "cospfLocalLsdbType")

                self.cospflocallsdblsid = YLeaf(YType.str, "cospfLocalLsdbLsid")

                self.cospflocallsdbrouterid = YLeaf(YType.str, "cospfLocalLsdbRouterId")

                self.cospflocallsdbsequence = YLeaf(YType.int32, "cospfLocalLsdbSequence")

                self.cospflocallsdbage = YLeaf(YType.int32, "cospfLocalLsdbAge")

                self.cospflocallsdbchecksum = YLeaf(YType.uint32, "cospfLocalLsdbChecksum")

                self.cospflocallsdbadvertisement = YLeaf(YType.str, "cospfLocalLsdbAdvertisement")
                self._segment_path = lambda: "cospfLocalLsdbEntry" + "[cospfLocalLsdbIpAddress='" + self.cospflocallsdbipaddress.get() + "']" + "[cospfLocalLsdbAddressLessIf='" + self.cospflocallsdbaddresslessif.get() + "']" + "[cospfLocalLsdbType='" + self.cospflocallsdbtype.get() + "']" + "[cospfLocalLsdbLsid='" + self.cospflocallsdblsid.get() + "']" + "[cospfLocalLsdbRouterId='" + self.cospflocallsdbrouterid.get() + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfLocalLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.Cospflocallsdbtable.Cospflocallsdbentry, ['cospflocallsdbipaddress', 'cospflocallsdbaddresslessif', 'cospflocallsdbtype', 'cospflocallsdblsid', 'cospflocallsdbrouterid', 'cospflocallsdbsequence', 'cospflocallsdbage', 'cospflocallsdbchecksum', 'cospflocallsdbadvertisement'], name, value)

            class Cospflocallsdbtype(Enum):
                """
                Cospflocallsdbtype

                The type of the link state advertisement.

                Each link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class Cospfvirtlocallsdbtable(Entity):
        """
        The OSPF Process's Link\-Local Link State Database
        for virtual links.
        
        .. attribute:: cospfvirtlocallsdbentry
        
        	A single Link State Advertisement
        	**type**\: list of  		 :py:class:`Cospfvirtlocallsdbentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.Cospfvirtlocallsdbtable, self).__init__()

            self.yang_name = "cospfVirtLocalLsdbTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cospfVirtLocalLsdbEntry" : ("cospfvirtlocallsdbentry", CISCOOSPFMIB.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry)}

            self.cospfvirtlocallsdbentry = YList(self)
            self._segment_path = lambda: "cospfVirtLocalLsdbTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.Cospfvirtlocallsdbtable, [], name, value)


        class Cospfvirtlocallsdbentry(Entity):
            """
            A single Link State Advertisement.
            
            .. attribute:: cospfvirtlocallsdbtransitarea  <key>
            
            	The Transit Area that the Virtual Link traverses. By definition, this is not 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbneighbor  <key>
            
            	The Router ID of the Virtual Neighbor
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbtype  <key>
            
            	The type of the link state advertisement. Each  link state type has a separate advertisement format
            	**type**\:  :py:class:`Cospfvirtlocallsdbtype <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry.Cospfvirtlocallsdbtype>`
            
            .. attribute:: cospfvirtlocallsdblsid  <key>
            
            	The Link State ID is an LS Type Specific field containing a 32 bit identifier in IP address format; it identifies the piece of the routing domain that is being described by the advertisement
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbrouterid  <key>
            
            	The 32 bit number that uniquely identifies the originating router in the Autonomous System
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfvirtlocallsdbsequence
            
            	The sequence number field is a  signed  32\-bit integer. It is used to detect old and duplicate link state advertisements. The space of sequence numbers is linearly ordered. The larger the sequence number the more recent the advertisement
            	**type**\: int
            
            	**range:** \-2147483647..2147483647
            
            .. attribute:: cospfvirtlocallsdbage
            
            	This field is the age of the link state advertisement in seconds
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospfvirtlocallsdbchecksum
            
            	This field is the checksum of the complete contents of the advertisement, excepting the age field. The age field is excepted so that an advertisement's age can be incremented without updating the checksum. The checksum used is the same that is used for ISO connectionless datagrams; it is commonly referred  to as the Fletcher checksum
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfvirtlocallsdbadvertisement
            
            	The entire Link State Advertisement, including its header
            	**type**\: str
            
            	**length:** 1..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry, self).__init__()

                self.yang_name = "cospfVirtLocalLsdbEntry"
                self.yang_parent_name = "cospfVirtLocalLsdbTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cospfvirtlocallsdbtransitarea = YLeaf(YType.str, "cospfVirtLocalLsdbTransitArea")

                self.cospfvirtlocallsdbneighbor = YLeaf(YType.str, "cospfVirtLocalLsdbNeighbor")

                self.cospfvirtlocallsdbtype = YLeaf(YType.enumeration, "cospfVirtLocalLsdbType")

                self.cospfvirtlocallsdblsid = YLeaf(YType.str, "cospfVirtLocalLsdbLsid")

                self.cospfvirtlocallsdbrouterid = YLeaf(YType.str, "cospfVirtLocalLsdbRouterId")

                self.cospfvirtlocallsdbsequence = YLeaf(YType.int32, "cospfVirtLocalLsdbSequence")

                self.cospfvirtlocallsdbage = YLeaf(YType.int32, "cospfVirtLocalLsdbAge")

                self.cospfvirtlocallsdbchecksum = YLeaf(YType.uint32, "cospfVirtLocalLsdbChecksum")

                self.cospfvirtlocallsdbadvertisement = YLeaf(YType.str, "cospfVirtLocalLsdbAdvertisement")
                self._segment_path = lambda: "cospfVirtLocalLsdbEntry" + "[cospfVirtLocalLsdbTransitArea='" + self.cospfvirtlocallsdbtransitarea.get() + "']" + "[cospfVirtLocalLsdbNeighbor='" + self.cospfvirtlocallsdbneighbor.get() + "']" + "[cospfVirtLocalLsdbType='" + self.cospfvirtlocallsdbtype.get() + "']" + "[cospfVirtLocalLsdbLsid='" + self.cospfvirtlocallsdblsid.get() + "']" + "[cospfVirtLocalLsdbRouterId='" + self.cospfvirtlocallsdbrouterid.get() + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfVirtLocalLsdbTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.Cospfvirtlocallsdbtable.Cospfvirtlocallsdbentry, ['cospfvirtlocallsdbtransitarea', 'cospfvirtlocallsdbneighbor', 'cospfvirtlocallsdbtype', 'cospfvirtlocallsdblsid', 'cospfvirtlocallsdbrouterid', 'cospfvirtlocallsdbsequence', 'cospfvirtlocallsdbage', 'cospfvirtlocallsdbchecksum', 'cospfvirtlocallsdbadvertisement'], name, value)

            class Cospfvirtlocallsdbtype(Enum):
                """
                Cospfvirtlocallsdbtype

                The type of the link state advertisement.

                Each  link state type has a separate advertisement format.

                .. data:: localOpaqueLink = 9

                """

                localOpaqueLink = Enum.YLeaf(9, "localOpaqueLink")



    class Cospfshamlinknbrtable(Entity):
        """
        A table of sham link neighbor information.
        
        .. attribute:: cospfshamlinknbrentry
        
        	Sham link neighbor information
        	**type**\: list of  		 :py:class:`Cospfshamlinknbrentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinknbrtable.Cospfshamlinknbrentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.Cospfshamlinknbrtable, self).__init__()

            self.yang_name = "cospfShamLinkNbrTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cospfShamLinkNbrEntry" : ("cospfshamlinknbrentry", CISCOOSPFMIB.Cospfshamlinknbrtable.Cospfshamlinknbrentry)}

            self.cospfshamlinknbrentry = YList(self)
            self._segment_path = lambda: "cospfShamLinkNbrTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.Cospfshamlinknbrtable, [], name, value)


        class Cospfshamlinknbrentry(Entity):
            """
            Sham link neighbor information.
            
            .. attribute:: cospfshamlinkslocalipaddrtype  <key>
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinkslocalipaddr  <key>
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cospfshamlinkslocalipaddr <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinkstable.Cospfshamlinksentry>`
            
            .. attribute:: cospfshamlinknbrarea  <key>
            
            	The area to which the sham link is part of
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbripaddrtype  <key>
            
            	The type of internet address of this sham link neighbor's IP address
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinknbripaddr  <key>
            
            	The IP address this sham link neighbor is using
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinknbrrtrid
            
            	A 32\-bit integer uniquely identifying the neighboring router
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinknbroptions
            
            	A Bit Mask corresponding to the neighbor's options field.  Bit 1, if set, indicates that the  system  will operate  on  Type of Service metrics other than TOS 0.  If zero, the neighbor will  ignore  all metrics except the TOS 0 metric.  Bit 2, if set, indicates  that  the  system  is Network  Multicast  capable; ie, that it implements  OSPF Multicast Routing
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: cospfshamlinknbrstate
            
            	The state of this sham link neighbor relation\- ship
            	**type**\:  :py:class:`Cospfshamlinknbrstate <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinknbrtable.Cospfshamlinknbrentry.Cospfshamlinknbrstate>`
            
            .. attribute:: cospfshamlinknbrevents
            
            	The number of  times  this sham link has changed state or an error has occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbrlsretransqlen
            
            	The  current  length  of  the   retransmission queue. The retransmission queue is maintained for LSAs that have been flooded but not acknowledged on this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinknbrhellosuppressed
            
            	Indicates whether Hellos are being  suppressed to the neighbor
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.Cospfshamlinknbrtable.Cospfshamlinknbrentry, self).__init__()

                self.yang_name = "cospfShamLinkNbrEntry"
                self.yang_parent_name = "cospfShamLinkNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cospfshamlinkslocalipaddrtype = YLeaf(YType.enumeration, "cospfShamLinksLocalIpAddrType")

                self.cospfshamlinkslocalipaddr = YLeaf(YType.str, "cospfShamLinksLocalIpAddr")

                self.cospfshamlinknbrarea = YLeaf(YType.str, "cospfShamLinkNbrArea")

                self.cospfshamlinknbripaddrtype = YLeaf(YType.enumeration, "cospfShamLinkNbrIpAddrType")

                self.cospfshamlinknbripaddr = YLeaf(YType.str, "cospfShamLinkNbrIpAddr")

                self.cospfshamlinknbrrtrid = YLeaf(YType.str, "cospfShamLinkNbrRtrId")

                self.cospfshamlinknbroptions = YLeaf(YType.int32, "cospfShamLinkNbrOptions")

                self.cospfshamlinknbrstate = YLeaf(YType.enumeration, "cospfShamLinkNbrState")

                self.cospfshamlinknbrevents = YLeaf(YType.uint32, "cospfShamLinkNbrEvents")

                self.cospfshamlinknbrlsretransqlen = YLeaf(YType.uint32, "cospfShamLinkNbrLsRetransQLen")

                self.cospfshamlinknbrhellosuppressed = YLeaf(YType.boolean, "cospfShamLinkNbrHelloSuppressed")
                self._segment_path = lambda: "cospfShamLinkNbrEntry" + "[cospfShamLinksLocalIpAddrType='" + self.cospfshamlinkslocalipaddrtype.get() + "']" + "[cospfShamLinksLocalIpAddr='" + self.cospfshamlinkslocalipaddr.get() + "']" + "[cospfShamLinkNbrArea='" + self.cospfshamlinknbrarea.get() + "']" + "[cospfShamLinkNbrIpAddrType='" + self.cospfshamlinknbripaddrtype.get() + "']" + "[cospfShamLinkNbrIpAddr='" + self.cospfshamlinknbripaddr.get() + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinkNbrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.Cospfshamlinknbrtable.Cospfshamlinknbrentry, ['cospfshamlinkslocalipaddrtype', 'cospfshamlinkslocalipaddr', 'cospfshamlinknbrarea', 'cospfshamlinknbripaddrtype', 'cospfshamlinknbripaddr', 'cospfshamlinknbrrtrid', 'cospfshamlinknbroptions', 'cospfshamlinknbrstate', 'cospfshamlinknbrevents', 'cospfshamlinknbrlsretransqlen', 'cospfshamlinknbrhellosuppressed'], name, value)

            class Cospfshamlinknbrstate(Enum):
                """
                Cospfshamlinknbrstate

                The state of this sham link neighbor relation\-

                ship.

                .. data:: down = 1

                .. data:: attempt = 2

                .. data:: init = 3

                .. data:: twoWay = 4

                .. data:: exchangeStart = 5

                .. data:: exchange = 6

                .. data:: loading = 7

                .. data:: full = 8

                """

                down = Enum.YLeaf(1, "down")

                attempt = Enum.YLeaf(2, "attempt")

                init = Enum.YLeaf(3, "init")

                twoWay = Enum.YLeaf(4, "twoWay")

                exchangeStart = Enum.YLeaf(5, "exchangeStart")

                exchange = Enum.YLeaf(6, "exchange")

                loading = Enum.YLeaf(7, "loading")

                full = Enum.YLeaf(8, "full")



    class Cospfshamlinkstable(Entity):
        """
        Information about this router's sham links.
        
        .. attribute:: cospfshamlinksentry
        
        	Information about a single sham link
        	**type**\: list of  		 :py:class:`Cospfshamlinksentry <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinkstable.Cospfshamlinksentry>`
        
        

        """

        _prefix = 'CISCO-OSPF-MIB'
        _revision = '2003-07-18'

        def __init__(self):
            super(CISCOOSPFMIB.Cospfshamlinkstable, self).__init__()

            self.yang_name = "cospfShamLinksTable"
            self.yang_parent_name = "CISCO-OSPF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cospfShamLinksEntry" : ("cospfshamlinksentry", CISCOOSPFMIB.Cospfshamlinkstable.Cospfshamlinksentry)}

            self.cospfshamlinksentry = YList(self)
            self._segment_path = lambda: "cospfShamLinksTable"
            self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOOSPFMIB.Cospfshamlinkstable, [], name, value)


        class Cospfshamlinksentry(Entity):
            """
            Information about a single sham link.
            
            .. attribute:: cospfshamlinksareaid  <key>
            
            	The area that this sham link is part of
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cospfshamlinkslocalipaddrtype  <key>
            
            	The type of internet address of this sham link's local IP address
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinkslocalipaddr  <key>
            
            	The Local IP address of the sham link
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksremoteipaddrtype  <key>
            
            	The type of internet address of this sham link's remote IP address
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cospfshamlinksremoteipaddr  <key>
            
            	The IP address of the other end router of the sham link
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cospfshamlinksretransinterval
            
            	The number of seconds between  link\-state  advertisement retransmissions, for adjacencies belonging to this link. This value is also used when retransmitting database  description and link\-state request packets. This value should be well over the expected round trip time
            	**type**\: int
            
            	**range:** 0..3600
            
            .. attribute:: cospfshamlinkshellointerval
            
            	The length of time, in  seconds,  between  the Hello  packets that the router sends on the sham link
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: cospfshamlinksrtrdeadinterval
            
            	The number of seconds that  a  router's  Hello packets  have  not been seen before it's neighbors declare the router down.  This  should  be some  multiple  of  the  Hello  interval
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cospfshamlinksstate
            
            	OSPF sham link states
            	**type**\:  :py:class:`Cospfshamlinksstate <ydk.models.cisco_ios_xe.CISCO_OSPF_MIB.CISCOOSPFMIB.Cospfshamlinkstable.Cospfshamlinksentry.Cospfshamlinksstate>`
            
            .. attribute:: cospfshamlinksevents
            
            	The number of state changes or error events on this sham link
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cospfshamlinksmetric
            
            	The Metric to be advertised
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'CISCO-OSPF-MIB'
            _revision = '2003-07-18'

            def __init__(self):
                super(CISCOOSPFMIB.Cospfshamlinkstable.Cospfshamlinksentry, self).__init__()

                self.yang_name = "cospfShamLinksEntry"
                self.yang_parent_name = "cospfShamLinksTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cospfshamlinksareaid = YLeaf(YType.str, "cospfShamLinksAreaId")

                self.cospfshamlinkslocalipaddrtype = YLeaf(YType.enumeration, "cospfShamLinksLocalIpAddrType")

                self.cospfshamlinkslocalipaddr = YLeaf(YType.str, "cospfShamLinksLocalIpAddr")

                self.cospfshamlinksremoteipaddrtype = YLeaf(YType.enumeration, "cospfShamLinksRemoteIpAddrType")

                self.cospfshamlinksremoteipaddr = YLeaf(YType.str, "cospfShamLinksRemoteIpAddr")

                self.cospfshamlinksretransinterval = YLeaf(YType.int32, "cospfShamLinksRetransInterval")

                self.cospfshamlinkshellointerval = YLeaf(YType.int32, "cospfShamLinksHelloInterval")

                self.cospfshamlinksrtrdeadinterval = YLeaf(YType.int32, "cospfShamLinksRtrDeadInterval")

                self.cospfshamlinksstate = YLeaf(YType.enumeration, "cospfShamLinksState")

                self.cospfshamlinksevents = YLeaf(YType.uint32, "cospfShamLinksEvents")

                self.cospfshamlinksmetric = YLeaf(YType.int32, "cospfShamLinksMetric")
                self._segment_path = lambda: "cospfShamLinksEntry" + "[cospfShamLinksAreaId='" + self.cospfshamlinksareaid.get() + "']" + "[cospfShamLinksLocalIpAddrType='" + self.cospfshamlinkslocalipaddrtype.get() + "']" + "[cospfShamLinksLocalIpAddr='" + self.cospfshamlinkslocalipaddr.get() + "']" + "[cospfShamLinksRemoteIpAddrType='" + self.cospfshamlinksremoteipaddrtype.get() + "']" + "[cospfShamLinksRemoteIpAddr='" + self.cospfshamlinksremoteipaddr.get() + "']"
                self._absolute_path = lambda: "CISCO-OSPF-MIB:CISCO-OSPF-MIB/cospfShamLinksTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOOSPFMIB.Cospfshamlinkstable.Cospfshamlinksentry, ['cospfshamlinksareaid', 'cospfshamlinkslocalipaddrtype', 'cospfshamlinkslocalipaddr', 'cospfshamlinksremoteipaddrtype', 'cospfshamlinksremoteipaddr', 'cospfshamlinksretransinterval', 'cospfshamlinkshellointerval', 'cospfshamlinksrtrdeadinterval', 'cospfshamlinksstate', 'cospfshamlinksevents', 'cospfshamlinksmetric'], name, value)

            class Cospfshamlinksstate(Enum):
                """
                Cospfshamlinksstate

                OSPF sham link states.

                .. data:: down = 1

                .. data:: pointToPoint = 4

                """

                down = Enum.YLeaf(1, "down")

                pointToPoint = Enum.YLeaf(4, "pointToPoint")


    def clone_ptr(self):
        self._top_entity = CISCOOSPFMIB()
        return self._top_entity

