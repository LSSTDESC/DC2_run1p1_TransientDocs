import sys
sys.path.insert(0, '/global/common/software/lsst/common/miniconda/py3-4.2.12/lib/python3.6/site-packages')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
import subprocess
assert u'lsst' in subprocess.check_output(['groups']).decode().split(), 'You need to be in the `lsst` group for this notebook to work'
import GCRCatalogs

## check version
print('GCRCatalogs =', GCRCatalogs.__version__, '|' ,'GCR =', GCRCatalogs.GCR.__version__)


# In[7]:

gc = GCRCatalogs.load_catalog('protoDC2')


# In[8]:

protoDC2_gals = pd.DataFrame(gc.get_quantities(['galaxy_id','size_disk_true', 'size_bulge_true', 'diskMassStellar', 'totalMassStellar', 'morphology/diskMinorAxisArcsec', 'morphology/diskMinorAxisArcsec', 'morphology/spheroidMinorAxisArcsec', 'morphology/spheroidMinorAxisArcsec', 'morphology/positionAngle']))


# In[9]:

rots = pd.read_csv('/global/homes/r/rbiswas/src/DC2/examples/protoDC2_reference_works.dat', delimiter=', ')


# In[10]:

assert len(rots) == len(protoDC2_gals)


# ##  Join tables

# In[33]:

def joinTables(catSim, protoDC2Gals, commonVars='totalMassStellar'):
    """
    Parameters
    ----------
    catSim : pd.DataFrame
        dataframe with the information from the catsim instance catalog
        containing the positions and position angles after rotation
    protoDC2Gals : pd.DataFrame
        dataframe with the information from the protoDC2 Galaxy Catalog
    """
    assert len(catSim) == len(protoDC2Gals)
    catSim.reset_index().set_index('galaxy_id', inplace=True)
    protoDC2Gals.reset_index().set_index('galaxy_id', inplace=True)
    xx = protoDC2Gals.join(catSim, rsuffix='_catsim')
    y = xx['totalMassStellar'] / xx['totalMassStellar_catsim']
    assert all(np.abs(y - 1.0) < 1.0e-12)
    cols = xx.columns
    keepcols = cols
    keepcols = list(col for col in cols if '_catsim' not in col)
    return xx[keepcols]


# In[34]:

protoDC2_rotated_gals = joinTables(rots, protoDC2_gals)


# In[36]:

protoDC2_rotated_gals.columns


# In[38]:

protoDC2_rotated_gals.to_csv('protoDC2_rotated_combined.csv')


# In[40]:

protoDC2_rotated_gals.to_hdf('protoDC2_rotated_combined.hdf', compression=9, key='0')


# In[37]:

fig, ax = plt.subplots()
ax.hexbin(protoDC2_rotated_gals.raJ2000, protoDC2_rotated_gals.decJ2000)


# In[41]:

df = pd.read_hdf('protoDC2_rotated_combined.hdf')


# In[42]:

df.head()


# In[44]:

get_ipython().system('du -h protoDC2_rotated_combined.csv')


# In[ ]:



