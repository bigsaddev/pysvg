from lib.svgpy import SVGCanvas

def main():
    canvas = SVGCanvas(800, 600, color="lightyellow", scaling_factor=10.0)
    canvas.setup_axis(color="gray", stroke_width=2)
    #canvas.rect(5, 5, 100, 150, fill="blue", stroke="black")
    #canvas.circle(-5, 0, 50, fill="red", stroke="black")
    
    
    canvas.plot_f(lambda x: 0.1 * -(x**2), -10, 10, stroke="green", stroke_width=1)
    canvas.plot_f(lambda x: x**2, -10, 10, stroke="orange", stroke_width=1)
    canvas.plot_f(lambda x: 0.5 * x**3 - 10 * x, -10, 10, stroke="purple", stroke_width=1)
    canvas.plot_f(lambda x: -0.1 * x**3, 0, 10, stroke="red", stroke_width=1)
    canvas.text(0, 0, "Hello, SVG!", font_size=24, fill="black")

    canvas.save("plot.svg")


if __name__ == "__main__":
    main()
