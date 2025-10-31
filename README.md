# Electronic Health Records
-------------------------------------

The **Electronic Health Records (EHR)** system is an intuitive, web-based digital solution designed to transform patient care within healthcare facilities.  
By providing a seamless platform for healthcare providers to efficiently track patient records, schedule appointments, and manage treatment plans,  
the system aims to streamline healthcare processes and improve the overall quality of patient care.

This project follows the **Client-Server Design pattern**, implementing both patient and doctor functionalities in a secure and user-friendly interface.

---

## 🏗️ Architecture
The architecture diagram for the app is shown below:

![Architecture Diagram](images/architecture_diagram.png)

---

## ⚙️ Functional Requirements

1. **Doctor:** View the list of patients scheduled for the day to prepare for consultations.  
   ![View Patients](images/case1_6.png)

2. **Doctor:** View a patient's medical records before the consultation to provide the best care possible.  
   ![View Medical Records](images/case2.png)

3. **Doctor:** Upload prescriptions electronically so patients can access them easily.  
   ![Upload Prescriptions](images/case3_4.png)

4. **Doctor:** Create and modify treatment plans for patients to provide structured recovery plans.  
   ![Modify Treatment Plans](images/case3_4.png)

5. **Doctor:** Set available hours and days so that patients can book appointments accordingly.  
   ![Available Hours](images/case5.png)

6. **Doctor:** Accept or reject appointment requests from patients and conduct consultations.  
   ![Accept Appointments](images/case1_6.png)

7. **Patient:** Book an appointment with a doctor to discuss health concerns.  
   ![Patient Dashboard](images/case_patient.png)  
   ![Book Appointment](images/case7_1.png)  
   ![Book Appointment](images/case7_2.png)  
   ![Book Appointment](images/case7_3.png)

8. **Patient:** Cancel an appointment if unable to attend, freeing up the slot for others.  
   ![Cancel Appointment](images/case8_1.png)

9. **Patient:** View and download prescriptions to acquire medications.  
   ![View Prescriptions](images/case9.png)

10. **Patient:** Update health status and information for doctor review.  
    ![Update Health Status](images/case10_1.png)  
    ![Update Health Status](images/case10_2.png)  
    ![Update Health Status](images/case10_3.png)

11. **User:** Sign up as a doctor or patient.  
    ![Sign Up](images/case11_1.png)  
    ![Sign Up](images/case11_2.png)  
    ![Sign Up](images/case11_3.png)

12. **User:** Log in to the website as a doctor or patient.  
    ![Log In](images/case12.png)

---

## 🚀 Getting Started

### 🧩 Installation

Create a Conda environment:
```bash
conda create --name project520 python=3.9 -y
```

Activate the Conda environment:
```bash
conda activate project520
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

Start the web app:
```bash
python server.py
```

---

## 🧪 Test Coverage

Run tests with coverage:
```bash
coverage run -m pytest test_server.py
```

Generate a coverage report:
```bash
coverage report -m
```

Or view it in HTML format (preferred):
```bash
coverage html
```

Coverage report can be found at:
```
htmlcov/index.html
```

---

## 🛠️ Technologies Used
- **Python**
- **Flask**
- **REST API**
- **SQLite3**
- **HTML**
- **CSS**
- **Jinja**
- **Pytest**

---

## 👥 Collaborators
<body>
<table>
  <tr>
    <td>
      <a href="https://github.com/eshag06">
        <img src="https://github.com/eshag06.png" alt="eshag06" width="100px" height="100px"/><br/>eshag06
      </a>
    </td>
    <td>
      <a href="https://github.com/IlMinCho">
        <img src="https://github.com/IlMinCho.png" alt="IlMinCho" width="100px" height="100px"/><br/>IlMinCho
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/kunalkumar168">
        <img src="https://github.com/kunalkumar168.png" alt="kunalkumar168" width="100px" height="100px"/><br/>kunalkumar168
      </a>
    </td>
    <td>
      <a href="https://github.com/Msushi">
        <img src="https://github.com/Msushi.png" alt="Msushi" width="100px" height="100px"/><br/>Msushi
      </a>
    </td>
  </tr>
</table>
</body>

---

## 🎥 Video Presentation
<a href="https://youtu.be/0jL7RjzliDg">
  <img src="https://i.imgur.com/y5MqjBJ.png" position="relative" height="150px"/>
</a>

---

### 📄 License
This project is developed for educational purposes and can be extended for research or institutional use.

---
