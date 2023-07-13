## Obtaining Population-Specific SFS from empirical datasets.

This workflow calculates geographically stratified SFS from:

1. The 1000 Genomes NYGC High Coverage Data
2. The gnomAD v3 sequencing data

### Configuring the workflow

To configure the workflow please look at the example `config.yaml` and the population definitions file in `data/`

You can then adapt the sample-sizes and appropriate population labels to your own specific interests.

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
