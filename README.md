# JPEG to PNG

현재 디렉토리에 있는 `.jpg`, `.jpeg` 이미지를 `.png`로 변환하는 간단한 Python 스크립트입니다.

## Requirements

- Python 3
- Pillow

```bash
pip install Pillow
```

## Usage

스크립트를 실행하면 현재 디렉토리의 JPEG 이미지들을 찾아 `output` 폴더에 PNG로 저장합니다.

```bash
python batch-jpg2png.py
```

## Output

```text
.
├── batch-jpg2png.py
├── image1.jpg
├── image2.jpeg
└── output/
    ├── image1.png
    └── image2.png
```

- 현재 디렉토리의 파일만 검색합니다. (하위 디렉토리 제외)
- 원본 파일은 유지합니다.
- `output` 폴더가 없으면 자동으로 생성합니다.
- 기존 `output` 폴더가 있으면 그대로 사용합니다.
