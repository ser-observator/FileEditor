# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Copyright (C) 2024-2026 NEO Organization, Department K
# Coded by AnonymousNEO (Github)

from tkinter import ttk, Menu
import tkinter as tk
from languages import l
from config import THEME

OTHER_FUNCTION_VERSION = "0.14.9 Beta"

def safe_call(callback, *args, **kwargs):
    """Безопасный вызов функции: проверяет, является ли объект вызываемым."""
    if callable(callback):
        return callback(*args, **kwargs)
    return None

def apply_global_theme(window, current_theme):
    """Применяет тему к окну и всем его виджетам."""
    style = ttk.Style(window) # Привязываем стиль к окну
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    # Настройки для стандартных tk-виджетов
    # Общие настройки
    window.option_add("*Background", current_theme["bg"])
    window.option_add("*Foreground", current_theme["fg"])
    
    # Меню
    window.option_add("*Menu.background", current_theme["bg"])
    window.option_add("*Menu.foreground", current_theme["fg"])
    window.option_add("*Menu.activeBackground", current_theme["abg"])
    window.option_add("*Menu.activeForeground", current_theme["afg"])
    window.option_add("*Menu.selectColor", current_theme["abg"])

    # Текстовые поля
    window.option_add("*Text.Background", current_theme["bg"])
    window.option_add("*Text.Foreground", current_theme["fg"])
    window.option_add("*Text.InsertBackground", current_theme["fg"])
    window.option_add("*Text.SelectBackground", current_theme["abg"])
    window.option_add("*Text.SelectForeground", current_theme["afg"])

    # Чекбоксы и Радиокнопки
    window.option_add("*Checkbutton.Background", current_theme["bg"])
    window.option_add("*Checkbutton.Foreground", current_theme["fg"])
    window.option_add("*Checkbutton.activeBackground", current_theme["abg"])
    window.option_add("*Checkbutton.activeForeground", current_theme["afg"])
    window.option_add("*Checkbutton.selectColor", current_theme["abg"])
    
    window.option_add("*Radiobutton.Background", current_theme["bg"])
    window.option_add("*Radiobutton.Foreground", current_theme["fg"])
    window.option_add("*Radiobutton.activeBackground", current_theme["abg"])
    window.option_add("*Radiobutton.activeForeground", current_theme["afg"])
    window.option_add("*Radiobutton.selectColor", current_theme["abg"])

    # Кнопки
    window.option_add("*Button.Background", current_theme["bbg"])
    window.option_add("*Button.Foreground", current_theme["bfg"])
    window.option_add("*Button.activeBackground", current_theme["abg"])
    window.option_add("*Button.activeForeground", current_theme["afg"])

    # Рамки и Метки
    window.option_add("*Frame.Background", current_theme["bg"])
    window.option_add("*Label.Background", current_theme["lbg"])
    window.option_add("*Label.Foreground", current_theme["lfg"])

    # Стили ttk
    style.configure(".",
                    background=current_theme["bg"],
                    foreground=current_theme["fg"],
                    fieldbackground=current_theme["bg"],
                    bordercolor=current_theme["bbg"],
                    lightcolor=current_theme["bg"],
                    darkcolor=current_theme["bg"])

    style.configure("TButton", background=current_theme["bbg"], foreground=current_theme["bfg"])
    style.map("TButton", 
              background=[("active", current_theme["abg"])], 
              foreground=[("active", current_theme["afg"])])

    style.configure("TCheckbutton", background=current_theme["bg"], foreground=current_theme["fg"])
    style.configure("TEntry", fieldbackground=current_theme["bg"], foreground=current_theme["fg"], bordercolor=current_theme["bbg"])

    style.configure("Treeview", background=current_theme["bg"], foreground=current_theme["fg"], fieldbackground=current_theme["bg"], rowheight=25)
    style.map("Treeview", background=[("selected", current_theme["abg"])], foreground=[("selected", current_theme["afg"])])
    style.configure("Treeview.Heading", background=current_theme["bbg"], foreground=current_theme["fg"])

    style.configure("TNotebook", background=current_theme["bg"], borderwidth=0)
    style.configure("TNotebook.Tab", background=current_theme["bbg"], foreground=current_theme["bfg"])
    style.map("TNotebook.Tab", background=[("selected", current_theme["abg"])], foreground=[("selected", current_theme["afg"])])

    window.configure(bg=current_theme["bg"])
    update_current_widgets(window, current_theme)

def update_current_widgets(widget, theme):
    """Рекурсивно обновляет цвета всех созданных виджетов."""
    widget_class = widget.winfo_class()

    try:
        if widget_class == "Frame":
            widget.configure(background=theme["bg"])
        elif widget_class == "Label":
            widget.configure(background=theme["lbg"], foreground=theme["lfg"])
        elif widget_class == "Button":
            widget.configure(background=theme["bbg"], foreground=theme["bfg"], 
                             activebackground=theme["abg"], activeforeground=theme["afg"])
        elif widget_class in ("Checkbutton", "Radiobutton"):
            widget.configure(background=theme["bg"], foreground=theme["fg"], 
                             activebackground=theme["abg"], activeforeground=theme["afg"], selectcolor=theme["abg"])
        elif widget_class == "Text":
            widget.configure(background=theme["bg"], foreground=theme["fg"], 
                             insertbackground=theme["fg"], selectbackground=theme["abg"], selectforeground=theme["afg"])
        elif widget_class == "Listbox":
            widget.configure(background=theme["bg"], foreground=theme["fg"], 
                             selectbackground=theme["abg"], selectforeground=theme["afg"])
        elif widget_class == "Entry":
            widget.configure(background=theme["bg"], foreground=theme["fg"], insertbackground=theme["fg"])
    except tk.TclError:
        pass

    for child in widget.winfo_children():
        update_current_widgets(child, theme)

def restart_gui_for_theme(GUI, user_theme):
    """Безопасно меняет тему интерфейса."""
    current_theme = THEME.get(user_theme)
    if current_theme:
        apply_global_theme(GUI, current_theme)

def create_menubar(GUI, RUN_IN_RECOVERY, component_func=None, component_func2=None, component_func3=None, component_func4=None, component_func5=None, component_func6=None):
    menubar = Menu(GUI)
    
    # Файл
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=l("file"), menu=file_menu)
    file_menu.add_command(label=l("open"), command=lambda: safe_call(component_func), accelerator="Ctrl+O")
    file_menu.add_command(label=l("save"), command=lambda: safe_call(component_func2), accelerator="Ctrl+S")
    file_menu.add_command(label=l("save_as"), command=lambda: safe_call(component_func3), accelerator="Ctrl+Shift+S")
    file_menu.add_separator()
    file_menu.add_command(label=l("exit"), command=lambda: safe_call(component_func4), accelerator="Alt+F4")

    # Вид
    view_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=l("view"), menu=view_menu)

    font_menu = tk.Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label=l("font"), menu=font_menu)
    fonts = ["Courier", "Arial", "Times New Roman", "Helvetica", "Verdana", "Consolas"]
    for font in fonts:
        font_menu.add_command(label=font, command=lambda f=font: safe_call(component_func5, f))

    size_menu = tk.Menu(view_menu, tearoff=0)
    view_menu.add_cascade(label=l("font_size"), menu=size_menu)
    sizes = [8, 10, 11, 12, 14, 16, 18, 20, 24]
    for size in sizes:
        size_menu.add_command(label=str(size), command=lambda s=size: safe_call(component_func6, s))

    # Темы (используем Radiobutton для исключающего выбора)
    theme_menu = Menu(menubar, tearoff=0)
    theme_var = tk.StringVar(value="dark") # Переменная состояния темы
    themes = [("dark", "dark"), ("white", "white"), ("red", "red"), ("green", "lime"), ("contrast", "black"), ("gray", "gray"), ("orange", "orange")]
    for label, theme_name in themes:
        theme_menu.add_radiobutton(label=l(label), variable=theme_var, value=theme_name, 
                                   command=lambda tn=theme_name: restart_gui_for_theme(GUI, tn))
    menubar.add_cascade(label=l("themes"), menu=theme_menu)

    # Поверх всех окон
    higher = tk.BooleanVar(value=not RUN_IN_RECOVERY)
    menubar.add_command(label=f'{l("topmost")}: {l("on2")}')
    topmost_index = menubar.index("end")

    def toggle_topmost():
        higher.set(not higher.get())
        GUI.attributes("-topmost", higher.get())
        status = l("on2") if higher.get() else l("off2")
        menubar.entryconfig(topmost_index, label=f'{l("topmost")}: {status}')

    menubar.entryconfig(topmost_index, command=toggle_topmost)

    # РЕАЛЬНЫЕ горячие клавиши (Binding)
    GUI.bind_all("<Control-o>", lambda e: [safe_call(component_func), "break"])
    GUI.bind_all("<Control-s>", lambda e: [safe_call(component_func2), "break"])
    GUI.bind_all("<Control-Shift-S>", lambda e: [safe_call(component_func3), "break"])
    GUI.bind_all("<Alt-F4>", lambda e: [safe_call(component_func4), "break"])

    GUI.config(menu=menubar)
    if not RUN_IN_RECOVERY:
        GUI.attributes("-topmost", True)
