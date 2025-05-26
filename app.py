from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import PredictionPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET'])
def show_form():
    return render_template('predict.html')

@app.route('/result', methods=['POST'])
def predict_result():
    data = CustomData(
        carat=float(request.form.get('carat')),
        depth=float(request.form.get('depth')),
        table=float(request.form.get('table')),
        x=float(request.form.get('x')),
        y=float(request.form.get('y')),
        z=float(request.form.get('z')),
        cut=request.form.get('cut'),
        color=request.form.get('color'),
        clarity=request.form.get('clarity')
    )

    final_new_data = data.get_data_as_dataframe()
    prediction_pipeline = PredictionPipeline()
    pred = prediction_pipeline.predict(final_new_data)
    result = round(pred[0], 2)

    return render_template('result.html', final_result=result)

if __name__ == "__main__":
    print("Server running at: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)