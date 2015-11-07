import parser

test_str_0 = "1 + 2 + 9 / 3 / 3"
test_str_1 = "1 - 2 - 2 + 3 / 3 / 3"
test_str_2 = "1 * 2 + 9 / 3 / 3"
test_str_3 = "1 / 2 + 9 / 3 / 3"

print(parser.main(test_str_0))
print(parser.main(test_str_1))
print(parser.main(test_str_2))
print(parser.main(test_str_3))