# py-lr-proxy

An HTTP REST Proxy exposing LiterRobot status and information over a plain JSON REST API.

This uses the [pylitterbot](https://github.com/natekspencer/pylitterbot/tree/main) project to gather information from the Whisker APIs, and turns around to expose those on unauthenticated REST.  It exists for use in my home-status-monitor project, written in MicroPython, so I don't have to figure out and maintain GraphQL in MicroPython.
