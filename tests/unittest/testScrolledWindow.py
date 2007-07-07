import unittest
import wx

import testPanel

"""
This file contains classes and methods for unit testing the API of
wx.ScrolledWindow

Methods yet to test:
__init__, AdjustScrollbars, CalcScrolledPosition, CalcScrollInc,
CalcUnscrolledPosition, Create, DoPrepareDC, EnableScrolling,
GetViewStart, Scroll, SetScrollbars
"""

class ScrolledWindowTest(testPanel.PanelTest):
    def setUp(self):
        self.app = wx.PySimpleApp()
        self.frame = wx.Frame(parent=None, id=wx.ID_ANY)
        self.testControl = wx.ScrolledWindow(parent=self.frame)
    
    def testScale(self):
        """SetScale, GetScaleX, GetScaleY"""
        for i in range(1000):
            self.testControl.SetScale(i,i)
            self.assertEquals(i, self.testControl.GetScaleX())
            self.assertEquals(i, self.testControl.GetScaleY())
    
    def testScrollPageSize(self):
        """SetScrollPageSize, GetScrollPageSize"""
        for i in range(1000):
            for orient in (wx.HSCROLL, wx.VSCROLL):
                self.testControl.SetScrollPageSize(orient,i)
                self.assertEquals(i, self.testControl.GetScrollPageSize(orient))
    
    def testScrollRate(self):
        """SetScrollRate, GetScrollPixelsPerUnit
        Note asymmetry between accessor methods"""
        for i in range(1000):
            self.testControl.SetScrollRate(i,i)
            self.assertEquals((i,i), self.testControl.GetScrollPixelsPerUnit())
        for tup in ((99,101),(31,27),(3,5),(1000,1)):
            self.testControl.SetScrollRate(*tup)
            self.assertEquals(tup, self.testControl.GetScrollPixelsPerUnit())
    
    def testTargetWindow(self):
        """SetTargetWindow, GetTargetWindow"""
        wins = (wx.Window(self.frame), wx.Window(self.frame), wx.Window(self.frame))
        for w in wins:
            self.testControl.SetTargetWindow(w)
            self.assertEquals(w, self.testControl.GetTargetWindow())
    
    # overrides test from testWindow (or rather, it's meant to)
    # kind of needs to sidestep the fact that there's a floor and ceiling
    # TODO: needs to take into better account when one xmin and ymin aren't the same
    def testVirtualSize(self):
        """SetVirtualSize, GetVirtualSize"""
        self.testControl.SetVirtualSize((1,1))
        xmin,ymin = self.testControl.GetVirtualSize()
        self.testControl.SetVirtualSize((40000,40000))
        xmax,ymax = self.testControl.GetVirtualSize()
        #print "maxes: %d, %d" % (xmax,ymax)
        #print "mins:  %d, %d" % (xmin,ymin)
        for i in range(min(xmin,ymin), max(xmax,ymax),10): # can't be too slow
            sz = wx.Size(i,i)
            self.testControl.SetVirtualSize(sz)
            self.assertEquals(sz, self.testControl.GetVirtualSize())
    

def suite():
    suite = unittest.makeSuite(ScrolledWindowTest)
    return suite
    
if __name__ == '__main__':
    unittest.main(defaultTest='suite')
