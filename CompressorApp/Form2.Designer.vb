<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form2
    Inherits MaterialSkin.Controls.MaterialForm

    'Form 重写 Dispose，以清理组件列表。
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Windows 窗体设计器所必需的
    Private components As System.ComponentModel.IContainer

    '注意: 以下过程是 Windows 窗体设计器所必需的
    '可以使用 Windows 窗体设计器修改它。  
    '不要使用代码编辑器修改它。
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form2))
        MaterialProgressBar1 = New MaterialSkin.Controls.MaterialProgressBar()
        Label1 = New Label()
        Label2 = New Label()
        SuspendLayout()
        ' 
        ' MaterialProgressBar1
        ' 
        MaterialProgressBar1.Depth = 0
        MaterialProgressBar1.Location = New Point(18, 84)
        MaterialProgressBar1.MouseState = MaterialSkin.MouseState.HOVER
        MaterialProgressBar1.Name = "MaterialProgressBar1"
        MaterialProgressBar1.Size = New Size(482, 5)
        MaterialProgressBar1.Step = 1
        MaterialProgressBar1.TabIndex = 0
        ' 
        ' Label1
        ' 
        Label1.Location = New Point(502, 78)
        Label1.Name = "Label1"
        Label1.Size = New Size(30, 17)
        Label1.TabIndex = 1
        Label1.Text = "0"
        Label1.TextAlign = ContentAlignment.MiddleRight
        ' 
        ' Label2
        ' 
        Label2.AutoSize = True
        Label2.Location = New Point(528, 78)
        Label2.Name = "Label2"
        Label2.Size = New Size(19, 17)
        Label2.TabIndex = 2
        Label2.Text = "%"
        Label2.TextAlign = ContentAlignment.MiddleCenter
        ' 
        ' Form2
        ' 
        AutoScaleDimensions = New SizeF(7.0F, 17.0F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(552, 110)
        Controls.Add(Label2)
        Controls.Add(Label1)
        Controls.Add(MaterialProgressBar1)
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        MaximizeBox = False
        MinimizeBox = False
        Name = "Form2"
        ShowIcon = False
        ShowInTaskbar = False
        Sizable = False
        StartPosition = FormStartPosition.CenterScreen
        Text = "Processing..."
        TopMost = True
        ResumeLayout(False)
        PerformLayout()
    End Sub

    Friend WithEvents MaterialProgressBar1 As MaterialSkin.Controls.MaterialProgressBar
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
End Class
