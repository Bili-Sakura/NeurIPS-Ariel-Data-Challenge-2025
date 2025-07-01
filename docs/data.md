# NeurIPS - Ariel Data Challenge 2025

[Source URL](https://www.kaggle.com/competitions/ariel-data-challenge-2025/data)

## Overview

Characterizing the chemistry of exoplanets is a major project in astronomy. The [European Space Agency's Ariel mission](https://arielmission.space/) will gather data on approximately 1,000 exoplanets. The challenge is to extract the chemical spectrum of exoplanet atmospheres using simulated Ariel data.

### Key Changes from Last Year

- More train and test data.
- Unique star models for each planet.
- Repeated observations of some planets.
- Upgraded physics model.

![Main Changes](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F1132983%2Fb602a4112c0e39fb6548752f15332e8c%2Fmain_changes.png?generation=1750802650151472&alt=media)

## Files

### Metadata Files

- **train.csv**: Ground truth spectra.
- **wavelengths.csv**: Wavelength grid for each spectrum.
- **axis_info.parquet**: Axis information for instruments.
- **adc_info.csv**: ADC conversion parameters.
- **[train/test]\_star_info.csv**: Star-planet system details.
- **sample_submission.csv**: Sample submission format.

### Signal Files

- **AIRS-CH0_signal**: 11,250 rows of images, flattened.
- **FGS1_signal**: 135,000 rows of images, flattened.

### Calibration Files

- **dark.parquet**: Captures thermal noise and bias.
- **dead.parquet**: Identifies dead or hot pixels.
- **flat.parquet**: Corrects pixel sensitivity variations.
- **linear_corr.parquet**: Linearity correction information.
- **read.parquet**: Captures electronic noise during readout.
