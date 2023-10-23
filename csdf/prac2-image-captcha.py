from captcha.image import ImageCaptcha

image = ImageCaptcha(width=200, height=90)

captcha_text = "Cyber"

data = image.generate(captcha_text)

image.write(captcha_text, "CAPTCHA.png")
