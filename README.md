Project description: an LLM-backed bot that speaks in my cloned voice based on information retrieved from PDF files

Technologies: PyTorch, Torchaudio, Hugging Face, Google PaLM2, Langchain, Microsoft SpeechT5, docker

Demo: https://virtual-ashley-zyplnvep6a-uc.a.run.app/ 

This is the PDF file with my personal information from which the bot retrieves data: https://drive.google.com/file/d/1i0r-x4JLz6OG7YmCcsHRLkM_sfnB4b7U/view?usp=sharing

VOICE CLONING RESULTS

This is a recording of my actual voice:
https://drive.google.com/file/d/1uFbrDOFocvNTcnWN637xxn7mLk6mgChk/view?usp=sharing

A clip generated from the SpeechT5 model with my own speaker embeddings before finetuning:
https://drive.google.com/file/d/1Xacb6UeJeuL8p9SSTOC73WtH25lQMU7R/view?usp=sharing

This is my voice clone after finetuning:
https://drive.google.com/file/d/1GMLsMRPANQN6oZ6sfhXOyrkKjyQAq9jG/view?usp=sharing

Another clip generated from the model before finetuning:
https://drive.google.com/file/d/1HK0T5iD-Y6ylRE4MSKgo6I7K5kleElc1/view?usp=sharing

My voice clone after finetuning:
https://drive.google.com/file/d/1CHdTUImO8HEQUHxZVpl9F9MlvdCbjcPJ/view?usp=sharing

The audio quality is limited by the fact that I recorded with a $20 mic.

MORE INFO

This is the finetuned SpeechT5 model that can perform text-to-speech using my voice:
https://huggingface.co/ashleyliu31/ashley_voice_clone_speecht5_finetuning
