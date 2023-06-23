import sys
import pandas as pd
import dill
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass



    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)





class CustomData:

    def __init__(self,
    make_model: str,
    body_type: str,
    Type: str,
    Upholstery: str,
    Fuel: str,
    Body_Color: str,
    Gearing_Type: str,
    km: float,
    hp: float,
    Displacement: float,
    Comfort_Convenience: float,
    Extras: float,
    Safety_Security: float,
    First_Registration: float,
    door_numbers: float,
    seat_numbers: float,
    consumption_comb: float,
    consumption_city: float,
    co2_emission: float):

   
     self.make_model=make_model

     self.body_type=body_type

     self.Type=Type

     self.Upholstery=Upholstery

     self.Fuel=Fuel

     self.Body_Color=Body_Color

     self.Gearing_Type=Gearing_Type

     self.km=km
     self.hp=hp
     self.Displacement=Displacement
     self.Comfort_Convenience=Comfort_Convenience
     self.Extras=Extras
     self.Safety_Security=Safety_Security
     self.First_Registration=First_Registration

     self.door_numbers=door_numbers
     self.seat_numbers=seat_numbers
     self.consumption_comb=consumption_comb
     self.consumption_city=consumption_city
     self.co2_emission=co2_emission



    def get_data_as_data_frame(self):
        try:

            Custom_data_input_dict = {
            'km': [self.km],
            'hp': [self.hp],
            'Displacement': [self.Displacement],
            'Comfort_Convenience': [self.Comfort_Convenience],
            'Extras': [self.Extras],
            'Safety_Security': [self.Safety_Security], 
            'First_Registration': [self.First_Registration],
            'door_numbers': [self.door_numbers],
            'seat_numbers': [self.seat_numbers],
            'consumption_comb': [self.consumption_comb],
            'consumption_city': [self.consumption_city],
            'co2_emission': [self.co2_emission],
            'make_model': [self.make_model], 
            'body_type': [self.body_type],
            'Type': [self.Type],
            'Upholstery': [self.Upholstery],
            'Fuel': [self.Fuel],
            'Body_Color': [self.Body_Color],
            'Gearing_Type': [self.Gearing_Type]
        }
         #numerical_columns=['price','km','hp','Displacement','Comfort_Convenience','Extras','Safety_Security',
           # 'First_Registration','door_numbers','seat_numbers','consumption_comb','consumption_city','co2_emission'],
    #categorical_columns=['make_model','body_type','Type','Upholstery','Fuel','Body_Color','Gearing_Type'],


            return pd.DataFrame(Custom_data_input_dict)
   
        except Exception as e:
            raise CustomException(e,sys)
   

   