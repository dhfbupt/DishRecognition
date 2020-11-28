import os
import shutil


dish_title = ['京酱肉丝', '凉拌土豆丝', '卤蛋', '卤蛋红烧肉', '双椒蒸鱼腩',
              '圆葱炒肝', '土豆炖排骨', '土豆炖鸡肉', '土豆牛腩', '宫保鸡丁',
              '家常豆腐', '尖椒干豆腐', '尖椒炒蛋', '干煸四季豆', '干煸菜花',
              '扒鸡', '打卤面', '木须柿子', '木须肉', '梅菜扣肉', '梅菜扣肉卤蛋',
              '水煮肉片', '水煮鱼', '油麦菜', '炒土豆丝', '炒土豆片', '炒河粉',
              '炒豆芽', '炝甘蓝', '炸鸡腿', '烤地瓜', '烧冬瓜', '烧茄子',
              '烧茄条', '玉米', '番茄牛腩', '白菜干豆腐', '白菜木耳', '白菜炖豆腐',
              '百叶结红烧肉', '米饭', '粉丝娃娃菜', '红烧刀鱼', '红烧狮子头',
              '红烧猪手', '红烧鱼', '肉炒菜花', '花卷', '芹菜豆干', '萝卜牛腩',
              '蒜苔炒肉', '藕片', '蛋炒面', '蛋炒饭', '蛋饺', '西兰花', '西瓜',
              '角瓜炒肉', '角瓜鸡蛋', '辣子鸡丁', '辣白菜炖丸子', '酸菜鱼',
              '青椒肉丝', '青笋炒肉片', '馒头', '香菇油菜', '鱼', '鹌鹑蛋红烧肉',
              '麻婆豆腐', '麻辣香锅', '黄瓜炒鸡蛋', '黄豆芽']

ori_path = 'Dishes/train'

def rename():
    dirs = os.listdir(ori_path)
    dirs = [f for f in dirs if os.path.isdir(os.path.join(ori_path, f))]

    for f in dirs:
        dir_name = os.path.join(ori_path, f)
        sub_count = 1
        sub_dirs = os.listdir(dir_name)
        sub_dirs = [s for s in sub_dirs if
                    os.path.isfile(os.path.join(dir_name, s))]
        for s in sub_dirs:
            file_name = os.path.join(dir_name, s)
            sType = os.path.splitext(file_name)[1]
            new_file_name = os.path.join(dir_name,
                                         str(sub_count).zfill(4) + sType)
            os.rename(file_name, new_file_name)
            sub_count += 1

    count = 1
    for f in dirs:
        dir_name = os.path.join(ori_path, f)
        new_dir_name = os.path.join(ori_path, str(count))
        os.rename(dir_name, new_dir_name)
        count += 1

    print('successfully rename.')


def move_file():
    dirs = os.listdir(ori_path)
    dirs = [d for d in dirs if os.path.isdir(os.path.join(ori_path, d))]

    for d in dirs:
        dpath = os.path.join(ori_path, d)
        new_dir_path = dpath.replace('train', 'test')
        os.mkdir(new_dir_path)

        for o in os.listdir(dpath)[:5]:
            shutil.move(os.path.join(dpath, o), os.path.join(new_dir_path, o))


# rename()
move_file()