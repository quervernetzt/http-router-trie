from typing import List
from solution.trie import Trie


class Router:
    def __init__(
            self: object,
            root_handler: str,
            not_found_handler: str) -> None:
        """Constructor.

            Parameters
            ----------
            root_handler : str, required
                The root handler (name).
            not_found_handler : str, required
                The not found handler (name).
        """
        if not root_handler or not not_found_handler:
            raise ValueError(
                "Please specify a valid root and not found handler...")
        if not isinstance(root_handler, str) or not isinstance(not_found_handler, str):
            raise TypeError("URL and handler name have to be of type str...")
        if len(root_handler) == 0 or len(not_found_handler) == 0:
            raise ValueError(
                "Please specify a valid root and not found handler...")

        self.router: Trie = Trie()
        self.router.root.handler = root_handler
        self.not_found_handler: str = not_found_handler

    def add_handler(
            self: object,
            url: str,
            handler_name: str) -> None:
        """Add handler to a given url in the router trie.

            Time Complexity: O(len(url) + <number of parts resulting from the split>)
            Space Complexity: O(<number of parts resulting from the split>)

            Parameters
            ----------
            url : str, required
                URL to assign the handler to.
            handler_name : str, required
                The name of the handler to assign to the URL.
        """

        if not url or not handler_name:
            return None
        if not isinstance(url, str) or not isinstance(handler_name, str):
            raise TypeError("URL and handler name have to be of type str...")
        if len(url) == 0 or len(handler_name) == 0:
            return None

        if url == "/":
            self.router.root.handler = handler_name
            return None

        url_parts: List[str] = self.split_path(url)

        if len(url_parts) > 0:
            self.router.insert(url_parts, handler_name)

    def lookup(self: object, url: str) -> str:
        """Get the handler for an URL.

            Time Complexity: O(len(url) + <number of parts resulting from the split>)
            Space Complexity: O(<number of parts resulting from the split>)

            Parameters
            ----------
            url : str, required
                URL to find the handler for.

            Returns
            ----------
            list
                Returns the handler (string). In case no handler exists it returns the 'Not Found' handler.
        """
        if not url:
            raise ValueError("Please provide an URL...")
        if not isinstance(url, str):
            raise TypeError("URL has to be of type str...")
        if len(url) == 0:
            raise ValueError("Please provide an URL...")

        if url == "/":
            return self.router.root.handler

        handler: str = None
        url_parts: List[str] = self.split_path(url)

        if len(url_parts) > 0:
            handler = self.router.find(url_parts)

        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self: object, url: str) -> List[str]:
        """Split url.

            Time Complexity: O(len(url))
            Space Complexity: O(number of parts resulting from the split)

            Parameters
            ----------
            url : str, required
                URL to split.

            Returns
            ----------
            list
                Returns the url parts as list.
        """

        if not url:
            return []
        if not isinstance(url, str):
            raise TypeError("URL has to be of type str...")
        if len(url) == 0:
            return []

        if url[-1] == "/":
            url = url[:-1]
        if url[0] == "/":
            url = url[1:]
        url_split: List[str] = url.split("/")

        return url_split
