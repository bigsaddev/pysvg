class SVGCanvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.elements = []
        self.axis_enabled = False

    def setup_axis(self, color: str = "black", stroke_width: int = 1):
        """Draw X and Y axes at origin (top-left) if enabled."""
        self.axis_enabled = True
        self.add_element(f'<line x1="0" y1="0" x2="{self.width}" y2="0" stroke="{color}" stroke-width="{stroke_width}" />')
        self.add_element(f'<line x1="0" y1="0" x2="0" y2="{self.height}" stroke="{color}" stroke-width="{stroke_width}" />')

    def add_element(self, element: str):
        self.elements.append(element)
    
    def rect(self, x: float, y: float, width: float, height: float, fill: str = "none", stroke: str = "black", stroke_width: int = 0):
        """Add a rectangle to the SVG canvas."""
        rect_element = f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'
        self.add_element(rect_element)
    
    def circle(self, cx: float, cy: float, r: float, fill: str = "none", stroke: str = "black", stroke_width: int = 0):
        """Add a circle to the SVG canvas."""
        circle_element = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'
        self.add_element(circle_element)

    def render(self) -> str:
        svg = f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg" style="background: white;">'
        svg += "\n".join(self.elements)
        svg += '</svg>'
        return svg

    def save(self, filename: str):
        """Save the SVG content to a file."""
        with open(filename, 'w') as f:
            f.write(self.render())
            print("SVG saved to", filename)
