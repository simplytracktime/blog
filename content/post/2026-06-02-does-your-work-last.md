---
title: "What is the life expectancy of your work?"
date: 2026-06-01T21:21:13+12:00
draft: true
---

The talk, [Building the Hundred-Year Web Service](https://unplannedobsolescence.com/talks/building-the-hundred-year-web-service/) by Alex Petros, 2024, has inspired me to think about the work that I have been doing over the last 30 years. The tldr; I took from the talk is a question we need to ask when building something, (actually anything) is "What is the maintainable life of this going to be?".

Alex Petros the uses a bridge to demonstrate product requirements that can be adapted to unimaginable uses, a bridge designed to carry foot traffic is now carrying motor vehicles, I reckon the built environment can also be used when discussing something as mundane as maintenance.

Imagine you are remodelling the ktichen in your house. You decide to lay tiles (porcelain floor tiles) on the floor. Five years after the kitchen is finished a tile gets cracked and damaged to the extent that you want to replace it. Let's say something heavy was dropped on the floor. Will you be able to source a replacement tile 5 years after you purchased the original batch? Does this mean you need to replace your entire floor to replace a single tile. It turns out that floor tiles tend to be a bit like the fashion industry and long running (in terms of decades) tile designs are not very easily found!. Yes, you could purchase some spare tiles just in case you need them, but, how many do you need to keep?

A similar situation applies when building software. It doesn't really matter whether it is a website, an integration process running on a vendor's platform, or an application built on a RAD[^1]. But this time it really applies to the tooling rather than the output, as this is usually tightly coupled to the system it is built on or the environment it runs on. Find a project you worked on 1 month ago, 12 months ago, 5 years ago. How long will it take you to make a simple change to it. If it is from more than 3 years ago, chances are your development environment has been replaced. Even if the technology stack uses LTS[^2] releases of libraries, some technology choices are unsupported and possibly unavailable after 3 years. You could argue that all the build environments are cloud hosted and this has you covered. How many years are you going to maintain these CI systems? Are you going to proactively update the dependencies of every project you have created in response to vunerablity notifications?

There was a time when it was very likely you could make changes to software with nothing but a text editor, particularly when the "compiler" was present in the runtime environment[^3].

Much like a bridge or a kitchen floor, people expect a software system to be maintainable and provide reliable srvice for its operational life. If the mainframe systems used in the banking industry are indicative this will be much longer than anyone expects.

Actions:

1. Estimate the life of expectency of the system you are working on and make design choices accordingly.
1. Understand the runtime economics of an operating environment when a possible cost of maintenance is a full rewrite. These need to be part of the purchasing considerations.
1. Given the above, what are the consequences if the runtime, a core dependency, the environment is "end-of-life", under mining the system.

[^1]: Rapid Application Development.

[^2]: Long Term Support

[^3]: By this I mean the process that converts the source code into an executable. For example the browser for HTML or Javascript, the SDK for Java or C#.
