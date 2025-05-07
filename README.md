# spcheck

한글 맞춤법 검사 CLI 도구

---

## 설치 및 실행 방법

```bash
# 저장소 클론
git clone https://github.com/lihuiruo101/spcheck.git

# 디렉토리 이동
cd spcheck

# 패키지 설치
pip install .

# 문장 검사
spcheck "안녕 하세요 저는 스파게티 입니당."

# 텍스트 파일 검사
spcheck example.txt

# 실행 후 직접 입력
spcheck
# 검사할 문장을 입력하세요: 안녕 하세요
