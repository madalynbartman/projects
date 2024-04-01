import segno

url = 'https://github.com/madalynbartman'

qr = segno.make(url)
qr.save('github_qr_code.png', scale=10)
