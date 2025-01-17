import qrcode   #imports the qrcode library, which is used for generating QR codes

import image  #imports the image module { command not needed: the 'qrcode' library as it's inbuilt image properties}


# creates an instance of the QRCode class from the qrcode library.
qr = qrcode.QRCode(
    
    version = 15,   # version parameter defines the size of the QR code
    
    box_size = 10,  # parameter specifies the number of pixels each box 
    
    border = 5      # defines the thickness of the border around the QR code
)

# to website or place or message where this QR sends
data = ' Have a Wonderful day ahead. '

qr.add_data(data)   # adds the data to the QR code object

qr.make(fit = True) # ensures that the QR code is sized appropriately to fit the data

img = qr.make_image(fill='black', back_color = 'white')    # generates an image of the QR code
 
img.save('test.png')


