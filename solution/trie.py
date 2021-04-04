from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self: object) -> None:
        """Constructor.
        """
        self.children: defaultdict = defaultdict(TrieNode)
        self.handler: str = None


class Trie:
    def __init__(self: object) -> None:
        """Constructor.
        """
        self.root: TrieNode = TrieNode()

    def insert(
            self: object,
            url_parts: List[str],
            handler_name: str) -> None:
        """Add a handler to the trie.

            Time Complexity = O(len(url_parts))
            Space Complexity = O(len(url_parts))

            Parameters
            ----------
            url : str, required
                URL to add the handler for.
            handler_name : str, required
                The name of the handler.
        """

        if not url_parts or not handler_name:
            return None
        if not isinstance(url_parts, list) or not isinstance(handler_name, str):
            raise TypeError(
                "URL has to be of type list and handler name has to be of type str...")
        if len(url_parts) == 0 or len(handler_name) == 0:
            return None
        if "/" in url_parts:
            raise ValueError("Don't add '/' to the url parts...")

        current_node: TrieNode = self.root

        for part in url_parts:
            current_node = current_node.children[part]

        current_node.handler = handler_name

    def find(self: object, url_parts: List[str]):
        """Find the Trie node with handler for the url path.

            Time Complexity = O(len(url_parts))
            Space Complexity = O(1)

            Parameters
            ----------
            url_parts : List[str], required
                List with the url parts in correct order starting coming from root.

            Returns
            ----------
            TrieNode
                Returns the handler (string) or None if not found.
        """

        if not url_parts:
            return None
        if not isinstance(url_parts, list):
            raise TypeError("URL parts has to be of type list...")
        if len(url_parts) == 0:
            return None

        current_node: TrieNode = self.root

        for url_part in url_parts:
            if url_part in current_node.children:
                current_node = current_node.children[url_part]
            else:
                return None

        return current_node.handler
