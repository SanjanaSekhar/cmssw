#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPETemplateReco.h"
#include "RecoLocalTracker/Records/interface/TkPixelCPERecord.h"
#include "RecoLocalTracker/ClusterParameterEstimator/interface/PixelClusterParameterEstimator.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/ModuleFactory.h"
#include "FWCore/Framework/interface/ESProducer.h"

#include "PhysicsTools/TensorFlow//interface/TfGraphRecord.h"
#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"
#include "PhysicsTools/TensorFlow/interface/TfGraphDefWrapper.h"
#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPENNReco.h"


#include <string>
#include <memory>

class PixelCPENNRecoESProducer : public edm::ESProducer {
public:
  PixelCPENNRecoESProducer(const edm::ParameterSet& p);
  ~PixelCPENNRecoESProducer() override;
  std::unique_ptr<PixelClusterParameterEstimator> produce(const TkPixelCPERecord& );
  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

private:
  edm::ESGetToken<MagneticField, IdealMagneticFieldRecord> magfieldToken_;
  edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> pDDToken_;
  edm::ESGetToken<TrackerTopology, TrackerTopologyRcd> hTTToken_;
  edm::ESGetToken<SiPixelLorentzAngle, SiPixelLorentzAngleRcd> lorentzAngleToken_;
  edm::ESGetToken<SiPixelTemplateDBObject, SiPixelTemplateDBObjectESProducerRcd> templateDBobjectToken_;
  std::string tfDnnLabel_;
  edm::ESGetToken<TfGraphDefWrapper, TfGraphRecord> tfDnnToken_;
  
  //const tensorflow::Session *tfSession_;


  edm::ParameterSet pset_;
  bool doLorentzFromAlignment_;
  bool useLAFromDB_;

  //const std::string filename_;
};

using namespace edm;

PixelCPENNRecoESProducer::PixelCPENNRecoESProducer(const edm::ParameterSet& p) {
//  tfDnnToken_(esConsumes(edm::ESInputTag("", tfDnnLabel_))) {
  std::string myname = p.getParameter<std::string>("ComponentName");
  tfDnnLabel_ = p.getParameter<std::string>("tfDnnLabel");
  //filename_ = p.getParameter<std::string>("FileName");
  
  useLAFromDB_ = p.getParameter<bool>("useLAFromDB");
  doLorentzFromAlignment_ = p.getParameter<bool>("doLorentzFromAlignment");

  pset_ = p;
  auto c = setWhatProduced(this, myname);
  magfieldToken_ = c.consumes();
  pDDToken_ = c.consumes();
  hTTToken_ = c.consumes();
  templateDBobjectToken_ = c.consumes();

  tfDnnToken_ = c.consumes(edm::ESInputTag("", tfDnnLabel_));

  if (useLAFromDB_ || doLorentzFromAlignment_) {
    char const* laLabel = doLorentzFromAlignment_ ? "fromAlignment" : "";
    lorentzAngleToken_ = c.consumes(edm::ESInputTag("", laLabel));
  }
}

PixelCPENNRecoESProducer::~PixelCPENNRecoESProducer() {}

std::unique_ptr<PixelClusterParameterEstimator> PixelCPENNRecoESProducer::produce(
    const TkPixelCPERecord& iRecord) {
  // Normal, default LA is used in case of template failure, load it unless
  // turned off
  // if turned off, null is ok, becomes zero
  //auto* graph = tensorflow::loadGraphDef(filename_);

  //const SiPixelLorentzAngle* lorentzAngleProduct = nullptr;
  //if (useLAFromDB_ || doLorentzFromAlignment_) {
  //  lorentzAngleProduct = &iRecord.get(lorentzAngleToken_);
  //}

  return std::make_unique<PixelCPENNReco>(pset_,
                                               // &iRecord.get(magfieldToken_),
                                                iRecord.get(pDDToken_),
                                                iRecord.get(hTTToken_),
                                                //lorentzAngleProduct,
                                                //&iRecord.get(templateDBobjectToken_),
                                                iRecord.get(tfDnnToken_).getSession());
}

void PixelCPENNRecoESProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  edm::ParameterSetDescription desc;

  // from PixelCPEBase
  PixelCPEBase::fillPSetDescription(desc);

  // from PixelCPETemplateReco
  PixelCPETemplateReco::fillPSetDescription(desc);

  // specific to PixelCPENNRecoESProducer
  desc.add<std::string>("ComponentName", "PixelCPENNReco");
  desc.add<std::string>("tfDnnLabel", "tracksterSelectionTf");

  //desc.add<std::string>("FileName","/uscms_data/d3/ssekhar/CMSSW_11_1_2/src/TrackerStuff/PixelHitsCNN/data/graph_x_1dcnn_p1_2024_by25k_irrad_BPIXL1_022122.pb");

  descriptions.add("_templates_NN_default",desc);
}

DEFINE_FWK_EVENTSETUP_MODULE(PixelCPENNRecoESProducer);
