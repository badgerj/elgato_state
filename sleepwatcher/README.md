For SleepWatcher to work, you will need to write sleep and
wakeup scripts, located here when using brew services:

  ~/.sleep
  ~/.wakeup

To start sleepwatcher now and restart at login:
  brew services start sleepwatcher
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/sleepwatcher/sbin/sleepwatcher -V -s /Users/cjones/.sleep -w /Users/cjones/.wakeup

https://www.cynosurex.com/myink/ViewPage.php?file=docs/SleepWatcher/SleepWatcher%20Man%20Page

or man sleepwatcher

I used this:

brew services --file /Users/cjones/Library/LaunchAgents/homebrew.mxcl.sleepwatcher_mod.plist sleepwatcher

With the contents being changed to wait for screen blanking (not sleeping).

Note: the -D and -E flags used to be -s and -w respectively.

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>KeepAlive</key>
	<true/>
	<key>Label</key>
	<string>homebrew.mxcl.sleepwatcher</string>
	<key>LimitLoadToSessionType</key>
	<array>
		<string>Aqua</string>
		<string>Background</string>
		<string>LoginWindow</string>
		<string>StandardIO</string>
		<string>System</string>
	</array>
	<key>ProgramArguments</key>
	<array>
		<string>/usr/local/opt/sleepwatcher/sbin/sleepwatcher</string>
		<string>-V</string>
		<string>-D</string>
		<string>/Users/<USER>/.sleep</string>
		<string>-E</string>
		<string>/Users/<USER>/.wakeup</string>
	</array>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>


This hooks into elgato_state which just runs a simple python command:

import asyncio

from elgato import Elgato, State, Info


async def main():
    """Show example on controlling your Elgato Light device."""
    async with Elgato("192.168.1.221") as elgato:
        info: Info = await elgato.info()
        print(info)

        state: State = await elgato.state()
        print(state)

        # Turn the light on
        await elgato.light(on=True)


if __name__ == "__main__":
    asyncio.run(main())

------

Change the on=False to turn it off. This is done from within a premade .venv so that elgato pypi module only needs to be installed in the .venv, not the host machine.
