from pathlib import Path
from PIL import Image

# 현재 실행 디렉토리
current_dir = Path.cwd()

# output 폴더 생성
output_dir = current_dir / "output"
output_dir.mkdir(exist_ok=True)

# 현재 디렉토리의 JPEG/JPG 파일 검색
image_files = [
    file for file in current_dir.iterdir()
    if file.is_file() and file.suffix.lower() in (".jpg", ".jpeg")
]

# 이미지 변환
for image_path in image_files:
    try:
        with Image.open(image_path) as image:
            # PNG 저장 호환성을 위해 RGB로 변환
            image = image.convert("RGB")

            # output 폴더에 PNG로 저장
            output_path = output_dir / f"{image_path.stem}.png"
            image.save(output_path, format="PNG")

            print(f"변환 완료: {image_path.name} -> {output_path}")

    except Exception as e:
        print(f"변환 실패: {image_path.name} ({e})")

print(f"\n총 {len(image_files)}개 파일 검색 완료")