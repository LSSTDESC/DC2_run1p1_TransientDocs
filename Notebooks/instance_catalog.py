"""
"""
from __future__ import absolute_import, print_function
import numpy
import os
from lsst.sims.utils import ObservationMetaData
from lsst.sims.catUtils.baseCatalogModels import OpSim3_61DBObject
from lsst.sims.catUtils.exampleCatalogDefinitions import PhoSimCatalogSN
from twinklesCatalogDefs import TwinklesCatalogSN, TwinklesCatalogZPoint

class DC21p1CatalogSN(TwinklesCatalogSN):

    def get_shorterFileNames(self):
        fnames = self.column_by_name('sedFilepath')
        sep = 'Dynamic/specFile_'
        split_names = []
        for fname in fnames:
            if 'None' not in fname:
                fname = sep + fname.split(sep)[-1] 
            else:
                fname = 'None'
            split_names.append(fname)
        return np.array(split_names)
    
        # column_outputs = PhoSimCatalogSN.column_outputs
        # column_outputs[PhoSimCatalogSN.column_outputs.index('sedFilepath')] = \
        #    'shorterFileNames'
        column_outputs = ['prefix', 'uniqueId', 'raPhoSim', 'decPhoSim',
                          'phoSimMagNorm', 'shorterFileNames', 'redshift',
                          'shear1', 'shear2', 'kappa', 'raOffset', 'decOffset',
                          'spatialmodel', 'internalExtinctionModel',
                          'galacticExtinctionModel', 'galacticAv', 'galacticRv']
        cannot_be_null = ['x0', 't0', 'z', 'shorterFileNames']

obsMD = OpSim3_61DBObject()
obs_list = obsMD.getObservationMetaData((53.0, -50.0), 2.0,
                                        fovRadius=0.1, makeCircBounds = True)
obs_metadata = obs_list[0]
print(obs_metadata)
phosimSN = DC21p1CatalogSN(sndb, obs_metadata=obs_list[0]) 
phosimSN.write_catalog("phoSim_example.txt",write_mode='w',write_header=True,chunk_size=20000)
exit()
#class DC2SN(object):
#    """
#    """
#    def __init__(self,
#                 obs_metadata,
#                 brightestStar_gmag_inCat=11.0,
#                 brightestGal_gmag_inCat=11.0,
#                 # availableConnections=None,
#                 sntable='SNwHosts',
#                 sn_sedfile_prefix='spectra_files/specFile_',
#                 db_config=None,
#                 cache_dir=None):
#        """
#        Parameters
#        ----------
#        obs_metadata : instance of `lsst.sims.utils.ObservationMetaData`
#            Observational MetaData associated with an OpSim Pointing
#        brightestStar_gmag_inCat : optional, float, defaults to 11.0
#            brightest star allowed in terms of its g band magnitude in
#            'ab' magsys. The reason for this constraint is to keep phosim
#            catalog generation times in check.
#        brightestGal_gmag_inCat : optional, float, defaults to 11.0
#            brightest galaxy allowed in terms of its g band magnitude in
#            'ab' magsys. The reason for this constraint is to keep phosim
#            catalog generation times in check.
#        sntable : string, optional, defaults to `TwinkSN_run3`
#            Name of the table on fatboy with the SN parameters desired. 
#        sn_sedfile_prefix : string, optional, defaults to `spectra_files/specFile_'
#            prefix for sed of the supernovae.
#        db_config : the name of a file overriding the fatboy connection information
#        cache_dir : the directory containing the source data of astrophysical objects
#        Attributes
#        ----------
#        snObj : CatalogDBObj for SN
#        available_connections : available connections
#        ..notes : 
#        """
#        #if cache_dir is None:
#        #    raise RuntimeError("Must specify cache_dir in TwinklesSky")
#
#        # Observation MetaData
#        self.obs_metadata = obs_metadata
#
#        # Constraint on the brightest star: 
#        #self.brightestStar_gmag_inCat = brightestStar_gmag_inCat
#        #self.brightestStarMag = 'gmag > {}'.format(self.brightestStar_gmag_inCat)
#
#        # Constraint on brightest galaxy
#        # self.brightestGal_gmag_inCat = brightestGal_gmag_inCat
#        # self.brightestGalMag = 'g_ab > {}'.format(self.brightestGal_gmag_inCat)
#
#        # self.availableConnections = availableConnections
#
#        # The databases of astrophysical objects
#        # gal_db_name = os.path.join(cache_dir, _galaxy_cache_db_name)
#        # star_db_name = os.path.join(cache_dir, 'star_cache.db')
#        sn_db_name = os.path.join(cache_dir, 'sn_cache.db')
#        # if not os.path.exists(gal_db_name):
#        #    raise RuntimeError("Cannot find %s" % gal_db_name)
#        #if not os.path.exists(star_db_name):
#        #    raise RuntimeError("Cannot find %s" % star_db_name)
#        #if not os.path.exists(sn_db_name):
#        #    raise RuntimeError("Cannot find %s" % sn_db_name)
#
#        # StarCacheDBObj.database = star_db_name
#        # GalaxyCacheBulgeObj.database = gal_db_name
#        # GalaxyCacheDiskObj.database = gal_db_name
#        # GalaxyCacheAgnObj.database = gal_db_name
#        SNCacheDBObj.database = sn_db_name
#
#        # Lists of component phosim Instance Catalogs and CatalogDBObjects
#        # Stars
#        # self.compoundStarDBList = [StarCacheDBObj]
#        # self.compoundStarICList = [TwinklesCatalogPoint]
#
#        # Galaxies
#        # self.compoundGalDBList = [GalaxyCacheBulgeObj, GalaxyCacheDiskObj, GalaxyCacheAgnObj]
#        # self.compoundGalICList = [TwinklesCatalogSersic2D, TwinklesCatalogSersic2D,
#         #                         TwinklesCatalogZPoint]
#
#        # SN 
#        ## SN catalogDBObject
#        # if self.availableConnections is None:
#        #    self.availableConnections = list()
#        #    self.snObj = SNCacheDBObj()
#        #    self.availableConnections.append(self.snObj.connection)
#        # else:
#        #   self.snObj = SNCacheDBObj(table=sntable, connection=self.availableConnections[0])
#        
#        self.sn_sedfile_prefix = sn_sedfile_prefix
#
#    def writePhoSimCatalog(self, fileName):
#        """
#        write the phosim instance catalogs of stars, galaxies and supernovae in
#        the Twinkles Sky to fileName
#        Parameters
#        ----------
#        fileName : string, mandatory
#            Name of the file to which the phoSim Instance Catalog will be
#            written
#        """
#        # starCat = CompoundInstanceCatalog(self.compoundStarICList,
#        #                                  self.compoundStarDBList,
#        #                                  obs_metadata=self.obs_metadata,
#        #                                  constraint=self.brightestStarMag)
#
#        # starCat._active_connections += self.availableConnections # append already open fatboy connections
#        # starCat.phoSimHeaderMap = TwinklesPhoSimHeader
#
#        # t_before_starCat = time.time()
#        # print("writing starCat ")
#        # starCat.write_catalog(fileName, chunk_size=10000)
#        # t_after_starCat = time.time()
#
#        # galCat = CompoundInstanceCatalog(self.compoundGalICList,
#        #                                 self.compoundGalDBList,
#        #                                 obs_metadata=self.obs_metadata,
#        #                                 constraint=self.brightestGalMag,
#        #                                 compoundDBclass=GalaxyCacheSprinklerObj)
#
#        # galCat._active_connections = starCat._active_connections  # pass along already open fatboy connections
#        # t_before_galCat = time.time()
#        # print("writing galCat")
#        # galCat.write_catalog(fileName, write_mode='a', chunk_size=10000,
#        #                     write_header=False)
#
#        # t_after_galCat = time.time()
#        snphosim = TwinklesCatalogSN(db_obj=self.snObj,
#                                     obs_metadata=self.obs_metadata)
#        ### Set properties
#        snphosim.writeSedFile = True
#        snphosim.suppressDimSN = True
#        snphosim.sn_sedfile_prefix = self.sn_sedfile_prefix
#        print("writing sne")
#        t_before_snCat = time.time()
#        snphosim.write_catalog(fileName, write_header=False,
#                               write_mode='a', chunk_size=10000)
#        t_after_snCat = time.time()

if __name__=='__main__':
    from lsst.sims.catalogs.db import fileDBObject
    
    
    dbName = 'DC2_Run1p1_SN.db'
    
    if os.path.exists(dbName):
        os.unlink(dbName)
    
    
    sndb = fileDBObject('hostedSN.csv', runtable='SNwHosts', database=dbName,
                         idColKey='id')
    
    query = 'select snra from SNwHosts'
    results = sndb.execute_arbitrary(query)
    for line in results:
            print(line)
