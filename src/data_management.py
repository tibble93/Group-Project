"""Data management for inventory system.

This module provides simple functions to act as a lightweight database
for storing inventory information in a JSON file. It offers operations
for loading and saving the full dataset as well as adding, updating,
removing, and querying individual items. All functions include basic
error handling to cope with file access problems.
"""

import json
import os
from typing import Any, Dict, Optional, List


DEFAULT_DATA_FILE = os.path.join(os.path.dirname(__file__), "inventory.json")


# Helper functions -----------------------------------------------------------

def _ensure_file(path: str) -> None:
    """Create the file with an empty dict if it doesn't exist."""
    if not os.path.exists(path):
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump({}, f)
        except OSError as exc:
            raise RuntimeError(f"unable to create data file {path}: {exc}")


def load_data(path: str = DEFAULT_DATA_FILE) -> Dict[str, Any]:
    """Load the entire dataset from a JSON file.

    Returns an empty dict if the file does not exist or is unreadable.
    """
    _ensure_file(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        # if file corrupted or unreadable, return empty but warn
        print(f"warning: failed to read data file {path}: {exc}")
        return {}


def save_data(data: Dict[str, Any], path: str = DEFAULT_DATA_FILE) -> None:
    """Save the provided dataset to the JSON file, overwriting existing.
    """
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError as exc:
        raise RuntimeError(f"unable to write to data file {path}: {exc}")


# CRUD operations -----------------------------------------------------------

def list_items(path: str = DEFAULT_DATA_FILE) -> List[Dict[str, Any]]:
    """Return a list of all items stored in the database."""
    data = load_data(path)
    return list(data.values())


def get_item(item_id: str, path: str = DEFAULT_DATA_FILE) -> Optional[Dict[str, Any]]:
    """Retrieve a single item by its identifier.

    Returns ``None`` if the item does not exist.
    """
    data = load_data(path)
    return data.get(item_id)


def add_item(item_id: str, item: Dict[str, Any], path: str = DEFAULT_DATA_FILE) -> None:
    """Add a new item to the database.

    Raises a ``RuntimeError`` if an item with the same id already exists.
    """
    data = load_data(path)
    if item_id in data:
        raise RuntimeError(f"item '{item_id}' already exists")
    data[item_id] = item
    save_data(data, path)


def update_item(item_id: str, item: Dict[str, Any], path: str = DEFAULT_DATA_FILE) -> None:
    """Update an existing item. Same signature as ``add_item``.

    Raises a ``RuntimeError`` if the item does not exist.
    """
    data = load_data(path)
    if item_id not in data:
        raise RuntimeError(f"item '{item_id}' does not exist")
    data[item_id] = item
    save_data(data, path)


def delete_item(item_id: str, path: str = DEFAULT_DATA_FILE) -> None:
    """Remove an item from the database.

    Does nothing if the item is not present.
    """
    data = load_data(path)
    if item_id in data:
        del data[item_id]
        save_data(data, path)


# Simple command-line interface for manual testing -------------------------

if __name__ == "__main__":
    # This section is minimal and can be expanded as needed. It is
    # primarily for quick sanity checks when running the module directly.
    import argparse

    parser = argparse.ArgumentParser(description="Manage inventory data file")
    parser.add_argument("--list", action="store_true", help="list all items")
    parser.add_argument("--get", metavar="ID", help="get item by id")
    parser.add_argument("--delete", metavar="ID", help="delete item by id")
    parser.add_argument("--add", nargs=2, metavar=("ID", "JSON"),
                        help="add a new item (provide id and JSON string)")
    parser.add_argument("--update", nargs=2, metavar=("ID", "JSON"),
                        help="update an existing item")
    args = parser.parse_args()

    if args.list:
        for itm in list_items():
            print(itm)
    elif args.get:
        print(get_item(args.get))
    elif args.delete:
        delete_item(args.delete)
    elif args.add:
        add_item(args.add[0], json.loads(args.add[1]))
    elif args.update:
        update_item(args.update[0], json.loads(args.update[1]))
    else:
        parser.print_help()