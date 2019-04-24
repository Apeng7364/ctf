import base64
a = "6789_-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base_fix = "tGRBtXMZgD6ZhalBtCUTgWgZfnkTgqoNsnAVsmUYsGtCt9pEtDEYsql3"
table = base_fix.maketrans(a, b)
print(base64.b64decode(base_fix.translate(table)))