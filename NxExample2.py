import NXOpen
import NXOpen.Annotations as ann
import NXOpen.UF
import NXOpen.Drawings

theSession = NXOpen.Session.GetSession()
theUfSession = NXOpen.UF.UFSession.GetUFSession()
workPart = theSession.Parts.Work

lw = theSession.ListingWindow #Info Window
lw.Open()


lw.WriteLine(f"{i}" for i in range(5))
lw.Close()