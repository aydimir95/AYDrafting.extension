# -*- coding: utf-8 -*-
__title__   = "Detail Level"
__doc__     = """Version = 1.0
Date        = 24.12.2024
________________________________________________________________
Description:

This button changes the Detail Level: "Course, Medium, Fine" 

________________________________________________________________
How-To Modify the Script:

1. [Hold ALT + CLICK] on the button to open its source folder.
You will be able to override this placeholder.

2. Automate Your Boring Work ;)

________________________________________________________________
TODO:
[FEATURE] - Create a pulldown menu to diplay the Detail Levels.
________________________________________________________________
Last Updates:
- [24.12.2024] v1.0: Created a button to change the Detail Level
_______________
Author: Aydimirov Aydimir"""

# imports
#==================================================
from Autodesk.Revit.DB import *

#.NET Imports
import clr
clr.AddReference('System')
from System.Collections.Generic import List


# variables
#==================================================
app    = __revit__.Application
uidoc  = __revit__.ActiveUIDocument
doc    = __revit__.ActiveUIDocument.Document #type:Document


# main
#==================================================
view = doc.ActiveView

d_lvl = view.DetailLevel

print(d_lvl)
print(type(d_lvl))


t = Transaction(doc, 'change name')
t.Start()

view.DetailLevel = ViewDetailLevel.Coarse


t.Commit()

print(view.DetailLevel)
