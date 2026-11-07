# FastSpeech 2 – English and Telugu Text-to-Speech

## Project Overview

This project explores the implementation and adaptation of FastSpeech 2 for English and Telugu text-to-speech (TTS).

The work includes dataset inspection, text preprocessing, model configuration, experimental English training, and inference testing.

## Technologies

- Python
- PyTorch
- FastSpeech 2
- HiFi-GAN
- NumPy
- Librosa
- Matplotlib

## Project Structure

'''text
FastSpeech2-English-Telugu-TTS/
├── English/
│   ├── train.py
│   ├── preprocess.py
│   ├── inference.py
│   ├── config.yaml
│   └── checkpoints/
├── Telugu/
│   ├── train.py
│   ├── preprocess.py
│   ├── inference.py
│   ├── config.yaml
│   └── checkpoints/
├── Results/
│   ├── English/
│   └── Telugu/
├── Report/
│   └── Technical_Report.pdf
├── README.md
└── requirements.txt
```

## Current Experimental Progress

### English
- Dataset preprocessing and feature inspection completed.
- FastSpeech 2 model loaded and tested using GPU.
- Experimental training completed for 20 steps.
- Checkpoints saved at steps 10 and 20.
- WAV inference generated successfully.
- Generated speech is currently unintelligible and requires further training and evaluation.

### Telugu
- Telugu text vocabulary and tokenization tested.
- Acoustic alignment and model training are not yet completed.

## Limitations

The current English checkpoint is an experimental checkpoint and is not a converged model. Telugu acoustic alignment and training remain incomplete. Further training, validation, pronunciation evaluation, and variance-adaptor analysis are required.

## Acknowledgements

This project is based on the FastSpeech 2 research implementation by [ming024/FastSpeech2](https://github.com/ming024/FastSpeech2).

This repository documents the experimental implementation and progress of the assignment.
