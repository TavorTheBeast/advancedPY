def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return f"__CONTENT_START__\n{content}__CONTENT_END__\n"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__\n"
    except:
        return "__CONTENT_START__\n__ERROR_OCCURRED__\n__CONTENT_END__\n"


print(read_file("one_lined_file.txt"))
print(read_file("file_does_not_exist.txt"))
