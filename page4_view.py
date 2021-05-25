import tkinter as tk
import requests


class Page4View(tk.Frame):
    """ Page 1 """

    def __init__(self, parent, page_popup_callback, update_popup, get_id):
        """ Initialize Page 1 """
        tk.Frame.__init__(self, parent)
        self._page_popup_callback = page_popup_callback
        self._parent = parent
        self._update_popup = update_popup
        self._get_id = get_id
        self._create_widgets()

    def _create_widgets(self):
        """ Creates the widgets for Page 4 """
        tk.Button(self, text="Search", fg="Blue", command=self._refresh).grid(row=2, column=4)
        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        tk.Button(self, text="Delete", command=self._delete).grid(row=2, column=6)
        tk.Button(self, text="View", command=self._get).grid(row=2, column=7)
        tk.Button(self, text="Add", command=self._add).grid(row=2, column=5)
        tk.Button(self, text="Update", command=self._update).grid(row=2, column=8)
        self._listbox = tk.Listbox(self, width=50, yscrollcommand=self._scrollbar.set)
        self._scrollbar.config(command=self._listbox.yview)
        self._listbox.grid(row=1, column=1, columnspan=10)
        self._scrollbar.grid(row=1, column=11, sticky=tk.N + tk.S + tk.W + tk.E)

        data_set = requests.get('http://127.0.0.1:5000/sports_team/member/{}'.format(self._get_id()))
        if data_set.status_code != 200:
            return
        self._listbox.insert(tk.END, "{} ({}) - {}".format(data_set.json()["name"], data_set.json()["id"], data_set.json()["position"]))

    def _add(self):
        """ Add Function """
        self._page_popup_callback(self._refresh)

    def _refresh(self):
        """ Refresh Button """
        self._listbox.destroy()
        self._listbox = tk.Listbox(self, width=50, yscrollcommand=self._scrollbar.set)
        self._scrollbar.config(command=self._listbox.yview)
        self._listbox.grid(row=1, column=1, columnspan=10)
        self._scrollbar.grid(row=1, column=11, sticky=tk.N + tk.S + tk.W + tk.E)

        data_set = requests.get('http://127.0.0.1:5000/sports_team/member/{}'.format(self._get_id()))
        if data_set.status_code != 200:
            return
        self._listbox.insert(tk.END, "{} ({}) - {}".format(data_set.json()["name"], data_set.json()["id"], data_set.json()["position"]))

    def _delete(self):
        """ Delete button """
        if tk.messagebox.askyesno('Verify', 'Really delete?'):
            try:
                chosen = self._listbox.get(self._listbox.curselection())
                chosen_id = chosen[chosen.find('(') + 1:chosen.find(')')]
                request = requests.delete('http://127.0.0.1:5000/sports_team/member/{}'.format(chosen_id))
                if request.status_code != 200:
                    print(request.status_code)
                    raise ValueError('Error')
            except ValueError:
                tk.messagebox.showinfo("Error:", "Non 200 Status Code")
            except Exception:
                tk.messagebox.showinfo("Error:", "Nothing Selected")
            self._refresh()

    def _get(self):
        """ Get Button """
        try:
            chosen = self._listbox.get(self._listbox.curselection())
            chosen_id = chosen[chosen.find('(')+1:chosen.find(')')]
            request = requests.get('http://127.0.0.1:5000/sports_team/member/{}'.format(chosen_id))
            if request.status_code != 200:
                print(request.status_code)
                raise ValueError('Error')
            if request.json()["type"].lower() == "coach":
                tk.messagebox.showinfo(
                    "Get ID: {}".format(chosen_id),
                    "Name: {}\nEmail: {}\nPhone Number: {}\nDate of Birth: {}\nSalary: {}\nPosition: {}".format(
                        request.json()["name"],
                        request.json()["email"],
                        request.json()["phone number"],
                        request.json()["date of birth"],
                        request.json()["salary"],
                        request.json()["position"]
                    ))
            if request.json()["type"].lower() == "player":
                tk.messagebox.showinfo(
                    "Get ID: {}".format(chosen_id),
                    "Name: {}\nEmail: {}\nPhone Number: {}\nDate of Birth: {}\nSalary: {}\nPosition: {}".format(
                        request.json()["name"],
                        request.json()["email"],
                        request.json()["phone number"],
                        request.json()["date of birth"],
                        request.json()["jersey number"],
                        request.json()["position"]
                    ))
        except ValueError:
            tk.messagebox.showinfo("Error:", "Non 200 Status Code")
        except Exception:
            tk.messagebox.showinfo("Error:", "Nothing Selected")

    def _update(self):
        """ Update function """
        try:
            chosen = self._listbox.get(self._listbox.curselection())
            chosen_id = chosen[chosen.find('(')+1:chosen.find(')')]
            self._update_popup(chosen_id)
        except Exception as e:
            print(e)
            tk.messagebox.showinfo("Error:", "Nothing Selected")
        self._refresh()
