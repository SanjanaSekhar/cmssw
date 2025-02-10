import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SiPixelRecHits._templates_NN_default_cfi import _templates_NN_default
templates = _templates_NN_default.clone()

#from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer 

# ====================================
# Graphs for X inference
# ====================================


from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer_x
L1U_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L1U_x",
    FileName = "graphs/graph_x_L1_U.pb"
)

L1F_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L1F_x",
    #FileName = "/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_1dcnn_p1_2024_BPIX_L1F_d21901_d22100_030524.pb"
    FileName = "graphs/graph_x_L1_U.pb" # need to change this
)

L2new_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L2new_x",
    FileName = "graphs/graph_x_L2new.pb"
)

L2old_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L2old_x",
    FileName = "graphs/graph_x_L2old.pb"
)
L3m_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L3m_x",
    FileName = "graphs/graph_x_L3m.pb"
)

L3p_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L3p_x",
    FileName = "graphs/graph_x_L3m.pb" # need to change this
)

L4m_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L4m_x",
    FileName = "graphs/graph_x_L4m.pb"
)

L4p_x = _tfGraphDefProducer_x.clone(
    ComponentName = "L4p_x",
    FileName = "graphs/graph_x_L4p.pb"
)

# ====================================
# Graphs for Y inference
# ====================================


from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer_y
L1U_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L1U_y",
    FileName = "graphs/graph_y_L1_U.pb"
)

L1F_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L1F_y",
    # FileName = "/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_1dcnn_p1_2024_BPIX_L1F_d21901_d22100_030524.pb"
    FileName = "graphs/graph_y_L1_U.pb"
)
L2new_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L2new_y",
    FileName = "graphs/graph_y_L2new.pb"
)

L2old_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L2old_y",
    FileName = "graphs/graph_y_L2old.pb"
)

L3m_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L3m_y",
    FileName = "graphs/graph_y_L3m.pb"
)

L3p_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L3p_y",
    FileName = "graphs/graph_y_L3p.pb"
)

L4m_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L4m_y",
    FileName = "graphs/graph_y_L4m.pb"
)

L4p_y = _tfGraphDefProducer_y.clone(
    ComponentName = "L4p_y",
    FileName = "graphs/graph_y_L4p.pb"
)

# NNCPE_x = _tfGraphDefProducer.clone(
#     ComponentNames = cms.vstring("L1U_x","L1F_x","L2old_x","L2new_x","L3m_x","L3p_x","L4m_x","L4p_x"),
#     tensorflowGraphs = cms.VPSet(
#         cms.PSet(
#             name = cms.string("L1U_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_1dcnn_p1_2024_BPIX_L1U_d21601_d21800_030524.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L1F_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_1dcnn_p1_2024_BPIX_L1F_d21901_d22100_030524.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L2old_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_L2old.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L2new_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_L2new.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L3m_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_L3m.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L3p_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_L3m.pb") #need to change this!
#         ),
#         cms.PSet(
#             name = cms.string("L4m_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_L4m.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L4p_x"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_x_L4p.pb")
#         ),
#     )
# )

# ====================================
# Graphs for Y inference
# ====================================

# NNCPE_y = _tfGraphDefProducer.clone(
#     ComponentNames = cms.vstring("L1U_y","L1F_y","L2old_y","L2new_y","L3m_y","L3p_y","L4m_y","L4p_y"),
#     tensorflowGraphs = cms.VPSet(
#         cms.PSet(
#             name = cms.string("L1U_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_1dcnn_p1_2024_BPIX_L1U_d21601_d21800_030524.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L1F_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_1dcnn_p1_2024_BPIX_L1F_d21901_d22100_030524.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L2old_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_L2old.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L2new_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_L2new.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L3m_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_L3m.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L3p_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_L3m.pb") #need to change this!
#         ),
#         cms.PSet(
#             name = cms.string("L4m_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_L4m.pb")
#         ),
#         cms.PSet(
#             name = cms.string("L4p_y"),
#             graphPath = cms.string("/uscms_data/d1/ssekhar/CMSSW_14_0_1/src/graphs/graph_y_L4p.pb")
#         ),
#     )
# )
    


