from hanspell import spell_checker
import sys
import os

def check_text(text):
    result = spell_checker.check(text)
    print("\n[원문] ", text)
    print("[수정] ", result.checked)
    print("[오타 수]", result.errors)

def main():
    if len(sys.argv) < 2:
        text = input("검사할 문장을 입력하세요: ")
        check_text(text)
    else:
        path = sys.argv[1]
        if os.path.exists(path):
            with open(path, encoding='utf-8') as f:
                content = f.read()
                check_text(content)
        else:
            check_text(path)

if __name__ == "__main__":
    main()
