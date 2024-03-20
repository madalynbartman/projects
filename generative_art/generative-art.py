import random
import uuid

from PIL import Image, ImageDraw

run_id = uuid.uuid1()

print(f'Processing run_id: {run_id}')

image = Image.new('RGB, {2000, 2000}')

image = Image.new('RGB', (2000, 2000))
width, height = image.size

rectangle_width = 100
rectangle_height = 100

number_of_squares = random.randint(10, 550)

draw_image = ImageDraw.Draw(image)
for i in  range(number_of_squares):
    rectangle_x = random.randint(0, width)
    rectangle_y = random.randint(0, height)

    rectangle_shape = [
        (rectangle_x, rectangle_y),
        (rectangle_x + rectangle_width, rectangle_y + rectangle_height)
    ]
    draw_image.rectangle(
        rectangle_shape,
        fill=(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    )

image save(f'./output/{run_id}.png')

# Generative art aka procedural art
# rules x inputs = outputs
# example: Every Tuesay at 7pm, take a picture of the sky
# - rule: action every T at 7om
# - input: sky

# Generative art with code
# increase scalability + breath of possibilities 
# Ex: generate a color for every word in the dictionary
# - rule: generate a color
# - input: dictionary words

# data sets can include classical paintings, photography, etc

# Generate squares on an image
# rule: generate squares
# - location
# - color
# input: random
# random input keeps the art diverse
# squares are a great basic project to start with
