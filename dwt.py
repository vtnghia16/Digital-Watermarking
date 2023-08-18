import cv2
import numpy as np
import pywt

# Tải hình ảnh gốc và hình ảnh chữ ký
img = cv2.imread('hinhnen.jpg')
signature = cv2.imread('mylogo.jpg', cv2.IMREAD_GRAYSCALE)

# Thay đổi kích thước hình ảnh chữ ký để phù hợp với kích thước của hình ảnh gốc
signature_resized = cv2.resize(signature, (img.shape[1], img.shape[0]))

# Áp dụng DWT cho từng kênh thang độ xám của ảnh gốc và ảnh chữ ký
coeffs_img = pywt.dwt2(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 'haar')
coeffs_sig = pywt.dwt2(signature_resized, 'haar')

# Trích xuất các hệ số băng con LL của từng DWT
(LL_img, (LH_img, HL_img, HH_img)) = coeffs_img
(LL_sig, (LH_sig, HL_sig, HH_sig)) = coeffs_sig

# Xác định giá trị alpha để sử dụng cho watermarking
alpha = 0.1 * np.std(LL_img) / np.std(LL_sig)

# Nhúng chữ ký vào hệ số băng con LL của ảnh gốc DWT
LL_watermarked = LL_img + alpha * LL_sig

# Xây dựng hệ số DWT thủy vân
coeffs_watermarked = (LL_watermarked, (LH_img, HL_img, HH_img))

# Áp dụng DWT nghịch đảo để có hình mờ
img_watermarked = pywt.idwt2(coeffs_watermarked, 'haar')

# Chuyển đổi hình ảnh thủy ấn trở lại định dạng BGR và lưu nó
img_watermarked_bgr = cv2.cvtColor(
    np.uint8(img_watermarked), cv2.COLOR_GRAY2BGR)
cv2.imwrite('watermarked_image.jpg', img_watermarked_bgr)
