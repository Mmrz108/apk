```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, Line
from kivy.metrics import dp


# ==========================================
# WINDOW
# ==========================================

Window.size = (380, 600)
Window.minimum_width = 320
Window.minimum_height = 500


# ==========================================
# COLORS
# ==========================================

BG = (0.12, 0.12, 0.12, 1)
PANEL = (0.25, 0.25, 0.25, 1)

GREEN = (0.28, 0.55, 0.18, 1)
GREEN_DARK = (0.18, 0.36, 0.12, 1)

GRAY = (0.35, 0.35, 0.35, 1)
GRAY_DARK = (0.20, 0.20, 0.20, 1)

RED = (0.60, 0.16, 0.16, 1)
BROWN = (0.48, 0.30, 0.12, 1)

TEXT_GREEN = (0.55, 1.0, 0.32, 1)
WHITE = (1, 1, 1, 1)


# ==========================================
# PIXEL BUTTON
# ==========================================

class MinecraftButton(Button):

    def __init__(self, bg_color=GRAY, **kwargs):

        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""

        self.background_color = bg_color

        self.color = WHITE

        self.font_size = dp(20)

        self.bold = True

        self.border = (0, 0, 0, 0)

        self.bind(pos=self.draw_border)
        self.bind(size=self.draw_border)

    def draw_border(self, *args):

        self.canvas.after.clear()

        with self.canvas.after:

            # Border
            Color(0.05, 0.05, 0.05, 1)

            Line(
                rectangle=(
                    self.x,
                    self.y,
                    self.width,
                    self.height
                ),
                width=dp(3)
            )


# ==========================================
# MAIN CALCULATOR
# ==========================================

class Calculator(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.orientation = "vertical"

        self.padding = dp(12)

        self.spacing = dp(8)

        self.background_color = BG

        self.expression = ""

        # ==================================
        # TITLE
        # ==================================

        title = Label(

            text="⛏  MINECRAFT CALCULATOR",

            font_size=dp(21),

            bold=True,

            color=WHITE,

            size_hint_y=None,

            height=dp(45)
        )

        self.add_widget(title)


        subtitle = Label(

            text="CRAFT • CALCULATE • BUILD",

            font_size=dp(10),

            bold=True,

            color=TEXT_GREEN,

            size_hint_y=None,

            height=dp(25)
        )

        self.add_widget(subtitle)


        # ==================================
        # DISPLAY
        # ==================================

        self.display = Label(

            text="0",

            font_size=dp(30),

            bold=True,

            color=TEXT_GREEN,

            halign="right",

            valign="middle",

            size_hint_y=None,

            height=dp(85)
        )

        self.display.text_size = (
            None,
            self.display.height
        )

        self.add_widget(self.display)


        # ==================================
        # BUTTON GRID
        # ==================================

        grid = GridLayout(

            cols=4,

            spacing=dp(7),

            size_hint_y=1
        )

        self.grid = grid

        self.add_widget(grid)


        # ==================================
        # BUTTONS
        # ==================================

        self.add_button(
            "C",
            self.clear,
            RED
        )

        self.add_button(
            "⌫",
            self.delete,
            BROWN
        )

        self.add_button(
            "(",
            lambda: self.add("("),
            GREEN_DARK
        )

        self.add_button(
            ")",
            lambda: self.add(")"),
            GREEN_DARK
        )


        self.add_button(
            "7",
            lambda: self.add("7")
        )

        self.add_button(
            "8",
            lambda: self.add("8")
        )

        self.add_button(
            "9",
            lambda: self.add("9")
        )

        self.add_button(
            "÷",
            lambda: self.add("/"),
            GREEN_DARK
        )


        self.add_button(
            "4",
            lambda: self.add("4")
        )

        self.add_button(
            "5",
            lambda: self.add("5")
        )

        self.add_button(
            "6",
            lambda: self.add("6")
        )

        self.add_button(
            "×",
            lambda: self.add("*"),
            GREEN_DARK
        )


        self.add_button(
            "1",
            lambda: self.add("1")
        )

        self.add_button(
            "2",
            lambda: self.add("2")
        )

        self.add_button(
            "3",
            lambda: self.add("3")
        )

        self.add_button(
            "−",
            lambda: self.add("-"),
            GREEN_DARK
        )


        self.add_button(
            "0",
            lambda: self.add("0")
        )

        self.add_button(
            ".",
            lambda: self.add(".")
        )

        self.add_button(
            "+",
            lambda: self.add("+"),
            GREEN_DARK
        )

        self.add_button(
            "=",
            self.calculate,
            GREEN
        )


    # ======================================
    # ADD BUTTON
    # ======================================

    def add_button(
        self,
        text,
        command,
        color=GRAY
    ):

        button = MinecraftButton(

            text=text,

            bg_color=color,

            size_hint_y=None,

            height=dp(55)
        )

        button.bind(
            on_release=lambda instance: command()
        )

        self.grid.add_widget(button)


    # ======================================
    # ADD VALUE
    # ======================================

    def add(self, value):

        self.expression += value

        self.update_display()


    # ======================================
    # UPDATE DISPLAY
    # ======================================

    def update_display(self):

        if self.expression == "":

            self.display.text = "0"

        else:

            self.display.text = (
                self.expression
                .replace("*", "×")
                .replace("/", "÷")
                .replace("-", "−")
            )


    # ======================================
    # CLEAR
    # ======================================

    def clear(self):

        self.expression = ""

        self.update_display()


    # ======================================
    # DELETE
    # ======================================

    def delete(self):

        self.expression = self.expression[:-1]

        self.update_display()


    # ======================================
    # CALCULATE
    # ======================================

    def calculate(self):

        if not self.expression:

            return

        try:

            # اجازه فقط به کاراکترهای ریاضی
            allowed = "0123456789+-*/(). "

            if any(
                char not in allowed
                for char in self.expression
            ):

                raise ValueError


            result = eval(
                self.expression,
                {"__builtins__": None},
                {}
            )


            if isinstance(result, float):

                if result.is_integer():

                    result = int(result)

                else:

                    result = round(result, 10)


            self.expression = str(result)

            self.update_display()


        except Exception:

            self.display.text = "ERROR"

            self.expression = ""


# ==========================================
# APP
# ==========================================

class MinecraftCalculatorApp(App):

    def build(self):

        self.title = "Minecraft Calculator"

        return Calculator()


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    MinecraftCalculatorApp().run()
