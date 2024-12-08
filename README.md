[Description]
Just a simple discord bot built to parse an xmltv file with basic commands.

[Current Commands]
/help - lists available commands
/nowplaying - returns the name, season, and episode of currently playing content
/upnext - returns the name, season, and episode of the next listing

[To-Do]
- implement basic error handling
- errors out when returning data for non-tv content, no episode num data available. Add check to mitigate this
- embed icon from xmltv file in discord message
- add timed content announcements + commands to enable/disable
- add dizque server polling and announcement if failure is detected
