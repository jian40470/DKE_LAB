import matplotlib.pyplot as plt
# 設置行列
rows = 6
columns = 10
LINE_1 = [59,201, 192, 275, 274, 273, 272, 271,419]
LINE_2 = [40, 291, 290, 289, 417]
LINE_3 = [416]
LINE_4 = [78, 311, 310, 309, 308, 307, 415]
LINE_5 = [412]
LINE_6 = [146, 343, 411]
LINE_7= [407]
LINE_8 = [111, 245, 254, 263, 406]
LINE_9 = [80, 229, 238, 331, 330, 246, 255, 264, 404]
LINE_10 = [152, 265, 402]
LINE_11 = [401]
LINE_12 = [82, 230, 239, 248, 257, 266, 400]
LINE_13 = [399]
LINE_14 = [47, 213, 222, 231, 240, 249, 258, 267, 398]
LINE_15 = [397]
LINE_16 = [158, 268, 396]
LINE_17= [395]
LINE_18 = [393]
LINE_19 = [25, 278, 279, 280, 281, 195, 204, 300, 301, 214, 223, 232, 241, 338, 339, 340, 341, 252, 261, 270, 392]
LINE_20 = [391]
LINE_21 = [105, 322, 323, 324, 385]
LINE_22 = [386]
LINE_23 = [53, 306, 383]
LINE_24 = [382]
LINE_25 = [69, 206, 197, 286, 287, 288, 381,402]
numer_list = [LINE_1, LINE_2, LINE_3, LINE_4, LINE_5, LINE_6, LINE_7, LINE_8, LINE_9, LINE_10, 
        LINE_11, LINE_12, LINE_13,  LINE_14,  LINE_15, LINE_16, LINE_17, LINE_18, LINE_19, LINE_20, 
        LINE_21, LINE_22, LINE_23, LINE_24,LINE_25]
# 創建一個圖形
fig, ax = plt.subplots()
# 加入參數
circle_radius = 0.3
square_side = 0.4  # 正方形的边长
circle_spacing = 1.5  # 两个圆之间的距离
square_spacing = 0.5  # 调整正方形和两个圆之间的距离
number_spacing=1.07
number_spacing_2=1
r=rows-1
s=2*(columns-1)
balance_line_spacing=2
# 設置編號
count = 1
horizontal_count = 1  # 用于横轴正方形的计数器
vertical_count = 6 * (columns - 1) + 1
c = 0
p=2*(rows-1)
q=columns-1
side_rectangle_no=2*(columns - 1)+1
side_rectangle_number=2*(rows - 1)+1
# Define line extension lengths for each direction
up_extension_length = 0.5  # Adjust this value for lines going upwards
down_extension_length = 0.5  # Adjust this value for lines going downwards
left_extension_length = 0.5  # Adjust this value for lines going to the left
right_extension_length = 0.5  # Adjust this value for lines going to the right
bottom_spacing=1
#可以調整標號間距
vertical_label_spacing = 0.1  # 可以根據需要調整垂直間距
outer_number=1
outer_number_2=2*columns
outer_number_3=outer_number_2+(2*rows-1)
outer_number_4=outer_number_3+(2*columns-2)
r=rows-1
s=2*(columns-1)
initial_x_line_number=2*(columns-1)*(rows-1)*2+1
x_line_number=2*(columns-1)*(rows-1)*2+1
x_line_number_2=2*(columns-1)*(rows-1)*2+1+(columns-1)
y_line_number=x_line_number+(rows-1)*2*(columns-1)
y_line_number_even=x_line_number+(rows-1)*2*(columns-1)+1
outer_counting=y_line_number+(columns-1)*2*(rows-1)
top_number=outer_counting+2*(rows-1)+4*(columns-1)+3
right_number = top_number+2*(rows-1)
COUT=1
bout=2
aout=19
dout=20
right_down_number=2
left_up_number=19
side_rectangle_no=2*(columns - 1)+1
side_rectangle_number=2*(rows - 1)+1
bottom_spacing=1
# 定義繪製延伸線的函數
def draw_balance_extended_down_lines(ax, center_x, center_y, square_side, up_extension_length, down_extension_length, x_line_number_2,color='purple'):
# Downward line
    down_extended_line_x = center_x
    down_extended_line_y = center_y + square_side / 2 + down_extension_length
    plt.plot([center_x, down_extended_line_x], [center_y + square_side / 2, down_extended_line_y], color=color)
# 繪製編號（上行線條）
    ax.text(down_extended_line_x, down_extended_line_y, str(x_line_number_2), va='center', ha='center', color='purple', fontsize=10)
def draw_balance_extended_up_lines(ax, center_x, center_y, square_side, up_extension_length, down_extension_length, x_line_number,color='purple'):  
    # Upward line
    up_extended_line_x = center_x
    up_extended_line_y = center_y - square_side / 2 - up_extension_length
    plt.plot([center_x, up_extended_line_x], [center_y - square_side / 2, up_extended_line_y], color=color)
    # 繪製編號（下行線條）
    ax.text(up_extended_line_x, up_extended_line_y, str(x_line_number), va='center', ha='center', color='purple', fontsize=10)
def draw_straight_left_lines(ax, center_x, center_y, square_side,left_extension_length, right_extension_length, y_line_number,color='purple'):
    # Leftward line
    left_extended_line_x = center_x - square_side / 2 - left_extension_length
    left_extended_line_y = center_y
    plt.plot([center_x - square_side / 2, left_extended_line_x], [center_y, left_extended_line_y], color=color)
    # 繪製編號（左行線條）
    ax.text(left_extended_line_x, left_extended_line_y, str(y_line_number), va='center', ha='center', color=color, fontsize=10)
def draw_straight_right_lines(ax, center_x, center_y, square_side,left_extension_length, right_extension_length, y_line_number_even,color='purple'):    
    # Rightward line
    right_extended_line_x = center_x + square_side / 2 + right_extension_length
    right_extended_line_y = center_y
    plt.plot([center_x + square_side / 2, right_extended_line_x], [center_y, right_extended_line_y], color=color)
    # 繪製編號（右行線條）
    ax.text(right_extended_line_x, right_extended_line_y, str(y_line_number_even), va='center', ha='center', color=color, fontsize=10)
def connect_outer_rectangles_right(ax, side_rectangle_no, outer_counting, circle_spacing, square_spacing, bottom_spacing, square_side):
    left_outer_rec_x = (columns - 1) * (circle_spacing + square_spacing) + 1 + circle_radius
    left_outer_rec_y = row * (circle_spacing + square_spacing - bottom_spacing) + 1
    outner_square_x1 = square_side / 2 + square_side + 2 * columns * circle_radius + circle_spacing * (columns - 1) + 0.4
    outner_square_y = left_outer_rec_y
    plt.plot([left_outer_rec_x, outner_square_x1], [left_outer_rec_y, outner_square_y], color='purple')
    # 繪製編號
    ax.text((left_outer_rec_x + outner_square_x1) / 2, (left_outer_rec_y + outner_square_y) / 2, str(outer_counting), va='center', ha='center', color='purple', fontsize=10)
def connect_outer_rectangles_bottom(ax, side_rectangle_no,circle_spacing, square_spacing, bottom_spacing, square_side, outer_counting):
# 連接最外圍每一個正方形到內部第一層圓形和正方形
    bottom_square_x = col * (circle_spacing + square_spacing - bottom_spacing) + 1
    bottom_square_y = -square_side / 7 + 0.05
    inner_square_x = bottom_square_x
    inner_square_y = bottom_square_y + square_side / 2 + square_spacing
    plt.plot([bottom_square_x, inner_square_x], [bottom_square_y, inner_square_y], color='purple')
    # 繪製編號
    ax.text((bottom_square_x + inner_square_x) / 2, (bottom_square_y + inner_square_y) / 2, str(outer_counting), va='center', ha='center', color='purple', fontsize=10)
def connect_outer_rectangles_top(ax, side_rectangle_no, top_number, circle_spacing, square_spacing, bottom_spacing, square_side, rows, columns, circle_radius):

    bottom_square_x = col * (circle_spacing + square_spacing - bottom_spacing) + 1
    bottom_square_y = (rows - 1) * (circle_spacing + square_spacing) + 1 + circle_radius
    inner_square_x = bottom_square_x
    inner_square_y = (circle_spacing + 2 * circle_radius) * (rows) - 0.5
    plt.plot([bottom_square_x, inner_square_x], [bottom_square_y, inner_square_y], color='purple')
    # 繪製遞減編號
    ax.text((bottom_square_x + inner_square_x) / 2, (bottom_square_y + inner_square_y) / 2, str(top_number), va='center', ha='center', color='purple', fontsize=10)
def connect_outer_rectangles_left(ax, side_rectangle_number, right_number,circle_spacing, square_spacing, bottom_spacing, square_side, rows, columns, circle_radius):
    left_outer_rec_x = -square_side / 7 + 0.05
    left_outer_rec_y = row * (circle_spacing + square_spacing - bottom_spacing) + 1
    outner_square_x1 = square_side / 2 + square_spacing
    outner_square_y = left_outer_rec_y
    plt.plot([left_outer_rec_x, outner_square_x1], [left_outer_rec_y, outner_square_y], color='purple')
    ax.text((left_outer_rec_x + outner_square_x1) / 2, (left_outer_rec_y + outner_square_y) / 2, str(right_number), va='center', ha='center', color='purple', fontsize=10)
def add_outer_rectangles(ax, side_rectangle_no, circle_spacing, square_spacing, bottom_spacing, square_side, outer_number, outer_number_2, outer_number_3, outer_number_4):
# 在第一列的下方增加2*(columns-1)+1个外圍正方形
    for col in range(side_rectangle_no):
        square_x_bottom = col * (circle_spacing + square_spacing - bottom_spacing) + 1
        square_y_bottom = -square_side / 2
        add_square(ax, square_x_bottom, square_y_bottom, square_side, outer_number, color='gray')
        outer_number += 1
    for col in range(side_rectangle_no):
        square_x_bottom = col * (circle_spacing + square_spacing - bottom_spacing) + 1
        square_y_bottom = (circle_spacing + 2 * circle_radius) * (rows) - 0.3
        add_square(ax, square_x_bottom, square_y_bottom, square_side, outer_number_3 + (side_rectangle_no - col - 1), color='gray')
    for row in range(side_rectangle_number):
        square_x_bottom = -square_side / 2
        square_y_bottom = row * (circle_spacing + square_spacing - bottom_spacing) + 1
        add_square(ax, square_x_bottom, square_y_bottom, square_side, outer_number_4 + side_rectangle_number - row, color='gray')
    for row in range(side_rectangle_number):
        square_x_bottom = (circle_spacing + 2 * circle_radius) * (columns) - 0.3
        square_y_bottom = row * (circle_spacing + square_spacing - bottom_spacing) + 1
        add_square(ax, square_x_bottom, square_y_bottom, square_side, outer_number_2, color='gray')
        outer_number_2 += 1
# 定義計算正方形座標的函數
def add_square(ax, x, y, side, count, color='gray'):
    ax.add_patch(plt.Rectangle((x - side / 2, y - side / 2), side, side, color=color, fill=False))
    ax.text(x, y, str(count), va='center', ha='center', color='red', fontsize=10)
def draw_line(ax, x1, y1, x2, y2, label=None,color='blue'):
    ax.plot([x1, x2], [y1, y2], color='purple')
    if label:
        # Calculate the midpoint for placing the label
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        ax.text(mid_x, mid_y, label, va='center', ha='center', color='purple', fontsize=8)
# 定義添加额外正方形的函數
def add_cross_line(ax, x, y, side, COUT,bout, color='purple'):
    # 計算四個角的座標
    top_left_x = x - 0.5 * side - circle_radius - 0.5 * square_spacing
    top_left_y = y + 0.5 * side + circle_radius + 0.5 * square_spacing
    top_right_x = x + 0.5 * side + circle_radius + 0.5 * square_spacing
    top_right_y = y + 0.5 * side + circle_radius + 0.5 * square_spacing
    bottom_left_x = x - 0.5 * side - circle_radius - 0.5 * square_spacing
    bottom_left_y = y - 0.5 * side - circle_radius - 0.5 * square_spacing
    bottom_right_x = x + 0.5 * side + circle_radius + 0.5 * square_spacing
    bottom_right_y = y - 0.5 * side - circle_radius - 0.5 * square_spacing
    for numer in numer_list:
        for num in numer:
            if num==COUT:
                draw_line(ax, x - 0.5 * side, y - 0.5 * side, bottom_left_x, bottom_left_y, label=str(COUT) , color=color)
            elif num==bout:
                draw_line(ax, x + 0.5 * side, y - 0.5 * side, bottom_right_x, bottom_right_y, label=str(bout) , color=color)
            elif num==aout:
                draw_line(ax, x - 0.5 * side, y + 0.5 * side, top_left_x, top_left_y, label=str(aout) , color=color)
            elif num==dout:
                draw_line(ax, x + 0.5 * side, y + 0.5 * side, top_right_x, top_right_y, label=str(dout) , color=color)   
# 繪圖
for row in range(rows):
    for col in range(columns):
        # 計算圓心座標
        x = col * (circle_spacing + square_spacing) +1 # 根据列数和间距计算 x 坐标
        y = row * (circle_spacing + square_spacing) +1  # 根据行数和间距计算 y 坐标
        ax.add_patch(plt.Circle((x, y), circle_radius, color='red', fill=False))

        # 計算正方形座標，以调整正方形和两个圆之间的距离
        if row != 0:
            square_y = y - (square_side / 2 + circle_radius + square_spacing)  # 调整距离
            add_square(ax, x, square_y, square_side, vertical_count, color='gray')
            vertical_count += 1

        # 添加橫軸方向的正方形
        if col != columns - 1:
            square_x_horizontal = x + (square_side / 2 + circle_radius + square_spacing)  # 在圆的右侧添加横向正方形
            add_square(ax, square_x_horizontal, y, square_side, horizontal_count, color='gray')
            horizontal_count += 1
        # 添加編號
        ax.text(x, y, str(count), va='center', ha='center', color='red', fontsize=10)
        # 遞增編號
        count += 1
        if col < columns - 1:  # 針對紫色正方形
            c += 1
        # 如果编號達到，結束
        if count > rows * columns:
            break
        # 在四个正方形中间的位置添加一个额外的正方形并编号
        if row < rows - 1 and col < columns - 1:
            center_x = x + (circle_spacing + square_spacing) / 2
            center_y = y + (circle_spacing + square_spacing) / 2
            add_square(ax, center_x, center_y, square_side, c, color='purple')
            add_cross_line(ax, center_x, center_y, square_side, COUT, bout, color='purple')
            COUT += 2
            bout += 2
            aout += 2
            dout += 2 
            cv=2*(columns-1)
            if (COUT-1)%cv==0:
                COUT+=cv
                bout+=cv
                aout+=cv
                dout += cv
            for numer in numer_list:
                for num in numer:
                    if num==x_line_number_2:
                        draw_balance_extended_down_lines(ax, center_x, center_y, square_side, up_extension_length, down_extension_length, x_line_number_2,color='purple')
                    if num==x_line_number:
                        draw_balance_extended_up_lines(ax, center_x, center_y, square_side, up_extension_length, down_extension_length, x_line_number,color='purple')
            x_line_number+=1
            x_line_number_2+=1
            if (x_line_number-initial_x_line_number)%9==0:
                x_line_number+=columns-1
                x_line_number_2+=columns-1
            for numer in numer_list:
                for num in numer:
                    if num==y_line_number:
                        draw_straight_left_lines(ax, center_x, center_y, square_side,left_extension_length, right_extension_length, y_line_number,color='purple')
                    if num==y_line_number_even:
                        draw_straight_right_lines(ax, center_x, center_y, square_side,left_extension_length, right_extension_length, y_line_number_even,color='purple')   
            y_line_number+=2
            y_line_number_even+=2 
for col in range(side_rectangle_no):
    outer_counting+=1
    for numer in numer_list:
        for num in numer:
            if num==outer_counting-1:
                connect_outer_rectangles_bottom(ax, side_rectangle_no, circle_spacing, square_spacing, bottom_spacing, square_side, outer_counting-1)
for row in range(side_rectangle_number):
    outer_counting+=1
    for numer in numer_list:
        for num in numer:
            if num==outer_counting-1:
                connect_outer_rectangles_right(ax, side_rectangle_no, outer_counting-1, circle_spacing, square_spacing, bottom_spacing, square_side)
for col in range(side_rectangle_no):
    top_number-=1
    for numer in numer_list:
        for num in numer:
            if num==top_number:
                connect_outer_rectangles_top(ax, side_rectangle_no, top_number, circle_spacing, square_spacing, bottom_spacing, square_side, rows, columns, circle_radius)
for row in range(side_rectangle_number):
    right_number-=1
    for numer in numer_list:
        for num in numer:
            if num==right_number+1:
                connect_outer_rectangles_left(ax, side_rectangle_number,right_number+1, circle_spacing, square_spacing, bottom_spacing, square_side, rows, columns, circle_radius)   
# 添加外圍正方形
add_outer_rectangles(ax, side_rectangle_no, circle_spacing, square_spacing, bottom_spacing, square_side, outer_number, outer_number_2, outer_number_3, outer_number_4)
# 设置座標範圍
ax.set_xlim(-circle_radius*2, columns * (circle_spacing + square_spacing) - circle_radius+3)
ax.set_ylim(-circle_radius*2, rows * (circle_spacing + square_spacing) - circle_radius+3)
# 坐標軸設定
ax.axis('off')
# 圖形顯示
plt.show()