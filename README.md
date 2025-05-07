---

## spcheck

**한글 맞춤법 검사 CLI 도구**  
`spcheck`는 네이버 맞춤법 검사기를 기반으로 작성된 간단한 명령줄 도구입니다.  
문장이나 텍스트 파일의 맞춤법/띄어쓰기를 검사하고 수정된 문장을 출력합니다.

---

## 설치 방법

```bash
git clone https://github.com/yourname/spcheck.git
cd spcheck
pip install .


---

실행 방법

1. 문장 직접 입력

spcheck "안녕 하세요 저는 챗지피티 입니당."

2. 텍스트 파일 검사

spcheck ./example.txt

3. 실행 후 인터랙티브 입력

spcheck
# 검사할 문장을 입력하세요: 안녕 하세요


---

출력 예시

[원문]  안녕 하세요 저는 스파게티 입니닷.
[수정]  안녕하세요 저는 스파게티입니다.
[오타 수] 2


---

의존성

py-hanspell
(네이버 맞춤법 검사기를 활용한 파이썬 라이브러리)



---

라이선스

MIT License

---
