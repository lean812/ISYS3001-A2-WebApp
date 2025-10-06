# 导入Flask框架及必要模块
from flask import Flask, render_template, request, redirect, url_for

# 初始化Flask应用（__name__表示当前文件为应用入口）
app = Flask(__name__)

# 模拟数据库：用列表存储任务（实际项目可替换为SQLite/MySQL，此处简化）
tasks = []

# 1. 首页路由：显示所有任务（GET请求）
@app.route('/')
def index():
    # 渲染templates文件夹下的index.html，并传递tasks列表到前端
    return render_template('index.html', tasks=tasks)

# 2. 添加任务路由：处理前端提交的任务（POST请求）
@app.route('/add-task', methods=['POST'])
def add_task():
    # 从前端表单获取“task”字段的值（对应index.html中的<input name="task">）
    task_content = request.form.get('task')
    # 若任务内容不为空，添加到tasks列表
    if task_content.strip():  # strip()去除空格，避免空任务
        tasks.append(task_content)
    # 重定向回首页，刷新任务列表
    return redirect(url_for('index'))

# 3. 删除任务路由：根据任务索引删除（GET请求）
@app.route('/delete-task/<int:task_index>')
def delete_task(task_index):
    # 验证索引有效性（避免越界错误）
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)  # 删除指定索引的任务
    # 重定向回首页
    return redirect(url_for('index'))

# 启动应用（仅在本地运行时生效，生产环境需关闭debug）
if __name__ == '__main__':
    app.run(debug=True)  # debug=True：代码修改后自动重启应用，便于开发