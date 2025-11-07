class SVGCanvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.elements = []
        self.axis_enabled = False
        self.normalized_x = self.width/2
        self.normalized_y = self.height/2
        self.normalized = (self.normalized_x, self.normalized_y)

    def setup_axis(self, color: str = "black", stroke_width: int = 1):
        """[summary]
        Setup the coordinate axis on the SVG canvas.
        Args:
            color (str, optional): The color of the axis lines. Defaults to "black".
            stroke_width (int, optional): The width of the axis lines. Defaults to 1.
        """
        self.axis_enabled = True
        self.add_element(f'<line x1="0" y1="{self.normalized_y}" x2="{self.width}" y2="{self.normalized_y}" stroke="{color}" stroke-width="{stroke_width}" />')
        self.add_element(f'<line x1="{self.normalized_x}" y1="0" x2="{self.normalized_x}" y2="{self.height}" stroke="{color}" stroke-width="{stroke_width}" />')

    def add_element(self, element: str):
        """[summary]
        Add an SVG element to the canvas.
        Args:
            element (str): The SVG element as a string.
        """
        self.elements.append(element)
    
    def rect(self, x: float, y: float, width: float, height: float, fill: str = "none", stroke: str = "black", stroke_width: int = 0):
        """[summary]
        Add a rectangle to the SVG canvas.
        
        ### Parameters
        # 1. x (float): The x-coordinate of the rectangle's top-left corner.
        # 2. y (float): The y-coordinate of the rectangle's top-left corner
        # 3. width (float): The width of the rectangle.
        # 4. height (float): The height of the rectangle.
        # 5. fill (str, optional): The fill color of the rectangle. Defaults
        # 6. stroke (str, optional): The stroke color of the rectangle. Defaults
        # 7. stroke_width (int, optional): The width of the stroke. Defaults
        """
        rect_element = f'<rect x="{self.normalized_x + x}" y="{self.normalized_y - y}" width="{width}" height="{height}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'
        self.add_element(rect_element)
    
    def circle(self, cx: float, cy: float, r: float, fill: str = "none", stroke: str = "black", stroke_width: int = 0):
        """[summary]
        Add a circle to the SVG canvas.
        
        ### Parameters
        1. cx (float): The x-coordinate of the circle's center.
        2. cy (float): The y-coordinate of the circle's center.
        3. r (float): The radius of the circle.
        4. fill (str, optional): The fill color of the circle. Defaults to "none".
        5. stroke (str, optional): The stroke color of the circle. Defaults to "black".
        6. stroke_width (int, optional): The width of the stroke. Defaults to 0.
        """
        circle_element = f'<circle cx="{self.normalized_x + cx}" cy="{self.normalized_y - cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'
        self.add_element(circle_element)
    
    def text(self, x: float, y: float, content: str, font_size: int = 16, fill: str = "black"):
        """[summary]
        Add text to the SVG canvas.
        
        ### Parameters
        1. x (float): The x-coordinate of the text's position.
        2. y (float): The y-coordinate of the text's position.
        3. content (str): The text content to display.
        4. font_size (int, optional): The font size of the text. Defaults to 16.
        5. fill (str, optional): The fill color of the text. Defaults to "black".
        """
        text_element = f'<text x="{self.normalized_x + x}" y="{self.normalized_y - y}" font-size="{font_size}" fill="{fill}">{content}</text>'
        self.add_element(text_element)

    def plot_f(self, func, x_start: float, x_end: float, step: float = 1.0, stroke: str = "black", stroke_width: int = 1):
        """[summary]
        Plot a mathematical function on the SVG canvas.
        Args:
            func (callable): The mathematical function to plot.
            x_start (float): The starting x-coordinate for plotting.
            x_end (float): The ending x-coordinate for plotting.
            step (float, optional): The step size for x-coordinates. Defaults to 1.0.
            stroke (str, optional): The stroke color of the plot line. Defaults to "black".
            stroke_width (int, optional): The width of the plot line. Defaults to 1.
        """
        points = []
        x = x_start
        while x <= x_end:
            y = func(x)
            svg_x = self.normalized_x + x
            svg_y = self.normalized_y - y
            points.append(f"{svg_x},{svg_y}")
            x += step
        points_str = " ".join(points)
        polyline_element = f'<polyline points="{points_str}" fill="none" stroke="{stroke}" stroke-width="{stroke_width}" />'
        self.add_element(polyline_element)

    def render(self) -> str:
        """[summary]
        Render the SVG content as a string.
        Returns:
            str: The SVG content as a string.
        """
        svg = f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg" style="background: white;">'
        svg += "\n".join(self.elements)
        svg += '</svg>'
        return svg

    def save(self, filename: str):
        """[summary]
        Save the SVG content to a file.
        Args:
            filename (str): The name of the file to save the SVG content to.
        """
        with open(filename, 'w') as f:
            f.write(self.render())
            print("SVG saved to", filename)
