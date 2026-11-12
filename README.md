# 디지몬 스토리 초 크로스워즈 블루 한글 패치 v1.0.1

일본판 Nintendo DS용 한글 패치입니다. **[릴리스에서 xdelta 다운로드](https://github.com/TeamLimRyan/DIGIMON_STORY_SUPER_XROS_WARS_BLUE_KOREAN_LOCALIZATION_RELEASE/releases/tag/v1.0.1)**

패치 파일: [`DIGIMON_STORY_SUPER_XROS_WARS_BLUE_KO_v1.0.1.xdelta`](DIGIMON_STORY_SUPER_XROS_WARS_BLUE_KO_v1.0.1.xdelta)

## 원본·적용 후·패치 해시

| 대상 | 크기(bytes) | SHA-256 |
|---|---:|---|
| 원본 일본판 ROM | 67108864 | `dc9dd0cf0e13b2e017ee5606343fb9198bbb5a95c2c926896a4bcaf4060f929a` |
| 패치 적용 후 ROM | 67108864 | `01d65a63dc68605bbd3d41173b04d83789682fd1c58ac2cf57f6968b58b5d5a7` |
| xdelta 패치 | 7565783 | `002d6b15def97c4f156c556e4960999888cf9c4348de09b6c0b016b419c6b075` |

원본 해시가 일치하는 ROM에만 적용하세요. 다른 지역판, 다른 버전, 트리밍한 ROM, 이미 수정한 ROM은 지원하지 않습니다.

## 적용 방법

1. 직접 보유한 일본판 원본의 SHA-256을 위 표와 비교합니다.
2. xdelta3로 아래 명령을 실행합니다. 원본과 출력은 서로 다른 파일이어야 합니다.

```text
xdelta3 -d -s "original.nds" "DIGIMON_STORY_SUPER_XROS_WARS_BLUE_KO_v1.0.1.xdelta" "korean.nds"
```

3. `korean.nds`의 SHA-256을 적용 후 해시와 비교합니다.

[상세 설치·복구](INSTALL.md) · [호환성과 검증 범위](COMPATIBILITY.md) · [문제 신고](SUPPORT.md) · [권리 안내](NOTICE.md)

게임 ROM, BIOS, 세이브, 키는 포함하지 않습니다. 비공식 한국어화 패치입니다.
