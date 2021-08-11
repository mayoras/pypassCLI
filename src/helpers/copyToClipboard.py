import pyperclip


def copy_to_clipboard(txt):
    pyperclip.copy(txt)
    pyperclip.paste()

    print('✨📎 Password copied to clipboard ;)')
