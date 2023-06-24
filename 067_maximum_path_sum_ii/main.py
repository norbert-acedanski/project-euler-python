from common import get_max_route_value_from_tree, read_file_with_multiple_lines

# The same as problem 18

triangle_list = read_file_with_multiple_lines("p067_triangle.txt")


if __name__ == "__main__":
    print(get_max_route_value_from_tree(triangle_array=triangle_list))
