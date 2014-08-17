cura-layer-retract-plugin
=========================

Plugin for Cura to allow retract on each layer change, using firmware retraction. No more blobby seams!

You may have to do the following to get this plugin working effectively:
+ turn on firmware retraction. Easiest way is including M209 S1 in your start gcode.
+ set your firmware retraction settings with M207 and M208, then M500 to save

Pending testing on Marlin.