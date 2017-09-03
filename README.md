# BRM-SmartTools
Simple script that add context sensitivity to blender's modeling tools. Basically mesh editing shortcuts will act differently depending on being in vertex, edge or face mode. Best to be tied to keyboard shortcuts.

Shortcuts:

**brm.smartconnect:**
- create an edge between selected vertexes in vertex mode
- create a cut between selected edges in edge mode

**brm.smartbevel:**
- vertex bevel in vertex mode
- edge bevel in edge mode

**brm.smartextrude**
- extend edges using the move commands in edge mode
- extrude along vertex normal in face mode using even offset

**brm.smartdelete**
- dissolve in vertex mode
- dissolve in edge mode
- delete in face mode
