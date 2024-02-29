import sys
from PIL import Image
def embed_message_into_image(image_path, message):
   image = Image.open(image_path).convert("RGB")
   encoded_image = image.copy()
   pixels = encoded_image.load()
   width, height = encoded_image.size
   binary_message = ''.join([format(ord(char), '08b') for char in message])
   binary_message += '1111111111111110'
   index = 0
     for row in range(height):
       for col in range(width):
         pixel = list(pixels[col, row])
         for n in range(3):
           if index < len(binary_message):
           current_bit = int(binary_message[index])
               if pixel[n] % 2 != current_bit:
                 if current_bit == 0:
                   pixel[n] = pixel[n] - 1 if pixel[n] % 2 != 0 else pixel[n]
                 else:
                   pixel[n] = pixel[n] + 1 if pixel[n] % 2 == 0 else pixel[n]
                   index += 1
                   pixels[col, row] = tuple(pixel)
                   encoded_image.save('image_with_secret_message.png')
                   
    def extract_message_from_image(image_path):
       image = Image.open(image_path).convert("RGB")
       pixels = image.load()
       width, height = image.size
       binary_message = ''
         for row in range(height):
           for col in range(width):
             pixel = pixels[col, row]
         for n in pixel[:3]:
           bits = [int(x) for x in format(n, '08b')]
           binary_message += str(bits[-1])
           binary_message = binary_message.split('1111111111111110')[0]
           message = ''
         for i in range(0, len(binary_message), 8):
         byte = binary_message[i:i+8]
         message += chr(int(byte, 2))
         return message
    if __name__ == "__main__":
     if len(sys.argv) < 3:
       print("Usage: python lsb.py <write/read> <image_path> [message]")
       sys.exit(1)
       command = sys.argv[1]
       image_path = sys.argv[2]
     if command == 'write':
    
     if len(sys.argv) != 4:
       print("Usage for write: python lsb.py write <image_path> <message>")
       sys.exit(1)
       message = sys.argv[3]
     if not all(char.isalnum() for char in message):
       print("Error: Message must contain only alphanumeric characters.")
       sys.exit(1)
       embed_message_into_image(image_path, message)
       print("Message embedded into image_with_secret_message.png")
     elif command == 'read':
       message = extract_message_from_image(image_path)
       print("Extracted message:", message)
     else:
       print("This functionality is not available.")
       sys.exit(1)
