import FWCore.ParameterSet.Config as cms

from RecoLocalTracker.SiPixelRecHits._templates_NN_default_cfi import _templates_NN_default
templates = _templates_NN_default.clone()

from PhysicsTools.TensorFlow.tfGraphDefProducer_cfi import tfGraphDefProducer as _tfGraphDefProducer
tracksterSelectionTf = _tfGraphDefProducer.clone(
    ComponentName = "tracksterSelectionTf",
    FileName = "graph_x_1dcnn_p1_2024_by25k_irrad_BPIXL1_022122.pb"
)
