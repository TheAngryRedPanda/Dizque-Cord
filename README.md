[Description]
Just a simple discord bot built to parse an xmltv file with basic commands.

[Current Commands]
/help - lists available commands
/nowplaying - returns the name, season, and episode of currently playing content
/upnext - returns the name, season, and episode of the next listing

[Installation]
- copy all files into the same directory
- rename .env.example to .env
- add discord bot token to DISCORDKEY in .env
- (optional) add tvdb api key to TVDBKEY in .env
- add xmltv url to XMLTVURL in config.json
- pip install -r requirements.txt
- python bot.py

[To-Do]
- add timed content announcements + commands to enable/disable
- add dizque server polling and announcement if failure is detected
