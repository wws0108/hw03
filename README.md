人脸识别 Demo
项目结构
hw03/
├─ app.py               # 主程序代码：基于 face_recognition 实现人脸检测，基于 Streamlit 提供网页交互界面
├─ requirements.txt     # 依赖清单：记录项目所需的 Python 库及版本
└─ README.md            # 项目说明文档：介绍功能、运行方式等
功能说明
核心功能
本项目实现人脸检测功能，流程如下：
用户通过网页上传 JPG/PNG 格式的图片
后端调用 face_recognition 库的 face_locations() 方法，检测图片中所有人脸的位置
统计人脸数量，并在网页中展示结果和原图
技术栈
人脸检测：face_recognition 库（基于 dlib 实现，封装了高效的人脸检测与特征提取算法）
Web 界面：Streamlit 框架（快速构建数据可视化与交互式网页应用）
图像处理：Pillow + numpy（用于图片加载与数组转换）
运行与访问方式
1. 环境准备
确保已安装 Python 3.9 环境
安装依赖库：
pip install -r requirements.txt
若使用 Windows 环境，推荐先安装 dlib-bin 预编译版本，避免编译 dlib 源码
2. 启动服务
在终端中执行以下命令：
streamlit run app.py
3. 访问应用
服务启动后，浏览器会自动打开本地页面，地址为：
http://localhost:8501
若未自动弹出，可手动复制该地址到浏览器访问。