"""Registry used to supervise stores."""

from __future__ import annotations

from typing import TYPE_CHECKING

from mandr.store import Store

if TYPE_CHECKING:
    from typing import Generator

    from mandr.storage import Storage


def children(store: Store) -> Generator[Store, None, None]:
    """Yield recursively `store` children."""
    stores = {store.uri}

    for uri in store.storage:
        if ((uri := uri.parent) not in stores) and (store.uri in uri):
            stores.add(uri)
            yield Store(uri, store.storage)


def parent(store: Store, /) -> Store:
    """Return `store` parent."""
    return Store(store.uri.parent, store.storage)


def stores(storage: Storage, /) -> Generator[Store, None, None]:
    """Yield stores saved in `storage`."""
    stores = set()

    for uri in storage:
        if (uri := uri.parent) not in stores:
            stores.add(uri)
            yield Store(uri, storage)