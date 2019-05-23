#!/usr/bin/env python3

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

def iter_slide_shapes(prs):
    for slide in prs.slides:
        print(f'slides={len(prs.slides)}')
        for shape in slide.shapes:
            print(f'...shapes={len(slide.shapes)}, {shape.shape_type}')
            if shape.shape_type == MSO_SHAPE_TYPE.PICTURE:
                yield shape

def get_images(filename):
    i = 0
    for picture in iter_slide_shapes(Presentation(filename)):
        i += 1
        image = picture.image
        # ---get image "file" contents---
        image_bytes = image.blob
        # ---make up a name for the file, e.g. 'image.jpg'---
        image_filename = 'image ' + str(i) + '.' + image.ext
        with open(image_filename, 'wb') as f:
            f.write(image_bytes)

def main():
    filename = 'ARG162-Flat.pptx'
    prs = Presentation(filename)
    get_images(filename)
    return

if __name__ == "__main__":
    main()

