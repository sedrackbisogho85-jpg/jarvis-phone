from PIL import Image, ImageDraw


def make(size):
    image = Image.new("RGB", (size, size), (3, 26, 29))
    draw = ImageDraw.Draw(image)
    c = size // 2
    teal = (53, 214, 214)
    for radius, width in ((0.36, 0.035), (0.27, 0.02)):
        r = int(size * radius)
        w = max(2, int(size * width))
        draw.ellipse([c - r, c - r, c + r, c + r], outline=teal, width=w)
    r = int(size * 0.15)
    draw.ellipse([c - r, c - r, c + r, c + r], fill=teal)
    return image


big = make(512)
big.save("icon-512.png")
big.resize((192, 192)).save("icon-192.png")
print("Icons made.")