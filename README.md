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

is a potential term representing the attraction, with $d_\ell$ the distance of cell $\ell$ to the river and $g$ a coupling constant.

The **probability of a configuration** is given by the Gibbs distribution:

$$
\pi(\omega) = \frac{1}{Z} \exp\Big(-\frac{1}{T} H(\omega)\Big),
$$

where T is a temperature parameter and Z is the partition function:

$$
Z = \sum_{\omega \in \Omega} \exp\Big(-\frac{1}{T} H(\omega)\Big).
$$

---

### 🗂 Conditional Probabilities per Region and Season

TThe grid is divided by the river into regions $\Lambda_1, \Lambda_2, \Lambda_3, \Lambda_4$, with corresponding configuration spaces $\Omega^1,\Omega^2,\Omega^3,\Omega^4$. For each region $i\in \{1,2,3,4\}$, season $x \in \{\rm Sp, Su, Fa, Wi\}$ and $\omega\in \Omega^i$:


$$
H_0^{(i,x)}(\omega) = \sum_{s_1 \sim s_2} (\omega_{s_1} - \omega_{s_2})^2 +\sum_{\substack{s\sim r\\  r\in R}}(\omega_s-
\boldsymbol{\omega}^{x}_r)^2
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

## 📂 Repository Structure

<details>
<summary>Parent Directory</summary>

The parent directory contains three main components: **Geographic Data**, **Seasonal Directories**, and **Scripts**. This structure mirrors the spatial inputs, seasonal segmentation, and automation needed to run all experiments.

---

### 🌍 Geographic Data
<details>
<summary>Click to expand</summary>

This section holds the spatial inputs used by the simulations. Objects created in **QGIS** receive a **unique feature ID**, which is used across files to consistently join geometry, centroids, neighborhoods, and model outputs. Note however that there are two IDs per grid coordinate, a **Global** ID independent on the region and for each region another **Local** ID

- **Neighborhood_Structure/**  
  - One file per region (e.g., `r1_vecinos.txt` … `r4_vecinos.txt`).  
  - Each row lists **neighbor QGIS IDs** for a given cell (first-order adjacency) Here **Local IDs** are used.  
  - Used to define the first order neighborhood relation and it is used by the Gibbs sampler program. 

- **Centroides-Elevacion_QGIS.csv**  
  - Columns include: **ID**, **x**, **y**, **z**.  
  - **ID** matches the QGIS **Global** ID for each cell.  
  - Used to reconstruct spatial maps and bind results to coordinates.

- **parameters.csv**  
  List all parameters used for the simulations for each season and region. For each season there is a unique value of Temperature **T**, for maximum number of individuals on the river **K**, and density of individuales along the river **rho** and for each Season-Region pair there is a value for the coupling constant **g**
</details>

---

### 🍂🌸☀️❄️ Seasons
<details>
<summary>Click to expand</summary>

Each season directory encapsulates **inputs, code, executables, and results** for that season, split into four spatial **regions**.  
Every region includes sub-directories:
- `*_Data/` → Contains input data for the gibbs sampling.
- `*_Gibbs_Sampling/` →  Contains C source and compiled programs for Gibbs simulation.
- `*_Energy_Stabilization/` *(or `*_Stabilization/` in some regions)* → Convergence/energy plots.
- `*_Results/` → Results from the Gibbs simulation program are stored here: final states (`*_x`), ergodic means (`*_p`), energy traces (`*_e`).
- `Stats.py` → Computes summary statistics from the region’s results.
- `R?_IDs.csv` → QGIS/grid IDs for this region, used to merge outputs with coordinates.

> **Output file semantics**
> - `*_x` = final state vector (per grid cell; integer counts).
> - `*_p` = ergodic average (expected counts per cell; used for heatmaps; floating point).
> - `*_e` = Hamiltonian value by iteration (used to assess stabilization and convergence).

---

#### 🍂 Season_Fa (Fall) — `Season_Fa/`
<details>
<summary>Click to expand</summary>

High-level contents for Fall:
- `Data_Frame_Full_Fa.csv` → Region-merged outputs with grid IDs. This can be directly uploaded to Qgis as a point geometry to then create the maps.
- `Grid_Full_Fa.gpkg` → GeoPackage with full seasonal grid + attributes.
- `Join_by_ID.py`→ Joins region outputs to grid IDs to produce Data_Frame_Full_Fa.csv. This takes as input the results in Season_Fa_Region_i/Season_Fa_Region_i_Results/, the file /Season_Fa_Region_i/Ri_IDs.csv (**Local** ids), and Centroides-Elevacion_QGIS.csv from the parent directory (Geographic Data) for $i\in [1,2,3,4]$.
- `Run_N_Times.sh` → Runs N times the gibbs Sampler throughout all the regions. The results are all saved on the corresponding results directory Season_Fa_Region_i/Season_Fa_Region_i_Results/
- `README.txt` → Season-level notes.
- `Season_Fa_Maps/` → Maps generated by QGIS this are generated independently (heatmaps, styles).
- `Season_Fa_Region_1/` … `Season_Fa_Region_4/` → Region workspaces.

<details>
<summary>Season_Fa_Maps/</summary>

- `ArcoIris_Total_E3p31.png` → Rainbow palette heatmap of expected counts. Graph of main result of simulations.
- `GreyScale_Total_Fa.pgw` → World file (georeferencing) for the grayscale PNG.
- `GreyScale_Total_Fa.png` → Grayscale heatmap of expected counts.
- `IE3_p31.png` → Scatter Plot of the expected count. Each point represents an occurence. 
- `README.txt` → Layer/style notes.
</details>

<details>
<summary>Season_Fa_Region_1/</summary>

- `R1_IDs.csv` → Region 1 **Local** grid/QGIS IDs for join operations.
- `README.txt` → Region 1 notes.

<details>
<summary>Season_Fa_Region_1_Data/</summary>

- `r1E3_datos.txt` → Inputs for /Season_Fa_Region_1_Gibbs_Sampling/ programs. Contains the Poisson simulation data for the number of individuals in the River sites in Region 1 for the Fall (Fa) season. The description of the columns is as follows: The first column corresponds to row site tag in Region 1. The second column corresponds to the neighborhood class of the site according to the distance from the River (class 0 for river sites and a positive integer value in the other sites). The third column corresponds to the number of individuals of the species at the site. For River sites the number of individuals is artificially determined by a Poisson Process with intensity rho=0.31, based on field data; the number of individuals is assumed to be zero for all of the other sites.
- `README.txt` → Data dictionary.
</details>

<details>
<summary>Season_Fa_Region_1_Energy_Stabilization/</summary>

- `energia_R1E3.png` → The graph "energia_R1E3" shows the energy stabilization in Region 1 for the Fall (Fa) season, with a total of (10^6)*(M) iterations of the Gibbs Sampling, where M=9310 is the total number of sites in Region 1.
- `r1E3_energia.png` → The graph "r1E3_energia" shows energy stabilization in Fall (Fa). The graphs show the first two million iterations of the Gibbs Sampling
- `README.txt` → How to read stabilization plots.
</details>

<details>
<summary>Season_Fa_Region_1_Gibbs_Sampling/</summary>

- `Season_Fa_r1E3gs.c`→ C source for Gibbs sampling routine (R1). In the code the Temperature and Coupling constant are hard coded and to run it calls the files Season_Fa_Region_1_Data/r1E3_datos.txt and Neighborhood_Structure/r1_vecinos.txt
- `Season_Fa_r1E3gs` → **Executable**; run as: `./Season_Fa_r1E3gs <tag>`
  - `<tag>` is appended to output basenames to keep runs separate.
- `Season_Fa_r1E3_energia.c` → Energy-only utility.
- `Season_Fa_r1E3_energia` → **Executable** to regenerate energy traces.
- `README.txt` → Compile/run notes and parameter hints.

> **Typical outputs created by `Season_Fa_r1E3gs`**
> - `Season_Fa_r1E3gs_<tag>_x` → Final state vector.
> - `Season_Fa_r1E3gs_<tag>_p` → Ergodic mean.
> - `Season_Fa_r1E3gs_<tag>_e` → Energy per iteration.
</details>

- `Season_Fa_Region_1_Results/` → **(~2k files)** All `_x`, `_p`, `_e` artifacts for different tags/seeds.
- `Stats.py`, `Stats.py~` → Summaries over `_p` and stabilization diagnostics.

</details>

<details>
<summary>Season_Fa_Region_2/</summary>

- `R2_IDs.csv` → Region 2 grid/QGIS IDs.
- `README.txt` → Region 2 notes.

<details>
<summary>Season_Fa_Region_2_Data/</summary>

- `r2E3_datos.txt` → Inputs for R2 (river counts/priors).
- `README.txt` → Data dictionary.
</details>

<details>
<summary>Season_Fa_Region_2_Stabilization/</summary>

- `energia_R2E3.png` → Energy stabilization (overview).
- `r2E3_energia.png` → Energy trace.
- `README.txt` → Plot interpretation.
</details>

<details>
<summary>Season_Fa_Region_2_Gibbs_Sampling/</summary>

- `Season_Fa_r2E3gs.c`, `Season_Fa_r2E3gs.c~` → Gibbs/Metropolis source (R2).
- `Season_Fa_r2E3gs` → **Executable**; usage: `./Season_Fa_r2E3gs <tag>`
- `Season_Fa_r2E3_energia.c` → Energy utility source.
- `Season_Fa_r2E3_energia` → **Executable** for energy plots.
- `README.txt` → Build/run notes.

> **Outputs**
> - `Season_Fa_r2E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Fa_Region_2_Results/` → **(~2k files)** Run artifacts.
- `Stats.py`, `Stats.py~` → Region stats.

</details>

<details>
<summary>Season_Fa_Region_3/</summary>

- `R3_IDs.csv` → Region 3 grid/QGIS IDs.
- `README.txt` → Region 3 notes.

<details>
<summary>Season_Fa_Region_3_Data/</summary>

- `r3E3_datos.txt` → Inputs for R3.
- `README.txt` → Data dictionary.
</details>

<details>
<summary>Season_Fa_Region_3_Energy_Stabilization/</summary>

- `energia_R3E3.png` → Energy stabilization (overview).
- `r3E3_energia.png` → Energy trace.
- `README.txt` → Plot interpretation.
</details>

<details>
<summary>Season_Fa_Region_3_Gibbs_Sampling/</summary>

- `Season_Fa_r3E3gs.c`, `Season_Fa_r3E3gs.c~` → Gibbs/Metropolis source (R3).
- `Season_Fa_r3E3gs` → **Executable**; usage: `./Season_Fa_r3E3gs <tag>`
- `Season_Fa_r3E3_energia.c` → Energy utility source.
- `Season_Fa_r3E3_energia` → **Executable**.
- `README.txt` → Build/run notes.

> **Outputs**
> - `Season_Fa_r3E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Fa_Region_3_Results/` → **(~2k files)** Run artifacts.
- `Stats.py`, `Stats.py~` → Region stats.

</details>

<details>
<summary>Season_Fa_Region_4/</summary>

- `R4_IDs.csv` → Region 4 grid/QGIS IDs.
- `README.txt` → Region 4 notes.

<details>
<summary>Season_Fa_Region_4_Data/</summary>

- `r4E3_datos.txt` → Inputs for R4.
- `README.txt` → Data dictionary.
</details>

<details>
<summary>Season_Fa_Region_4_Energy_Stabilization/</summary>

- `energia_R4E3.png` → Energy stabilization (overview).
- `r4E3_energia.png` → Energy trace.
- `README.txt` → Plot interpretation.
</details>

<details>
<summary>Season_Fa_Region_4_Gibbs_Sampling/</summary>

- `Season_Fa_r4E3gs.c`, `Season_Fa_r4E3gs.c~` → Gibbs/Metropolis source (R4).
- `Season_Fa_r4E3gs` → **Executable**; usage: `./Season_Fa_r4E3gs <tag>`
- `Season_Fa_r4E3_energia.c`, `Season_Fa_r4E3_energia.c~` → Energy utility source.
- `Season_Fa_r4E3_energia` → **Executable**.
- `README.txt` → Build/run notes.

> **Outputs**
> - `Season_Fa_r4E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Fa_Region_4_Results/` → **(~2k files)** Run artifacts.
- `Stats.py`, `Stats.py~` → Region stats.

</details>

</details>

---

#### 🌸 Season_Sp (Spring) — `Season_Sp/`
<details>
<summary>Click to expand</summary>

High-level contents for Spring:
- `Data_Frame_Full_Sp.csv`, `Grid_Full_Sp.gpkg`
- `Join_by_ID.py`, `Join_by_ID.py~`
- `Run_N_Times.sh`, `Run_N_Times.sh~`
- `README.txt`
- `Season_Sp_Maps/` *(seasonal map products; PNGs/QML similar to Fall)*
- `Season_Sp_Region_1/` … `Season_Sp_Region_4/`

> **Note**: Filenames mirror Fall but with the `Season_Sp_` prefix.

<details>
<summary>Season_Sp_Region_1/</summary>

- `R1_IDs.csv`, `README.txt`

<details>
<summary>Season_Sp_Region_1_Data/</summary>

- `r1E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_1_Energy_Stabilization/</summary>

- `energia_R1E3.png`, `r1E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_1_Gibbs_Sampling/</summary>

- `Season_Sp_r1E3gs.c`, `Season_Sp_r1E3gs.c~`, `Season_Sp_r1E3gs` (**executable**)
- `Season_Sp_r1E3_energia.c`, `Season_Sp_r1E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Sp_r1E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Sp_Region_1_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Sp_Region_2/</summary>

- `R2_IDs.csv`, `README.txt`

<details>
<summary>Season_Sp_Region_2_Data/</summary>

- `r2E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_2_Energy_Stabilization/</summary>

- `energia_R2E3.png`, `r2E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_2_Gibbs_Sampling/</summary>

- `Season_Sp_r2E3gs.c`, `Season_Sp_r2E3gs.c~`, `Season_Sp_r2E3gs` (**executable**)
- `Season_Sp_r2E3_energia.c`, `Season_Sp_r2E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Sp_r2E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Sp_Region_2_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Sp_Region_3/</summary>

- `R3_IDs.csv`, `README.txt`

<details>
<summary>Season_Sp_Region_3_Data/</summary>

- `r3E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_3_Energy_Stabilization/</summary>

- `energia_R3E3.png`, `r3E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_3_Gibbs_Sampling/</summary>

- `Season_Sp_r3E3gs.c`, `Season_Sp_r3E3gs.c~`, `Season_Sp_r3E3gs` (**executable**)
- `Season_Sp_r3E3_energia.c`, `Season_Sp_r3E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Sp_r3E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Sp_Region_3_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Sp_Region_4/</summary>

- `R4_IDs.csv`, `README.txt`

<details>
<summary>Season_Sp_Region_4_Data/</summary>

- `r4E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_4_Energy_Stabilization/</summary>

- `energia_R4E3.png`, `r4E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Sp_Region_4_Gibbs_Sampling/</summary>

- `Season_Sp_r4E3gs.c`, `Season_Sp_r4E3gs.c~`, `Season_Sp_r4E3gs` (**executable**)
- `Season_Sp_r4E3_energia.c`, `Season_Sp_r4E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Sp_r4E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Sp_Region_4_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

</details>

---

#### ☀️ Season_Su (Summer) — `Season_Su/`
<details>
<summary>Click to expand</summary>

High-level contents for Summer:
- `Data_Frame_Full_Su.csv`, `Grid_Full_Su.gpkg`
- `Join_by_ID.py`, `Join_by_ID.py~`
- `Run_N_Times.sh`, `Run_N_Times.sh~`
- `README.txt`
- `Season_Su_Maps/` *(seasonal map products; PNGs/QML similar to Fall)*
- `Season_Su_Region_1/` … `Season_Su_Region_4/`

> **Note**: Filenames mirror Fall but with the `Season_Su_` prefix.

<details>
<summary>Season_Su_Region_1/</summary>

- `R1_IDs.csv`, `README.txt`

<details>
<summary>Season_Su_Region_1_Data/</summary>

- `r1E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_1_Energy_Stabilization/</summary>

- `energia_R1E3.png`, `r1E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_1_Gibbs_Sampling/</summary>

- `Season_Su_r1E3gs.c`, `Season_Su_r1E3gs.c~`, `Season_Su_r1E3gs` (**executable**)
- `Season_Su_r1E3_energia.c`, `Season_Su_r1E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Su_r1E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Su_Region_1_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Su_Region_2/</summary>

- `R2_IDs.csv`, `README.txt`

<details>
<summary>Season_Su_Region_2_Data/</summary>

- `r2E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_2_Energy_Stabilization/</summary>

- `energia_R2E3.png`, `r2E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_2_Gibbs_Sampling/</summary>

- `Season_Su_r2E3gs.c`, `Season_Su_r2E3gs.c~`, `Season_Su_r2E3gs` (**executable**)
- `Season_Su_r2E3_energia.c`, `Season_Su_r2E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Su_r2E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Su_Region_2_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Su_Region_3/</summary>

- `R3_IDs.csv`, `README.txt`

<details>
<summary>Season_Su_Region_3_Data/</summary>

- `r3E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_3_Energy_Stabilization/</summary>

- `energia_R3E3.png`, `r3E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_3_Gibbs_Sampling/</summary>

- `Season_Su_r3E3gs.c`, `Season_Su_r3E3gs.c~`, `Season_Su_r3E3gs` (**executable**)
- `Season_Su_r3E3_energia.c`, `Season_Su_r3E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Su_r3E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Su_Region_3_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Su_Region_4/</summary>

- `R4_IDs.csv`, `README.txt`

<details>
<summary>Season_Su_Region_4_Data/</summary>

- `r4E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_4_Energy_Stabilization/</summary>

- `energia_R4E3.png`, `r4E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Su_Region_4_Gibbs_Sampling/</summary>

- `Season_Su_r4E3gs.c`, `Season_Su_r4E3gs.c~`, `Season_Su_r4E3gs` (**executable**)
- `Season_Su_r4E3_energia.c`, `Season_Su_r4E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Su_r4E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Su_Region_4_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

</details>

---

#### ❄️ Season_Wi (Winter) — `Season_Wi/`
<details>
<summary>Click to expand</summary>

High-level contents for Winter:
- `Data_Frame_Full_Wi.csv`, `Grid_Full_Wi.gpkg`
- `Join_by_ID.py`, `Join_by_ID.py~`
- `Run_N_Times.sh`, `Run_N_Times.sh~`
- `README.txt`
- `Season_Wi_Maps/` *(seasonal map products; PNGs/QML similar to Fall)*
- `Season_Wi_Region_1/` … `Season_Wi_Region_4/`

> **Note**: Filenames mirror Fall but with the `Season_Wi_` prefix.

<details>
<summary>Season_Wi_Region_1/</summary>

- `R1_IDs.csv`, `README.txt`

<details>
<summary>Season_Wi_Region_1_Data/</summary>

- `r1E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_1_Energy_Stabilization/</summary>

- `energia_R1E3.png`, `r1E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_1_Gibbs_Sampling/</summary>

- `Season_Wi_r1E3gs.c`, `Season_Wi_r1E3gs.c~`, `Season_Wi_r1E3gs` (**executable**)
- `Season_Wi_r1E3_energia.c`, `Season_Wi_r1E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Wi_r1E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Wi_Region_1_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Wi_Region_2/</summary>

- `R2_IDs.csv`, `README.txt`

<details>
<summary>Season_Wi_Region_2_Data/</summary>

- `r2E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_2_Energy_Stabilization/</summary>

- `energia_R2E3.png`, `r2E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_2_Gibbs_Sampling/</summary>

- `Season_Wi_r2E3gs.c`, `Season_Wi_r2E3gs.c~`, `Season_Wi_r2E3gs` (**executable**)
- `Season_Wi_r2E3_energia.c`, `Season_Wi_r2E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Wi_r2E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Wi_Region_2_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Wi_Region_3/</summary>

- `R3_IDs.csv`, `README.txt`

<details>
<summary>Season_Wi_Region_3_Data/</summary>

- `r3E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_3_Energy_Stabilization/</summary>

- `energia_R3E3.png`, `r3E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_3_Gibbs_Sampling/</summary>

- `Season_Wi_r3E3gs.c`, `Season_Wi_r3E3gs.c~`, `Season_Wi_r3E3gs` (**executable**)
- `Season_Wi_r3E3_energia.c`, `Season_Wi_r3E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Wi_r3E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Wi_Region_3_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

<details>
<summary>Season_Wi_Region_4/</summary>

- `R4_IDs.csv`, `README.txt`

<details>
<summary>Season_Wi_Region_4_Data/</summary>

- `r4E3_datos.txt`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_4_Energy_Stabilization/</summary>

- `energia_R4E3.png`, `r4E3_energia.png`, `README.txt`
</details>

<details>
<summary>Season_Wi_Region_4_Gibbs_Sampling/</summary>

- `Season_Wi_r4E3gs.c`, `Season_Wi_r4E3gs.c~`, `Season_Wi_r4E3gs` (**executable**)
- `Season_Wi_r4E3_energia.c`, `Season_Wi_r4E3_energia` (**executable**)
- `README.txt`

> **Outputs**
> - `Season_Wi_r4E3gs_<tag>_x`, `..._p`, `..._e`
</details>

- `Season_Wi_Region_4_Results/` (many files)
- `Stats.py`, `Stats.py~`
</details>

</details>

</details>


---

### ⚙️ Scripts
<details>
<summary>Click to expand</summary>

These scripts automate **compilation** and **execution** of all C programs across seasons and regions.

- **`Compile_all_c.sh`**  
  - **Purpose:** Compile all region-specific C sources with `gcc`.  
  - **Assumes:** POSIX shell; `gcc` available on the system.  
  - **Typical usage:**
    ```bash
    bash Compile_all_c.sh
    ```
  - **Effect:** Produces region executables (e.g., `Season_Fa_r1E3gs`) inside their respective season/region folders.

- **`Execute_all_c.sh`**  
  - **Purpose:** Execute all compiled binaries per season and region.  
  - **Assumes:** Binaries already compiled; execute permission set (`chmod +x` if needed).  
  - **Typical usage:**
    ```bash
    bash Execute_all_c.sh <tag>
    ```
  - **Behavior:** Passes `<tag>` to each binary; each run emits:
    - `*_x` — final state vector  
    - `*_p` — ergodic average (expected value)  
    - `*_e` — energy (Hamiltonian) per iteration  

</details>

</details>

