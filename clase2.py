import flet as ft

def main(page: ft.Page):
    page.adaptive = True 
    # Definir tamaño de la ventana
    page.window_width = 600
    page.window_height = 400
    page.title = "Lista"
    page.vertical_alignment = "center"  # Asignar valor

    # Contenido pal header
    logo = ft.Image(src="../img/logo.png", width=100, height=100)
    logoN = ft.Text(value="Sakuya Izayoi", color="white", size=50, weight=ft.FontWeight.BOLD)

    # Funcion para el boton editar
    def edit_clicked(e, checkbox):
        new_value = ft.TextField(value=checkbox.label, hint_text="Nuevo valor")
        save_button = ft.ElevatedButton("Guardar", on_click=lambda e: save_clicked(e, checkbox, new_value))
        # El codigo de abajo abre un dialog para poder editar el texto (no queria hacer el constructor de la pagina de flet profe)
        page.dialog = ft.AlertDialog(content=ft.Column([new_value, save_button],width=100, height=100, alignment= ft.MainAxisAlignment.CENTER))
        page.dialog.open = True
        page.update()

    # Funcion para el boton guardar para el text dialog
    def save_clicked(e, checkbox, new_value):
        checkbox.label = new_value.value
        page.dialog.open = False
        checkbox.update()
        page.update()

    # Funcion para el boton eliminar
    def delete_clicked(e, row):
        page.controls.remove(row)
        page.update()

    # Funcion para el boton agregar
    def add_clicked(e):
        checkbox = ft.Checkbox(label=new_task.value)
        row = ft.Row(
            [
                checkbox,
                #El codigo de abajo es el diseño de los botones de editar y eliminar mediante iconos que proporciona FLET
                ft.IconButton(
                    icon=ft.icons.EDIT,
                    icon_color="blue400",
                    icon_size=20,
                    tooltip="Editar",
                    on_click=lambda e: edit_clicked(e, checkbox)
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE,
                    icon_color="red400",
                    icon_size=20,
                    tooltip="Eliminar",
                    on_click=lambda e: delete_clicked(e, row)
                )
            ],
            alignment="center"
        )

        page.add(row)
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="Nippa!")

    #Estructura del header
    header = ft.Row(
        [
            logo, logoN
            ], alignment="center")
    #Agregar todos los elementos a la pagina
    page.add(
        header,

        ft.Row(
            [
                ft.Text(value="Bem-vindo!",size=15)
            ],alignment="center"
        ),
        
        ft.Divider(height=10),

        ft.Row(
            [
                new_task,
                ft.ElevatedButton("Agregar", on_click=add_clicked),
            ],
            alignment="center"
        )
    )

ft.app(target=main)