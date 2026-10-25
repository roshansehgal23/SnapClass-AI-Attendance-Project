
import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
from datetime import datetime
import pandas as pd
from src.components.dialog_attendance_results import show_attendance_result


@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):

    st.write(
        "Record audio of students saying 'I am present'. "
        "Then AI will recognize the students."
    )

    audio_data = st.audio_input("Record Classroom Audio")

    if st.button(
        "Analyze Audio",
        width="stretch",
        type="primary"
    ):

        # Check audio before starting processing
        if audio_data is None:
            st.warning("Please record the classroom audio first.")
            return

        with st.spinner("Processing Audio Data..."):

            try:
                # Fetch enrolled students
                enrolled_res = (
                    supabase.table("subject_students")
                    .select("*, students(*)")
                    .eq("subject_id", selected_subject_id)
                    .execute()
                )

                enrolled_students = enrolled_res.data or []

                if not enrolled_students:
                    st.warning("No students enrolled in this course.")
                    return

                # Prepare voice profiles with integer student IDs
                candidates_dict = {
                    int(node["students"]["student_id"]):
                    node["students"]["voice_embedding"]
                    for node in enrolled_students
                    if node.get("students")
                    and node["students"].get("student_id") is not None
                    and node["students"].get("voice_embedding") is not None
                }

                if not candidates_dict:
                    st.error(
                        "No enrolled students have voice profiles registered."
                    )
                    return

                # Read recorded audio
                audio_bytes = audio_data.getvalue()

                if not audio_bytes:
                    st.warning("The recorded audio is empty. Please record again.")
                    return

                # Identify speakers
                detected_scores = process_bulk_audio(
                    audio_bytes,
                    candidates_dict
                )

                results = []
                attendance_to_log = []

                current_timestamp = datetime.now().strftime(
                    "%Y-%m-%dT%H:%M:%S"
                )

                # Prepare attendance results
                for node in enrolled_students:

                    student = node.get("students")

                    if not student:
                        continue

                    student_id = int(student["student_id"])
                    score = detected_scores.get(student_id, 0.0)

                    is_present = score > 0

                    results.append({
                        "Name": student["name"],
                        "ID": student_id,
                        "Source": round(score, 4) if is_present else "_",
                        "Status": "✅ Present" if is_present else "❌ Absent"
                    })

                    attendance_to_log.append({
                        "student_id": student_id,
                        "subject_id": selected_subject_id,
                        "timestamp": current_timestamp,
                        "is_present": bool(is_present)
                    })

                if not results:
                    st.warning("No valid student records were found.")
                    return

                # Save results for display
                st.session_state.voice_attendance_results = (
                    pd.DataFrame(results),
                    attendance_to_log
                )

            except Exception as e:
                st.error(
                    f"Voice attendance error: {type(e).__name__}: {e}"
                )
                st.exception(e)
                return

    # Display attendance results
    if st.session_state.get("voice_attendance_results"):
        st.divider()

        df_results, logs = st.session_state.voice_attendance_results

        show_attendance_result(df_results, logs)
