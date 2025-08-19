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

## 📐 Mathematical Method

The simulation is based on a **lattice model with local interactions**, inspired by methods from statistical mechanics.

- The study region is discretized into a **grid of sites**, each representing a spatial unit.
- Each site is assigned a **state variable**, which evolves according to:
  - **Local rules** depending on the site’s attributes, and
  - **Neighborhood interactions** defined by adjacency relations.

Formally, the system configuration is represented by a vector:

$$
\omega = (\omega_{i,j})_{(i,j) \in \Lambda},
$$

where $\omega_{i,j}$ is the average numbers of frogs in cell $(i,j)$ and $\Lambda$ is the grid of all cells.  

The **energy functional** (Hamiltonian) is defined as:

$$
H(\omega) = H_0(\omega) + V_g(\omega),
$$

where

$$
H_0(\omega) = \sum_{\ell \sim \jmath} (\omega_\ell - \omega_\jmath)^2
$$

represents local differences between neighboring cells (with $\ell \sim \jmath$ indicating neighbors), and

$$
V_g(\omega) = g \sum_{\ell \in \Lambda} d_\ell^2 \, \omega_\ell
$$

is a potential term representing the attraction to specific features (e.g., rivers), with $d_\ell$ the distance of cell $\ell$ to the feature and $g$ a coupling constant.

The **probability of a configuration** is given by the Gibbs distribution:

$$
\pi(\omega) = \frac{1}{Z} \exp\Big(-\frac{1}{T} H(\omega)\Big),
$$

where $T$ is a temperature parameter and $Z$ is the partition function:

$$
Z = \sum_{\omega \in \Omega} \exp\Big(-\frac{1}{T} H(\omega)\Big).
$$

---

### 🗂 Conditional Probabilities per Region and Season

TThe grid is divided by the river into regions $\Lambda_1, \Lambda_2, \Lambda_3, \Lambda_4$, with corresponding configuration spaces $\Omega^i$. For each region $i$ and season $x \in \{\rm Sp, Su, Fa, Wi\}$:

Hamiltonian per region and season:

$$
H_0^{(i,x)}(\omega) = \sum_{s_1 \sim s_2} (\omega_{s_1} - \omega_{s_2})^2 + \sum_{s \sim r,  r \in R} (\omega_s - \boldsymbol{\omega}^x_r)^2
$$

$$
V_{g^{(i,x)}}^{(i,x)}(\omega) = g^{(i,x)} \sum_{s \in \Lambda^i} d_s^2 , \omega_s
$$

$$
H^{(i,x)}(\omega) = H_0^{(i,x)}(\omega) + V_{g^{(i,x)}}^{(i,x)}(\omega)
$$

where $\boldsymbol{\omega}^x_r$ is the observed (or Poisson-simulated) number of individuals on the river cell $r$ for season $x$, and $g^{(i,x)}$ is the region- and season-specific coupling constant.

Conditional probability of a configuration in region $i$ given river data:

$$
\pi^{(i,x)}(\omega) = \frac{1}{Z^{(i,x)}} \exp\Big(-\frac{1}{T} H^{(i,x)}(\omega)\Big)
$$

with partition function

$$
Z^{(i,x)} = \sum_{\omega \in \Omega^i} \exp\Big(-\frac{1}{T} H^{(i,x)}(\omega)\Big)
$$


---

### 🔄 Stochastic Simulation (Gibbs Sampling)

A **Gibbs sampling sequence** is generated to approximate the equilibrium distribution:

1. Start from an initial configuration $\omega^{(0;i,x)} = 0$ for all $p \in \Lambda^i$.
2. For each site $\ell_n$ in a fixed neighbor-order sequence, propose a new state $\tilde{\omega}_{\ell_n} \in \{0,1,\dots,K^x\}$.
3. Accept the proposal with probability:

$$
P = \min\Bigg(1, \frac{\pi^{(i,x)}(\tilde{\omega})}{\pi^{(i,x)}(\omega^{(n-1;i,x)})}\Bigg)
= \min\Bigg(1, \exp\Big(-\frac{1}{T} \big[ H^{(i,x)}(\tilde{\omega}) - H^{(i,x)}(\omega^{(n-1;i,x)}) \big] \Big)\Bigg).
$$

4. Repeat for all sites and iterate until convergence.

This procedure guarantees convergence to the **conditional stationary distribution** under standard conditions (aperiodicity and irreducibility).

---

### 📊 Outputs

- **Final state vector** $(\omega^{(n;i,x)})$: One realization of the system.
- **Ergodic averages**: Expectation values used to reconstruct abundance distributions.
- **Energy traces**: Diagnostic to monitor convergence.

The ergodic averages are used for the actual prediction and heat maps. 

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

