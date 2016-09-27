# Blurrer

I like 8 bit art, and I wanted to make an easy method for pixellating existing images from the command line.

## With this script, you can:

- Convert images of common filetypes to pixellated versions
- Specify the size of the pixels to be used in the resulting image

## What it does

The input image is divided into squares matching the input final pixel size.

The average color of each of those squares is then calculated by averaging each of the RBGA values from the member pixels.

A new image is then constructed of squares matching the input final pixel size, with the color of those squares being set to the calculated average color of the original pixels in that area.

## How we deal with remainders

Pixellated art should end up with an whole number of vertical and horizontal pixels. In order to keep the result looking correct, the input images are cropped to the largest even multiple of the specified final pixel size.

## An example

Here's a 700x500 image of a Mario Mushroom from Wikipedia:

![Mario Mushroom][mushroom]

[mushroom]: https://raw.githubusercontent.com/jordanwdunne/Blurrer/master/test.png "Mario Mushroom"

The goal is to pixellate this photo, with the resulting picture having square 35x35 pixels.

To make this happen, the following command line arguments are used:

```
python blur.py blur test.png 35
```

The resulting image was pixellated, with the end result composed of 35x35 pixel squares:

![Blurred Mario Mushroom][blurred35Mushroom]

[blurred35Mushroom]: https://raw.githubusercontent.com/jordanwdunne/Blurrer/master/blurred_35_test.png "Blurred Mario Mushroom"

## Another example (with cropping being necessary)

If a specified pixel size isn't evenly divisible into the input image's dimensions, then the result needs to be cropped so no partial pixels are present.

As an example, again relying on the Mario mushroom picture, we will specify a pixel size of 60. This isn't evenly divisible, so cropping will occur to the nearest full pixel of that size.

```
python blur.py blur test.png 60
```

The resulting image was pixellated, with the end result composed of 60x60 pixel squares, and has been cropped (it's now 11 by 8 "pixels")

![Blurred Mario Mushroom][blurred60Mushroom]

[blurred60Mushroom]: https://raw.githubusercontent.com/jordanwdunne/Blurrer/master/blurred_60_test.png "Blurred Mario Mushroom"

As of now, cropping will only occur from the right and bottom edges of a photo (note that the 60x60 blurred image seems shifted to the bottom right)

## Todos:

- Correct shifting in cropped images (crop evenly from the center)
- Add support for other filetypes
- Add support for animated GIF blurring and recomposition
