from flask import Flask, render_template

# Flask 앱 인스턴스를 생성합니다.
# template_folder 설정을 통해 htmls 폴더 안에 있는 html 파일들을 인식하도록 합니다.
app = Flask(__name__, template_folder='htmls')

@app.route('/')
def index():
    """
    루트 경로('/')로 접속했을 때 
    htmls/index.html 파일을 화면에 출력합니다.
    """
    return render_template('index.html')

if __name__ == '__main__':
    # 서버를 실행합니다. 
    # debug=True 설정은 코드 수정 시 서버가 자동으로 재시작되어 개발하기 편리합니다.
    app.run(debug=True)
