import flet as ft
import os
import glob
import time
import matplotlib
from main_funcs import main_func, par_error_rate, calculate_impulse_len
from plot import plot
from note import note_txt
matplotlib.use("agg")


def main(page: ft.Page) -> None:

    def main_calculate(e) -> None:
        try:
            n = int(input_points.value)
            if n > 1:
                t, uvx, uvix = main_func(n)

                files = glob.glob("C:/Users/user/Desktop/Учеба/Курсач/*.png")
                for file in files:
                    os.remove(file)

                plot(t, uvx, n, "Uvx")
                plot(t, uvix, n, "Uvix")

                plot_uvx.content = ft.Image(f"plot_Uvx_{n}.png", border_radius=50)
                plot_uvix.content = ft.Image(f"plot_Uvix_{n}.png", border_radius=50)

                db.controls.clear()
                db.controls.append(
                    ft.Row(
                        [
                            ft.Text(f'', size=30, color=ft.colors.BLACK, width=40),
                            ft.Text("t", size=30, color=ft.colors.BLACK, width=80),
                            ft.Text("Uvx", size=30, color=ft.colors.BLACK, width=110),
                            ft.Text("Uvix", size=30, color=ft.colors.BLACK, width=80)
                        ]
                    )
                 )

                for i in range(n):
                    db.controls.append(
                        ft.Row(
                            [
                                ft.Text(f'', size=20, color=ft.colors.BLACK, width=40),
                                ft.Text(f'{t[i]}', size=20, color=ft.colors.BLACK, width=80),
                                ft.Text(f'{uvx[i]}', size=20, color=ft.colors.BLACK, width=110),
                                ft.Text(f'{uvix[i]}', size=20, color=ft.colors.BLACK, width=80)
                            ]
                        )
                    )
            else:
                input_points.value = "Число должно быть > 1!"
                input_points.read_only = True
                page.update()
                time.sleep(2)
                input_points.value = ""
                input_points.read_only = False
                page.update()

        except ValueError:
            input_points.value = "Ошибка!"
            input_points.read_only = True
            page.update()
            time.sleep(2)
            input_points.value = ""
            input_points.read_only = False
            page.update()

        output_field.content = db
        page.update()

    def optimal_error_rate(e) -> None:
        try:
            a = float(input_error_rate.value)
            if a >= 0.001:
                db2.controls.clear()
                db2.controls.append(
                    ft.Row(
                        [
                            ft.Text(f"", width=20),
                            ft.Text("N", size=12, color=ft.colors.BLACK, width=40),
                            ft.Text("Пар. Uvx", size=12, color=ft.colors.BLACK, width=60),
                            ft.Text("Пар. Uvix", size=12, color=ft.colors.BLACK, width=60),
                            ft.Text("α_Uvx", size=12, color=ft.colors.BLACK, width=40),
                            ft.Text("α_Uvix", size=12, color=ft.colors.BLACK, width=40)
                        ]
                    )
                )

                n = 2
                while True:
                    t, uvx, uvix = main_func(n)
                    a_uvx, a_uvix = par_error_rate(n)
                    db2.controls.append(
                        ft.Row(
                            [
                                ft.Text(f"", width=20),
                                ft.Text(f"{n}", size=12, color=ft.colors.BLACK, width=40),
                                ft.Text(f"{calculate_impulse_len(n, uvx)}", size=12, color=ft.colors.BLACK, width=60),
                                ft.Text(f"{calculate_impulse_len(n, uvix)}", size=12, color=ft.colors.BLACK, width=60),
                                ft.Text(f"{'%.3f' % a_uvx}", size=12, color=ft.colors.BLACK, width=40),
                                ft.Text(f"{'%.3f' % a_uvix}", size=12, color=ft.colors.BLACK, width=40)
                            ]
                        )
                    )
                    if a_uvx <= a and a_uvix <= a:
                        output_field.content = db2
                        page.update()
                        break
                    else:
                        n *= 2
            else:
                input_error_rate.value = "Погрешность > 0.001!"
                input_error_rate.read_only = True
                page.update()
                time.sleep(2)
                input_error_rate.value = ""
                input_error_rate.read_only = False
                page.update()

        except ValueError:
            input_error_rate.value = "Ошибка!"
            input_error_rate.read_only = True
            page.update()
            time.sleep(2)
            input_error_rate.value = ""
            input_error_rate.read_only = False
            page.update()

    def par(e) -> None:

        try:
            n = int(input_points.value)
            t, uvx, uvix = main_func(n)
            par_uvx = calculate_impulse_len(n, uvx)
            par_uvix = calculate_impulse_len(n, uvix)
            output_par.content = ft.Text(
                f'Длительность импульса сигнала\nдля Uvx: {par_uvx}, для Uvix: {par_uvix}',
                size=15,
                color=ft.colors.BLACK,
                text_align=ft.TextAlign.CENTER
            )
            page.update()

        except ValueError:
            input_points.value = "Ошибка!"
            page.update()
            time.sleep(2)
            input_points.value = ""
            page.update()

    def close_banner(e) -> None:
        page.banner.open = False
        page.update()

    def show_banner_click(e) -> None:
        page.banner.open = True
        page.update()

    page.title = "Cursach"
    page.window_width = 740
    page.window_height = 600
    page.bgcolor = ft.colors.BLUE_200
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = "CENTER"
    page.update()

    db = ft.Column(
        spacing=10,
        height=255,
        width=350,
        scroll=ft.ScrollMode.ALWAYS
    )

    db2 = ft.Column(
        spacing=10,
        height=255,
        width=350,
        scroll=ft.ScrollMode.ALWAYS
    )

    input_points = ft.TextField(
        label='Введите количество точек N',
        on_submit=main_calculate,
        color='BLack',
        bgcolor='#EDF5E1',
        border_color='#F5DEB3',
        border_radius=10,
        width=350,
        height=65
    )

    input_error_rate = ft.TextField(
        label='Введите погрешность > 0.001',
        on_submit=optimal_error_rate,
        color='BLack',
        bgcolor='#EDF5E1',
        border_color='#F5DEB3',
        border_radius=10,
        width=350,
        height=65
    )

    btn_info = ft.ElevatedButton(
        text="Информация",
        on_click=show_banner_click,
        bgcolor='#EDF5E1',
        color='BLack',
        width=170
    )

    par_txt = ft.Text("Рассчитать параметр", size=12)

    btn_par = ft.ElevatedButton(
        content=par_txt,
        on_click=par,
        bgcolor='#EDF5E1',
        color='BLack',
        width=170
    )

    output_par = ft.Card(
        content=ft.Text('Длительность импульса сигнала:',
                        size=12,
                        color=ft.colors.BLACK,
                        text_align=ft.TextAlign.CENTER
                        ),
        color='#EDF5E1',
        width=350,
        height=60
    )

    page.banner = ft.Banner(
        bgcolor='#EDF5E1',
        content=ft.Text(note_txt, color=ft.colors.BLACK, size=15),
        actions=[ft.TextButton("Закрыть", on_click=close_banner)]
    )

    plot_uvx = ft.Card(width=333, height=266, color='#F5DEB3')
    plot_uvix = ft.Card(width=333, height=266, color='#F5DEB3')

    output_field = ft.Container(db, bgcolor='#EDF5E1', border_radius=10)

    page.add(
        ft.Row([plot_uvx, output_field]),
        ft.Row(
            [
                plot_uvix, ft.Column(
                    [
                        input_points,
                        input_error_rate,
                        ft.Row([btn_par, btn_info]),
                        output_par
                    ]
                )
            ]
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
