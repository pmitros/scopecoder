Stack-a-scope
----------

This is an experiment. It's intended to give images with focus stacking from a microscope. It's not anything more than a bit of play with image processing at this point -- it doesn't really work very well. So please move along, unless you're *really* interested in half-working projects.

The way this project works is:

* Mount a camera on a microscope
* Take a video while adjusting focus
* Convert the video to still images
* Align the images with `align.py`
* Finally, the `merge.py` script tries to merge the images into a single, focus-stacked one

Where do we fail?

For one, we don't really do a good job in aligning images. As we refocus the microscope, the angle-of-view changes a bit, which plays odd games on what we need to do there. Second, looking for maximum contrast doesn't really work for figuring out where the right slices are. Big parts of images are a flat color, and the algorithm falls flat on its face there. The transitions are also a bit rough; we should blur between the images somehow.

Those aren't necessarily hard problems to solve; but this project was an evening of hacking for fun, so I never actually solved them.