import tkinter as tk
from tkinter import messagebox as tkMessageBox
import requests
import json, re


class PopupView2(tk.Frame):
    """ Popup Window """

    def __init__(self, parent, close_popup_callback, member_id):
        """ Initialize the nav bar """
        tk.Frame.__init__(self, parent)
        self._member_id = member_id
        self._widget_holder = tk.Frame(self)
        self._widget_holder.grid(row=2, column=0, columnspan=9, rowspan=9)
        self._players_or_coaches = 0
        self._parent = parent
        self.grid(rowspan=2, columnspan=2)
        self._close_popup_callback = close_popup_callback
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for the nav bar """
        tk.Label(self, text="Updating Member ID: {}".format(self._member_id)).grid(row=0, columnspan=2, padx=10, pady=10)
        request = requests.get('http://127.0.0.1:5000/sports_team/member/{}'.format(self._member_id))
        if request.status_code == 200:
            member_type = request.json()["type"].lower()
            if member_type == 'player':
                self._choose_players()
            if member_type == 'coach':
                self._choose_coaches()
        else:
            print(request.status_code)
        tk.Button(self, text="Cancel", fg="Red", command=self._close_popup_callback).grid(row=20, column=0, pady=10)

    def _choose_coaches(self):
        """ Coach Option """
        self._players_or_coaches = 2
        self._make_more_widgets()

    def _choose_players(self):
        """ Player Option """
        self._players_or_coaches = 1
        self._make_more_widgets()

    def _make_more_widgets(self):
        """ Creates Inputs Boxes """
        try:
            self._widget_holder.destroy()
            self._widget_holder = tk.Frame(self)
            self._widget_holder.grid(row=2, column=0, columnspan=10, rowspan=10)
        except Exception as e:
            print(e)
        if self._players_or_coaches == 1:
            tk.Button(self, text="Submit", command=self._add).grid(row=20, column=2)
            self._entry1 = tk.Entry(self._widget_holder)
            self._entry1.grid(row=2, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Name:").grid(row=2)
            self._entry2 = tk.Entry(self._widget_holder)
            self._entry2.grid(row=3, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Email:").grid(row=3)
            self._entry3 = tk.Entry(self._widget_holder)
            self._entry3.grid(row=4, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Phone Number:").grid(row=4)
            self._entry4 = tk.Entry(self._widget_holder)
            self._entry4.grid(row=5, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Date of Birth:").grid(row=5)
            self._entry5 = tk.Entry(self._widget_holder)
            self._entry5.grid(row=6, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Jersey Number:").grid(row=6)
            self._entry6 = tk.Entry(self._widget_holder)
            self._entry6.grid(row=7, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Position:").grid(row=7)
        if self._players_or_coaches == 2:
            tk.Button(self, text="Submit", command=self._add).grid(row=20, column=2)
            self._entry1 = tk.Entry(self._widget_holder)
            self._entry1.grid(row=2, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Name:").grid(row=2)
            self._entry2 = tk.Entry(self._widget_holder)
            self._entry2.grid(row=3, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Email:").grid(row=3)
            self._entry3 = tk.Entry(self._widget_holder)
            self._entry3.grid(row=4, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Phone Number:").grid(row=4)
            self._entry4 = tk.Entry(self._widget_holder)
            self._entry4.grid(row=5, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Date of Birth:").grid(row=5)
            self._entry5 = tk.Entry(self._widget_holder)
            self._entry5.grid(row=6, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Salary:").grid(row=6)
            self._entry6 = tk.Entry(self._widget_holder)
            self._entry6.grid(row=7, column=1, columnspan=2)
            tk.Label(self._widget_holder, text="Position:").grid(row=7)
        request = requests.get('http://127.0.0.1:5000/sports_team/member/{}'.format(self._member_id)).json()
        self._entry1.insert(0, request["name"])
        self._entry2.insert(0, request["email"])
        self._entry3.insert(0, request["phone number"])
        self._entry4.insert(0, request["date of birth"])
        if self._players_or_coaches == 1:
            self._entry5.insert(0, request["jersey number"])
        if self._players_or_coaches == 2:
            self._entry5.insert(0, request["salary"])
        self._entry6.insert(0, request["position"])

    def _add(self):
        """ Add New Member """
        if self._players_or_coaches == 1:
            try:
                request = requests.put('http://127.0.0.1:5000/sports_team/member/{}'.format(self._member_id), json={
                    "name": self._entry1.get(),
                    "email": self._entry2.get(),
                    "phone number": int(self._entry3.get()),
                    "date of birth": self._entry4.get(),
                    "jersey number": int(self._entry5.get()),
                    "position": self._entry6.get(),
                    "type": "player"
                })
                if request.status_code != 200:
                    raise Exception(request.content)
                else:
                    tk.messagebox.showinfo("Success!", "Member {} updated".format(self._member_id))
            except Exception as e:
                tk.messagebox.showinfo("Error:",  re.sub(r"[^\w\ ]*", '', str(e)))
        if self._players_or_coaches == 2:
            try:
                request = requests.put('http://127.0.0.1:5000/sports_team/member/{}'.format(self._member_id), json={
                    "name": self._entry1.get(),
                    "email": self._entry2.get(),
                    "phone number": int(self._entry3.get()),
                    "date of birth": self._entry4.get(),
                    "salary": int(self._entry5.get()),
                    "position": self._entry6.get(),
                    "type": "coach"
                })
                if request.status_code != 200:
                    raise Exception(request.content)
                else:
                    tk.messagebox.showinfo("Success!", "Member {} updated".format(self._member_id))
            except Exception as e:
                tk.messagebox.showinfo("Error:", re.sub(r"[^\w\ ]*", '', str(e)))
