<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits MaterialSkin.Controls.MaterialForm

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        MaterialDrawer1 = New MaterialSkin.Controls.MaterialDrawer()
        RunButton = New MaterialSkin.Controls.MaterialButton()
        OutputSelectButton = New MaterialSkin.Controls.MaterialButton()
        InputSelectButton = New MaterialSkin.Controls.MaterialButton()
        InputPathEntry = New MaterialSkin.Controls.MaterialTextBox()
        OutputDirEntry = New MaterialSkin.Controls.MaterialTextBox()
        HEVCSwitch = New MaterialSkin.Controls.MaterialSwitch()
        FocusLabel = New MaterialSkin.Controls.MaterialLabel()
        QualitySelection = New MaterialSkin.Controls.MaterialComboBox()
        WarningLabel1 = New Label()
        EstSizeLabel = New Label()
        EstSizeResLabel = New Label()
        SuspendLayout()
        ' 
        ' MaterialDrawer1
        ' 
        MaterialDrawer1.AutoHide = False
        MaterialDrawer1.AutoShow = False
        MaterialDrawer1.BackgroundWithAccent = False
        MaterialDrawer1.BaseTabControl = Nothing
        MaterialDrawer1.Depth = 0
        MaterialDrawer1.HighlightWithAccent = True
        MaterialDrawer1.IndicatorWidth = 0
        MaterialDrawer1.IsOpen = False
        MaterialDrawer1.Location = New Point(-250, 0)
        MaterialDrawer1.MouseState = MaterialSkin.MouseState.HOVER
        MaterialDrawer1.Name = "MaterialDrawer1"
        MaterialDrawer1.ShowIconsWhenHidden = False
        MaterialDrawer1.Size = New Size(250, 120)
        MaterialDrawer1.TabIndex = 13
        MaterialDrawer1.UseColors = False
        ' 
        ' RunButton
        ' 
        RunButton.AutoSizeMode = AutoSizeMode.GrowAndShrink
        RunButton.Cursor = Cursors.Hand
        RunButton.Density = MaterialSkin.Controls.MaterialButton.MaterialButtonDensity.Default
        RunButton.Depth = 0
        RunButton.Enabled = False
        RunButton.HighEmphasis = True
        RunButton.Icon = Nothing
        RunButton.Location = New Point(491, 290)
        RunButton.Margin = New Padding(4, 6, 4, 6)
        RunButton.MouseState = MaterialSkin.MouseState.HOVER
        RunButton.Name = "RunButton"
        RunButton.NoAccentTextColor = Color.Empty
        RunButton.Size = New Size(140, 36)
        RunButton.TabIndex = 2
        RunButton.Text = "Compress Now!"
        RunButton.Type = MaterialSkin.Controls.MaterialButton.MaterialButtonType.Contained
        RunButton.UseAccentColor = False
        RunButton.UseVisualStyleBackColor = True
        ' 
        ' OutputSelectButton
        ' 
        OutputSelectButton.AutoSize = False
        OutputSelectButton.AutoSizeMode = AutoSizeMode.GrowAndShrink
        OutputSelectButton.Cursor = Cursors.Hand
        OutputSelectButton.Density = MaterialSkin.Controls.MaterialButton.MaterialButtonDensity.Default
        OutputSelectButton.Depth = 0
        OutputSelectButton.HighEmphasis = True
        OutputSelectButton.Icon = Nothing
        OutputSelectButton.Location = New Point(531, 155)
        OutputSelectButton.Margin = New Padding(4, 6, 4, 6)
        OutputSelectButton.MouseState = MaterialSkin.MouseState.HOVER
        OutputSelectButton.Name = "OutputSelectButton"
        OutputSelectButton.NoAccentTextColor = Color.Empty
        OutputSelectButton.Size = New Size(100, 50)
        OutputSelectButton.TabIndex = 7
        OutputSelectButton.Text = "Select Path"
        OutputSelectButton.Type = MaterialSkin.Controls.MaterialButton.MaterialButtonType.Contained
        OutputSelectButton.UseAccentColor = False
        OutputSelectButton.UseVisualStyleBackColor = True
        ' 
        ' InputSelectButton
        ' 
        InputSelectButton.AutoSize = False
        InputSelectButton.AutoSizeMode = AutoSizeMode.GrowAndShrink
        InputSelectButton.Cursor = Cursors.Hand
        InputSelectButton.Density = MaterialSkin.Controls.MaterialButton.MaterialButtonDensity.Default
        InputSelectButton.Depth = 0
        InputSelectButton.HighEmphasis = True
        InputSelectButton.Icon = Nothing
        InputSelectButton.Location = New Point(531, 88)
        InputSelectButton.Margin = New Padding(4, 6, 4, 6)
        InputSelectButton.MouseState = MaterialSkin.MouseState.HOVER
        InputSelectButton.Name = "InputSelectButton"
        InputSelectButton.NoAccentTextColor = Color.Empty
        InputSelectButton.Size = New Size(100, 50)
        InputSelectButton.TabIndex = 8
        InputSelectButton.Text = "Select Path"
        InputSelectButton.Type = MaterialSkin.Controls.MaterialButton.MaterialButtonType.Contained
        InputSelectButton.UseAccentColor = False
        InputSelectButton.UseVisualStyleBackColor = True
        ' 
        ' InputPathEntry
        ' 
        InputPathEntry.AnimateReadOnly = False
        InputPathEntry.BorderStyle = BorderStyle.None
        InputPathEntry.Depth = 0
        InputPathEntry.Enabled = False
        InputPathEntry.Font = New Font("Roboto", 16.0F, FontStyle.Regular, GraphicsUnit.Pixel)
        InputPathEntry.Hint = "Input File Path"
        InputPathEntry.LeadingIcon = Nothing
        InputPathEntry.Location = New Point(22, 88)
        InputPathEntry.MaxLength = 50
        InputPathEntry.MouseState = MaterialSkin.MouseState.OUT
        InputPathEntry.Multiline = False
        InputPathEntry.Name = "InputPathEntry"
        InputPathEntry.Size = New Size(502, 50)
        InputPathEntry.TabIndex = 9
        InputPathEntry.Text = ""
        InputPathEntry.TrailingIcon = Nothing
        ' 
        ' OutputDirEntry
        ' 
        OutputDirEntry.AnimateReadOnly = False
        OutputDirEntry.BorderStyle = BorderStyle.None
        OutputDirEntry.Depth = 0
        OutputDirEntry.Enabled = False
        OutputDirEntry.Font = New Font("Roboto", 16.0F, FontStyle.Regular, GraphicsUnit.Pixel)
        OutputDirEntry.Hint = "Output Directory Path"
        OutputDirEntry.LeadingIcon = Nothing
        OutputDirEntry.Location = New Point(22, 155)
        OutputDirEntry.MaxLength = 50
        OutputDirEntry.MouseState = MaterialSkin.MouseState.OUT
        OutputDirEntry.Multiline = False
        OutputDirEntry.Name = "OutputDirEntry"
        OutputDirEntry.Size = New Size(502, 50)
        OutputDirEntry.TabIndex = 10
        OutputDirEntry.Text = ""
        OutputDirEntry.TrailingIcon = Nothing
        ' 
        ' HEVCSwitch
        ' 
        HEVCSwitch.AutoSize = True
        HEVCSwitch.Depth = 0
        HEVCSwitch.Location = New Point(234, 224)
        HEVCSwitch.Margin = New Padding(0)
        HEVCSwitch.MouseLocation = New Point(-1, -1)
        HEVCSwitch.MouseState = MaterialSkin.MouseState.HOVER
        HEVCSwitch.Name = "HEVCSwitch"
        HEVCSwitch.Ripple = True
        HEVCSwitch.Size = New Size(397, 37)
        HEVCSwitch.TabIndex = 11
        HEVCSwitch.Text = "Use HEVC as output encoder for smaller file size"
        HEVCSwitch.UseVisualStyleBackColor = True
        ' 
        ' FocusLabel
        ' 
        FocusLabel.AutoSize = True
        FocusLabel.Depth = 0
        FocusLabel.Font = New Font("Roboto", 14.0F, FontStyle.Regular, GraphicsUnit.Pixel)
        FocusLabel.Location = New Point(544, 296)
        FocusLabel.MouseState = MaterialSkin.MouseState.HOVER
        FocusLabel.Name = "FocusLabel"
        FocusLabel.Size = New Size(44, 19)
        FocusLabel.TabIndex = 14
        FocusLabel.Text = "Focus"
        ' 
        ' QualitySelection
        ' 
        QualitySelection.AutoResize = False
        QualitySelection.BackColor = Color.FromArgb(CByte(255), CByte(255), CByte(255))
        QualitySelection.Depth = 0
        QualitySelection.DrawMode = DrawMode.OwnerDrawVariable
        QualitySelection.DropDownHeight = 174
        QualitySelection.DropDownStyle = ComboBoxStyle.DropDownList
        QualitySelection.DropDownWidth = 121
        QualitySelection.Font = New Font("Microsoft Sans Serif", 14.0F, FontStyle.Bold, GraphicsUnit.Pixel)
        QualitySelection.ForeColor = Color.FromArgb(CByte(222), CByte(0), CByte(0), CByte(0))
        QualitySelection.FormattingEnabled = True
        QualitySelection.Hint = "Compression Level"
        QualitySelection.IntegralHeight = False
        QualitySelection.ItemHeight = 43
        QualitySelection.Items.AddRange(New Object() {"Auto", "Low", "Medium", "High"})
        QualitySelection.Location = New Point(22, 224)
        QualitySelection.MaxDropDownItems = 4
        QualitySelection.MouseState = MaterialSkin.MouseState.OUT
        QualitySelection.Name = "QualitySelection"
        QualitySelection.Size = New Size(207, 49)
        QualitySelection.StartIndex = 0
        QualitySelection.TabIndex = 15
        ' 
        ' WarningLabel1
        ' 
        WarningLabel1.Font = New Font("Microsoft YaHei UI", 9.0F, FontStyle.Regular, GraphicsUnit.Point, CByte(134))
        WarningLabel1.ForeColor = Color.DarkGray
        WarningLabel1.Location = New Point(289, 252)
        WarningLabel1.Name = "WarningLabel1"
        WarningLabel1.Size = New Size(346, 17)
        WarningLabel1.TabIndex = 16
        WarningLabel1.Text = "Not recommended. Some devices may not support HEVC."
        ' 
        ' EstSizeLabel
        ' 
        EstSizeLabel.AutoSize = True
        EstSizeLabel.Location = New Point(318, 307)
        EstSizeLabel.Name = "EstSizeLabel"
        EstSizeLabel.Size = New Size(99, 17)
        EstSizeLabel.TabIndex = 17
        EstSizeLabel.Text = "Estimated Size: "
        EstSizeLabel.Visible = False
        ' 
        ' EstSizeResLabel
        ' 
        EstSizeResLabel.AutoSize = True
        EstSizeResLabel.Location = New Point(413, 307)
        EstSizeResLabel.Name = "EstSizeResLabel"
        EstSizeResLabel.Size = New Size(63, 17)
        EstSizeResLabel.TabIndex = 18
        EstSizeResLabel.Text = "9999 MiB"
        EstSizeResLabel.TextAlign = ContentAlignment.MiddleRight
        EstSizeResLabel.Visible = False
        ' 
        ' Form1
        ' 
        AutoScaleDimensions = New SizeF(7.0F, 17.0F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(652, 345)
        Controls.Add(EstSizeResLabel)
        Controls.Add(EstSizeLabel)
        Controls.Add(WarningLabel1)
        Controls.Add(QualitySelection)
        Controls.Add(HEVCSwitch)
        Controls.Add(OutputDirEntry)
        Controls.Add(InputSelectButton)
        Controls.Add(OutputSelectButton)
        Controls.Add(RunButton)
        Controls.Add(MaterialDrawer1)
        Controls.Add(InputPathEntry)
        Controls.Add(FocusLabel)
        HelpButton = True
        Margin = New Padding(2, 3, 2, 3)
        MaximizeBox = False
        Name = "Form1"
        Padding = New Padding(2, 54, 2, 3)
        Sizable = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "Slim Video Compressor"
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents MaterialDrawer1 As MaterialSkin.Controls.MaterialDrawer
    Friend WithEvents RunButton As MaterialSkin.Controls.MaterialButton
    Friend WithEvents OutputSelectButton As MaterialSkin.Controls.MaterialButton
    Friend WithEvents InputSelectButton As MaterialSkin.Controls.MaterialButton
    Friend WithEvents InputPathEntry As MaterialSkin.Controls.MaterialTextBox
    Friend WithEvents OutputDirEntry As MaterialSkin.Controls.MaterialTextBox
    Friend WithEvents HEVCSwitch As MaterialSkin.Controls.MaterialSwitch
    Friend WithEvents FocusLabel As MaterialSkin.Controls.MaterialLabel
    Friend WithEvents QualitySelection As MaterialSkin.Controls.MaterialComboBox
    Friend WithEvents WarningLabel1 As Label
    Friend WithEvents EstSizeLabel As Label
    Friend WithEvents EstSizeResLabel As Label

End Class
