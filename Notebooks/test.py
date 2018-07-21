"""
"""
from __future__ import absolute_import, print_function
import numpy
import os
from lsst.sims.utils import ObservationMetaData
from lsst.sims.catUtils.baseCatalogModels import OpSim3_61DBObject
from lsst.sims.catUtils.exampleCatalogDefinitions import PhoSimCatalogSN
from twinklesCatalogDefs import TwinklesCatalogSN, TwinklesCatalogZPoint
from lsst.sims.catalogs.db import CatalogDBObject
from lsst.sims.catUtils.baseCatalogModels import SNDBObj
from lsst.sims.catalogs.db import fileDBObject
from lsst.sims.catUtils.utils import ObservationMetaDataGenerator

dbName = 'DC2_Run1p1_SN.db'
    
if os.path.exists(dbName):
    os.unlink(dbName)

class SNDB(fileDBOject)
    
sndb = fileDBObject('hostedSN.csv', runtable='SNwHosts', database=dbName,
                    idColKey='id')
sndb.columns = [('raJ2000', 'snra*PI()/180.'),
               ('decJ2000', 'sndec*PI()/180.'),
               ('t0', 't0'),
               ('x0', 'x0'),
               ('x1', 'x1'),
               ('c', 'c'),
               ('snid', 'snid'),
               ('redshift', 'z')]
query = 'select snra from SNwHosts LIMIT 5'
results = sndb.execute_arbitrary(query)
for line in results:
    print(line)
print(sndb.column
print(sndb.database)
print(sndb.table)
opsimdb = '/Users/rbiswas/data/LSST/OpSimData/minion_1016_sqlite.db'
obs_gen = ObservationMetaDataGenerator(database=opsimdb, driver='sqlite')
obsmd = obs_gen.getObservationMetaData(obsHistID=230,
                                       boundType='circle',
                                       boundLength=3.0)[0]
print(obsmd)
# obs_metadata = obs_list[0]
# print(obs_metadata)
# exit()
snphosim = TwinklesCatalogSN(db_obj=sndb, obs_metadata=obsmd)
snphosim.write_catalog('phosim_instance.dat',  chunk_size=10000)





#33#class SNObj(SNDBObj, CatalogDBObject):
#33#    host = None
#33#    port = None
#33#    tableid = 'sn_cache_table'
#33#    driver = 'sqlite'
#33#
#33#    def query_columns(self, *args, **kwargs):
#33#        return CatalogDBObject.query_columns(self, *args, **kwargs)
#33#
#33#class DC21p1CatalogSN(TwinklesCatalogSN):
#33#
#33#    def get_shorterFileNames(self):
#33#        fnames = self.column_by_name('sedFilepath')
#33#        sep = 'Dynamic/specFile_'
#33#        split_names = []
#33#        for fname in fnames:
#33#            if 'None' not in fname:
#33#                fname = sep + fname.split(sep)[-1] 
#33#            else:
#33#                fname = 'None'
#33#            split_names.append(fname)
#33#        return np.array(split_names)
#33#    
#33#        # column_outputs = PhoSimCatalogSN.column_outputs
#33#        # column_outputs[PhoSimCatalogSN.column_outputs.index('sedFilepath')] = \
#33#        #    'shorterFileNames'
#33#        column_outputs = ['prefix', 'uniqueId', 'raPhoSim', 'decPhoSim',
#33#                          'phoSimMagNorm', 'shorterFileNames', 'redshift',
#33#                          'shear1', 'shear2', 'kappa', 'raOffset', 'decOffset',
#33#                          'spatialmodel', 'internalExtinctionModel',
#33#                          'galacticExtinctionModel', 'galacticAv', 'galacticRv']
#33#        cannot_be_null = ['x0', 't0', 'z', 'shorterFileNames']
#33#
#33#
#33#
#33#
#33#phosimSN = DC21p1CatalogSN(sndb, obs_metadata=obs_list[0]) 
#33#phosimSN.write_catalog("phoSim_example.txt", write_mode='w', write_header=True,
#33#                       chunk_size=20000)
#33#    
#33#    
