import NXOpen
import NXOpen.Annotations as ann
import NXOpen.UF
import NXOpen.Drawings

theSession = NXOpen.Session.GetSession()
theUfSession = NXOpen.UF.UFSession.GetUFSession()
workPart = theSession.Parts.Work

xvg = NXOpen.Drawings.DrawingSheetCollection.CurrentDrawingSheet
xgg = dir(xvg)

theUfSession.Ui.DisplayMessage(str(xgg), 1)