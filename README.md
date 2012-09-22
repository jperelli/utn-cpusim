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
Inheritance approach: Each algorithm is a subclass of a generic algorithm.
Define "hook functions" to specific moments in time.
To create a new algorithm, simply redefine those hooks.

The simulator should have an option to show the OS (scheduler, int handler) execution time.

As of first version, it should have support for all this.

As of second mature version, it will add graphical support (details open to discussion)


