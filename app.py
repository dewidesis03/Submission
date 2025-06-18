import streamlit as st
import pandas as pd
import pickle

# Load model yang sudah dilatih
@st.cache_data()
def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

# Fungsi untuk melakukan prediksi
def predict(model, input_data):
    X_new = pd.DataFrame(input_data, index=[0])
    y_pred = model.predict(X_new)
    return y_pred[0]

# Fungsi utama dashboard
def main():
    # Judul dashboard
    st.title('Prediksi Dropout Mahasiswa')

    # Deskripsi dan informasi input data
    st.header('Masukkan Data untuk Prediksi')
    st.markdown('Isi kolom-kolom berikut dengan data mahasiswa yang ingin Anda prediksi.')

    # Kolom input untuk masukkan data
    marital_status = st.selectbox('Marital Status', [1, 2, 3, 4, 5, 6])
    application_mode = st.selectbox('Application Mode', [15, 1, 17, 39, 18, 53, 44, 51, 43, 7, 42, 16, 5, 2, 10, 57, 26, 27])
    application_order = st.selectbox('Application Order', [1, 5, 2, 4, 3, 6, 9, 0])
    course = st.selectbox('Course', [9254, 9070, 9773, 8014, 9991, 9500, 9238, 9670, 9853, 9085, 9130, 9556, 9147, 9003, 33, 9119, 171])
    daytime_evening_attendance = st.selectbox('Attendance Time', [0, 1])
    previous_qualification = st.selectbox('Previous Qualification', [1, 19, 42, 39, 10, 3, 40, 2, 4, 12, 43, 15, 6, 9, 38, 5, 14])
    previous_qualification_grade = st.number_input('Previous Qualification Grade', value=160.0)
    mothers_qualification = st.selectbox('Mother\'s Qualification', [1, 2, 3])
    fathers_qualification = st.selectbox('Father\'s Qualification', [3, 4, 5])
    mothers_occupation = st.selectbox('Mother\'s Occupation', [1, 2, 3])
    fathers_occupation = st.selectbox('Father\'s Occupation', [1, 2, 3])
    admission_grade = st.number_input('Admission Grade', value=142.5)
    debtor = st.selectbox('Debtor', [0, 1])
    tuition_fees_up_to_date = st.selectbox('Tuition Fees Up-to-date', [0, 1])
    displaced = st.selectbox('Displaced', [0, 1])
    gender = st.selectbox('Gender', [0, 1])
    scholarship_holder = st.selectbox('Scholarship Holder', [0, 1])
    age_at_enrollment = st.number_input('Age at Enrollment', value=19)
    curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', value=6)
    curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Sem Evaluations', value=6)
    curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved', value=6)
    curricular_units_1st_sem_without_evaluations = st.number_input('Curricular Units 1st Sem Without Evaluations', value=0)
    curricular_units_2nd_sem_credited = st.number_input('Curricular Units 2nd Sem Credited', value=0)
    curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', value=6)
    curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations', value=6)
    curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved', value=6)
    curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular Units 2nd Sem Without Evaluations', value=0)
    gdp = st.number_input('GDP', value=0.79)
    status = st.selectbox('Status', [0, 1])
    ratio_approved_1st_sem = st.number_input('Ratio Approved 1st Sem', value=1.0)
    ratio_approved_2nd_sem = st.number_input('Ratio Approved 2nd Sem', value=1.0)

    # Tombol untuk memulai prediksi
    if st.button('Prediksi'):
        # Load model
        model = load_model('model.pkl')

        # Masukkan data ke dalam dictionary
        input_data = {
            'Marital_status': [marital_status],
            'Application_mode': [application_mode],
            'Application_order': [application_order],
            'Course': [course],
            'Daytime_evening_attendance': [daytime_evening_attendance],
            'Previous_qualification': [previous_qualification],
            'Previous_qualification_grade': [previous_qualification_grade],
            'Mothers_qualification': [mothers_qualification],
            'Fathers_qualification': [fathers_qualification],
            'Mothers_occupation': [mothers_occupation],
            'Fathers_occupation': [fathers_occupation],
            'Admission_grade': [admission_grade],
            'Displaced': [displaced],
            'Debtor': [debtor],
            'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
            'Gender': [gender],
            'Scholarship_holder': [scholarship_holder],
            'Age_at_enrollment': [age_at_enrollment],
            'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
            'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
            'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
            'Curricular_units_1st_sem_without_evaluations': [curricular_units_1st_sem_without_evaluations],
            'Curricular_units_2nd_sem_credited': [curricular_units_2nd_sem_credited],
            'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
            'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
            'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
            'Curricular_units_2nd_sem_without_evaluations': [curricular_units_2nd_sem_without_evaluations],
            'GDP': [gdp],
            'Status': [status],
            'Ratio_approved_1st_sem': [ratio_approved_1st_sem],
            'Ratio_approved_2nd_sem': [ratio_approved_2nd_sem]
        }

        # Lakukan prediksi
        prediction = predict(model, input_data)

        # Tampilkan hasil prediksi
        if prediction == '1':
            st.success('Hasil Prediksi: Tidak dropout')
        else:
            st.warning('Hasil Prediksi: Berpotensi dropout')

# Memanggil fungsi utama untuk menjalankan dashboard
if __name__ == '__main__':
    main()