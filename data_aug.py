# import cv2
# import albumentations as A
# import os
#
# # file_path = r"E:\论文\sun-bursh-codetr\data\rule\dataaugment\2\2.jpg"
# file_path='demo/5-4.jpg'
# # 加载原始图像
# image = cv2.imread(file_path)
#
# # 定义增强方法
# transform = A.Compose([
#     A.HorizontalFlip(p=1),  # 随机水平翻转，概率为1
# ])
#
# # 应用增强
# transformed = transform(image=image)
# transformed_image = transformed["image"]
#
# # 保存增强后的图像到指定文件夹
# output_folder = 'demo/data_aug'
# output_path = os.path.join(output_folder, "transformed_image.jpg")
# os.makedirs(output_folder, exist_ok=True)
# cv2.imwrite(output_path, transformed_image)
# print("Transformed image saved at:", output_path)


