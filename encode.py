from PIL import Image

def encode_image(input_image_path, message, output_image_path):
    img = Image.open(input_image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    message += chr(0)  # Add a null character as a delimiter
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                r, g, b = img.getpixel((col, row))
                r = (r & ~1) | int(binary_message[index])
                index += 1
                if index < len(binary_message):
                    g = (g & ~1) | int(binary_message[index])
                    index += 1
                if index < len(binary_message):
                    b = (b & ~1) | int(binary_message[index])
                    index += 1
                encoded.putpixel((col, row), (r, g, b))
            else:
                break
    encoded.save(output_image_path)
    print("Message encoded successfully.")
