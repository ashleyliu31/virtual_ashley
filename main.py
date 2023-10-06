from flask import Flask, render_template, send_file, request
from scipy.io.wavfile import write
import io
from rag import rag
from generate_voice import generate_voice
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # get user input
        prompt = request.form.get('human_input')
        # use input as prompt for LLM to perform RAG 
        response = rag(prompt)
        # generate voice from LLM response
        voice = generate_voice(response)
        # creat wav audio file and send it to user's browser
        wav_output = io.BytesIO()
        rate = 16000
        write(wav_output, rate, voice)
        wav_output.seek(0)
        return send_file(wav_output, mimetype='audio/wav', as_attachment=True, download_name="audio.wav")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))