# Blurrer

I like 8 bit art, and I wanted to make an easy method for pixellating existing images from the command line.

## With 8bitify, you can:

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

![Mario Mushroom][logo]

[logo]: https://github.com/jordanwdunne/8bitify/test.png "Mario Mushroom"

I want to pixellate this photo, with the resulting picture having square 35x35 pixels.

To make this happen, the following command line arguments are used:

```
python blur.py blur test.png 35
```
