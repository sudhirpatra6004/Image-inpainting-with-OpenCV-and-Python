# Image-inpainting-with-OpenCV-and-Python



When applying inpainting with OpenCV, we need to provide two images:

1:   The input image we wish to inpaint and restore. Presumably, this image is “damaged” in some manner, and we need to apply inpainting algorithms to fix it
2:   The mask image, which indicates where in the image the damage is. This image should have the same spatial dimensions (width and height) as the input image. Non-zero pixels        correspond to areas that should be inpainted (i.e., fixed), while zero pixels are considered “normal” and do not need inpaint![opencv_inpainting_header](https://user-images.githubusercontent.com/44130329/111456117-9b67f100-873c-11eb-8a1e-0d15b6c22685.jpg)

