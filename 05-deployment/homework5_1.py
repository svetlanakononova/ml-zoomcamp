import pickle
import sklearn

model_file_name = "pipeline_v1.bin"

test_record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

if __name__ == '__main__':
    with open(model_file_name, 'rb') as f_in: # very important to use 'rb' here, it means read-binary 
        pipeline = pickle.load(f_in)
    result = pipeline.predict_proba(test_record)[0, 1]
    print (result)



