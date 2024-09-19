import wx

class MultiplicationTableApp(wx.Frame):
    def __init__(self, parent, title):
        super(MultiplicationTableApp, self).__init__(parent, title=title, size=(300, 150))

        self.InitUI()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Create an edit box for user input
        self.edit = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        vbox.Add(self.edit, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Create a button to generate the multiplication table
        self.button = wx.Button(panel, label="Generate Table")
        vbox.Add(self.button, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Create a text area to display the multiplication table
        self.result_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        vbox.Add(self.result_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        panel.SetSizer(vbox)

        # Bind button click and Enter key press events to the table generation function
        self.Bind(wx.EVT_BUTTON, self.OnGenerateTable, self.button)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnGenerateTable, self.edit)

    def OnGenerateTable(self, event):
        try:
            num = int(self.edit.GetValue())
            # Generate the multiplication table and format it as a string
            table = "\n".join([f"{num} x {i} = {num * i}" for i in range(1, 11)])
            # Display the table in the text area
            self.result_text.SetValue(table)
        except ValueError:
            # Display an error message if the user enters invalid input
            wx.MessageBox("Please enter a valid integer.", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == '__main__':
    app = wx.App()
    # Create an instance of the MultiplicationTableApp class
    MultiplicationTableApp(None, title='Multiplication Table Generator')
    # Start the wxPython main event loop
    app.MainLoop()
