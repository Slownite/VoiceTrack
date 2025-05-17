
# 🗣️ VoiceTrack: Speaker-Aware Transcription in Python

**VoiceTrack** is a privacy-conscious, offline tool for diarizing and transcribing `.wav` audio using Hugging Face foundation models. It combines **PyAnnote** for speaker diarization and **Whisper** for speech recognition — giving you clean, speaker-labeled transcripts straight from the command line.

No cloud upload. No external dependencies. Just Python, Hugging Face, and your audio.

---

## 📁 Project Structure

```
├── voicetrack.py               # Main script for diarization + transcription
├── .env                        # Stores Hugging Face token
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation (you're reading it)
```

---

## 🚀 Features

- 🎙️ Speaker diarization using `pyannote/speaker-diarization-3.1`
- 📝 Transcription via `openai/whisper-small` (via Transformers)
- ⏱️ Timestamp alignment to match text to speaker segments
- 🌈 Color-coded CLI output
- 📄 Optional output to text file

---

## 📦 Setup & Run

> Works best with `.wav` files (mono, 16 kHz).

### 1. Clone & install dependencies
```bash
git clone https://github.com/yourusername/voicetrack.git
cd voicetrack
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Add your Hugging Face token
Create a `.env` file:
```dotenv
HUGGINGFACE=your_huggingface_access_token
```

### 3. Run on your audio file
```bash
python voicetrack.py path/to/audio.wav
```

### Optional: Save to file
```bash
python voicetrack.py path/to/audio.wav --output transcript.txt
```

---

## 🧪 Sample Output

```bash
[Speaker A] Hello, how are you?
[Speaker B] I'm good, thanks! And you?
[Speaker A] Doing well, thank you.
```

Output is color-coded in the terminal and cleanly saved if using `--output`.

---

## 📋 Requirements

- Python 3.8+
- ffmpeg (optional, for audio conversion)
- Hugging Face account (for PyAnnote access)

---

## 📘 How It Works

1. Transcribes the full file using Whisper (`openai/whisper-small`)
2. Runs diarization using PyAnnote (`pyannote/speaker-diarization-3.1`)
3. Aligns timestamps between transcription chunks and speaker turns
4. Outputs readable speaker-labeled text

---

## 🧱 Model Notes

- **Whisper model**: `openai/whisper-small` (swap with `tiny` for speed or `base` for quality)
- **Diarization model**: `pyannote/speaker-diarization-3.1`
- Audio should be **16 kHz, mono `.wav`** for best performance

---

## 📄 License

MIT — free to use, modify, and share.

---

## 🙋‍♂️ Author

**Samuel Diop**  
Ph.D. Researcher in Computer Vision and Deep Learning  
[🌐 samueldiop.com](http://samueldiop.com) · [🐙 GitHub](https://github.com/Slownite) · [💼 LinkedIn](https://www.linkedin.com/in/samuel-diop)
