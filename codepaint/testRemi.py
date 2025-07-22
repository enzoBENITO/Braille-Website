import remi.gui as gui
from remi import start, App


class MyApp(App):
    def main(self):
        self.first_point = None

        mainContainer = gui.VBox(width=1300, height=700, margin='150px auto')
        self.canvas = gui.Svg(width=1000, height=450, style={'border': '1px solid black', 'cursor': 'cross'})
        self.canvas.onmousedown.do(self.on_click)

        hbox = gui.HBox(width=700)
        bt1 = gui.Button('Eraser', width=100, height=30)
        bt2 = gui.Button('Save', width=100, height=30)

        hbox.append(bt1, 'bt1')
        hbox.append(bt2,"bt2")

        bt1.onclick.do(self.eraser)
        bt2.onclick.do(self.save_svg)

        mainContainer.append(hbox, 'functionality')
        mainContainer.append(self.canvas, 'paintboard')

        return mainContainer

    def on_click(self, widget, x, y):
        point = gui.SvgCircle(x, y, 2)
        point.set_fill('black')
        point.set_stroke('black')
        self.canvas.append(point)

        if self.first_point is None:
            self.first_point = (x, y)
        else:
            x1, y1 = self.first_point
            line = gui.SvgLine(x1, y1, x, y)
            line.set_style({'stroke': 'red', 'stroke-width': '2'})
            self.canvas.append(line)
            self.first_point = None           

    def save_svg(self, widget):
        svg_code = self.canvas.repr()

        filename = "dessin"
        svg_path = f"{filename}.svg"

        with open(svg_path, "w", encoding='utf-8') as f:
            f.write(svg_code)

    def eraser(self, widget):
        self.canvas.empty()


if __name__ == "__main__":
    start(MyApp, address='127.0.0.1', port=8081, start_browser=True)
