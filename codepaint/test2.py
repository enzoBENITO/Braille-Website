import remi.gui as gui
from remi import App, start


class TwoPointLineApp(App):
    def main(self):
        self.first_point = None  # Pour mémoriser le premier clic

        # Création du canvas
        self.canvas = gui.Svg(width=600, height=400, style={'border': '1px solid black', 'cursor': 'cross'})
        self.canvas.onmousedown.do(self.on_click)

        #Creation des bouttons
        hbox = gui.HBox(width=700)
        bt1 = gui.Button('Eraser', width=100, height=30)
        hbox.append(bt1, 'bt1')
        bt1.onmousedown.do(self.eraser)
        return self.canvas

    def on_click(self, widget, x, y):
        # Dessine un petit point (cercle) à chaque clic
        point = gui.SvgCircle(x, y, 2)
        point.set_fill('black')
        point.set_stroke('black')
        self.canvas.append(point)

        # Si c'est le premier clic, on le stocke
        if self.first_point is None:
            self.first_point = (x, y)
        else:
            # Deuxième clic : dessine une ligne entre les deux points
            x1, y1 = self.first_point
            x2, y2 = x, y

            line = gui.SvgLine(x1, y1, x2, y2)
            line.set_style({
                'stroke': 'red',
                'stroke-width': '2'
            })
            self.canvas.append(line)

            self.first_point = None  # Réinitialise pour une nouvelle paire

    def eraser(self):
        self.canvas = gui.Svg(width=600, height=400, style={'border': '1px solid black', 'cursor': 'cross'})
        return self.canvas

if __name__ == "__main__":
    start(TwoPointLineApp, address='127.0.0.1', port=8081, start_browser=True)
