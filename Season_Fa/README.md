# 🐸 Population Modeling of *Plectrohyla sagorum*  
*A Hamiltonian & Geo-statistical Approach*

---

## 📖 Overview

This repository contains the implementation of a **novel statistical mechanics-based approach** for studying **population dynamics** of individuals in ecology across different seasons of the year.  

We apply our method to the case of the vulnerable amphibian **_Plectrohyla sagorum_** ([IUCN, 2020](https://www.iucnredlist.org/species/55853/54352590)), a stream-breeding frog inhabiting the **cloud forests of the Tacaná Volcano Biosphere Reserve, Chiapas, Mexico**.

Our approach combines:

- ⚛️ **Hamiltonian framework from physics** (kinetic + potential terms)  
- 🌍 **Geo-statistics** and **Markov Random Fields (MRF)**  
- 🧮 **Approximate minimization problems** inspired by statistical mechanics  

This fusion allows us to generate **probability distributions of individuals** across seasons, reflecting ecological processes such as spreading during rainy seasons and attraction to streams during the dry season.  

---

## 🧪 Methodology Highlights

- Individuals’ distribution is modeled as a balance between:
  - **Kinetic term** → spreading across the region  
  - **Potential term** → attraction to water bodies  

- The **Hamiltonian minimization** provides equilibrium states that balance both tendencies.  
- **Markov Random Fields** ensure spatial consistency across neighboring regions.  
- **Coupling constants** are fitted from field data (frog counts and locations).  

This yields **probability distributions** of frog abundance per location, reconstructed across seasons.  

---

## 🐸 Biological Case Study  

- **Species**: *Plectrohyla sagorum*  
- **Habitat**: Canyon stream within cloud forest, Tacaná Volcano Biosphere Reserve, Chiapas, Mexico.  
- **Key ecological insights**:  
  - In the **dry season (winter)** → frogs cluster near streams.  
  - In the **rainy season** → frogs disperse farther away from the river.  

---

---

## 📂 Repository Summary

<details>
<summary>Click to expand</summary>

The repository reflects the **seasonal and spatial segmentation** of the study.  

- **Seasons**:  
  - `Season_Fa` → Fall  
  - `Season_Sp` → Spring  
  - `Season_Su` → Summer  
  - `Season_Wi` → Winter  

- **Regions**:  
  Each season is further divided into four subdirectories:  
  `Season_X_Region_1` through `Season_X_Region_4` (where `X` is Fa, Sp, Su, Wi).  
  Each region contains:  
  - A **C source file** (e.g., `Season_Fa_r1E3gs.c`)  
  - A **compiled executable** (e.g., `Season_Fa_r1E3gs`)  
  These implement the Gibbs sampling routines for stochastic predictions.  

- **Parent directory contents**:  
  - `Centroides-Elevacion_QGIS.csv` → Grid coordinates & elevations  
  - `Neighborhood_Structure/` → Adjacency lists defining neighborhood structure  
  - `parameters.csv` → Simulation parameters (population size `K`, coupling constant `g`, system temperature)  
  - `Compile_all_c.sh`, `Execute_all_c.sh` → Shell scripts to compile & run all simulations  

- **Running simulations**:  
  1. Navigate to a specific region (e.g., `Season_Fa_Region_1_Gibbs_Sampling/`).  
  2. Run the binary (e.g., `./Season_Fa_r1E3gs <tag>`).  
     - The `<tag>` is appended to output filenames.  
  3. Simulation outputs:  
     - `*_x` → final state vector  
     - `*_p` → ergodic average (expected value, for heat maps)  
     - `*_e` → energy values (Hamiltonian) per iteration  

- **Post-processing**:  
  - `Join_by_ID.py` → Reconstructs full dataset across all regions into  
    - `Data_Frame_Full_<Season>.csv` (QGIS-ready CSV)  
    - `Grid_Full_<Season>.gpkg` (GeoPackage for direct GIS visualization)  
  - `Run_N_Times.sh` → Batch runs across regions  
  - `Stats.py` → Computes summary statistics from simulation results  

Maintaining the provided folder structure is **essential**, as relative paths in the source code are hardcoded.

</details>

