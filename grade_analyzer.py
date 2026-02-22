def process_scores(students):
    averages = {}
    for name, scores in students.items():
        # Calculate average and round to 2 decimal places
        avg = sum(scores) / len(scores)
        averages[name] = round(avg, 2)
    return averages

def classify_grades(averages):

    A_LIMIT = 90
    B_LIMIT = 75
    C_LIMIT = 60
    
    classified = {}
    for name, avg in averages.items():
        if avg >= A_LIMIT:
            grade = 'A'
        elif avg >= B_LIMIT:
            grade = 'B'
        elif avg >= C_LIMIT:
            grade = 'C'
        else:
            grade = 'F'
        classified[name] = (avg, grade)
    return classified

def generate_report(classified, passing_avg=70):
    print(f"{'='*5} Student Grade Report {'='*5}")
    passed_count = 0
    total_students = len(classified)
    
    for name, (avg, grade) in classified.items():
        # Determine pass/fail status
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed_count += 1
        print(f"{name:<10} | Avg: {avg:<5.2f} | Grade: {grade} | Status: {status}")
        
    print("=" * 32)
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {total_students - passed_count}")
    
    return passed_count

# Main Block
if __name__ == "__main__":
    student_data = {
        "Alice": [85, 90, 82, 88],
        "Bob": [60, 65, 58, 67],
        "Clara": [95, 98, 92, 100]
    }
    averages_dict = process_scores(student_data)
    classified_dict = classify_grades(averages_dict)
    total_passed = generate_report(classified_dict, passing_avg=70)