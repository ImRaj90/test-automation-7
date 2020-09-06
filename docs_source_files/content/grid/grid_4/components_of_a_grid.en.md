---
title: "Components"
weight: 1
---

## Router
* Routes request each request to the corresponding handler.

__Router__ is a point where all the requests to run a new session are sent.
It forwards the request to __Distributor__ for further processing. It routes different
requests based on where they are meant to be sent. It also helps to communicate with the
Session Map. All the communication with a session is done via router.

## Distributor
* Contains information on nodes and its capabilities.
* Selects node on which session is run.

__Distributor__ is responsible for selecting the node on which your session will be run.
It has all the information related to nodes and is aware of each node's capabilities.

## SessionMap
* Datastore mapping for session id and the node.

__SessionMap__ is data store used to store the map of session id and the node on which the session is running.

## Nodes

* Where the browsers live
* Registers itself to the hub and communicates its capabilities
* Receives requests from the hub and executes them

__Nodes__ are different Selenium instances
that will execute tests on individual computer systems.
There can be many nodes in a grid.
The machines which are nodes do not need to be the same platform
or have the same browser selection as that of the hub or the other nodes.
A node on Windows might have the capability of
offering Internet Explorer as a browser option,
whereas this wouldn't be possible on Linux or Mac.

## Hub
* Accepts requests to run tests
* Acts as a Router
* Acts as a Distributor
* Acts as a SessionMap
* Takes instructions from client and executes them remotely on the nodes

A __Hub__ is a central point where all your tests are sent.
It allows you to run a Router, Distributor and a SessionMap on the same machine using a single command. 
The hub needs to be reachable from the respective clients (i.e. CI server, Developer machine etc.). 
It communicates with the node to run your selenium sessions. Instead of running each component separately, 
you can use _hub_ role to run all 3 together.

## Standalone

A __Standalone__ version of Grid consists of all components running as single process, including the node.
You can directly start running sessions after starting the standalone version of the Grid.
