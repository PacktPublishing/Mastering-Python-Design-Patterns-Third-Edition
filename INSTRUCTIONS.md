# Instructions about code examples

## Most of the code is formatted using Black

So some code snippets in the code files as well as in the book's pages may look like the following:

```
State = Enum(
    "State",
    "NEW RUNNING SLEEPING RESTART ZOMBIE",
)
```

```
msg = (
    f"trying to create process '{name}' "
    f"for user '{user}'"
)
print(msg)

```

This improves readability of the code snippets inserted in the book.

## The code inserted in the book may be shortened

* When docstrings are too long, we remove them from the code snippets in the book, to improve readability of the code.

* When some code (class or function) is too long to display in the chapter's pages, we may shorten it and refer the reader to the complete code in the file.

* ...


## The `if __name__ == "__main__"` trick

