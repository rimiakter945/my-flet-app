import flet as ft

def main(page: ft.Page):
    page.title = "Password Manager"
    page.add(ft.Text("Password Manager App"))

ft.app(target=main)
