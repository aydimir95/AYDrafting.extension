# -*- coding: utf-8 -*-
__title__ = "Rename Views"
__doc__ = """Version = 1.0
Date    = Dec. 8, 2024
_____________________________________________________________________
Description:
Rename views in Revit by using Find/Replace Logic.
_____________________________________________________________________
How-to:
-> Click on the button
-> Select Views
-> Define Renaming Rules
-> Rename Views
_____________________________________________________________________
Last update:
- [Dec. 8, 2024] - 1.0 RELEASE
_____________________________________________________________________
Author: Aydimir Aydimirov"""

# ╦╔╦╗╔═╗╔═╗╦═╗╔╦╗╔═╗
# ║║║║╠═╝║ ║╠╦╝ ║ ╚═╗
# ╩╩ ╩╩  ╚═╝╩╚═ ╩ ╚═╝ IMPORTS
#==================================================
# Regular + Autodesk
from Autodesk.Revit.DB import *

# pyRevit
from pyrevit import forms

# FlexForm for UI
from rpw.ui.forms import FlexForm, Label, TextBox, Separator, Button

# ╦  ╦╔═╗╦═╗╦╔═╗╔╗ ╦  ╔═╗╔═╗
# ╚╗╔╝╠═╣╠╦╝║╠═╣╠╩╗║  ║╣ ╚═╗
#  ╚╝ ╩ ╩╩╚═╩╩ ╩╚═╝╩═╝╚═╝╚═╝ VARIABLES
#==================================================
doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument
app   = __revit__.Application

# ╔╦╗╔═╗╦╔╗╔
# ║║║╠═╣║║║║
# ╩ ╩╩ ╩╩╝╚╝ MAIN
#==================================================

# Step 1: Select Views
sel_el_ids = uidoc.Selection.GetElementIds()
sel_elem   = [doc.GetElement(e_id) for e_id in sel_el_ids]
sel_views  = [el for el in sel_elem if issubclass(type(el), View)]

# If no views selected, prompt using pyRevit's select_views
if not sel_views:
    sel_views = forms.select_views()

# Ensure views are selected
if not sel_views:
    forms.alert('No Views Selected. Please Try Again', exitscript=True)

# Step 2: Define Renaming Rules with FlexForm
components = [
    Label('Prefix:'), TextBox('prefix'),
    Label('Find:'), TextBox('find'),
    Label('Replace:'), TextBox('replace'),
    Label('Suffix:'), TextBox('suffix'),
    Separator(), Button('Rename Views')
]

form = FlexForm('Rename Views', components)
form.show()

# Handle case where user closes the form without input
if not form.values:
    forms.alert('Form closed without input. Exiting.', exitscript=True)

# Retrieve inputs
prefix = form.values.get('prefix', '')
find = form.values.get('find', '')
replace = form.values.get('replace', '')
suffix = form.values.get('suffix', '')

# Step 3: Rename Views
t = Transaction(doc, 'Rename Views')
t.Start()

for view in sel_views:
    # Create new view name
    old_name = view.Name
    new_name = prefix + old_name.replace(find, replace) + suffix

    # Ensure unique view name
    for i in range(20):
        try:
            view.Name = new_name
            print('{} -> {}'.format(old_name, new_name))
            break
        except:
            new_name += '*'

t.Commit()

print('-' * 50)
print('Done!')
