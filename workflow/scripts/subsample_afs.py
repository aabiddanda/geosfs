#!python3

"""Subsampling allele frequencies across populations from large catalogs."""

import numpy as np 
import pandas as pd

def resample_alleles(ac, an, min_n = 100, n=5000, seed=42):
    """Resample alleles for a given sample-size.
    
    We exclude variants where there are fewer than min_n called genotypes...
    """
    assert ac.size == an.size
    assert min_n > 1
    assert seed > 0   
    np.random.seed(seed)
    af = np.nan_to_num(ac/an)
    ac_resamp = np.random.binomial(n=n, p=af)
    af_resamp = ac_resamp / n
    ac_resamp[an < min_n] = 0
    af_resamp[an < min_n] = 0
    return ac_resamp, af_resamp


def resamp_alleles_multipop(acs, ans, props=np.array([1.0, 0.0, 0.0, 0.0, 0.0]), n=5000, seed=42):
    """Resample multipopulation alleles ..."""
    assert acs.shape[0] == ans.shape[0]
    assert acs.shape[1] == ans.shape[1]
    assert props.size == acs.shape[1]
    assert np.all(props >= 0.0)
    if ~np.isclose(np.sum(props), 1.0):
        # Rescale if necessary here ... 
        props = props / np.sum(props)

    joint_acs = np.zeros(shape=acs.shape, dtype=np.uint16)
    joint_afs = np.zeros(shape=acs.shape, dtype=np.float16)
    new_ns = np.zeros(props.size, dtype=np.uint32)
    for i in range(props.size):
        # Iterate through the populations now 
        cur_n = int(n*props[i])
        new_ns[i] = cur_n
        if cur_n < 1:
            pass
        else:
            assert cur_n > 0
            ac_pop, af_pop = resample_alleles(acs[:,i], ans[:,i], n=cur_n, seed=seed)
            joint_acs[:,i] = ac_pop
            joint_afs[:,i] = af_pop
    meta_acs = np.sum(joint_acs, axis=1)
    meta_afs = meta_acs / n
    return meta_acs, meta_afs, joint_acs, joint_afs, new_ns


if __name__ == "__main__":
    chr22_sfs_df = pd.read_csv(snakemake.input['gnomAD_jsfs'], sep="\t")
    # Any variants not called in a single population will be dropped ... 
    chr22_sfs_df[chr22_sfs_df == '.'] = np.nan
    chr22_sfs_df.dropna(subset=['AN_NFE', 'AN_EAS', 'AN_SAS', 'AN_MID', 'AN_OTH'], inplace=True)
    chr22_sfs_df
