import numpy as np
from glob import glob


def Read_Image_Folder(Path):
	folder_path = []
	image_extension = ['bmp','jpg','jpeg','png','tif','tiff','gif']
	total_path = glob(initial_path + r'\*')
	while (True):
		path = total_path.pop(0)
		data_path = glob(path + r'\*')
		if len(data_path) == 0:
			continue
		extension = data_path[0].split("\\")[-1].split(".")
		if len(extension) == 2:
			if extension[1] in image_extension:
				folder_path.append(path)
		elif len(extension) == 1:
			total_path += data_path

		if len(total_path) == 0:
			break
	return folder_path


if __name__ == '__main__':
	initial_path = r"C:\Users\jianjie\Documents\Contrel\Project\210917_FVI_OCR\20210927_OCR裁切"
	folder_path = Read_Image_Folder(initial_path)
	print(folder_path)