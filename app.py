from flask import Flask, render_template, request, send_file
from PIL import Image
import os
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    files = request.files.getlist('images')

    if not files:
        return "파일이 업로드되지 않았습니다.", 400

    image_list = []
    for file in files:
        img = Image.open(file.stream).convert('RGB')
        image_list.append(img)

    if not image_list:
        return "이미지 변환 실패", 400

    # 첫 이미지만 따로 저장, 나머지는 append_pages로 추가
    pdf_io = io.BytesIO()
    image_list[0].save(pdf_io, format='PDF', save_all=True, append_images=image_list[1:])
    pdf_io.seek(0)

    return send_file(
        pdf_io,
        as_attachment=True,
        download_name="converted.pdf",
        mimetype='application/pdf'
    )

if __name__ == '__main__':
    app.run(debug=True)
