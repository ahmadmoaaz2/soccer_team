import tkinter as tk


class TopNavbarView(tk.Frame):
    """ Navigation Bar """

    PAGE1 = 1
    PAGE2 = 2
    PAGE3 = 3
    PAGE4 = 4

    def __init__(self, parent, page_callback):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._parent = parent

        self._page_callback = page_callback
        self._page = tk.IntVar()
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        tk.Label(self,
                 text="Get:").grid(row=0, column=0)

        self.curr_page = tk.IntVar()

        tk.Radiobutton(self,
                       text="Coaches",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.PAGE3).grid(row=0, column=3)

        tk.Radiobutton(self,
                       text="Players",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.PAGE2).grid(row=0, column=2)

        tk.Radiobutton(self,
                       text="All",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.PAGE1).grid(row=0, column=1)

        tk.Radiobutton(self,
                       text="ID:",
                       variable=self.curr_page,
                       command=self._page_callback,
                       value=TopNavbarView.PAGE4).grid(row=0, column=4)
        self.entry = tk.Entry(self, width=4)
        self.entry.grid(row=0, column=5)
        self.entry.insert(0, "1")

        self.curr_page.set(TopNavbarView.PAGE1)


        self._page.set(1)
