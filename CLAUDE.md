# ClosetFit (클로젯핏) — Project Context

## 서비스 개요

**클로젯핏(ClosetFit)**은 집에 있는 옷(상의·하의)을 선택하면 AI가 컬러를 분석해 매칭 룩을 추천해주는 모바일 앱 서비스입니다.

- **타겟층**: 20~40대
- **핵심 가치**: "옷장에 있는 옷으로, 더 잘 입는다"
- **GitHub**: https://github.com/davegpt25/business.git (branch: master)

---

## 폴더 구조

```
기획서/
├── CLAUDE.md                        ← 이 파일
├── 클로젯핏_서비스기획서.md          ← 서비스 기획서 (Markdown 원본)
├── 클로젯핏_서비스기획서.docx        ← 기획서 Word 변환본
├── convert_to_docx.py               ← .md → .docx 변환 스크립트
├── mock/
│   ├── index.html                   ← 모바일 앱 UI 목업 (메인 파일)
│   └── serve.py                     ← 로컬 개발 서버 (Python HTTP)
└── .claude/
    └── launch.json                  ← Claude Preview 서버 설정
```

---

## 개발 서버 실행

### 방법 1: Claude Preview (권장)
`.claude/launch.json`에 설정 완료. Claude Code에서 자동으로 실행 가능.

### 방법 2: 직접 실행
```bash
cd mock
python serve.py
# → http://localhost:3001 에서 확인
```

**중요 사항:**
- `serve.py`는 `PORT` 환경변수를 읽음 (기본값: 3001)
- Python 절대 경로: `C:\Users\hwlll\AppData\Local\Programs\Python\Python312\python.exe`
- Windows에서 `ConnectionAbortedError` 방지를 위해 `ThreadingMixIn + TCPServer` 구조 사용

---

## 목업 (mock/index.html)

### 구조
- **폰 프레임**: 375×780px, border-radius: 50px, Dynamic Island 포함
- **화면 4개** (JS `switchScreen()`으로 전환):
  - `screen-0`: 홈 (오늘의 추천 코디)
  - `screen-1`: 내 옷장 (업로드한 옷 목록)
  - `screen-2`: 컬러 매칭 (색상 분석 결과)
  - `screen-3`: 스타일 리포트 (월간 통계)
- **하단 탭바**: 홈 / 옷장 / 매칭 / 리포트

### 디자인 시스템
| 항목 | 값 |
|------|-----|
| 배경 | Unsplash 패션 에디토리얼 사진 (`photo-1558618666-fcd25c85cd64`) + 다크 그라데이션 오버레이 |
| 좌측 패널 | 글라스모피즘 (`backdrop-filter: blur(24px)`, `rgba(255,255,255,0.04)`) |
| 폰 배경 | `#0F0F1A` (딥 네이비) |
| 강조색 | `#7C6FF7` (퍼플), `#4ECDC4` (틸) |
| 폰트 | Noto Sans KR |
| 의류 이미지 | Unsplash CDN (`images.unsplash.com/photo-{id}?w=&h=&fit=crop&q=80`) 총 31개 |

---

## 기획서 변환

`.md` → `.docx` 변환 시 `convert_to_docx.py` 실행:
```bash
python convert_to_docx.py
```
- 라이브러리: `python-docx` (`python -m pip install python-docx`)
- 폰트: 맑은 고딕
- 제목 색상: #2E75B6 (파란색)
- 표: 교대 행 음영 처리

---

## 서비스 기획 핵심 내용

### 주요 기능
1. **옷장 등록** — 상·하의 사진 업로드 및 AI 색상 분석
2. **컬러 매칭** — 보유 아이템 기반 코디 조합 추천
3. **룩북 저장** — 마음에 드는 코디 저장 및 공유
4. **스타일 리포트** — 월간 착용 패턴 분석

### 기술 스택 (기획 기준)
| 구분 | 기술 |
|------|------|
| 프론트엔드 | React Native (iOS/Android) |
| 백엔드 | FastAPI (Python) |
| AI 분석 | OpenAI Vision API / 자체 컬러 분석 모델 |
| 데이터베이스 | PostgreSQL + Redis |
| 스토리지 | AWS S3 |
| 인프라 | AWS ECS + CloudFront |

### 수익 모델
- 프리미엄 구독 (월 4,900원): 무제한 매칭, 고급 리포트
- 제휴 쇼핑 연동: 추천 아이템 커머스 연결
- 브랜드 스타일링 제안 광고

### 로드맵
| 단계 | 기간 | 내용 |
|------|------|------|
| MVP | 0~3개월 | 옷장 등록, 기본 컬러 매칭 |
| v1.0 | 4~6개월 | 룩북, 소셜 공유, 쇼핑 연동 |
| v2.0 | 7~12개월 | AI 고도화, 브랜드 파트너십 |

---

## Git 정보

- **원격 저장소**: `https://github.com/davegpt25/business.git`
- **브랜치**: `master`
- **초기 푸시 완료** (서비스 기획서 .md, .docx, 목업 포함)

---

## 알려진 이슈 및 해결책

| 문제 | 해결책 |
|------|--------|
| Port 3000 충돌 | `autoPort: true` 설정으로 3001 자동 할당 |
| Windows Python PATH 미등록 | 절대 경로 사용 (`C:\Users\hwlll\...`) |
| ConnectionAbortedError (WinError 10053) | `ThreadingMixIn + TCPServer` 사용 |
| python-docx 미설치 | `python -m pip install python-docx` |
