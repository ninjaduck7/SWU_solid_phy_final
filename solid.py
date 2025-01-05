import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
)

# 定义章节和标题的映射
chapters = {
    1: "晶体结构",
    2: "固体的结合",
    3: "晶格振动与晶体的热学性质",
    4: "能带理论",
    5: "晶体中电子在电场和磁场中的运动",
    6: "金属电子论"
}

titles = {
    1: [
        "一些晶格的实例", "晶格的周期性", "晶向,晶面和它们的标志", "倒格子体积",
        "晶体的宏观对称性", "点群", "晶格的对称性", "晶体表面的几何结构",
        "非晶态材料的结构", "准晶态"
    ],
    2: [
        "离子性结合", "共价结合", "金属性结合", "范德瓦尔斯结合", "元素和化合物晶体结合的规律性"
    ],
    3: [
        "简谐近似和简正坐标", "一维单原子链", "一维双原子链 声学波和光学波",
        "三维晶格的振动", "离子晶体的长光学波", "确定晶格振动谱的实验方法",
        "局域振动", "晶格热容的量子理论", "晶格振动模式密度",
        "晶格的状态方程和热膨胀", "晶格的热传导", "非晶固体中的原子振动"
    ],
    4: [
        "布洛赫定理", "一维周期场中电子运动的近自由电子近似",
        "三维周期场中电子运动的近自由电子近似", "赝势",
        "紧束缚近似--原子轨道线性组合法", "晶体能带的对称性",
        "能态密度和费米面", "表面电子态", "无序系统中的电子态"
    ],
    5: [
        "准经典运动", "恒定电场作用下电子的运动", "导体,绝缘体和半导体的能带论解释",
        "在恒定磁场中电子的运动", "回旋共振", "德·哈斯-范·阿尔芬效应"
    ],
    6: [
        "费米统计和电子热容量", "功函数与接触电势"
    ]
}

# 随机选择标题
def get_random_title():
    chapter = random.choice(list(titles.keys()))
    title = random.choice(titles[chapter])
    return chapter, title

# 主窗口类
class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("章节标题测试")
        self.setGeometry(100, 100, 500, 400)

        # 初始化随机标题
        self.correct_chapter, self.random_title = get_random_title()

        # 主布局
        layout = QVBoxLayout()

        # 显示章节列表
        chapters_text = "\n".join([f"{key}: {value}" for key, value in chapters.items()])
        self.chapters_label = QLabel(f"章节列表：\n{chapters_text}", self)
        layout.addWidget(self.chapters_label)

        # 显示随机标题
        self.title_label = QLabel(f"标题：{self.random_title}", self)
        layout.addWidget(self.title_label)

        # 输入框
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("请输入章节编号(1-6)")
        layout.addWidget(self.input_field)

        # 提交按钮
        self.submit_button = QPushButton("提交答案", self)
        self.submit_button.clicked.connect(self.check_answer)
        layout.addWidget(self.submit_button)

        # 下一题按钮
        self.next_button = QPushButton("下一题", self)
        self.next_button.clicked.connect(self.next_title)
        layout.addWidget(self.next_button)

        # 退出按钮
        self.exit_button = QPushButton("退出", self)
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        # 设置中央窗口
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # 检查答案
    def check_answer(self):
        user_input = self.input_field.text()
        try:
            user_answer = int(user_input)
            if user_answer == self.correct_chapter:
                QMessageBox.information(self, "结果", f"正确！标题属于章节 {self.correct_chapter}: {chapters[self.correct_chapter]}。")
            else:
                QMessageBox.warning(self, "结果", f"错误！标题实际属于章节 {self.correct_chapter}: {chapters[self.correct_chapter]}。")
        except ValueError:
            QMessageBox.critical(self, "错误", "输入无效，请输入1-6的数字。")

    # 下一题
    def next_title(self):
        self.correct_chapter, self.random_title = get_random_title()
        self.title_label.setText(f"标题：{self.random_title}")
        self.input_field.clear()

# 主函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QuizApp()
    main_window.show()
    sys.exit(app.exec_())