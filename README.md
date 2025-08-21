# 🐸 Population Modeling of *Plectrohyla sagorum*  
*A Hamiltonian & Geo-statistical Approach*

---

## 📖 Overview

This repository contains the implementation of a **novel statistical mechanics-based approach** for studying **population dynamics** of individuals in ecology across different seasons of the year.  

We apply our method to the case of the vulnerable amphibian **_Plectrohyla sagorum_** ([IUCN, 2020](https://www.iucnredlist.org/species/55853/a54352590)), a stream-breeding frog inhabiting the **cloud forests of the Tacaná Volcano Biosphere Reserve, Chiapas, Mexico**.

Our approach combines:

- ⚛️ **Hamiltonian framework from physics** (kinetic + potential terms)  
- 🌍 **Geo-statistics** and **Markov Random Fields (MRF)**  
- 🧮 **Approximate minimization problems** inspired by statistical mechanics  

This fusion allows us to generate **probability distributions of individuals** across seasons, reflecting ecological processes such as spreading during rainy seasons and attraction to streams during the dry season.  

---

## 🧪 Methodology Highlights

- Individuals' distribution is modeled as a balance between:
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

- The study region is discretized into a **grid of sites** (see `Geographic Data/Centroides-Elevacion_QGIS.csv`), each representing a spatial unit.
- Each site is assigned a **state variable**, which evolves according to:
  - **Local rules** depending on the site's attributes, and
  - **Neighborhood interactions** defined by adjacency relations (see `Geographic Data/Neighborhood_Structure/`).

Formally, the system configuration is represented by a vector:

$
\omega = (\omega_{i,j})_{(i,j) \in \Lambda},
$

where $\omega_{i,j}$ is the average numbers of frogs in cell $(i,j)$ and $\Lambda$ is the grid of all cells.  

The **energy functional** (Hamiltonian) is defined as:

$
H(\omega) = H_0(\omega) + V_g(\omega),
$

where

$
H_0(\omega) = \sum_{\ell \sim \jmath} (\omega_\ell - \omega_\jmath)^2
$

represents local differences between neighboring cells (with $\ell \sim \jmath$ indicating neighbors from `Geographic Data/Neighborhood_Structure/r*_vecinos.txt`), and

$
V_g(\omega) = g \sum_{\ell \in \Lambda} d_\ell^2 \, \omega_\ell
$

is a potential term representing the attraction, with $d_\ell$ the distance of cell $\ell$ to the river and $g$ a coupling constant (stored in `Geographic Data/parameters.csv`).

The **probability of a configuration** is given by the Gibbs distribution:

$
\pi(\omega) = \frac{1}{Z} \exp\Big(-\frac{1}{T} H(\omega)\Big),
$

where T is a temperature parameter (from `Geographic Data/parameters.csv`) and Z is the partition function:

$
Z = \sum_{\omega \in \Omega} \exp\Big(-\frac{1}{T} H(\omega)\Big).
$

---

### 🗂 Conditional Probabilities per Region and Season

The grid is divided by the river into regions $\Lambda_1, \Lambda_2, \Lambda_3, \Lambda_4$, with corresponding configuration spaces $\Omega^1,\Omega^2,\Omega^3,\Omega^4$. For each region $i\in \{1,2,3,4\}$, season $x \in \{\rm Sp, Su, Fa, Wi\}$ and $\omega\in \Omega^i$:

$
H_0^{(i,x)}(\omega) = \sum_{s_1 \sim s_2} (\omega_{s_1} - \omega_{s_2})^2 +\sum_{\substack{s\sim r\\  r\in R}}(\omega_s-
\boldsymbol{\omega}^{x}_r)^2
$

$
V_{g^{(i,x)}}^{(i,x)}(\omega) = g^{(i,x)} \sum_{s \in \Lambda^i} d_s^2 , \omega_s
$

$
H^{(i,x)}(\omega) = H_0^{(i,x)}(\omega) + V_{g^{(i,x)}}^{(i,x)}(\omega)
$

where $\boldsymbol{\omega}^x_r$ is the observed (or Poisson-simulated) number of individuals on the river cell $r$ for season $x$ (found in `Season_*/Season_*_Region_*/Season_*_Region_*_Data/*_datos.txt`), and $g^{(i,x)}$ is the region- and season-specific coupling constant (stored in `Geographic Data/parameters.csv`).

Conditional probability of a configuration in region $i$ given river data:

$
\pi^{(i,x)}(\omega) = \frac{1}{Z^{(i,x)}} \exp\Big(-\frac{1}{T} H^{(i,x)}(\omega)\Big)
$

with partition function

$
Z^{(i,x)} = \sum_{\omega \in \Omega^i} \exp\Big(-\frac{1}{T} H^{(i,x)}(\omega)\Big)
$

---

### 🔄 Stochastic Simulation (Gibbs Sampling)

A **Gibbs sampling sequence** is generated to approximate the equilibrium distribution (implemented in `Season_*/Season_*_Region_*/Season_*_Region_*_Gibbs_Sampling/*.c`):

1. Start from an initial configuration $\omega^{(0;i,x)} = 0$ for all $p \in \Lambda^i$.
2. For each site $\ell_n$ in a fixed neighbor-order sequence, propose a new state $\tilde{\omega}_{\ell_n} \in \{0,1,\dots,K^x\}$ where $K^x$ is the seasonal carrying capacity (from `Geographic Data/parameters.csv`).
3. Accept the proposal with probability:

$
P = \min\Bigg(1, \frac{\pi^{(i,x)}(\tilde{\omega})}{\pi^{(i,x)}(\omega^{(n-1;i,x)})}\Bigg)
= \min\Bigg(1, \exp\Big(-\frac{1}{T} \big[ H^{(i,x)}(\tilde{\omega}) - H^{(i,x)}(\omega^{(n-1;i,x)}) \big] \Big)\Bigg).
$

4. Repeat for all sites and iterate until convergence (monitored via energy traces in `Season_*/Season_*_Region_*/Season_*_Region_*_Energy_Stabilization/`).

This procedure guarantees convergence to the **conditional stationary distribution** under standard conditions (aperiodicity and irreducibility).

---

### 📊 Outputs

The simulation generates three types of output files (stored in `Season_*/Season_*_Region_*/Season_*_Region_*_Results/`):

- **Final state vector** $(\omega^{(n;i,x)})$: One realization of the system (files `*_x`)
- **Ergodic averages**: Expectation values used to reconstruct abundance distributions (files `*_p`)
- **Energy traces**: Diagnostic to monitor convergence (files `*_e`)

The ergodic averages are used for the actual prediction and heat maps (visualized in `Season_*/Season_*_Maps/`).


---

# 📂 Repository Structure

<details>
<summary>Parent Directory</summary>

The parent directory contains three main components: **Geographic Data**, **Seasonal Directories**, and **Scripts**. This structure mirrors the spatial inputs, seasonal segmentation, and automation needed to run all experiments.

---

## 🌍 Geographic Data

<details>
<summary>Click to expand</summary>

This section holds the spatial inputs used by the simulations. Objects created in **QGIS** receive a **unique feature ID**, which is used across files to consistently join geometry, centroids, neighborhoods, and model outputs. Note that there are two types of IDs per grid coordinate: a **Global ID** that is independent of the region, and for each region another **Local ID**.

### **Neighborhood_Structure/**
- One file per region (e.g., `r1_vecinos.txt` … `r4_vecinos.txt`).
- Each row lists **neighbor QGIS IDs** for a given cell (first-order adjacency). Here **Local IDs** are used.
- Used to define the first-order neighborhood relation and is utilized by the Gibbs sampler program.
- This adjacency structure is crucial for the spatial correlation modeling in the Markov Random Field framework.

### **Centroides-Elevacion_QGIS.csv**
- Columns include: **ID**, **x**, **y**, **z**.
- **ID** matches the QGIS **Global ID** for each cell.
- Used to reconstruct spatial maps and bind results to coordinates.
- The elevation data (z-coordinate) provides topographic context for the ecological modeling.

### **parameters.csv**
- Lists all parameters used for the simulations for each season and region.
- For each season there is a unique value of:
  - Temperature **T** (affects species distribution patterns)
  - Maximum number of individuals on the river **K** (carrying capacity)
  - Density of individuals along the river **ρ** (rho)
- For each Season-Region pair there is a value for the coupling constant **g** (controls spatial interaction strength)
- These parameters are derived from field observations and calibrated to match ecological patterns.

</details>

---

## 🍂🌸☀️❄️ Seasons

<details>
<summary>Click to expand</summary>

Each season directory encapsulates **inputs, code, executables, and results** for that season, split into four spatial **regions**. The repository contains directories for all four seasons (Fall, Winter, Spring, Summer), but for brevity, we detail **Fall (Season_Fa)** and **Region 1** as representative examples. All other seasons (Winter, Spring, Summer) and regions (2, 3, 4) follow identical structural patterns and naming conventions.

Every region within each season includes the following sub-directories:
- `*_Data/` → Contains input data for the Gibbs sampling algorithm
- `*_Gibbs_Sampling/` → Contains C source code and compiled programs for Gibbs simulation
- `*_Energy_Stabilization/` *(or `*_Stabilization/` in some regions)* → Convergence analysis and energy evolution plots
- `*_Results/` → Results from the Gibbs simulation program are stored here: final states (`*_x`), ergodic means (`*_p`), energy traces (`*_e`)
- `Stats.py` → Python script that computes summary statistics from the region's results
- `R?_IDs.csv` → QGIS/grid ID mapping for this region, used to merge outputs with geographic coordinates

### **Output File Semantics**
- `*_x` = Final state vector (per grid cell; integer counts representing final population distribution)
- `*_p` = Ergodic average (expected counts per cell; used for heatmaps; floating point values representing long-term expected population)
- `*_e` = Hamiltonian value by iteration (energy trace used to assess stabilization and convergence of the MCMC chain)

---

### 🍂 Season_Fa (Fall) — `Season_Fa/`

<details>
<summary>Click to expand</summary>

The Fall season directory contains the complete workflow for autumn ecological modeling, including data preparation, simulation execution, and result visualization.

**High-level contents for Fall:**
- `Data_Frame_Full_Fa.csv` → Region-merged outputs with grid IDs. This file can be directly uploaded to QGIS as point geometry to create spatial distribution maps.
- `Grid_Full_Fa.gpkg` → GeoPackage format file containing the full seasonal grid with all attributes for GIS analysis.
- `Join_by_ID.py` → Python script that joins region outputs to grid IDs to produce `Data_Frame_Full_Fa.csv`.
  - **Inputs:** 
    - `Season_Fa_Region_i/Season_Fa_Region_i_Results/` (simulation results)
    - `Season_Fa_Region_i/Ri_IDs.csv` (**Local IDs**)
    - `Centroides-Elevacion_QGIS.csv` (from parent directory `Geographic Data`) 
    - for i ∈ [1,2,3,4]
- `Run_N_Times.sh` → Bash script that runs the Gibbs Sampler N times throughout all regions. Results are automatically saved in `Season_Fa_Region_i/Season_Fa_Region_i_Results/`.
- `README.txt` → Season-level documentation and metadata.
- `Season_Fa_Maps/` → Directory containing maps generated by QGIS (heatmaps, style files).
- `Season_Fa_Region_1/ … Season_Fa_Region_4/` → Individual region workspaces containing region-specific data and code.

---

#### **📍 Season_Fa_Maps/**

<details>
<summary>Click to expand</summary>

This directory contains the final visualization outputs and cartographic products from the Fall season modeling.

- `ArcoIris_Total_E3p31.png` → Rainbow color palette heatmap showing expected population counts. This represents the main simulation results in a visually intuitive format.
- `GreyScale_Total_Fa.pgw` → World file providing georeferencing information for the grayscale PNG image.
- `GreyScale_Total_Fa.png` → Grayscale heatmap of expected population counts, suitable for publication or analysis requiring monochrome output.
- `IE3_p31.png` → Scatter plot visualization of expected counts where each point represents an individual occurrence or high-density location.
- `README.txt` → Documentation covering QGIS layer configurations, coordinate reference system information, and style file descriptions.

</details>

---

#### **📍 Season_Fa_Region_1/**

<details>
<summary>Click to expand</summary>

Region 1 serves as the representative example for the regional structure. All other regions (2, 3, 4) maintain identical organizational patterns with region-specific parameter values and geographic extents.

- `R1_IDs.csv` → Region 1 **Local** grid/QGIS ID mapping table used for spatial join operations between simulation results and geographic coordinates.
- `README.txt` → Region-specific documentation including parameter ranges, geographic boundaries, and methodological notes.

---

##### **Season_Fa_Region_1_Data/**

<details>
<summary>Click to expand</summary>

Contains the input data files required for the Gibbs sampling simulation in Region 1 during Fall.

- `r1E3_datos.txt` → Primary input file for the Gibbs sampling algorithm located in `Season_Fa_Region_1_Gibbs_Sampling/`.
  - **Column 1:** Row site identifier tag within Region 1 (sequential numbering of grid cells)
  - **Column 2:** Neighborhood class of the site representing distance from the river system
    - Class 0: River sites (directly adjacent to water bodies)
    - Positive integers: Increasing distance from river (1, 2, 3, etc.)
  - **Column 3:** Initial number of individuals observed at each site
    - **River sites:** Generated using Poisson process with intensity ρ=0.31 (calibrated from field survey data)
    - **Non-river sites:** Initialized to 0 (assumes initial population concentration along water sources)
- `README.txt` → Comprehensive data dictionary explaining input file format, assumptions, and data collection methodology.

</details>

---

##### **Season_Fa_Region_1_Energy_Stabilization/**

<details>
<summary>Click to expand</summary>

This directory contains diagnostic plots and analysis tools for assessing MCMC convergence and energy stabilization.

- `energia_R1E3.png` → Complete energy stabilization plot for Region 1 Fall simulation. Shows (10^6) × M iterations of Gibbs Sampling, where M=9,310 (total grid sites in Region 1). This long run ensures proper mixing and convergence.
- `r1E3_energia.png` → Focused energy stabilization plot showing the first 2 million iterations. Used for initial convergence assessment and burn-in period determination.
- `README.txt` → Guide for interpreting stabilization plots, including criteria for convergence assessment and identification of proper mixing behavior.

The energy plots are essential for validating that the Markov Chain Monte Carlo algorithm has reached its stationary distribution before collecting samples for inference.

</details>

---

##### **Season_Fa_Region_1_Gibbs_Sampling/**

<details>
<summary>Click to expand</summary>

Contains the core computational engine for the ecological modeling using Gibbs sampling methodology.

**Source Code:**
- `Season_Fa_r1E3gs.c` → Main C source file implementing the Gibbs sampling routine for Region 1.
  - **Hard-coded parameters:** Temperature (T) and Coupling constant (g) values specific to Fall/Region 1
  - **Input dependencies:**
    - `Season_Fa_Region_1_Data/r1E3_datos.txt` (initial population data)
    - `Neighborhood_Structure/r1_vecinos.txt` (spatial adjacency matrix)
  - **Algorithm:** Implements a Markov Random Field model with Gibbs sampling for spatial population dynamics

**Executables:**
- `Season_Fa_r1E3gs` → **Main executable**. Execute using:
  ```bash
  ./Season_Fa_r1E3gs <tag>
  ```
  The `<tag>` parameter is appended to all output filenames to distinguish different simulation runs or parameter sets.

**Utility Programs:**
- `Season_Fa_r1E3_energia.c` → Specialized C program for energy-only calculations (lightweight version of main sampler)
- `Season_Fa_r1E3_energia` → Executable for regenerating energy traces without full population sampling
- `README.txt` → Compilation instructions, runtime parameters, and usage guidelines

**Standard Output Files Generated by Season_Fa_r1E3gs:**
- `Season_Fa_r1E3gs_<tag>_x` → Final state vector containing integer population counts per grid cell after convergence
- `Season_Fa_r1E3gs_<tag>_p` → Ergodic mean values representing expected population density per cell (floating-point averages)
- `Season_Fa_r1E3gs_<tag>_e` → Energy trace file containing Hamiltonian values for each iteration (used for convergence diagnostics)

**Note:** All other seasons (Winter, Spring, Summer) and regions (2, 3, 4) contain analogous Gibbs sampling implementations with season/region-specific parameter values and file naming conventions.

</details>

</details>

</details>

</details>

---

## ⚙️ Scripts

<details>
<summary>Click to expand</summary>

These automation scripts streamline the **compilation** and **execution** workflow for all C programs across the complete seasonal and regional matrix (4 seasons × 4 regions = 16 distinct simulations).

### **`Compile_all_c.sh`**
- **Purpose:** Automated compilation of all region-specific C source files using the GCC compiler
- **System Requirements:** 
  - POSIX-compliant shell environment
  - GCC compiler suite available in system PATH
  - Appropriate file permissions for source code access
- **Typical Usage:**
  ```bash
  bash Compile_all_c.sh
  ```
- **Behavior:** 
  - Recursively locates all `.c` source files in seasonal/regional directories
  - Compiles each source file with appropriate flags and optimization settings
  - Generates executable binaries (e.g., `Season_Fa_r1E3gs`) within their respective directories
  - Provides compilation status and error reporting
- **Output:** Production-ready executables for all 16 season-region combinations

### **`Execute_all_c.sh`**
- **Purpose:** Batch execution of all compiled Gibbs sampling binaries across the complete experimental matrix
- **Prerequisites:** 
  - All binaries must be successfully compiled using `Compile_all_c.sh`
  - Execute permissions properly set (use `chmod +x` if needed)
  - Input data files properly formatted and accessible
- **Typical Usage:**
  ```bash
  bash Execute_all_c.sh <tag>
  ```
- **Parameters:**
  - `<tag>`: User-defined identifier passed to each binary for output file naming and experiment tracking
- **Execution Behavior:**
  - Systematically executes each binary in predetermined order
  - Passes the `<tag>` parameter to ensure unique output identification
  - Monitors execution status and provides progress feedback
  - Handles error conditions and failed simulations
- **Generated Outputs (per region):**
  - `*_x` — Final state vector (integer population counts)
  - `*_p` — Ergodic average (expected population density values)
  - `*_e` — Energy trajectory (Hamiltonian evolution for convergence analysis)

**Workflow Integration:** These scripts enable researchers to execute the complete experimental pipeline with minimal manual intervention, ensuring consistency and reproducibility across all seasonal and regional simulations.

</details>

</details>
