from lib.svgpy import SVGCanvas

def main():
    canvas = SVGCanvas(800, 600)
    canvas.setup_axis(color="gray", stroke_width=2)
    canvas.rect(50, 50, 100, 150, fill="blue", stroke="black")
    canvas.circle(-50, 0, 50, fill="red", stroke="black")
    canvas.text(0, 0, "Hello, SVG!", font_size=24, fill="black")
    canvas.plot_f(lambda x: 0.01 * x**2, -200, 200, stroke="green", stroke_width=4)

    canvas.save("plot.svg")


if __name__ == "__main__":
    main()
