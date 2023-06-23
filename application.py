from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline2 import CustomData, PredictPipeline

aplication=Flask(__name__)

app=aplication

# Route for a home page

@app.route('/')
def index():
    return render_template('index.html')
    # numerical_columns=['km','hp','Displacement','Comfort_Convenience','Extras','Safety_Security',
        #    'First_Registration','door_numbers','seat_numbers','consumption_comb','consumption_city','co2_emission']
        #    categorical_columns=['make_model','body_type','Type','Upholstery','Fuel','Body_Color','Gearing_Type']


# Define the dictionary containing the options
options = {
    'Gearing_Type': ['Manual', 'Automatic', 'Semi-automatic'],
    'make_model': ['Audi A3', 'Audi A1', 'Opel Insignia', 'Opel Astra', 'Opel Corsa',
    'Renault Clio', 'Renault Espace', 'Renault Duster', 'Audi A2'],
    'body_type': ['Sedans', 'Station wagon', 'Compact', 'Van', 'Other', 'Transporter',
    'Off-Road', 'Coupe', 'Convertible'],
    'Type': ['Used', 'New', 'Pre-registered', "Employee's car", 'Demonstration'],
    'Upholstery': ['Cloth, Black', 'Other', 'Part leather, Black', 'Cloth', 'Cloth, Grey',
    'Cloth, Other', 'Full leather, Black', 'Black', 'Grey', 'Other, Other',
    'Full leather', 'Part leather', 'Part leather, Grey',
    'Full leather, Brown', 'Other, Black', 'Full leather, Other',
    'Full leather, Grey', 'Part leather, Other', 'Part leather, Brown',
    'alcantara, Black', 'Full leather, Beige', 'Velour, Black',
    'Cloth, Brown', 'Velour', 'Other, Grey', 'Cloth, Beige', 'Brown',
    'Cloth, Blue', 'Cloth, White', 'Velour, Grey', 'alcantara, Grey',
    'Cloth, Red', 'Other, Yellow', 'Beige', 'Part leather, Red',
    'Full leather, Blue', 'alcantara, Other', 'Blue', 'Part leather, Beige',
    'White', 'alcantara', 'Part leather, White', 'Other, Brown',
    'Cloth, Orange', 'Full leather, Red', 'Full leather, White'],
    'Fuel': ['BENZINE', 'DIESEL', 'CNG', 'LPG', 'Others', 'Electric'],
    'Body_Color': ['Black', 'Grey', 'White', 'Silver', 'Blue', 'Red', 'Brown', 'Green',
    'Beige', 'Yellow', 'Violet', 'Bronze', 'Orange', 'Gold'],


    
    # Include other options here
}



@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():

    if request.method=='GET':
        return render_template('predictdata.html',options=options)
    else:
        data=CustomData(
            km=float(request.form.get('km')),
            hp=float(request.form.get('hp')),
            Displacement=float(request.form.get('Displacement')),
            Comfort_Convenience=float(request.form.get('Comfort_Convenience')),
            Extras=float(request.form.get('Extras')),
            Safety_Security=float(request.form.get('Safety_Security')),
            First_Registration=float(request.form.get('First_Registration')),
            door_numbers=float(request.form.get('door_numbers')),
            seat_numbers=float(request.form.get('seat_numbers')),
            consumption_comb=float(request.form.get('consumption_comb')),
            consumption_city=float(request.form.get('consumption_city')),
            co2_emission=float(request.form.get('co2_emission')),
            make_model=request.form.get('make_model'),
            body_type=request.form.get('body_type'),
            Type=request.form.get('Type'),
            Upholstery=request.form.get('Upholstery'),
            Fuel=request.form.get('Fuel'),
            Body_Color=request.form.get('Body_Color'),
            Gearing_Type=request.form.get('Gearing_Type'),
            


        )


        


        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print(data)

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        return    render_template('show_price.html', options=options,results=results[0])






# Render the template and pass the options dictionary

#@app.route('/prediction-form')
#def prediction_form():
#    return render_template('prediction_form.html', options=options)




if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)


