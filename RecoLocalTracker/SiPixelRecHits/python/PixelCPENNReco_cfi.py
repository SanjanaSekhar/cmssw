import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SiPixelRecHits._templates_NN_default_cfi import _templates_NN_default
templates = _templates_NN_default.clone()

from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer_x
NNCPE_x = _tfGraphDefProducer_x.clone(
    ComponentName = "NNCPE_x",
    FileName = "/uscms_data/d3/ssekhar/CMSSW_12_6_2/src/graph_x_1dcnn_p1_2024_by25k_irrad_BPIXL1_022122.pb"
)

from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer_y
NNCPE_y = _tfGraphDefProducer_y.clone(
    ComponentName = "NNCPE_y",
    FileName = "/uscms_data/d3/ssekhar/CMSSW_12_6_2/src/graph_y_1dcnn_p1_2024_by25k_irrad_BPIXL1_022122.pb"
)
