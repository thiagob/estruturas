s = "ThiagoBohn"

snake_case_str = ""
for c in s:
    if c.isupper():
        if snake_case_str != "":
            snake_case_str += "_"
    snake_case_str += c.lower()

print(snake_case_str)