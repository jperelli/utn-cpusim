utn-cpusim
==========

Cpu scheduling algorithms simulator written in Python


Objective
=========

To have a graphical simulator for the following cpu scheduling algorithms
 - FCFS
 - SJF
 - SRTF

To be easily extensible to add new algorithms
Herency approach: Each algorithm is a subclass of a generic algorithm.
Define "hook functions" to specific moments in time.
To create a new algorithm, simply redefine those hooks.

The simulator should have an option to show the OS (scheduler, int handler) execution time.

As of first version, it should have support for all this.

As of second mature version, it will add graphical support (details open to discussion)


Internals Idea
==============

System(Object): is the main execution, it calls the specified Scheduler events. Simulates the systems execution.

Scheduler(Scheduler): It's a subclass. Defines the actions to take in specific events


Algorithm Hooks
===============

iniciar(self, proceso)
 - start running

siguiente(self, eliminar=False)
 - select next process to be executed

asignarCPU(self, proceso)
 - set the "proceso" to execution state

inicioES(self, proceso)
 - set the "proceso" to wait (for IO) state

finES(self, proceso)
 - "proceso" has finished IO, must handle int
