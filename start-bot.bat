@echo off
echo Running Telegram bot...
cd C:\Telegram_bot_SuperPinger
powershell -Command "Start-Process -Verb RunAs python bot.py"
exit
