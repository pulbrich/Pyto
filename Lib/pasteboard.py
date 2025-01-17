# -*- coding: utf-8 -*-
"""
Pasteboard Access

This module gives access to the pasteboard.
"""

from UIKit import UIPasteboard as __UIPasteboard__, UIImage
from typing import List
try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(class_name):
        return None


NSURL = ObjCClass("NSURL")


def general_pasteboard():
    return __UIPasteboard__.generalPasteboard


# MARK: - Text


def string() -> str:
    """
    Returns the text contained in the pasteboard.
    """
    return str(general_pasteboard().string)


def strings() -> List[str]:
    """
    Returns all strings contained in the pasteboard.
    """
    return general_pasteboard().strings


def set_string(text: str):
    """
    Copy the given text to the pasteboard.

    :param text: The text to copy.
    """
    general_pasteboard().string = text


def set_strings(array: List[str]):
    """
    Copy the given strings to the pasteboard.

    :param array: A list of strings to copy.
    """
    general_pasteboard().strings = array


# MARK: - Images


def image() -> UIImage:
    """
    Returns the image contained in the pasteboard as an Objective-C ``UIImage``.
    """
    return general_pasteboard().image


def images() -> List[UIImage]:
    """
    Returns all images contained in the pasteboard as Objective-C ``UIImage``s.
    """
    return general_pasteboard().images


def set_image(image: UIImage):
    """
    Copy the given image to the pasteboard.

    :param image: The image to copy.
    """
    general_pasteboard().image = image


def set_images(array: List[UIImage]):
    """
    Copy the given images to the pasteboard.

    :param array: A list of images to copy.
    """
    general_pasteboard().images = array


# MARK: - URLs


def url() -> NSURL:
    """
    Returns the URL contained in the pasteboard as an Objective-C ``NSURL``.
    """
    return general_pasteboard().url


def urls() -> List[NSURL]:
    """
    Returns all URLs contained in the pasteboard as Objective-C ``NSURL``s.
    """
    return general_pasteboard().urls


def set_url(url: NSURL):
    """
    Copy the given URL to the pasteboard.

    :param url: The Objective-C ``NSURL`` to copy.
    """
    general_pasteboard().url = url


def set_urls(array: List[NSURL]):
    """
    Copy the given URLs to the pasteboard.

    :param array: A list of Objective-C ``NSURL``s to copy.
    """
    general_pasteboard().urls = array
