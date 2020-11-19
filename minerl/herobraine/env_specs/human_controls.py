# Copyright (c) 2020 All Rights Reserved
# Author: William H. Guss, Brandon Houghton

import abc
from abc import ABC
from minerl.herobraine.hero.handlers.translation import TranslationHandler
from minerl.herobraine.hero.handler import Handler

from minerl.herobraine.hero import handlers
from minerl.herobraine.hero.mc import INVERSE_KEYMAP
from minerl.herobraine.env_spec import EnvSpec

from typing import List

KEYBOARD_ACTIONS = [
    "forward",
    "back",
    "left",
    "right",
    "jump",
    "sneak",
    "sprint",
    "attack",
    "use",
    "drop",
    "inventory"
]


class HumanControlEnvSpec(EnvSpec, ABC):
    """
    A simple base environment from which all other simple envs inherit.
    """

    def __init__(self, name, *args, resolution=(640, 480), **kwargs):
        self.resolution = resolution
        super().__init__(name, *args, **kwargs)

    def create_observables(self) -> List[TranslationHandler]:
        return [
            handlers.POVObservation(self.resolution),
        ]

    def create_actionables(self) -> List[TranslationHandler]:
        """
        Simple envs have some basic keyboard control functionality, but
        not all.
        """
        return [
                   handlers.KeybasedCommandAction(k, INVERSE_KEYMAP[k]) for k in KEYBOARD_ACTIONS
               ] + [
                   handlers.KeybasedCommandAction(f"hotbar.{i}", i) for i in range(10)
               ] + [
                   handlers.CameraAction()
               ]

    def create_monitors(self) -> List[TranslationHandler]:
        return []  # No monitors by default!