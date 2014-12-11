Inputs
======

Sensor based
------------
- Pulse
- Sleep
- BP
- Activity

User parameters
---------------
- Age
- Weight
- Height
- Takes pills?

Processing
==========

Issue Checker
-------------
Finds out what problems the user has based on data from sensors. These 
recommendations are based on a lookup table which sets limits beyond which a
particular health problem occurs would be triggered. It does time series 
analysis and finds statistical parameters over a range of time such as 
gradient, range, etc which are then used to find problems.

Issue Picker
------------
Uses result from the Issue Checker and finds out which ones are the important
ones for the users health.

On device processor
-------------------
The on device processor uses the selected issues to provide tips how what the
user should do. In case the remote service is not available the device
processor uses a simpler analysis to give suggestions.

Web Service
-----------
Wraps up the health engine in a web service so that it can be queried by any
device which has the health data from sensors.


Outputs
=======
- Issue
- Severity
- Trend
- Tips