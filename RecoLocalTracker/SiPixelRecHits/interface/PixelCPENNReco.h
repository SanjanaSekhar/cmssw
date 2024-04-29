#ifndef RecoLocalTracker_SiPixelRecHits_PixelCPENNReco_H
#define RecoLocalTracker_SiPixelRecHits_PixelCPENNReco_H

#include "RecoLocalTracker/SiPixelRecHits/interface/PixelCPEBase.h"
#include "PhysicsTools/TensorFlow/interface/TensorFlow.h"

// Already in the base class
//#include "Geometry/CommonDetUnit/interface/GeomDetType.h"
//#include "Geometry/CommonDetUnit/interface/PixelGeomDetUnit.h"
//#include "Geometry/TrackerGeometryBuilder/interface/RectangularPixelTopology.h"
//#include "Geometry/CommonDetAlgo/interface/MeasurementPoint.h"
//#include "Geometry/CommonDetAlgo/interface/MeasurementError.h"
//#include "Geometry/Surface/interface/GloballyPositioned.h"
//#include "FWCore/ParameterSet/interface/ParameterSet.h"

#ifndef SI_PIXEL_TEMPLATE_STANDALONE
#include "CondFormats/SiPixelTransient/interface/SiPixelTemplate.h"
#else
#include "SiPixelTemplate.h"
#endif

#include <utility>
#include <vector>

#if 0
/** \class PixelCPETemplateReco
 * Perform the position and error evaluation of pixel hits using
 * the Det angle to estimate the track impact angle
 */
#endif
//struct CacheData {
//  CacheData() : graphDef(nullptr) {}
//  std::atomic<tensorflow::GraphDef*> graphDef;
//};

//tensorflow::setLogging("3");
class MagneticField;
class PixelCPENNReco : public PixelCPEBase{
public:
  struct ClusterParamTemplate : ClusterParam {
    ClusterParamTemplate(const SiPixelCluster &cl) : ClusterParam(cl) {}
    // The result of PixelTemplateReco2D
    float NNXrec_;
    float NNYrec_;
    float NNSigmaX_;
    float NNSigmaY_;
    // Add new information produced by SiPixelTemplateReco::PixelTempReco2D &&&
    // These can only be accessed if we change silicon pixel data formats and add them to the rechit
    //float templProbX_;
    //float templProbY_;

    //float templProbQ_;

    //int templQbin_;
    
    int ierr;
    
    //const std::vector<tensorflow::Session *> session_x_vec;
    //const std::vector<tensorflow::Session *> session_y_vec;
  };

  // PixelCPETemplateReco( const DetUnit& det );
  PixelCPENNReco(edm::ParameterSet const &conf,
                       const MagneticField *,
                       const TrackerGeometry &,
                       const TrackerTopology &,
                       const SiPixelLorentzAngle *,
                     //  const SiPixelTemplateDBObject *,
                       const std::vector<tensorflow::Session> *,
                       const std::vector<tensorflow::Session> *
                       ) ;

  ~PixelCPENNReco() override;

  static void fillPSetDescription(edm::ParameterSetDescription &desc);
//  static std::unique_ptr<CacheData> initializeGlobalCache(const edm::ParameterSet&);
//  static void globalEndJob(const CacheData*);

private:
  std::unique_ptr<ClusterParam> createClusterParam(const SiPixelCluster &cl) const override;

  // We only need to implement measurementPosition, since localPosition() from
  // PixelCPEBase will call it and do the transformation
  // Gavril : put it back
  LocalPoint localPosition(DetParam const &theDetParam, ClusterParam &theClusterParam) const override;

  // However, we do need to implement localError().
  LocalError localError(DetParam const &theDetParam, ClusterParam &theClusterParam) const override;

  // Template storage
  std::vector<SiPixelTemplateStore> thePixelTemp_;

  int speed_;

  bool UseClusterSplitter_;

  // Template file management (when not getting the templates from the DB)
  int barrelTemplateID_;
  int forwardTemplateID_;
  std::string templateDir_;

  std::string graphPath_x, graphPath_y;
  std::string inputTensorName_x, inputTensorName_y, anglesTensorName_x, anglesTensorName_y;
  std::string outputTensorName_x, outputTensorName_y;
  //std::string     fRootFileName;

  const std::vector<tensorflow::Session> * session_x_vec; 
  const std::vector<tensorflow::Session> * session_y_vec; 
  
  //float micronsToCm = 1e-4;
  std::string cpe; 
  //int layer, ladder, module;
  //float clsize_1[MAXCLUSTER][2], clsize_2[MAXCLUSTER][2], clsize_3[MAXCLUSTER][2], clsize_4[MAXCLUSTER][2], clsize_5[MAXCLUSTER][2], clsize_6[MAXCLUSTER][2];
  //struct timeval now0, now1;
  //struct timezone timz;
  //bool DoCosmics_;
  //bool LoadTemplatesFromDB_;
};

#endif
