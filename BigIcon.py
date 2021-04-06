#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Sat Apr  3 16:27:01 2021
#
# (C)By BigSam

import wx
from wx.core import DIRP_DIR_MUST_EXIST

# begin wxGlade: dependencies
# end wxGlade


# begin wxGlade: extracode
# end wxGlade

import os
import shutil
from PIL import Image
from os.path import join, getsize

__version__ = '0.1'
picfiles = []

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((640, 480))
        self.SetTitle("Resize Icon For STM32CubeIDE")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        self.sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.panel_2 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.sizer_1.Add(self.panel_2, 0, wx.EXPAND, 0)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)

        label_1 = wx.StaticText(self.panel_2, wx.ID_ANY, "STM32CubeIDE Install Root")
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_2, wx.ID_ANY, "", style=wx.TE_READONLY)
        sizer_2.Add(self.text_ctrl_1, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.button_1 = wx.Button(self.panel_2, wx.ID_ANY, "Browse")
        sizer_2.Add(self.button_1, 0, wx.ALL, 4)

        self.panel_3 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.sizer_1.Add(self.panel_3, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)

        self.notebook_1 = wx.Notebook(self.panel_3, wx.ID_ANY)
        sizer_3.Add(self.notebook_1, 1, wx.EXPAND, 0)

        self.notebook_1_pane_1 = wx.Panel(self.notebook_1, wx.ID_ANY)
        self.notebook_1.AddPage(self.notebook_1_pane_1, "Info")

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)

        self.tcInfo = wx.TextCtrl(self.notebook_1_pane_1, wx.ID_ANY, "Please use the \"Browse\" button to specify the installation directory of STM32CubeIDE, and then use the \"Perform Adjustments\" button in the lower left corner to modify the size of those icons.\n\nYou can use the \"Revert\" button to restore those icons. (Size: 16*16)\n\n**Note** that every modified icon will have a backup with the prefix \"old_\" added.", style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer_5.Add(self.tcInfo, 1, wx.ALL | wx.EXPAND, 4)

        self.panel_4 = wx.Panel(self.panel_1, wx.ID_ANY)
        self.sizer_1.Add(self.panel_4, 0, wx.ALL | wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)

        self.btADJ = wx.Button(self.panel_4, wx.ID_ANY, "Perform Adjustments")
        self.btADJ.Enable(False)
        sizer_4.Add(self.btADJ, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        label_4 = wx.StaticText(self.panel_4, wx.ID_ANY, "New Size")
        sizer_4.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.tcNewSizt = wx.TextCtrl(self.panel_4, wx.ID_ANY, "32")
        self.tcNewSizt.SetMinSize((48, -1))
        sizer_4.Add(self.tcNewSizt, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        sizer_4.Add((0, 20), 1, wx.ALL | wx.EXPAND, 4)

        self.btRevert = wx.Button(self.panel_4, wx.ID_ANY, "Revert")
        self.btRevert.Enable(False)
        sizer_4.Add(self.btRevert, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        sizer_4.Add((20, 20), 0, 0, 0)

        self.button_2 = wx.Button(self.panel_4, wx.ID_ANY, "Exit")
        sizer_4.Add(self.button_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 4)

        self.panel_4.SetSizer(sizer_4)

        self.notebook_1_pane_1.SetSizer(sizer_5)

        self.panel_3.SetSizer(sizer_3)

        self.panel_2.SetSizer(sizer_2)

        self.panel_1.SetSizer(self.sizer_1)

        self.Layout()
        self.Centre()

        self.Bind(wx.EVT_BUTTON, self.openFileDig, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.runAdj, self.btADJ)
        self.Bind(wx.EVT_TEXT, self.enableADJ, self.tcNewSizt)
        self.Bind(wx.EVT_BUTTON, self.RevertIcon, self.btRevert)
        self.Bind(wx.EVT_BUTTON, self.exit_program, self.button_2)
        # end wxGlade

    def openFileDig(self, event):  # wxGlade: MyFrame.<event_handler>
        Dlg = wx.DirDialog(None, "STM32CudeIDE's install path ...", "", DIRP_DIR_MUST_EXIST)
        ret = Dlg.ShowModal()
        if ret == wx.ID_OK:
            self.text_ctrl_1.Value = Dlg.GetPath()
            self.btADJ.Enable()
            self.btRevert.Enable()
        self.tcInfo.write('\nOK!\n')

    def exit_program(self, event):  # wxGlade: MyFrame.<event_handler>
        self.Close()

    def runAdj(self, event):  # wxGlade: MyFrame.<event_handler>
        self.tcInfo.write('\nRUN PNG\n-------------------------')
        scanPic(self.text_ctrl_1.Value, '.PNG', self.tcNewSizt.Value, self.tcInfo)
        self.tcInfo.write('\nRUN GIF\n-------------------------')
        scanPic(self.text_ctrl_1.Value, '.GIF', self.tcNewSizt.Value, self.tcInfo)
        self.tcInfo.write('\n\n*********** RESIZE END! ******************')
        self.btADJ.Enable(False)

    def RevertIcon(self, event):  # wxGlade: MyFrame.<event_handler>
        self.tcInfo.write('\nStart Revert\n-------------------------')
        revertIDE_icon(self.text_ctrl_1.Value, '.PNG')
        revertIDE_icon(self.text_ctrl_1.Value, '.GIF')
        self.tcInfo.write('\n*********** REVERT ICON END! ******************')

    def enableADJ(self, event):  # wxGlade: MyFrame.<event_handler>
        self.btADJ.Enable(True)
# end of class MyFrame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

def revertIDE_icon(rootdir, pictype):
    global picfiles 
    picfiles = []
    srcname = ''
    for root, dirs, files in os.walk(rootdir):
        for imgfile in files:
            if pictype.lower() in imgfile.lower():
                picfiles.append(root + '\\' + imgfile)
    for imgfile in picfiles:
        if 'old_' in imgfile:
            if os.path.exists(imgfile.replace('old_', '')):
                os.remove(imgfile.replace('old_', ''))                           
                shutil.copyfile(imgfile, imgfile.replace('old_' + srcname, srcname))
            

def scanPic(rootdir, pictype, newSize, Info_out):
    global picfiles 
    picfiles = []
    for root, dirs, files in os.walk(rootdir):
        for imgfile in files:
            if pictype.lower() in imgfile.lower():
                picfiles.append(root + '\\' + imgfile)
    Info_out.write("\n\r\n\r Files Count: " + str(len(picfiles)) + "\n\r==========================\n\r" +  "\n\r".join(picfiles))
    checkSize(pictype.replace('.', ''), newSize)

def checkSize(pictype, newSize):
    global picfiles 
    isOK = True
    srcname = ''
    for imgfile in picfiles:
        print("\n\r", imgfile, "\n\r")
        if os.path.exists(imgfile):
            srcname = os.path.basename(imgfile)
            if os.path.getsize(imgfile)>8:                
                img = Image.open(imgfile)
            else:
                img = Image.new('RGBA', (16,16))
            if img.format != None:
                if img.size==(16,16):
                    if 'old_' in imgfile:
                        if os.path.exists(imgfile.replace('old_', '')):
                            os.remove(imgfile.replace('old_', ''))                           
                    else:
                        shutil.copyfile(imgfile, imgfile.replace(srcname, 'old_' + srcname))
                    newSize = int(newSize)
                    img = img.resize((newSize, newSize), Image.LANCZOS)
                    img.convert('RGBA')
                    if 'old_' in imgfile:
                        imgfile = imgfile.replace('old_', '')
                    img.save(imgfile, pictype)
                    img.close()

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()