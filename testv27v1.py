#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Example code for a PyQt image-display widget which Just Works™
TODO: Split this into a loader wrapper and a widget wrapper so it can be used
      in designs which maintain a preloaded queue of upcoming images to improve
      the perception of quick load times.
"""

from __future__ import (absolute_import, division, print_function,
                        with_statement, unicode_literals)

__author__ = "Stephan Sokolow (deitarion/SSokolow)"
__license__ = "MIT"

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImageReader, QMovie, QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QFrame, QLabel, QVBoxLayout

class SaneDefaultsImageLabel(QFrame):
    """Compound widget to work around some shortcomings in Qt image display.
    - Animated GIFs will animate, like in a browser, by transparently switching
      between QImage and QMovie internally depending on the number of frames
      detected by QImageReader.
    - Content will scale up or down to fit the widget while preserving its
      aspect ratio and will do so without imposing a minimum size of 100%.
    - Letterbox/pillarbox borders will default to black.
      (It's a bit of a toss-up whether an application will want this or the
       default window background colour, so this defaults to the choice that
       provides an example of how to accomplish it.)
    Note that QImageReader doesn't have an equivalent to GdkPixbufLoader's
    `area-prepared` and `area-updated` signals, so incremental display for
    for high-speed scanning (ie. hitting "next" based on a partially loaded
    images) isn't really possible. The closest one can get is to experiment
    with QImageReader's support for loading just part of a JPEG file to see if
    it can be done without significantly adding to the whole-image load time.
    (https://wiki.qt.io/Loading_Large_Images)
    """

    movie_aspect = None
    orig_pixmap = None

    def __init__(self):
        super(SaneDefaultsImageLabel, self).__init__()

        # We need a layout if we want to prevent the image from distorting
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # Set the letterbox/pillarbox bars to be black
        # https://wiki.qt.io/How_to_Change_the_Background_Color_of_QWidget
        pal = self.palette()
        pal.setColor(QPalette.Background, Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        # No black bordering on non-letterbox/pillarbox edges
        layout.setContentsMargins(0, 0, 0, 0)

    def load(self, source):
        """Load anything that QImageReader or QMovie constructors accept"""

        # Use QImageReader to identify animated GIFs for separate handling
        # (Thanks to https://stackoverflow.com/a/20674469/435253 for this)
        image_reader = QImageReader(source)
        from PyQt5.QtGui import QImageIOHandler
        if image_reader.supportsAnimation() and image_reader.imageCount() > 1:
            movie = QMovie(source)

            # Calculate the aspect ratio and adjust the widget size
            movie.jumpToFrame(0)
            movie_size = movie.currentImage().size()
            self.movie_aspect = movie_size.width() / movie_size.height()
            self.resizeEvent()

            self.label.setMovie(movie)
            movie.start()

            # Free memory if the previous image was non-animated
            self.orig_pixmap = None
        else:
            self.orig_pixmap = QPixmap(image_reader.read())
            self.label.setPixmap(self.orig_pixmap)

            # Fail quickly if our violated invariants result in stale
            # aspect-ratio information getting reused
            self.movie_aspect = None

        # Keep the image from preventing downscaling
        self.setMinimumSize(1, 1)

    def resizeEvent(self, _event=None):
        """Resize handler to update dimensions of displayed image/animation"""
        rect = self.geometry()

        movie = self.label.movie()
        if movie:
            # Manually implement aspect-preserving scaling for QMovie
            #
            # Thanks to Spencer @ https://stackoverflow.com/a/50166220/435253
            # for figuring out that this approach must be taken to get smooth
            # up-scaling out of QMovie.
            width = rect.height() * self.movie_aspect
            if width <= rect.width():
                size = QSize(width, rect.height())
            else:
                height = rect.width() / self.movie_aspect
                size = QSize(rect.width(), height)

            movie.setScaledSize(size)
        elif self.orig_pixmap and not self.orig_pixmap.isNull():
            # To avoid having to change which widgets are hidden and shown,
            # do our upscaling manually.
            #
            # This probably won't be suitable for widgets intended to be
            # resized as part of normal operation (aside from initially, when
            # the window appears) but it works well enough for my use cases and
            # was the quickest, simplest thing to implement.
            #
            # If your problem is downscaling very large images, I'd start by
            # making this one- or two-line change to see if it's good enough:
            #  1. Use Qt.FastTransformation to scale to the closest power of
            #     two (eg. 1/2, 1/4, 1/8, etc.) that's still bigger and gives a
            #     decent looking intermediate result.
            #  2. Use Qt.SmoothTransform to take the final step to the desired
            #     size.
            #
            # If it's not or you need actual animation, you'll want to look up
            # how to do aspect-preserving display of images and animations
            # under QML (embeddable in a QWidget GUI using QQuickWidget) so Qt
            # can offload the scaling to the GPU.
            size = QSize(rect.width(), rect.height())

            # Don't waste CPU generating a new pixmap if the resize didn't
            # alter the dimension that's currently bounding its size
            pixmap_size = self.label.pixmap().size()
            if (pixmap_size.width() == size.width() and
              pixmap_size.height() <= size.height()):
                return
            if (pixmap_size.height() == size.height() and
              pixmap_size.width() <= size.width()):
                return

            self.label.setPixmap(self.orig_pixmap.scaled(size,
                Qt.KeepAspectRatio, Qt.SmoothTransformation))

def main():
    """Main entry point for demonstration code"""
    import sys
    sys.argv[0]='gato.gif'
    '''if len(sys.argv) != 2:
        print("Usage: {} <image path>".format(sys.argv[0]))
        sys.exit(1)'''

    # I don't know how reliable it is, but making `app` a global which outlives
    # `main()` seems to fix the "segmentation fault on exit" bug caused by
    # Python and Qt disagreeing on the destruction order for the QObject tree
    # and it's certainly the most concise solution I've yet found.
    global app  # pylint: disable=global-statement, global-variable-undefined

    app = QApplication(sys.argv)

    # Take advantage of how any QWidget subclass can be used as a top-level
    # window for demonstration purposes
    window = SaneDefaultsImageLabel()
    window.load('e:\freelancer\biomecanica\gato.gif')
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

# vim: set sw=4 sts=4 expandtab :
