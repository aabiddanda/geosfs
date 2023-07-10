## Obtaining Population-Specific SFS from 1KG Data

This workflow calculates geographically stratified SFS from the 1000 Genomes NYGC High Coverage Data


### Configuring the workflow

To configure the workflow 

### Running the workflow

Once you have configured the workflow and created the environment using `conda` (or `mamba`). You can run:

```
mamba activate geosfs
snakemake -j <njobs> --cores <number of cores> -p -n
```
