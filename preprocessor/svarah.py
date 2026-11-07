
import os
import csv
import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm
from text import _clean_text


def prepare_align(config):
    in_dir = config["path"]["corpus_path"]
    out_dir = config["path"]["raw_path"]

    sampling_rate = config["preprocessing"]["audio"]["sampling_rate"]
    max_wav_value = config["preprocessing"]["audio"]["max_wav_value"]
    cleaners = config["preprocessing"]["text"]["text_cleaners"]

    for split in ["train", "val"]:
        metadata_path = os.path.join(in_dir, f"{split}_metadata.csv")
        wav_dir = os.path.join(in_dir, split, "wavs")

        speaker = f"Svarah_{split}"
        output_dir = os.path.join(out_dir, speaker)
        os.makedirs(output_dir, exist_ok=True)

        with open(metadata_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in tqdm(reader, desc=f"Preparing Svarah {split}"):
                base_name = os.path.splitext(row["filename"])[0]
                text = _clean_text(row["text"], cleaners)

                wav_path = os.path.join(wav_dir, row["filename"])

                if not os.path.exists(wav_path):
                    continue

                wav, _ = librosa.load(wav_path, sr=sampling_rate)

                peak = np.max(np.abs(wav))
                if peak > 0:
                    wav = wav / peak * max_wav_value

                wav = np.clip(wav, -32768, 32767)

                wavfile.write(
                    os.path.join(output_dir, base_name + ".wav"),
                    sampling_rate,
                    wav.astype(np.int16)
                )

                with open(
                    os.path.join(output_dir, base_name + ".lab"),
                    "w",
                    encoding="utf-8"
                ) as lab_file:
                    lab_file.write(text)
