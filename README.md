## Obtaining Population-Specific SFS from empirical datasets.

This workflow calculates geographically stratified SFS from:

1. The gnomAD v3 sequencing data


### Configuring the workflow

To configure the workflow please look at the example `config.yaml`

You can then adapt the sample-sizes and appropriate population proportions to your own specific schemes.

### Key Inference Method

For subsampling the script `workflow/scripts/subsample_afs.py` can be run as a standalone python script. Currently it is run using a snakemake pipeline for the GnomAD dataset but it is portable to run for another dataset as long as the file format is similar (and that the input files contain the same/similar headers). 

The `config.yaml` file indicates the individual subsampling experiments that we want to perform (defining total sample size and proportion of samples from each population defined in GnomAD). 


### Setup the environment

To setup the environment you can run:

```
conda env create -f env.yaml
conda activate geosfs
```

If you can, dependency management and setup using `mamba` is much faster (just replace all `conda` statements with `mamba`)

### Running the workflow

Once you have configured the workflow and created the environment using `conda` (or `mamba`). You can run:

```
mamba activate geosfs
snakemake -j <njobs> --cores <number of cores> -p -n
```
