# tests/test_bdd.py
import pytest
from pytest_bdd import scenarios
from features.steps.parking_steps import *  # noqa: F401, F403

scenarios('../features/parking.feature')