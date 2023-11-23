import matplotlib.pyplot as plt

# 設置行列
rows = 10
columns = 10

# 創建一個圖形
fig, ax = plt.subplots()

# 加入參數
circle_radius = 0.3
square_side = 0.4  # 正方形的边长
circle_spacing = 1.5  # 两个圆之间的距离
square_spacing = 0.5  # 调整正方形和两个圆之间的距离
number_spacing=1.07
number_spacing_2=1
ji=0.1

# 設置編號
count = 1
horizontal_count = 1  # 用于横轴正方形的计数器
vertical_count = 6 * (columns - 1) + 1
c=0
k=1
l=0
m=0
n=0
O=-1
p=2*(rows-1)
q=columns-1
r=rows-1
s=2*(columns-1)
x_line_number=2*(columns-1)*(rows-1)*2+1
y_line_number=x_line_number+(rows-1)*2*(columns-1)
outer_counting=y_line_number+(columns-1)*2*(rows-1)
COUT=1
right_down_number=2
left_up_number=19
side_rectangle_no=2*(columns - 1)+1
side_rectangle_number=2*(rows - 1)+1
bottom_spacing=1
#可以調整標號間距
vertical_label_spacing = 0.1  # 可以根據需要調整垂直間距
outer_number=1
outer_number_2=2*columns
outer_number_3=outer_number_2+(2*rows-1)
outer_number_4=outer_number_3+(2*columns-2)


# Define line extension lengths for each direction
up_extension_length = 0.5  # Adjust this value for lines going upwards
down_extension_length = 0.5  # Adjust this value for lines going downwards
left_extension_length = 0.5  # Adjust this value for lines going to the left
right_extension_length = 0.5  # Adjust this value for lines going to the right

for i in range(p):
     for col in range(q):
            if(i==p%2):
                #左下部分標號
                x = col * (circle_spacing+square_spacing)+1
                y = i * number_spacing+0.1+1
                left_down_line_x=x + (circle_spacing + square_spacing) /4
                left_down_line_y = y
                ax.text(left_down_line_x,left_down_line_y,COUT,va='center',ha='center')
                COUT+=2
                #右下部分標號
                x = col * (circle_spacing+square_spacing)+1
                y = i * number_spacing+0.1+1
                right_down_line_x=x + (circle_spacing + square_spacing) /2+square_spacing
                right_down_line_y=y
                ax.text(right_down_line_x,right_down_line_y,right_down_number,va='center',ha='center')
                right_down_number+=2
            else:
                #左下部分標號
                x = col * (circle_spacing+square_spacing)+1
                y = i * number_spacing+0.1+1
                left_down_line_x=x + (circle_spacing + square_spacing) /4
                left_down_line_y = y+(square_spacing)/4
                ax.text(left_down_line_x,left_down_line_y,COUT,va='center',ha='center')
                COUT+=2
                #右下部分標號
                x = col * (circle_spacing+square_spacing)+1
                y = i * number_spacing+0.1+1
                right_down_line_x=x + (circle_spacing + square_spacing) /2+square_spacing
                right_down_line_y=y+square_spacing/4
                ax.text(right_down_line_x,right_down_line_y,right_down_number,va='center',ha='center')
                right_down_number+=2
for y_line in range(p):
     for x_line in range(q):
            #直線部分編號
            if y_line==p%2:
                length=x_line*(circle_spacing+square_spacing)+1+0.1+1
                height=y_line *number_spacing+0.5+1
                height_interval=height
                ax.text(length,height_interval,x_line_number,va='center',ha='center')
                x_line_number+=1
            else:
                length=x_line*(circle_spacing+square_spacing)+1+0.1+1
                height=y_line *number_spacing+0.2+1
                height_interval=height
                ax.text(length,height_interval,x_line_number,va='center',ha='center')
                x_line_number+=1 
for Y_line in range(r):
     for X_line in range(s):
            #橫線部分編號
            if X_line==s%2:
                len=X_line*(number_spacing_2)+0.4+1
                hei=Y_line *(number_spacing)*1.8+1.4+1
                len_interval=len
                ax.text(len_interval,hei,y_line_number,va='center',ha='center')
                y_line_number+=1
            else:
                len=X_line*(number_spacing_2)+0.4+1
                hei=Y_line *(number_spacing)*1.8+1.4+1
                len_interval=len
                ax.text(len_interval,hei,y_line_number,va='center',ha='center')
                y_line_number+=1 
#底部編號
for outerline_bottom in range(2*columns-1):
     outerline_bottom_number=outer_counting+outerline_bottom
     lenth=outerline_bottom*(number_spacing/1.1)+1.1
     heith=number_spacing_2-0.5
     ax.text(lenth,heith,outerline_bottom_number,va='center',ha='center')
#右側編號
for outerline_right in range(2*rows-1):
     outerline_right_number=outer_counting+outerline_right+2*columns-1
     lenth=(circle_spacing+2*circle_radius)*(columns)
     heith=outerline_right*(number_spacing)+0.8
     ax.text(lenth,heith,outerline_right_number,va='center',ha='center')
#頂部編號
for outerline_top in range(2*columns-1):
     outerline_top_number=outer_counting+2*columns-1+2*rows-1+2*columns-1-outerline_top-1
     if outerline_top<=(2*columns-1)/2:
        lenth=outerline_top*(number_spacing/1.02)+0.7
        heith=(circle_spacing+2*circle_radius)*(rows)-0.3
        ax.text(lenth,heith,outerline_top_number,va='center',ha='center')
     else:
        lenth=outerline_top*(number_spacing/1.06)+0.8
        heith=(circle_spacing+2*circle_radius)*(rows)-0.3
        ax.text(lenth,heith,outerline_top_number,va='center',ha='center')
#左側編號
for outerline_right in range(2*rows-1):
     outerline_left_number=outer_counting+2*columns-1+2*rows-1+2*columns-1+2*rows-1-outerline_right-1
     lenth=square_spacing-0.5
     heith=outerline_right*(number_spacing)+0.8
     ax.text(lenth,heith,outerline_left_number,va='center',ha='center')
for row in range(rows):
    for col in range(columns):
        # 計算圓心座標
        x = col * (circle_spacing + square_spacing) +1 # 根据列数和间距计算 x 坐标
        y = row * (circle_spacing + square_spacing) +1 # 根据行数和间距计算 y 坐标
        ax.add_patch(plt.Circle((x, y), circle_radius, color='red', fill=False))

        # 計算正方形座標，以调整正方形和两个圆之间的距离
        if row != 0:
            square_x = x  # 保持在圆心的位置
            square_y = y - (square_side / 2 + circle_radius + square_spacing)  # 调整距离
            ax.add_patch(plt.Rectangle((square_x - square_side / 2, square_y - square_side / 2), square_side, square_side, color='gray', fill=False))
            ax.text(square_x, square_y, str(vertical_count), va='center', ha='center', color='red', fontsize=10)
            vertical_count += 1

        # 添加橫軸方向的正方形
        if col != columns - 1:
            square_x_horizontal = x + (square_side / 2 + circle_radius + square_spacing)  # 在圆的右侧添加横向正方形
            square_y_horizontal = y  # 保持在相同的 y 坐标
            ax.add_patch(plt.Rectangle((square_x_horizontal - square_side / 2, square_y_horizontal - square_side / 2), square_side, square_side, color='gray', fill=False))
            ax.text(square_x_horizontal, square_y_horizontal, str(horizontal_count), va='center', ha='center', color='red', fontsize=10)
            horizontal_count += 1

        # 添加編號
        ax.text(x, y, str(count), va='center', ha='center', color='red', fontsize=10)

        # 遞增編號
        count += 1
        if col<columns-1: #針對紫色正方形
            c+=1

        # 如果编號達到，結束
        if count > rows*columns:
            break

        # 在四个正方形中间的位置添加一个额外的正方形并编号
        if row < rows - 1 and col < columns - 1 :
                center_x = x + (circle_spacing + square_spacing) / 2
                center_y = y + (circle_spacing + square_spacing) / 2
                ax.add_patch(plt.Rectangle((center_x - square_side / 2, center_y - square_side / 2), square_side, square_side, color='purple', fill=False))
                ax.text(center_x, center_y, str(c), va='center', ha='center', color='red', fontsize=10)
                #左上正方形
                top_left_gray_x = center_x - 0.5 * square_side - circle_radius - 0.5 * square_spacing
                top_left_gray_y = center_y + 0.5 * square_side + circle_radius + 0.5 * square_spacing
                #右上正方形
                top_right_gray_x = center_x + 0.5 * square_side + circle_radius + 0.5 * square_spacing
                top_right_gray_y = center_y + 0.5 * square_side + circle_radius + 0.5 * square_spacing
                #左下正方形
                bottom_left_gray_x = center_x - 0.5 * square_side - circle_radius - 0.5 * square_spacing
                bottom_left_gray_y = center_y - 0.5 * square_side - circle_radius - 0.5 * square_spacing
                #右下正方形
                bottom_right_gray_x = center_x + 0.5 * square_side + circle_radius + 0.5 * square_spacing
                bottom_right_gray_y = center_y - 0.5 * square_side - circle_radius - 0.5 * square_spacing
                #劃出斜線
                plt.plot([center_x - 0.5 * square_side, top_left_gray_x], [center_y + 0.5 * square_side, top_left_gray_y], color='purple')
                plt.plot([center_x + 0.5 * square_side, top_right_gray_x], [center_y + 0.5 * square_side, top_right_gray_y], color='purple')
                plt.plot([center_x - 0.5 * square_side, bottom_left_gray_x], [center_y - 0.5 * square_side, bottom_left_gray_y], color='purple')
                plt.plot([center_x + 0.5 * square_side, bottom_right_gray_x], [center_y - 0.5 * square_side, bottom_right_gray_y], color='purple')
                 # Upward line
                up_extended_line_x = center_x
                up_extended_line_y = center_y - square_side / 2 - up_extension_length
                plt.plot([center_x, up_extended_line_x], [center_y - square_side / 2, up_extended_line_y], color='purple')
                # Downward line
                down_extended_line_x = center_x
                down_extended_line_y = center_y + square_side / 2 + down_extension_length
                plt.plot([center_x, down_extended_line_x], [center_y + square_side / 2, down_extended_line_y], color='purple')
                # Leftward line
                left_extended_line_x = center_x - square_side / 2 - left_extension_length
                left_extended_line_y = center_y
                plt.plot([center_x - square_side / 2, left_extended_line_x], [center_y, left_extended_line_y], color='purple')
                # Rightward line
                right_extended_line_x = center_x + square_side / 2 + right_extension_length
                right_extended_line_y = center_y
                plt.plot([center_x + square_side / 2, right_extended_line_x], [center_y, right_extended_line_y], color='purple')
# 在第一列的下方增加2*(columns-1)+1个外圍正方形
for col in range(side_rectangle_no):
    square_x_bottom = col * (circle_spacing + square_spacing-bottom_spacing)+1
    square_y_bottom = -square_side / 2
    ax.add_patch(plt.Rectangle((square_x_bottom - square_side / 2, square_y_bottom - square_side / 2), square_side, square_side, color='gray', fill=False))
    ax.text(square_x_bottom, square_y_bottom, str(outer_number), va='center', ha='center', color='red', fontsize=10)
    if outer_number<side_rectangle_no:
         outer_number+=1
for col in range(side_rectangle_no):
    square_x_bottom = col * (circle_spacing + square_spacing-bottom_spacing)+1
    square_y_bottom = (circle_spacing+2*circle_radius)*(rows)-0.3
    ax.add_patch(plt.Rectangle((square_x_bottom - square_side / 2, square_y_bottom - square_side / 2), square_side, square_side, color='gray', fill=False))
    ru=outer_number_3+(side_rectangle_no - col - 1) 
    ax.text(square_x_bottom, square_y_bottom, str(ru), va='center', ha='center', color='red', fontsize=10)
for row in range(side_rectangle_number):
    square_x_bottom = -square_side / 2
    square_y_bottom = row * (circle_spacing + square_spacing-bottom_spacing)+1
    ax.add_patch(plt.Rectangle((square_x_bottom - square_side / 2, square_y_bottom - square_side / 2), square_side, square_side, color='gray', fill=False))
    pu=outer_number_4+side_rectangle_number-row
    ax.text(square_x_bottom, square_y_bottom, str(pu), va='center', ha='center', color='red', fontsize=10)
for row in range(side_rectangle_number):
    square_x_bottom = (circle_spacing+2*circle_radius)*(columns)-0.3
    square_y_bottom = row * (circle_spacing + square_spacing-bottom_spacing)+1
    ax.add_patch(plt.Rectangle((square_x_bottom - square_side / 2, square_y_bottom - square_side / 2), square_side, square_side, color='gray', fill=False))
    ax.text(square_x_bottom, square_y_bottom, str(outer_number_2), va='center', ha='center', color='red', fontsize=10)
    if outer_number_2<outer_number_2+side_rectangle_number :
         outer_number_2+=1
# 連接最外圍每一個正方形到內部第一層圓形和正方形
for col in range(side_rectangle_no):
    bottom_square_x = col * (circle_spacing + square_spacing - bottom_spacing) + 1
    bottom_square_y = -square_side / 7+0.05
    # 連接到內部第一層正方形
    inner_square_x = bottom_square_x
    inner_square_y = bottom_square_y + square_side / 2 + square_spacing

    plt.plot([bottom_square_x, inner_square_x], [bottom_square_y, inner_square_y], color='purple')
for col in range(side_rectangle_no):
    bottom_square_x = col * (circle_spacing + square_spacing - bottom_spacing) + 1
    
    bottom_square_y = (rows-1)*(circle_spacing+square_spacing)+1+circle_radius
   
    # 連接到內部第一層正方形
    inner_square_x = bottom_square_x
    
    inner_square_y = (circle_spacing+2*circle_radius)*(rows)-0.5
    
    plt.plot([bottom_square_x, inner_square_x], [bottom_square_y, inner_square_y], color='purple')
for row in range(side_rectangle_number):
     left_outer_rec_x = -square_side / 7+0.05
     left_outer_rec_y = row * (circle_spacing + square_spacing-bottom_spacing)+1
    # 連接到內部第一層正方形
     outner_square_x1 =  square_side/2+square_spacing
     outner_square_y = left_outer_rec_y
     plt.plot([left_outer_rec_x, outner_square_x1], [left_outer_rec_y, outner_square_y], color='purple')
for row in range(side_rectangle_number):
     left_outer_rec_x = (columns-1)*(circle_spacing+square_spacing)+1+circle_radius
     left_outer_rec_y = row * (circle_spacing + square_spacing-bottom_spacing)+1
    # 連接到內部第一層正方形
     outner_square_x1 = square_side/2+square_side+2*columns*circle_radius+circle_spacing*(columns-1)+0.4
     outner_square_y = left_outer_rec_y
     plt.plot([left_outer_rec_x, outner_square_x1], [left_outer_rec_y, outner_square_y], color='purple')
# 设置座標範圍
ax.set_xlim(-circle_radius*2, columns * (circle_spacing + square_spacing) - circle_radius+3)
ax.set_ylim(-circle_radius*2, rows * (circle_spacing + square_spacing) - circle_radius+3)

# 坐標軸設定
ax.axis('OFF')

# 圖形顯示
plt.show()