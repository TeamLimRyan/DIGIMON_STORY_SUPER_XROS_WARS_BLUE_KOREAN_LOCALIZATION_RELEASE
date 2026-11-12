# 설치와 복구

필요 도구: xdelta3(검증 버전 3.2.2). 도구 실행 파일은 포함하지 않습니다.

1. 원본 ROM과 세이브를 백업합니다.
2. 원본 SHA-256이 README와 같은지 확인합니다.
3. 빈 작업 폴더에서 아래 명령을 실행합니다. 기존 출력이 있으면 이름을 변경하세요.

```text
xdelta3 -d -s "original.nds" "DIGIMON_STORY_SUPER_XROS_WARS_BLUE_KO_v1.0.1.xdelta" "korean.nds"
```

4. 결과 크기와 SHA-256을 README 또는 `patch_manifest.json`과 비교합니다.

Windows PowerShell: `Get-FileHash -Algorithm SHA256 -LiteralPath "original.nds"`와 `Get-FileHash -Algorithm SHA256 -LiteralPath "korean.nds"`.
Linux: `sha256sum original.nds korean.nds`. macOS: `shasum -a 256 original.nds korean.nds`.

Windows x64에서 xdelta3 3.2.2로 원본에서 적용한 결과가 검수본과 바이트 단위로 일치함을 확인했습니다. Linux/macOS의 위 해시 확인 명령은 안내이며 해당 환경 설치 시험은 수행하지 않았습니다.

오류·중단 시 원본은 유지하고 불완전한 출력 파일만 제거한 뒤 다시 적용합니다. 체크섬 오류를 무시하는 옵션은 사용하지 마세요. 제거하려면 패치된 출력 파일을 제거하고 백업 원본을 사용합니다. 세이브는 별도로 백업하고, 기존 세이브 전반의 호환성은 보장하지 않습니다.
