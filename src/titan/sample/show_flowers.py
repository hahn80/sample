#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations


class Flower:
    def __init__(self, name: str):
        self.name = name

    def blooming(self):
        return f"Flower {self.name} is booming"


def upper_name(name: str):
    return name.upper()
