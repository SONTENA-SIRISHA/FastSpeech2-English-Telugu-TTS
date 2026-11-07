# FastSpeech 2: English and Telugu Text-to-Speech

## Project Overview

This project explores the implementation of FastSpeech 2 for English and Telugu text-to-speech synthesis as part of an internship assignment.

The implementation is based on the FastSpeech 2 reference repository by ming024.

## Implementation

### English
- Dataset: Svarah
- Text preprocessing and acoustic feature inspection completed.
- FastSpeech 2 model loaded and tested on a GPU.
- Experimental training performed for 20 steps.
- Checkpoints saved at steps 10 and 20.
- One inference WAV and its spectrogram generated.
- The generated audio was not intelligible and requires further training.

### Telugu
- Dataset: IndicTTS Telugu.
- Telugu Unicode vocabulary and text tokenization tested.
- Acoustic alignment, model training and speech generation remain incomplete.

## Repository Structure

- `English/`: English training, preprocessing, inference and configuration.
- `Telugu/`: Telugu implementation status.
- `Results/`: Available experimental outputs.
- `Report/`: Technical report.
- Shared model implementation and utility modules are maintained at the repository root.

## Experimental Configuration

- Sample rate: 22050 Hz
- Mel channels: 80
- Batch size: 8
- English training steps: 20
- Checkpoints: Steps 10 and 20

These are experimental settings, not evidence of a converged model.

## Reproducibility

The original datasets are not included in this repository. Obtain the permitted datasets separately and arrange them according to the paths in the configuration files before running preprocessing and training.

The current checkpoints and audio are experimental artifacts. Further training, validation and speech-quality evaluation are necessary.

## Limitations

A complete bilingual TTS system has not yet been achieved. Telugu acoustic alignment and training are pending, and the current English generated audio is not intelligible.

## Reference

Original implementation: https://github.com/ming024/FastSpeech2


## Dependencies

- `requirements.txt` contains the original reference repository's dependency pins.
- `requirements-original.txt` preserves the same original dependency list.
- `requirements-kaggle-tested.txt` records package versions observed in the Kaggle experiment environment.

The Kaggle environment used Python 3.13.16 and PyTorch 2.11.0 with CUDA 13.0. Some original dependencies were not installed or verified. The tested-environment file is a record of the experiment environment, not a guarantee that the complete project can be reproduced by installing that file alone.
