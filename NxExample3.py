import NXOpen
import NXOpen.Annotations as ann
import NXOpen.UF
import NXOpen.Drawings

theSession = NXOpen.Session.GetSession()
theUFSession = NXOpen.UF.UFSession.GetUFSession()
workPart = theSession.Parts.Work
tnTag = 0 #Int tag value
lw = theSession.ListingWindow
lw.Open()
# Get current sheet
for sheet in workPart.DrawingSheets:
    # Open sheet (it's necessary to get its data)
    sheet.Open()
        #For each visible objects in the sheet
    for obj in sheet.View.AskVisibleObjects():
            # If it is a table
            if isinstance(obj, NXOpen.Annotations.TableSection):
                lw.WriteLine('Tabular section tag: ' + str(obj.Tag) + ' and name: ' + obj.Name)
                # Table section TAG
                tsTag = obj.Tag
                # Get tabnote TAG
                tnTag = theUFSession.Tabnot.AskTabularNoteOfSection(tsTag)
