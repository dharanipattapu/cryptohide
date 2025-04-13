from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    binary_data = ""
    decoded_message = ""

    for pixel in img.getdata():
        for value in pixel[:3]:  # RGB only
            binary_data += str(value & 1)

    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        char = chr(int(byte, 2))
        if char == chr(0):
            break
        decoded_message += char
    print("Decoded Message:", decoded_message)
    return decoded_message
