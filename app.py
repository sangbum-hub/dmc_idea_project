# app.py
# flask 사용을 위한 임포트 부분
from flask import Flask, render_template, request, url_for
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# 플래스크 실행 /static 폴더에서 이미지, CSS 파일 등 을 관리
app = Flask(__name__, static_url_path='/static')
# 아래의 @app.route() annotation을 통하여 “/”, “/calculate” 2개의 URL에 대한 웹 페이지를 생성하며
# 각 함수에서는 랜더링할 html 페이지를 return render_template 함수를 통하여 지정한다.

# URL ‘/’일 때 houseinfo.html 파일을 이용하여 웹 화면을 랜더링 한다.
@app.route('/')
def main_get():
    return render_template('houseInfo.html')

# URL ‘/calculate’일 때 비즈니스 로직 처리 후 result.html 파일을 이용하여 웹 화면을 랜더링 한다.
@app.route('/calculate')
def calculate(num=None):
    style_ranch = 0
    style_vitorian = 0
# request 파라미터로 area를 가져온다.
    area = request.args.get('area')
    area = int(area)
    bedrooms = request.args.get('bedrooms')
    bedrooms = int(bedrooms)
# request 파라미터로 neighborhood를 가져온다.
    neighborhood = request.args.get('neighborhood')
    if neighborhood == 'B':
        neighborhood = 1
    else:
        pass
# request 파라미터로 style를 가져온다.
    style = request.args.get('style')
    if style == 'ranch':
        style_ranch = 1
    elif style == 'victorian':
        style_vitorian = 1
    else:
        pass
    data = np.array([[area, bedrooms, neighborhood, style_ranch, style_vitorian]])
    model = joblib.load('lr_model.pkl')
    pred_data = model.predict(data)
    print(pred_data)
    return render_template('result.html', template_name=format(pred_data[0], ','))
if __name__ == '__main__':
  app.run(debug=True, threaded=True)