# 🐸 Population Dynamics of *Plectrohyla sagorum*  
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

## 📂 Repository Structure  

The repository mirrors the **seasonal and spatial segmentation** of the study.  

