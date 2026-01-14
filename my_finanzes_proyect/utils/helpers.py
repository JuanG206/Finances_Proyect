#!/usr/bin/env python3
"""
Module: helpers
Auxiliary functions.
"""

import uuid

def generate_id():
    """Generate a unique string ID."""
    return str(uuid.uuid4())
