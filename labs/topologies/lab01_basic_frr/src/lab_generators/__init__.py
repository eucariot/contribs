from annet.generators import BaseGenerator
from annet.storage import Storage

from . import frr


def get_generators(store: Storage) -> list[BaseGenerator]:
    """All the generators should be returned by the function"""

    return [
        frr.Frr(store),
    ]
