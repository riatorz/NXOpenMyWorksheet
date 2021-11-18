Option Strict Off
Imports System
Imports System.Collections.Generic
Imports NXOpen
Imports NXOpen.UF


Module export_tabular_notes
 
    Dim theSession As Session = Session.GetSession()
    Dim theUfSession As UFSession = UFSession.GetUFSession()
    Dim workPart As Part = theSession.Parts.Work
 
    Sub Main()
 
        Dim lw As ListingWindow = theSession.ListingWindow
        lw.Open()
 
        Dim myTabNotes As New List(Of Tag)
        FindTabularNotes(myTabNotes)
 
        lw.WriteLine("Number of tabular notes found: " & myTabNotes.Count.ToString)
        lw.WriteLine("")
 
        lw.WriteLine("First tabular note info:")
        lw.WriteLine("")
 
        Dim numSections As Integer = 0
        theUfSession.Tabnot.AskNmSections(myTabNotes.Item(0), numSections)
        lw.WriteLine("Number of sections in tabular note: " & numSections.ToString)
 
        Dim numRows As Integer = 0
        theUfSession.Tabnot.AskNmRows(myTabNotes.Item(0), numRows)
        lw.WriteLine("Number of rows in tabular note: " & numRows.ToString)
 
        Dim numCols As Integer = 0
        theUfSession.Tabnot.AskNmColumns(myTabNotes.Item(0), numCols)
        lw.WriteLine("Number of columns in tabular note: " & numCols.ToString)
        lw.WriteLine("")
 
        Dim rowTag As Tag = Nothing
        Dim colTag As Tag = Nothing
        Dim cellTag As Tag = Nothing
 
        For j As Integer = 0 To numRows - 1
 
            theUfSession.Tabnot.AskNthRow(myTabNotes.Item(0), j, rowTag)
 
            For k As Integer = 0 To numCols -1
 
                theUfSession.Tabnot.AskNthColumn(myTabNotes.Item(0), k, colTag)
                theUfSession.Tabnot.AskCellAtRowCol(rowTag, colTag, cellTag)
                Dim cellText As String = ""
                Dim evalCellText As String = ""
                theUfSession.Tabnot.AskCellText(cellTag, cellText)
                theUfSession.Tabnot.AskEvaluatedCellText(cellTag, evalCellText)
 
                lw.WriteLine("Cell[" & j.ToString & "," & k.ToString & "]")
                lw.WriteLine("text: " & cellText)
                lw.WriteLine("evaluated text: " & evalCellText)
                lw.WriteLine("")
 
            Next
        Next
 
    End Sub
 
 
    Sub FindTabularNotes(ByRef tagList As List(Of Tag))
 
        Dim tmpTabNote As NXOpen.Tag = NXOpen.Tag.Null
        Dim NxType As Integer
        Dim NxSubtype As Integer
 
        Do
            theUfSession.Obj.CycleObjsInPart(workPart.Tag, UFConstants.UF_tabular_note_type, tmpTabNote)
            If tmpTabNote <> NXOpen.Tag.Null Then 
                theUfSession.Obj.AskTypeAndSubtype(tmpTabNote, NxType, NxSubtype)
                If NxSubtype = UFConstants.UF_tabular_note_subtype Then
                    tagList.Add(tmpTabNote) 
                End If
            End If
        Loop Until tmpTabNote = NXOpen.Tag.Null
 
    End Sub 
 
End Module
