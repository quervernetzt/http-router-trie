import unittest
from solution.router import Router


class TestCasesRouter(unittest.TestCase):
    def initialize_router_handlers_are_none_raise_value_error(self: object) -> None:
        # Arrange
        root_handler_0: str = None
        not_found_handler_0: str = "not found handler"

        root_handler_1: str = "root handler"
        not_found_handler_1: str = None

        # Act & Assert
        self.assertRaises(ValueError, Router, root_handler_0,
                          not_found_handler_0)
        self.assertRaises(ValueError, Router, root_handler_1,
                          not_found_handler_1)

    def initialize_router_handlers_are_not_str_raise_type_error(self: object) -> None:
        # Arrange
        root_handler_0: int = 123
        not_found_handler_0: str = "not found handler"

        root_handler_1: str = "root handler"
        not_found_handler_1: int = 123

        # Act & Assert
        self.assertRaises(TypeError, Router, root_handler_0,
                          not_found_handler_0)
        self.assertRaises(TypeError, Router, root_handler_1,
                          not_found_handler_1)

    def initialize_router_handlers_are_empty_raise_value_error(self: object) -> None:
        # Arrange
        root_handler_0: str = ""
        not_found_handler_0: str = "not found handler"

        root_handler_1: str = "root handler"
        not_found_handler_1: str = ""

        # Act & Assert
        self.assertRaises(ValueError, Router, root_handler_0,
                          not_found_handler_0)
        self.assertRaises(ValueError, Router, root_handler_1,
                          not_found_handler_1)

    def initialize_router_handlers_are_fine(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"

        # Act
        result: Router = Router(root_handler, not_found_handler)

        # Assert
        self.assertEqual(result.router.root.handler, root_handler)
        self.assertEqual(result.not_found_handler, not_found_handler)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def split_path_url_is_none_return_emtpy_list(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = None

        # Act
        result: str = router.split_path(url)

        # Assert
        self.assertEqual(result, [])

    def split_path_url_is_not_str_raise_type_error(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: int = 123

        # Act & Assert
        self.assertRaises(TypeError, router.split_path, url)

    def split_path_url_is_empty_return_emtpy_list(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = ""

        # Act
        result: str = router.split_path(url)

        # Assert
        self.assertEqual(result, [])

    def split_path_url_is_fine_return_list_with_parts(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "/home/test/part"

        # Act
        result: str = router.split_path(url)

        # Assert
        self.assertEqual(result, ["home", "test", "part"])

    def split_path_url_is_fine_with_trailing_slash_return_list_with_parts(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "/home/test/part/"

        # Act
        result: str = router.split_path(url)

        # Assert
        self.assertEqual(result, ["home", "test", "part"])

    def split_path_url_is_fine_without_preceding_slash_return_list_with_parts(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "home/test/part"

        # Act
        result: str = router.split_path(url)

        # Assert
        self.assertEqual(result, ["home", "test", "part"])

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def add_handler_url_is_none(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = None
        handler_name: str = "Test handler"

        # Act & Assert
        router.add_handler(url, handler_name)

    def add_handler_url_is_empty(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = ""
        handler_name: str = "Test handler"

        # Act & Assert
        router.add_handler(url, handler_name)

    def add_handler_url_is_not_str_raise_type_error(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: int = 12
        handler_name: str = "Test handler"

        # Act & Assert
        self.assertRaises(TypeError, router.add_handler, url, handler_name)

    def add_handler_handler_name_is_none(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "/test"
        handler_name: str = None

        # Act & Assert
        router.add_handler(url, handler_name)

    def add_handler_handler_name_is_empty(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "/test"
        handler_name: str = ""

        # Act & Assert
        router.add_handler(url, handler_name)

    def add_handler_handler_name_is_not_str_raise_type_error(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "/test"
        handler_name: int = 12

        # Act & Assert
        self.assertRaises(TypeError, router.add_handler, url, handler_name)

    def add_handler_url_is_root(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "/"
        handler_name: str = "Test handler"

        # Act & Assert
        router.add_handler(url, handler_name)

    def add_handler_url_has_multiple_elements(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)
        url: str = "/home/test/part"
        handler_name: str = "Test handler"

        # Act & Assert
        router.add_handler(url, handler_name)

    # ---------------------------------------------------------------------
    # ---------------------------------------------------------------------

    def lookup_url_url_is_none_raise_value_error(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        # Act & Assert
        self.assertRaises(ValueError, router.lookup, None)

    def lookup_url_url_is_not_str_raise_type_error(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        # Act & Assert
        self.assertRaises(TypeError, router.lookup, 123)

    def lookup_url_url_is_empty_raise_value_error(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        # Act & Assert
        self.assertRaises(ValueError, router.lookup, "")

    def lookup_url_is_root_handler_is_the_one_from_init_return_init_handler(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        # Act
        result: str = router.lookup("/")

        # Assert
        self.assertEqual(result, root_handler)

    def lookup_url_is_root_handler_is_the_new_one_return_new_handler(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        url: str = "/"
        new_root_handler: str = "new root handler"
        router.add_handler(url, new_root_handler)

        # Act
        result: str = router.lookup("/")

        # Assert
        self.assertEqual(result, new_root_handler)

    def lookup_url_is_fine_handler_exists_return_handler(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        url: str = "/home/test/part"
        handler: str = "test handler"
        router.add_handler(url, handler)

        # Act
        result: str = router.lookup(url)

        # Assert
        self.assertEqual(result, handler)

    def lookup_url_is_fine_handler_exists_with_trailing_slash_return_handler(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        url: str = "/home/test/part/"
        handler: str = "test handler"
        router.add_handler(url, handler)

        # Act
        result: str = router.lookup(url)

        # Assert
        self.assertEqual(result, handler)

    def lookup_url_is_fine_handler_exists_without_preceding_slash_return_handler(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        url: str = "home/test/part"
        handler: str = "test handler"
        router.add_handler(url, handler)

        # Act
        result: str = router.lookup(url)

        # Assert
        self.assertEqual(result, handler)

    def lookup_url_is_fine_handler_not_exists_return_not_found_handler(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        url: str = "/home/test/part"
        handler: str = "test handler"
        router.add_handler(url, handler)

        # Act
        result: str = router.lookup("/home/test")

        # Assert
        self.assertEqual(result, not_found_handler)

    def lookup_url_not_exists_return_not_found_handler(self: object) -> None:
        # Arrange
        root_handler: str = "root handler"
        not_found_handler: str = "not found handler"
        router: Router = Router(root_handler, not_found_handler)

        url: str = "/home/test/part"
        handler: str = "test handler"
        router.add_handler(url, handler)

        # Act
        result: str = router.lookup("/shopping")

        # Assert
        self.assertEqual(result, not_found_handler)
