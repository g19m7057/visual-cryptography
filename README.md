# visual-cryptography
Python script that can decode an image into two images and reconstruct the image using the 2 images.
uses python opencv, numpy, random and sys.

To encode.
```bash:
$ python visualCrypto.py encode imageToEncode.png
```
This creates two images of the encoded message.

To reconstruct the image:
```bash:
$ python visualCrypto.py decode encoded1.png encoded2.png
```
This returns the original image.
