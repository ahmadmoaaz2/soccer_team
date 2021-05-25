import tkinter as tk
from top_navbar_view import TopNavbarView
from page3_view import Page3View
from page2_view import Page2View
from bottom_navbar_view import BottomNavbarView
from popup_view import PopupView
from popup_view2 import PopupView2
from page1_view import Page1View
from page4_view import Page4View
import subprocess
import sys
import atexit


class MainAppController(tk.Frame):
    """ Main Application for GUI """

    def __init__(self, parent):
        """ Initialize Main Application """
        tk.Frame.__init__(self, parent)
        self._top_navbar = TopNavbarView(self, self._page_callback)
        self._page1 = Page1View(self, self._page_popup_callback, self._page_popup_callback2)
        self._page2 = Page2View(self, self._page_popup_callback, self._page_popup_callback2)
        self._page3 = Page3View(self, self._page_popup_callback, self._page_popup_callback2)
        self._page4 = Page4View(self, self._page_popup_callback, self._page_popup_callback2, self._id_search)
        self._bottom_navbar = BottomNavbarView(self, self._quit_callback)

        self._top_navbar.grid(row=0, columnspan=4, pady=10)
        self._page1.grid(row=1, columnspan=4)
        self._curr_page = TopNavbarView.PAGE1
        self._bottom_navbar.grid(row=2, columnspan=4, pady=10)

    def _id_search(self):
        """ Id search function """
        try:
            return int(self._top_navbar.entry.get())
        except ValueError:
            tk.messagebox.showinfo("Error", "Input Must be an integer")

    def _page_callback(self):
        """ Handle Switching Between Pages """
        curr_page = self._top_navbar.curr_page.get()
        if self._curr_page != curr_page:
            if curr_page == TopNavbarView.PAGE1:
                if self._curr_page == TopNavbarView.PAGE2:
                    self._page2.grid_forget()
                if self._curr_page == TopNavbarView.PAGE3:
                    self._page3.grid_forget()
                if self._curr_page == TopNavbarView.PAGE4:
                    self._page4.grid_forget()
                self._page1.grid(row=1, columnspan=4)
                self._curr_page = TopNavbarView.PAGE1
            if curr_page == TopNavbarView.PAGE2:
                if self._curr_page == TopNavbarView.PAGE1:
                    self._page1.grid_forget()
                if self._curr_page == TopNavbarView.PAGE3:
                    self._page3.grid_forget()
                if self._curr_page == TopNavbarView.PAGE4:
                    self._page4.grid_forget()
                self._page2.grid(row=1, columnspan=4)
                self._curr_page = TopNavbarView.PAGE2
            if curr_page == TopNavbarView.PAGE3:
                if self._curr_page == TopNavbarView.PAGE2:
                    self._page2.grid_forget()
                if self._curr_page == TopNavbarView.PAGE1:
                    self._page1.grid_forget()
                if self._curr_page == TopNavbarView.PAGE4:
                    self._page4.grid_forget()
                self._page3.grid(row=1, columnspan=4)
                self._curr_page = TopNavbarView.PAGE3
            if curr_page == TopNavbarView.PAGE4:
                if self._curr_page == TopNavbarView.PAGE2:
                    self._page2.grid_forget()
                if self._curr_page == TopNavbarView.PAGE1:
                    self._page1.grid_forget()
                if self._curr_page == TopNavbarView.PAGE3:
                    self._page3.grid_forget()
                self._page4.grid(row=1, columnspan=4)
                self._curr_page = TopNavbarView.PAGE4

    def _page_popup_callback(self, refresh_callback):
        self._popup_win = tk.Toplevel()
        self._popup = PopupView(self._popup_win, self._close_popup_callback, refresh_callback)

    def _close_popup_callback(self):
        self._popup_win.destroy()

    def _page_popup_callback2(self, member_id):
        """ Popup for update """
        self._popup_win2 = tk.Toplevel()
        self._popup = PopupView2(self._popup_win2, self._close_popup_callback2, member_id)

    def _close_popup_callback2(self):
        """ Pop Close for update popup """
        self._popup_win2.destroy()

    def _quit_callback(self):
        self.quit()


if __name__ == "__main__":
    root = tk.Tk()
    a = subprocess.Popen([sys.executable, 'sports_team_api.py'])
    atexit.register(a.kill)
    MainAppController(root).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    root.mainloop()

