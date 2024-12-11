# [Description]
Just a simple discord bot built to parse an xmltv file with basic commands.




# [Current Commands]
- /help - lists available commands
- /nowplaying - returns the name, season, and episode of currently playing content
- /upnext - returns the name, season, and episode of the next listing
- /announcements enable (admin only) - enable automatic announcements, runs on startup then announces current program whenever a new one starts
- /announcements disable (admin only) - disable automatic announcements




# [Config.json]
- XMLTVURL - should point to the dizquetv instance's xmltv file
- MAINCHANNEL - points to the channel number it'll use to pull program data, dizque-cord currently only supports a single channel
- ANNOUNCEMENTS_ENABLED - determines whether announcements will be enabled or disabled at startup, can be changed by commands
- ANNOUNCEMENTS_CHANNEL_ID - discord channel id for announcements
- CHANNEL_NAME - changes the server/channel name displayed on the commands
- ADMIN_ROLE_NAME - which server role is considered to have admin permissions for dizque-cord




# [Environment Variables]
- DISCORDKEY - Your discord bot token (required)
- TVDBKEY - Your TVDB api key (optional), used to return program artwork
  
<sub> *Environment variables can be added at the OS level or configured in the .env file </sub>




# [Installation - Python]
- Clone repository
- Navigate to directory of cloned repository
- Run 'pip install -r requirements.txt'
- Configure environment variables
- Fill out config.json
- Run 'python bot.py'




# [Installation - Executable]
- Download release files
- Fill out config.json
- Configure environment variables
- Run Dizque-Cord.exe
