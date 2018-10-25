"""Skeleton of a handler."""

import logging

import rasterio

import pyskel

logger = logging.getLogger("pyskel")
logger.setLevel(logging.INFO)


def main(event, context):
    """Handler."""
    return pyskel.has_legs
