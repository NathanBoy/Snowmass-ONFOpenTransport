import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_ServiceendpointUuid_LayerprotocolLocalidImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._serviceEndPoint:
            if localId in be.Context._serviceEndPoint[uuid]._layerProtocol:
                return be.Context._serviceEndPoint[uuid]._layerProtocol[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
