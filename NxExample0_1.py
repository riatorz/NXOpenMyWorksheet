import NXOpen
import NXOpen.UF

theSession  = NXOpen.Session.GetSession()#: :type theSession: NXOpen.Session
workPart = theSession.Parts.Work#: :type workPart: NXOpen.BasePart
displayPart = theSession.Parts.Display#: :type displayPart: NXOpen.BasePart
theUFSession = NXOpen.UF.UFSession.GetUFSession()#: :type theUFSession: NXOpen.UF
def main():
    vvs()
def vvs():
    theUI = NXOpen.UI.GetUI()
    MsgBox = theUI.NXMessageBox
    MsgBox.Show("Hello Info", NXOpen.NXMessageBox.DialogType.Information, "Hello World")
if __name__ == '__main__':
    main()