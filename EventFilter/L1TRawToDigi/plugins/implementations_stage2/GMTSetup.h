#ifndef L1T_PACKER_STAGE2_GMTSETUP_H
#define L1T_PACKER_STAGE2_GMTSETUP_H

#include "EventFilter/L1TRawToDigi/interface/Packer.h"
#include "EventFilter/L1TRawToDigi/interface/Unpacker.h"

#include "EventFilter/L1TRawToDigi/interface/PackingSetup.h"

#include "GMTCollections.h"
#include "GMTTokens.h"

namespace l1t {
   namespace stage2 {
      class GMTSetup : public PackingSetup {
         public:
            std::unique_ptr<PackerTokens> registerConsumes(const edm::ParameterSet& cfg, edm::ConsumesCollector& cc) override;
            void fillDescription(edm::ParameterSetDescription& desc) override;
            PackerMap getPackers(int fed, unsigned int fw) override;
            void registerProducts(edm::stream::EDProducerBase& prod) override;
            std::unique_ptr<UnpackerCollections> getCollections(edm::Event& e) override;
            UnpackerMap getUnpackers(int fed, int board, int amc, unsigned int fw) override;
      };
   }
}

#endif