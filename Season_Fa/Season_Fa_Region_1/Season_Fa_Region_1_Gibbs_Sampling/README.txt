Core computational engine for ecological modeling using Gibbs sampling.

Source Code:
- Season_Fa_r1E3gs.c: Main C program for Gibbs sampling (Fall, Region 1)
  - Hard-coded parameters: Temperature (T) and Coupling constant (g)
  - Inputs:
    - Season_Fa_Region_1_Data/r1E3_datos.txt (initial population)
    - Neighborhood_Structure/r1_vecinos.txt (spatial adjacency)
  - Algorithm: Markov Random Field with Gibbs sampling

Executables:
- Season_Fa_r1E3gs: Run with ./Season_Fa_r1E3gs <tag>
  - <tag> differentiates output files for different runs

Utility Programs:
- Season_Fa_r1E3_energia.c: Energy-only calculations
- Season_Fa_r1E3_energia: Generates energy traces
- README.txt: Compile/run instructions

Output Files (from Season_Fa_r1E3gs):
- Season_Fa_r1E3gs_<tag>_x: Final population per grid cell
- Season_Fa_r1E3gs_<tag>_p: Expected population density per cell
- Season_Fa_r1E3gs_<tag>_e: Energy trace (Hamiltonian values)
