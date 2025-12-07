def student_profile(**profile):
    for key, value in profile.items():
        print(key, ":", value)
        
student_profile(Name="Bob", Age=30, Hobby="Coding")