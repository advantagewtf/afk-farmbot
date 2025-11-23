@echo off
echo installing dependencies...
python -m pip install -r requirements.txt

echo running bot...
python bot.py

echo thanks for using afk-farmbot!
pause >nul