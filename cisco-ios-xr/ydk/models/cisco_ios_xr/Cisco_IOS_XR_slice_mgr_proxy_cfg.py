""" Cisco_IOS_XR_slice_mgr_proxy_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR slice\-mgr\-proxy package configuration.

This module contains definitions
for the following management objects\:
  node\-path\: Node act path

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NodePath(Entity):
    """
    Node act path
    
    .. attribute:: node
    
    	Node (Physical location of the node in R\_S\_I format)
    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_slice_mgr_proxy_cfg.NodePath.Node>`
    
    

    """

    _prefix = 'slice-mgr-proxy-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(NodePath, self).__init__()
        self._top_entity = None

        self.yang_name = "node-path"
        self.yang_parent_name = "Cisco-IOS-XR-slice-mgr-proxy-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {"node" : ("node", NodePath.Node)}

        self.node = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XR-slice-mgr-proxy-cfg:node-path"

    def __setattr__(self, name, value):
        self._perform_setattr(NodePath, [], name, value)


    class Node(Entity):
        """
        Node (Physical location of the node in R\_S\_I
        format)
        
        .. attribute:: node_name  <key>
        
        	Location in R\_S\_I format
        	**type**\: str
        
        .. attribute:: slice_ids
        
        	Slice
        	**type**\:  :py:class:`SliceIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_slice_mgr_proxy_cfg.NodePath.Node.SliceIds>`
        
        

        """

        _prefix = 'slice-mgr-proxy-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(NodePath.Node, self).__init__()

            self.yang_name = "node"
            self.yang_parent_name = "node-path"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"slice-ids" : ("slice_ids", NodePath.Node.SliceIds)}
            self._child_list_classes = {}

            self.node_name = YLeaf(YType.str, "node-name")

            self.slice_ids = NodePath.Node.SliceIds()
            self.slice_ids.parent = self
            self._children_name_map["slice_ids"] = "slice-ids"
            self._children_yang_names.add("slice-ids")
            self._segment_path = lambda: "node" + "[node-name='" + self.node_name.get() + "']"
            self._absolute_path = lambda: "Cisco-IOS-XR-slice-mgr-proxy-cfg:node-path/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NodePath.Node, ['node_name'], name, value)


        class SliceIds(Entity):
            """
            Slice
            
            .. attribute:: slice_id
            
            	Slice Id on which configuration will be applied
            	**type**\: list of  		 :py:class:`SliceId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_slice_mgr_proxy_cfg.NodePath.Node.SliceIds.SliceId>`
            
            

            """

            _prefix = 'slice-mgr-proxy-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(NodePath.Node.SliceIds, self).__init__()

                self.yang_name = "slice-ids"
                self.yang_parent_name = "node"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self._child_container_classes = {}
                self._child_list_classes = {"slice-id" : ("slice_id", NodePath.Node.SliceIds.SliceId)}

                self.slice_id = YList(self)
                self._segment_path = lambda: "slice-ids"

            def __setattr__(self, name, value):
                self._perform_setattr(NodePath.Node.SliceIds, [], name, value)


            class SliceId(Entity):
                """
                Slice Id on which configuration will be
                applied
                
                .. attribute:: slice_id  <key>
                
                	The identifier for this slice
                	**type**\: int
                
                	**range:** 0..4
                
                .. attribute:: state
                
                	set val 0 to shutdown
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: breakout
                
                	10G Breakout Config
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: mode
                
                	set val 4 for OTU4 
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'slice-mgr-proxy-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(NodePath.Node.SliceIds.SliceId, self).__init__()

                    self.yang_name = "slice-id"
                    self.yang_parent_name = "slice-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.slice_id = YLeaf(YType.uint32, "slice-id")

                    self.state = YLeaf(YType.int32, "state")

                    self.breakout = YLeaf(YType.int32, "breakout")

                    self.mode = YLeaf(YType.int32, "mode")
                    self._segment_path = lambda: "slice-id" + "[slice-id='" + self.slice_id.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(NodePath.Node.SliceIds.SliceId, ['slice_id', 'state', 'breakout', 'mode'], name, value)

    def clone_ptr(self):
        self._top_entity = NodePath()
        return self._top_entity

