---
title: "Grid"
linkTitle: "Grid"
weight: 9
description: >
  Want to run tests in parallel across multiple machines? Then, Grid is for you.
---

{{% pageinfo color="warning" %}}
<p class="lead">
   <i class="fas fa-language display-4"></i> 
   Page being translated from 
   English to German. Do you speak German? Help us to translate
   it by sending us pull requests!
</p>
{{% /pageinfo %}}

Selenium Grid allows the execution of WebDriver scripts on remote machines (virtual
or real) by routing commands sent by the client to remote browser instances.
It aims to provide an easy way to run tests in parallel on multiple machines.

Selenium Grid allows us to run tests in parallel on multiple machines,
and to manage different browser versions and browser configurations centrally
(instead of in each individual test).

Selenium Grid is not a silver bullet.
It solves a subset of common delegation and distribution problems,
but will for example not manage your infrastructure,
and might not suit your specific needs.

## Zweck und hauptsächlich genutze Funktionalität

* Central entry point for all tests
* Management and control of the nodes / environment where the browsers run
* Scaling
* Running tests in parallel
* Cross platform testing
* Load balancing


_Selenium Grid 4_ is a fresh implementation and does not share the codebase
the previous version had.

Grid 4 has an approach to take advantage of a number of new technologies in order 
to facilitate scaling up, while still allowing local execution.

To get all the details of Grid 4 components, understand how it works, and how to set
up you own, please browse thorough the following sections.