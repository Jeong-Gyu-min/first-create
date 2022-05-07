import pickle
profile_file = open("profile.pickle", "wb") # 피클은 꼭 바이너리(b)를 정의해줘야 된다
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()
