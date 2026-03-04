
from functions.write_file import write_file

print("Attempting to write to 'lorem.txt' in the current directory:")
result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(f"  {result}")

print("Attempting to write to 'pkg/morelorem.txt' in the 'pkg' directory:")
result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(f"  {result}")

print("Attempting to write to '/tmp/temp.txt' outside the working directory:")
result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(f"  {result}")