import unittest
from typing import List
from solution.trie import Trie


class TestCasesTrie(unittest.TestCase):
    def insert_url_parts_is_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = None
        handler_name: str = "Test handler"

        # Act & Assert
        trie.insert(url_parts, handler_name)

    def insert_url_parts_is_empty(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = []
        handler_name: str = "Test handler"

        # Act & Assert
        trie.insert(url_parts, handler_name)

    def insert_url_parts_is_not_list_raise_type_error(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: int = 12
        handler_name: str = "Test handler"

        # Act & Assert
        self.assertRaises(TypeError, trie.insert, url_parts, handler_name)

    def insert_handler_name_is_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = ["home", "test"]
        handler_name: str = None

        # Act & Assert
        trie.insert(url_parts, handler_name)

    def insert_handler_name_is_empty(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = ["home", "test"]
        handler_name: str = ""

        # Act & Assert
        trie.insert(url_parts, handler_name)

    def insert_handler_name_is_not_str_raise_type_error(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = ["home", "test"]
        handler_name: int = 123

        # Act & Assert
        self.assertRaises(TypeError, trie.insert, url_parts, handler_name)

    def insert_url_parts_is_root(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = ["/"]
        handler_name: str = "Test Handler"

        # Act & Assert
        self.assertRaises(ValueError, trie.insert, url_parts, handler_name)

    def insert_url_parts_has_multiple_elements(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = ["home", "test", "part"]
        handler_name: str = "Test handler"

        # Act & Assert
        trie.insert(url_parts, handler_name)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def find_url_parts_is_none_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = None

        # Act
        result: str = trie.find(url_parts)

        # Assert
        self.assertIsNone(result)

    def find_url_parts_is_empty_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = []

        # Act
        result: str = trie.find(url_parts)

        # Assert
        self.assertIsNone(result)

    def find_url_parts_is_not_list_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: int = 123

        # Act & Assert
        self.assertRaises(TypeError, trie.find, url_parts)

    def find_url_parts_is_fine_search_for_url_that_exists_return_handler_name(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = ["home", "test", "part"]
        handler_name: str = "Test handler"

        # Act
        trie.insert(url_parts, handler_name)
        result: str = trie.find(url_parts)

        # Assert
        self.assertEqual(result, handler_name)

    def find_url_parts_is_fine_search_for_url_that_not_exists_return_none(self: object) -> None:
        # Arrange
        trie: Trie = Trie()
        url_parts: List[str] = ["home", "test", "part"]
        handler_name: str = "Test handler"

        # Act
        trie.insert(url_parts, handler_name)
        result: str = trie.find(["hello"])

        # Assert
        self.assertIsNone(result)
