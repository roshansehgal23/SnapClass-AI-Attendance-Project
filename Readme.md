# SnapClass AI Attendance System

An AI-powered attendance management system built using Python and Streamlit. SnapClass aims to simplify classroom attendance through face recognition and voice-based student identification, with attendance records managed using Supabase.

## 🚀 Features

- **Face Recognition:** Identify registered students using facial features.
- **Voice Recognition:** Identify registered students from recorded classroom audio.
- **Student Management:** Manage student information and enrollment in subjects.
- **Subject Management:** Create classes or subjects and manage enrolled students.
- **Attendance Tracking:** Record attendance with timestamps.
- **Attendance Results:** View attendance status for students.
- **Cloud Database:** Store and retrieve application data using Supabase.
- **Interactive Interface:** User-friendly web interface built with Streamlit.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend / UI:** Streamlit
- **Database:** Supabase
- **Face Recognition:** dlib, NumPy, scikit-learn
- **Voice Recognition:** Resemblyzer, librosa
- **Image Processing:** face-recognition models and related libraries
- **Data Processing:** NumPy, Pandas

## 📁 Project Structure

```text
SnapClass-AI-Attendance/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── .streamlit/
│   └── secrets.toml
│
└── src/
    ├── components/
    ├── database/
    ├── pipelines/
    ├── screens/
    └── ui/
```

> Note: The `.streamlit/secrets.toml` file is used for local configuration and should not be committed to GitHub.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/roshansehgal23/SnapClass-AI-Attendance-.git
cd SnapClass-AI-Attendance-
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Supabase

Create a Supabase project and configure the required credentials in your local Streamlit secrets file:

`.streamlit/secrets.toml`

Add the configuration keys expected by your application. Never publish real API keys, database passwords, or other credentials in your repository.

### 5. Run the application

```bash
streamlit run app.py
```

The application will start locally, and Streamlit will provide a URL to open it in your browser.

## 🔄 How It Works

1. **Student Registration:** Student information and required recognition data are registered.
2. **Subject Enrollment:** Students are associated with their respective subjects.
3. **Recognition:** The system processes facial input or recorded audio to identify registered students.
4. **Attendance Processing:** The application determines attendance based on the recognition results and configured matching rules.
5. **Database Storage:** Attendance records are saved with student, subject, timestamp, and status information.
6. **Results:** Teachers can review the attendance results through the application interface.

## 🔐 Security

- Keep API keys and database credentials out of source code.
- Store local secrets in `.streamlit/secrets.toml`.
- Use Streamlit Cloud Secrets when deploying the application.
- Do not commit `.env` files, credentials, or private configuration files.

## ☁️ Deployment

The application can be deployed using Streamlit Community Cloud by connecting the GitHub repository, selecting the appropriate branch, and setting `app.py` as the main application file.

Configure the required secrets and verify that all dependencies in `requirements.txt` are compatible with the deployment environment.

## ⚠️ Limitations

Recognition accuracy can depend on audio quality, background noise, lighting, camera quality, and the quality of registered samples. Attendance results should be reviewed when recognition confidence is uncertain.

## 👨‍💻 Author

**Roshan Sehgal**

B.Tech — Information Technology

SnapClass AI Attendance System

---

*This project is developed for educational and academic purposes.*