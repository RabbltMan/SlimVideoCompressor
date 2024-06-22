Imports MaterialSkin

Public Class Form1

    Dim InputFilePath As String
    Dim OutputDirPath As String
    Dim IsInputPathEntryFilled As Boolean = False
    Dim IsOutputDirEntryFilled As Boolean = False

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Dim SkinManager As MaterialSkinManager = MaterialSkinManager.Instance
        SkinManager.AddFormToManage(Me)
        SkinManager.Theme = MaterialSkinManager.Themes.LIGHT
        SkinManager.ColorScheme = New ColorScheme(Primary.Teal400, Primary.Teal500, Primary.BlueGrey100, Accent.Teal700, TextShade.WHITE)
        ' Additional load for original WinForm Components
        WarningLabel1.Font = New Font("Microsoft YaHei UI", 9.0F, FontStyle.Regular, GraphicsUnit.Point, CByte(134))
        WarningLabel1.ForeColor = Color.DarkGray
        EstSizeLabel.Font = New Font("Microsoft YaHei UI", 9.0F, FontStyle.Regular, GraphicsUnit.Point, CByte(134))
        EstSizeLabel.ForeColor = Color.DarkSlateGray
        EstSizeResLabel.Font = New Font("Microsoft YaHei UI", 9.0F, FontStyle.Regular, GraphicsUnit.Point, CByte(134))
        EstSizeResLabel.ForeColor = Color.DarkSlateGray
        Me.ActiveControl = FocusLabel
    End Sub

    Private Sub InputSelectButton_Click(sender As Object, e As EventArgs) Handles InputSelectButton.Click
        Using InputFileExplorerDialog As New OpenFileDialog()
            InputFileExplorerDialog.Filter = "Media File|*.mp4;*.avi;*.mkv;*.mov;*.wmv;*.flv;*.mpeg;*.webm;*.3gp;*.m4v;*.ogv;*.asf|All|*"
            Dim res As DialogResult = InputFileExplorerDialog.ShowDialog()
            If res = DialogResult.OK Then
                InputFilePath = InputFileExplorerDialog.FileName
                InputPathEntry.Text = InputFilePath
                IsInputPathEntryFilled = True
            End If
        End Using
        If IsInputPathEntryFilled And IsOutputDirEntryFilled Then
            RunButton.Enabled = True
        End If
        Me.ActiveControl = FocusLabel
    End Sub

    Private Sub OutputSelectButton_Click(sender As Object, e As EventArgs) Handles OutputSelectButton.Click
        Using OutputFileExplorerDialog As New FolderBrowserDialog()
            Dim res As DialogResult = OutputFileExplorerDialog.ShowDialog()
            If res = DialogResult.OK Then
                OutputDirPath = OutputFileExplorerDialog.SelectedPath
                OutputDirEntry.Text = OutputDirPath
                IsOutputDirEntryFilled = True
            End If
        End Using
        If IsInputPathEntryFilled And IsOutputDirEntryFilled Then
            RunButton.Enabled = True
        End If
        Me.ActiveControl = FocusLabel
    End Sub

    Private Sub RunButton_Click(sender As Object, e As EventArgs) Handles RunButton.Click
        Me.ActiveControl = FocusLabel
    End Sub

    Private Sub HEVCSwitch_CheckedChanged(sender As Object, e As EventArgs) Handles HEVCSwitch.CheckedChanged
        If HEVCSwitch.Checked() Then
            WarningLabel1.ForeColor = Color.Red
            WarningLabel1.Font = New Font("Microsoft YaHei UI", 9.0F, FontStyle.Regular, GraphicsUnit.Point, CByte(134))
        Else
            WarningLabel1.ForeColor = Color.DarkGray
        End If

        Me.ActiveControl = FocusLabel
    End Sub

    Private Sub QualitySelection_SelectedIndexChanged(sender As Object, e As EventArgs) Handles QualitySelection.DropDownClosed
        Me.ActiveControl = FocusLabel
    End Sub

End Class
