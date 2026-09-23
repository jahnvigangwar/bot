# Voice assistant prototype

A small Python experiment that combines speech recognition, desktop shortcuts, and an OpenAI API example.

## What is here

- `main.py` listens for speech and opens a few websites or reports the time.
- `openaiTest.py` is an unfinished text-generation example using the legacy OpenAI Completions interface.
- `config.py` reads the API key from the `OPENAI_API_KEY` environment variable.

This is an early prototype, not a packaged application. The voice assistant uses macOS commands and needs microphone access. Set a local music file path before enabling the music shortcut.

## Setup

Create and activate a virtual environment, then install the packages used by the scripts:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install SpeechRecognition PyAudio openai
```

Set an API key only in your local shell before running the OpenAI example:

```sh
export OPENAI_API_KEY='your-new-key'
python openaiTest.py
```

The example still uses the retired `text-davinci-003` model and an older SDK interface; update those before relying on it. Never commit an API key, `.env` file, or local credentials. Revoke any key that has been committed previously; deleting it from the current branch does not remove it from Git history.

## Known limitations

- macOS-specific `say` and `open` commands are used by the voice assistant.
- The music file path is tied to one developer's computer and must be replaced with a local path.
- There is no dependency lockfile, automated test suite, or error handling for missing audio devices yet.
