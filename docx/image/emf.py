# encoding: utf-8

from __future__ import absolute_import, division, print_function

from struct import Struct

from .constants import MIME_TYPE
from .image import BaseImageHeader


# EMS Header information extracted from
# https://docs.microsoft.com/en-us/openspecs/windows_protocols/
#         ms-emf/ae7e7437-cfe5-485e-84ea-c74b51b000be
# on 2019-02-28
class Emf(BaseImageHeader):
    """
    Image header parser for EMF images. This is Extended (Enhanced) Metafile
    Format by Microsoft
    """
    @classmethod
    def from_stream(cls, stream):
        """
        Return |emf| instance having header properties parsed from EMF image
        in *stream*.
        """
        px_width, px_height = cls._dimensions_from_stream(stream)
        return cls(px_width, px_height, 72, 72)

    @property
    def content_type(self):
        """
        MIME content type for this image, unconditionally `image/x-emf` for
        EMF images.
        """
        return MIME_TYPE.EMF

    @property
    def default_ext(self):
        """
        Default filename extension, always 'gif' for GIF images.
        """
        return 'emf'

    @classmethod
    def _dimensions_from_stream(cls, stream):
        stream.seek(8)
        bytes_ = stream.read(16)
        struct = Struct('<IIII')
        px_left, px_top, px_width, px_height = struct.unpack(bytes_)
        return px_width - px_left, px_height - px_top
