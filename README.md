# py-sm-proxy

An HTTP REST API/Proxy that exposes statuses of a number of my homelab's services.

Originally built to proxy the LiterRobot status and information over a plain JSON REST API using PyLitterBot, the scope expanded as it does.

This uses the [pylitterbot](https://github.com/natekspencer/pylitterbot/tree/main) project to gather information from the Whisker APIs, and turns around to expose those on unauthenticated REST.  It exists for use in my home-status-monitor project, written in MicroPython, so I don't have to figure out and maintain GraphQL in MicroPython.
