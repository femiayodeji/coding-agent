from config import MAX_CHARS
from functions.get_file_content import get_file_content

print("Result for current directory:")
result = get_file_content("calculator", "lorem.txt")
#todo: You don't need to print the entire content; just check the length and the truncation message at the end if applicable.
print(f"  Content length: {len(result)}")
if result.endswith(f"[...File \"lorem.txt\" truncated at {MAX_CHARS} characters]"):
    print("  The content was truncated as expected.")
print("-----" * 10)
print("Result for main.py:")
result = get_file_content("calculator", "main.py")
print(f"  {result}")

print("Result for pkg/calculator.py:")
result = get_file_content("calculator", "pkg/calculator.py")
print(f"  {result}")

print("Result for /bin/cat:")
result = get_file_content("calculator", "/bin/cat")
print(f"  {result}")

print("Result for pkg/does_not_exist.py:")
result = get_file_content("calculator", "pkg/does_not_exist.py")
print(f"  {result}")

