MathematicaClick
======
In Mathematica, the following sequence would happen upon multiple clicks:<br />
a = GeoBoundingBox[GeoDisk[{38.9016395, -76.6524634}, 15000]]<br />
a = GeoBoundingBox[GeoDisk[{`38.9016395`, -76.6524634}, 15000]]<br />
a = GeoBoundingBox[GeoDisk[{`38.9016395, -76.6524634`}, 15000]]<br />
a = GeoBoundingBox[GeoDisk[`{38.9016395, -76.6524634}`, 15000]]<br />
a = GeoBoundingBox[GeoDisk[`{38.9016395, -76.6524634}, 15000`]]<br />
a = GeoBoundingBox[`GeoDisk[{38.9016395, -76.6524634}, 15000]`]<br />
a = `GeoBoundingBox[GeoDisk[{38.9016395, -76.6524634}, 15000]]`<br />
`a = GeoBoundingBox[GeoDisk[{38.9016395, -76.6524634}, 15000]]`

So, I made a plugin for sublime to do it.  It is by no means perfect right now, but that will change soon.
