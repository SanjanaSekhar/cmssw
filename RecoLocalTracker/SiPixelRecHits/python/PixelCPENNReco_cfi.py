import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SiPixelRecHits._templates_NN_default_cfi import _templates_NN_default
templates = _templates_NN_default.clone()

from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer_x
NNCPE_x_ = _tfGraphDefProducer_x.clone(
    NNCPE_x = cms.vstring('L1F_x','L1U_x','L2old_x','L2new_x','L3m_x','L3p_x','L4m_x','L4p_x'),
    FileName = cms.vstring("/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_1dcnn_p1_2024_BPIX_L1F_d21901_d22100_030524.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_1dcnn_p1_2024_BPIX_L1U_d21601_d21800_030524.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L2old.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L2new.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L3m.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L3m.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L4m.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L4p.pb")
)

from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer_y
NNCPE_y_ = _tfGraphDefProducer_y.clone(
    NNCPE_y = cms.vstring('L1U_y','L1F_y','L2old_y','L2new_y','L3m_y','L3p_y','L4m_y','L4p_y'),
    FileName = cms.vstring("/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_1dcnn_p1_2024_BPIX_L1F_d21901_d22100_030524.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_1dcnn_p1_2024_BPIX_L1U_d21601_d21800_030524.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L2old.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L2new.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L3m.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L3m.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L4m.pb",
                            "/uscms_data/d3/ssekhar/CMSSW_14_0_0/src/graphs/graph_x_L4p.pb")
)
