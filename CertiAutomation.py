import cv2

input_txt_file = 'C:\certi\certi-namelist.txt'

template_file_path = 'C:\certi\CERTI_TEMPLATE.png'

output_directory_path = 'C:\certi\Generated_Certificates\\'

font_size = 4.2
font_color = (51, 51, 51)

coordinate_y_adjustment = -500

coordinate_x_adjustment = -4

print('The Script is executing...')

with open(input_txt_file) as input_list:

    content = input_list.read().splitlines()

    for line in content:

        certi_name = line

        img = cv2.imread(template_file_path)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = certi_name

        textsize = cv2.getTextSize(text, font, font_size, 10)[0]
        text_x = (img.shape[1] - textsize[0]) / 2 + coordinate_x_adjustment
        text_y = (img.shape[0] + textsize[1]) / 2 - coordinate_y_adjustment
        text_x = int(text_x)
        text_y = int(text_y)

        cv2.putText(img, text, (text_x, text_y),
                    font, font_size, font_color, 10)
        certi_path = output_directory_path + certi_name + '.png'
        cv2.imwrite(certi_path, img)

cv2.destroyAllWindows()
