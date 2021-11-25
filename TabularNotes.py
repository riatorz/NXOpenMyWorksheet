import NXOpen
import NXOpen.UF

theSession = NXOpen.Session.GetSession()
theUfSession = NXOpen.UF.UFSession.GetUFSession()
workPart = theSession.Parts.Work
lw = theSession.ListingWindow
lw.Open()



def main():
    myTabNotes = []
    numSection = 0
    numRows = 0
    numCols = 0
    findTabularNotes(myTabNotes)
    lw.WriteLine(f"Number of tabular notes found: {len(myTabNotes)}")
    lw.WriteLine(str(f'First tabular note info:\n'))
    numSections = theUfSession.Tabnot.AskNmSections(myTabNotes[0])
    lw.WriteLine(str(f'Number of sections in tabular note: {numSections}'))
    numRows = theUfSession.Tabnot.AskNmRows(myTabNotes[0])
    lw.WriteLine(str(f'Number of rows in tabular note: {numRows}'))
    numCols = theUfSession.Tabnot.AskNmColumns(myTabNotes[0])
    lw.WriteLine(str(f'Number of columns in tabular note: {numCols}\n'))

    rowTag = 0
    colTag = 0
    cellTag = 0
    for j in range(0, numRows):
        rowTag = theUfSession.Tabnot.AskNthRow(myTabNotes[0], j)
        for k in range(0, numCols):
            colTag =theUfSession.Tabnot.AskNthColumn(myTabNotes[0], k)
            cellTag = theUfSession.Tabnot.AskCellAtRowCol(rowTag, colTag)
            cellText = ""
            evalCellText = ""
            cellText = theUfSession.Tabnot.AskCellText(cellTag)
            evalCellText = theUfSession.Tabnot.AskEvaluatedCellText(cellTag)
            lw.WriteLine(f"Cell[{j}{k}] \n Text-> {cellText} \n Evuluated text: {evalCellText}")
            
def findTabularNotes(tagList):
    tmpTabNote = 0
    NxType = 0
    NxSubtype = 0
    while True:
        tmpTabNote = theUfSession.Obj.CycleObjsInPart(workPart.Tag, NXOpen.UF.UFConstants.UF_tabular_note_type, tmpTabNote)
        if tmpTabNote != 0:
            NxType , NxSubtype = theUfSession.Obj.AskTypeAndSubtype(tmpTabNote)
            if NxSubtype == NXOpen.UF.UFConstants.UF_tabular_note_subtype:
                tagList.append(tmpTabNote)
        else:
            break
if __name__ == "__main__":
    main()
