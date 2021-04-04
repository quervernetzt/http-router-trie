from solution.router import Router
from tests.test_trie import TestCasesTrie
from tests.tests_router import TestCasesRouter


if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_trie: TestCasesTrie = TestCasesTrie()

    tests_trie.insert_url_parts_is_none()
    tests_trie.insert_url_parts_is_empty()
    tests_trie.insert_url_parts_is_not_list_raise_type_error()
    tests_trie.insert_handler_name_is_none()
    tests_trie.insert_handler_name_is_empty()
    tests_trie.insert_handler_name_is_not_str_raise_type_error()
    tests_trie.insert_url_parts_is_root()
    tests_trie.insert_url_parts_has_multiple_elements()

    tests_trie.find_url_parts_is_none_return_none()
    tests_trie.find_url_parts_is_empty_return_none()
    tests_trie.find_url_parts_is_not_list_return_none()
    tests_trie.find_url_parts_is_fine_search_for_url_that_exists_return_handler_name()
    tests_trie.find_url_parts_is_fine_search_for_url_that_not_exists_return_none()

    tests_router: TestCasesRouter = TestCasesRouter()

    tests_router.initialize_router_handlers_are_none_raise_value_error()
    tests_router.initialize_router_handlers_are_not_str_raise_type_error()
    tests_router.initialize_router_handlers_are_empty_raise_value_error()
    tests_router.initialize_router_handlers_are_fine()

    tests_router.split_path_url_is_none_return_emtpy_list()
    tests_router.split_path_url_is_not_str_raise_type_error()
    tests_router.split_path_url_is_empty_return_emtpy_list()
    tests_router.split_path_url_is_fine_return_list_with_parts()
    tests_router.split_path_url_is_fine_with_trailing_slash_return_list_with_parts()
    tests_router.split_path_url_is_fine_without_preceding_slash_return_list_with_parts()

    tests_router.add_handler_url_is_none()
    tests_router.add_handler_url_is_empty()
    tests_router.add_handler_url_is_not_str_raise_type_error()
    tests_router.add_handler_handler_name_is_none()
    tests_router.add_handler_handler_name_is_empty()
    tests_router.add_handler_handler_name_is_not_str_raise_type_error()
    tests_router.add_handler_url_is_root()
    tests_router.add_handler_url_has_multiple_elements()

    tests_router.lookup_url_url_is_none_raise_value_error()
    tests_router.lookup_url_url_is_not_str_raise_type_error()
    tests_router.lookup_url_url_is_empty_raise_value_error()
    tests_router.lookup_url_is_root_handler_is_the_one_from_init_return_init_handler()
    tests_router.lookup_url_is_root_handler_is_the_new_one_return_new_handler()
    tests_router.lookup_url_is_fine_handler_exists_return_handler()
    tests_router.lookup_url_is_fine_handler_exists_with_trailing_slash_return_handler()
    tests_router.lookup_url_is_fine_handler_exists_without_preceding_slash_return_handler()
    tests_router.lookup_url_is_fine_handler_not_exists_return_not_found_handler()
    tests_router.lookup_url_not_exists_return_not_found_handler()

    ###################################
    # Demo
    ###################################
    root_handler: str = "root handler"
    not_found_handler: str = "not found handler"
    router: Router = Router(root_handler, not_found_handler)

    router.add_handler("/home/about", "about handler")

    print(router.lookup("/"))  # should print 'root handler'
    # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home"))
    print(router.lookup("/home/about"))  # should print 'about handler'
    # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/"))
    # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about/me"))
