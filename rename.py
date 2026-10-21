import os

def rename_reports():
    target_dir = r"D:\Automation_Tester_report"
    
    rename_map = {
        "1.docx": "srs_requirement_analysis.docx",
        "Feature.docx": "feature_requirements.docx",
        "Report 2.docx": "test_plan_and_strategy.docx",
        "report 3.docx": "test_scenario_mapping.docx",
        "report 4.docx": "test_cases_authentication.docx",
        "Report 5.docx": "test_cases_user_profile.docx",
        "Report 6.docx": "test_data_preparation.docx",
        "Em gửi Report ngày 14.docx": "cucumber_bdd_feature_writing.docx",
        "Report 15.docx": "manual_test_execution_phase1.docx",
        "Report 16.docx": "bug_reporting_and_tracking.docx",
        "Report 19.docx": "interim_testing_progress_report.docx",
        "report 20.docx": "boundary_value_analysis_tests.docx",
        "Report 21.docx": "playwright_framework_setup.docx",
        "Report 22.docx": "playwright_locator_strategies.docx",
        "report 23.docx": "automation_script_login_flow.docx",
        "Report 26.docx": "playwright_auto_wait_handling.docx",
        "Report 27.docx": "storage_state_session_handling.docx",
        "Report 28.docx": "regression_testing_execution.docx",
        "Report 29.docx": "playwright_trace_viewer_debugging.docx",
        "Report for 30.docx": "final_test_summary_report.docx"
    }

    if not os.path.exists(target_dir):
        print(f"Không tìm thấy thư mục: {target_dir}")
        return

    files_in_dir = os.listdir(target_dir)
    success_count = 0
    
    for old_name, new_name in rename_map.items():
        matched_files = [f for f in files_in_dir if f.lower() == old_name.lower()]
        if matched_files:
            old_path = os.path.join(target_dir, matched_files[0])
            new_path = os.path.join(target_dir, new_name)
            try:
                os.rename(old_path, new_path)
                print(f"Thành công: {matched_files[0]} -> {new_name}")
                success_count += 1
            except Exception as e:
                print(f"Lỗi file {matched_files[0]}: {e}")
                
    print(f"\nXong! Đã đổi tên thành công {success_count}/{len(rename_map)} file.")

if __name__ == "__main__":
    rename_reports()