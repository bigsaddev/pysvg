from lib.svgpy import SVGCanvas

def main():
    canvas = SVGCanvas(400, 400)
    canvas.setup_axis(color="gray", stroke_width=2)
    canvas.rect(50, 50, 100, 150, fill="blue", stroke="black")
    canvas.circle(200, 200, 50, fill="red", stroke="black")
    
    canvas.save("plot.svg")


if __name__ == "__main__":
    main()
