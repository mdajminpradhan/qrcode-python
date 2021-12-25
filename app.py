import qrcode

# setting optional settings here
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=50,
    border=5,
)

# taking user input from here

name = input('Hello! What is your name: ')
country = input('What is country name: ')
language = input('What is your primary language: ')
profession = input('What do you do: ')
p_language = input('What is your primary programming language: ')

data = {
    name: name,
    country: country,
    language: language,
    profession: profession,
    p_language: p_language
}

qr.add_data(data)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_app.png")