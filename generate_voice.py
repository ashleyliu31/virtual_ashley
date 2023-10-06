import os
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech
import torch
from speechbrain.pretrained import EncoderClassifier
from transformers import SpeechT5HifiGan
import numpy as np
import tempfile


def generate_voice(text):
    # set up vocoder 
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
    # download fine-tuned SpeechT5 model trained on my voice
    finetuned_model = SpeechT5ForTextToSpeech.from_pretrained("ashleyliu31/ashley_voice_clone_speecht5_finetuning")
    # set up SpeechT5 processor
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    # make temp directory to store classifier for speaker embedding
    tempfile.mkdtemp()
    # set up classifier for speaker embedding
    classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-xvect-voxceleb", savedir=tempfile.gettempdir())
    # load numpy array that contains my voice's speaker embedding
    filename = "array.npy"
    path= os.path.join('assets', filename)
    loaded_array = np.load(path)
    # generate speaker embedding from my voice
    speaker_embeddings = classifier.encode_batch(torch.tensor(loaded_array))
    # tokenize user input
    inputs = processor(text=text, return_tensors="pt")
    # generate spectrogram from tokenized input and speaker embedding
    finetuned_spectrogram = finetuned_model.generate_speech(inputs["input_ids"], speaker_embeddings.squeeze(0)) 
    # use vocoder to convert spectrogram into torch tensor
    with torch.no_grad():
        finetuned_speech = vocoder(finetuned_spectrogram)
    # convert torch tensor into numpy array and return it to be converted into a wav audio file in main.py
    return finetuned_speech.numpy()