import NXOpen
import NXOpen.Annotations as ann
import NXOpen.UF
import NXOpen.Drawings
import qrcode

theSession = NXOpen.Session.GetSession()
theUfSession = NXOpen.UF.UFSession.GetUFSession()
workPart = theSession.Parts.Work
lw = theSession.ListingWindow
lw.Open()
#
imgpath = workPart.FullPath.split("\\")[-1].replace(".prt",".png")
#
myTabNotes = []
numSections = 0
numRows = 0
numCols = 0
rowTag = 0
colTag = 0
cellTag = 0
tmpTabNote = 0
NxType = 0
NxSubtype = 0
#Function Tabular Notes
while True:
    tmpTabNote = theUfSession.Obj.CycleObjsInPart(workPart.Tag, NXOpen.UF.UFConstants.UF_tabular_note_type, tmpTabNote)
    if tmpTabNote != 0:
        NxType , NxSubtype = theUfSession.Obj.AskTypeAndSubtype(tmpTabNote)
        if NxSubtype == NXOpen.UF.UFConstants.UF_tabular_note_subtype:
            myTabNotes.append(tmpTabNote)  
        #if NxSubtype == NXOpen.UF.UFConstants.UF_tabular_note_subtype or NxSubtype==NXOpen.UF.UFConstants.UF_tabular_note_section_subtype:
        # if NxSubtype == 3:
        #     myTabNotes.append(tmpTabNote)
        
        lw.WriteLine(f"{NXOpen.UF.UFConstants.UF_tabular_note_subtype}")
        lw.WriteLine(str(f"{tmpTabNote} -- {NxType} !!- {NxSubtype} -X {tmpTabNote}")) #for test
    else:
        break
lw.WriteLine(str(f"Number of tabular notes found: {len(myTabNotes)}\n"))
###############################
trueTable = 0
trueRows = 6
trueCols = 8
for i in range(len(myTabNotes)):
    #lw.WriteLine(str(f'{i+1}. tabular note info:\n'))
    numSections = theUfSession.Tabnot.AskNmSections(myTabNotes[i])
    #lw.WriteLine(str(f'Number of sections in tabular note: {numSections}'))
    numRows = theUfSession.Tabnot.AskNmRows(myTabNotes[i])
    #lw.WriteLine(str(f'Number of rows in tabular note: {numRows}'))
    numCols = theUfSession.Tabnot.AskNmColumns(myTabNotes[i])
    #lw.WriteLine(str(f'Number of columns in tabular note: {numCols}'))
    if numRows==trueRows and numCols==trueCols:
        trueTable = i 
#if you had a one tabular note please use
# numSections = theUfSession.Tabnot.AskNmSections(myTabNotes[0])
# lw.WriteLine(str(f'Number of sections in tabular note: {numSections}'))
# numRows = theUfSession.Tabnot.AskNmRows(myTabNotes[0])
# lw.WriteLine(str(f'Number of rows in tabular note: {numRows}'))
# numCols = theUfSession.Tabnot.AskNmColumns(myTabNotes[0])
# lw.WriteLine(str(f'Number of columns in tabular note: {numCols}'))

#coltags and celltag
myTags = ["06","20","22","23","24","25","26","27","40","41","45"]
tagDict = {}
qrTextDict = {}
qrText = ""
for j in range(0, trueRows):
        rowTag = theUfSession.Tabnot.AskNthRow(myTabNotes[trueTable], j)
        for k in range(0, trueCols):
            colTag =theUfSession.Tabnot.AskNthColumn(myTabNotes[trueTable], k)
            cellTag = theUfSession.Tabnot.AskCellAtRowCol(rowTag, colTag)
            cellText = ""
            evalCellText = ""
            cellText = theUfSession.Tabnot.AskCellText(cellTag)
            evalCellText = theUfSession.Tabnot.AskEvaluatedCellText(cellTag)
            #lw.WriteLine(f"{colTag}-- [{j}{k}] {cellText}")
            if cellText != "" and f"{j}{k}" in myTags:
                tagDict.update({f"{j}{k}":cellTag})
                #lw.WriteLine(str(f'Cell[{j},{k}] = {cellText}'))
for i in tagDict:
    AcellText = theUfSession.Tabnot.AskCellText(tagDict[i])
    qrTextDict.update({f"{tagDict[i]}":AcellText})
for i in qrTextDict:
    lw.WriteLine(f"{qrTextDict[i]}")
    qrText += f"{qrTextDict[i]};"
qrText = qrText[:-1]
qrpath = ''.join(str(i)+"\\" for i in workPart.FullPath.split("\\")[:3])+imgpath
img=qrcode.make(f"{qrText}")
img.save(qrpath)
lw.WriteLine(f"qrCode belirtilen dizine kaydedildi.")
lw.WriteLine(f"Dizin: {qrpath}\nDosya ismi: {imgpath}")
imgfile = qrpath

imgCoordinates = [float(190),float(30),float(0)]
imageTag = 0
sheetTag = 0
imageTag = theUfSession.Drf.CreateImageFromFile(imgfile,sheetTag,imgCoordinates)
if imageTag != 0:
    myImageData = theUfSession.Drf.AskImageData(imageTag)
    theUfSession.Drf.SetImageAspectRatioLock(imageTag, False)
    theUfSession.Drf.SetImageWidth(imageTag,float(35))
    theUfSession.Drf.SetImageHeight(imageTag,float(35))
