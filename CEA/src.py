import cv2
import numpy as np

def embed_watermark_dct(image, strength=15):
    """
    Nhúng watermark vào hệ số DCT (4,4) của mỗi block 8x8
    """
    img = np.float32(image)
    h, w = img.shape

    watermarked = np.zeros_like(img)

    for y in range(0, h - h % 8, 8):
        for x in range(0, w - w % 8, 8):

            block = img[y:y+8, x:x+8]

            # DCT
            dct_block = cv2.dct(block)

            # Nhúng watermark
            dct_block[4, 4] += strength

            # IDCT
            idct_block = cv2.idct(dct_block)

            watermarked[y:y+8, x:x+8] = idct_block

    return np.clip(watermarked, 0, 255).astype(np.uint8)


def simulate_jpeg_compression(image, quality=50):
    """
    Mô phỏng nén JPEG
    """
    encode_param = [
        int(cv2.IMWRITE_JPEG_QUALITY),
        quality
    ]

    success, encoded = cv2.imencode(
        ".jpg",
        image,
        encode_param
    )

    if not success:
        raise Exception("JPEG encoding failed")

    decoded = cv2.imdecode(
        encoded,
        cv2.IMREAD_GRAYSCALE
    )

    return decoded


def calculate_psnr(original, processed):
    mse = np.mean(
        (original.astype(np.float32) -
         processed.astype(np.float32)) ** 2
    )

    if mse == 0:
        return float('inf')

    return 20 * np.log10(255.0 / np.sqrt(mse))


# ==========================
# MAIN
# ==========================

img = cv2.imread(
    "D:\\Python\\CEA\\anh4x6_xanh.jpg",
    cv2.IMREAD_GRAYSCALE
)

watermarked = embed_watermark_dct(
    img,
    strength=15
)

compressed = simulate_jpeg_compression(
    watermarked,
    quality=50
)

psnr_wm = calculate_psnr(
    img,
    watermarked
)

psnr_jpeg = calculate_psnr(
    img,
    compressed
)

print(f"PSNR after watermark: {psnr_wm:.2f} dB")
print(f"PSNR after JPEG: {psnr_jpeg:.2f} dB")

cv2.imwrite(
    "watermarked.png",
    watermarked
)

cv2.imwrite(
    "compressed.jpg",
    compressed
)

print("Done!")

# Thêm đoạn này vào cuối file code của bệ hạ để kiểm tra:

# 1. Đọc lại ảnh đã nhúng watermark (hoặc ảnh đã bị nén)
img_wm = cv2.imread("watermarked.png", cv2.IMREAD_GRAYSCALE)
h, w = img_wm.shape

extracted_watermarks = []

# 2. Quét qua các block 8x8 để tìm watermark
for y in range(0, h - h % 8, 8):
    for x in range(0, w - w % 8, 8):
        block = np.float32(img_wm[y:y+8, x:x+8])
        dct_block = cv2.dct(block)
        
        # Lấy giá trị tại vị trí [4, 4]
        extracted_watermarks.append(dct_block[4, 4])

# 3. In ra giá trị trung bình của watermark tìm được
avg_value = np.mean(extracted_watermarks)
print(f"-> Giá trị watermark trích xuất được (Trung bình): {avg_value:.2f}")