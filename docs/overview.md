# NeurIPS - Ariel Data Challenge 2025

[Competition Page on Kaggle](https://www.kaggle.com/competitions/ariel-data-challenge-2025/overview)

---

## Overview

The NeurIPS - Ariel Data Challenge 2025 invites participants to derive exoplanet signals from simulated data from ESA's Ariel mission, which aims to characterize 1,000 exoplanets after its 2029 launch. The challenge is to recover the true exoplanet spectrum from noisy observations, pushing the boundaries of astronomical data analysis.

This year's competition builds on the [2024 challenge](https://www.kaggle.com/c/ariel-data-challenge-2024) with a more realistic dataset, including effects such as stellar limb darkening, validated star-planet pairs, diverse atmospheric models, and Ariel's actual observation cadence. New challenges include generalization, data efficiency, and integrating observations from multiple visits.

Your work could help accelerate exoplanet research, support scientists preparing for the Ariel mission, and contribute to answering the question: _Are we alone in the universe?_

---

## Evaluation

Predicted spectra (μ_user) and uncertainties (σ_user) are evaluated against the ground truth spectrum (y) using the Gaussian Log-likelihood (GLL):

$$
GLL = -\frac{1}{2} \left( \log(2\pi) + \log(\sigma_{user}^2) + \frac{(y - \mu_{user})^2}{\sigma_{user}^2} \right)
$$

The total GLL is summed across all wavelengths and the test set, then transformed into a score:

$$
score = \frac{L- L_{ref}}{L_{ideal} - L_{ref}}
$$

- **L_ideal**: Perfect match to ground truth, with uncertainty of 10 ppm for AIRS and 1 ppm for FGS1.
- **L_ref**: Uses the mean and variance of the training dataset as prediction.

Channels are weighted by spectral channel width and number of points; FGS1's weight is doubled.

- FGS1: 0.4
- AIRS-Ch0: ≈ 0.0069 per spectral point

Scores range from 0 to 1 (negative scores are set to 0).

[Full metric implementation](https://www.kaggle.com/code/metric/ariel-gaussian-log-likelihood)

### Submission File

- Predict a mean and uncertainty for each `planet_id`.
- Each row: `planet_id`, 283 spectra columns, 283 uncertainty columns (567 columns total).
- Example submission file is provided in the Data Files.

---

## Timeline

- **June 26, 2025**: Start Date
- **September 17, 2025**: Entry & Team Merger Deadline
- **September 24, 2025**: Final Submission Deadline

All deadlines are at 11:59 PM UTC.

---

## Prizes

- 1st Place: $15,000
- 2nd Place: $10,000
- 3rd Place: $8,000
- 4th Place: $7,000
- 5th Place: $5,000
- 6th Place: $5,000

---

## Code Requirements

- Submissions must be made through Kaggle Notebooks.
- CPU/GPU Notebook: ≤ 9 hours run-time
- Internet access disabled
- Freely & publicly available external data allowed (including pre-trained models)
- Submission file must be named `submission.csv`

See the [Code Competition FAQ](https://www.kaggle.com/docs/competitions#notebooks-only-FAQ) for more details.

---

## Acknowledgements

**Organising Team:**  
K.H. Yip, L.V. Mugnai, R.L. Coates, A. Bocchieri, O. Faucoz, A. NG, G. Morello, A. Papageorgiou, A. Syty, T. Tahseen, I.P. Waldmann

**Supporting Individuals:**  
Giovanni Bruno, Patricio Cubillos Vallejos, C. Danielski, J. Davey, M. Min, L. Pagliaro, Emilie Panek, Alice Radcliffe, T. Zingales, and the Ariel Science Consortium

**Institutions:**  
University College London, Cardiff University, Sapienza Università di Roma, CNES, Instituto de Astrofísica de Andalucía (IAA-CSIC), Institut d'Astrophysique de Paris (IAP), Università degli studi di Padova, SRON Netherlands Institute for Space Research, INAF-Osservatorio Astrofisico di Arcetri, INAF - Catania Astrophysical Observatory, Space Research Institute (Austrian Academy of Sciences), The University of Alabama, Observatoire de Paris

---

## Citation

Kai Hou Yip, Lorenzo V. Mugnai, Rebecca L. Coates, Andrea Bocchieri, Orphée Faucoz, Arun Nambiyath Govindan, Giuseppe Morello, Andreas Papageorgiou, Angèle Syty, Tara Tahseen, Sohier Dane, Maggie Demkin, Jean-Philippe Beaulieu, Sudeshna Boro Saikia, Giovanni Bruno, Quentin Changeat, Camilla Danielski, Pascale Danto, Jack Davey, Pierre Drossart, Paul Eccleston, Billy Edwards, Clare Jenner, Ryan King, Theresa Lueftinger, Michiel Min, Nikolaos Nikolaou, Leonardo Pagliaro, Enzo Pascale, Emilie Panek, Alice Radcliffe, Luís F. Simões, Patricio Cubillos Vallejos, Tiziano Zingales, Giovanna Tinetti, Ingo P. Waldmann.  
**NeurIPS - Ariel Data Challenge 2025.** https://kaggle.com/competitions/ariel-data-challenge-2025, 2025. Kaggle.

---

## Host

**University College London**

---
