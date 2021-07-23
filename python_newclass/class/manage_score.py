import json
import pickle as pi

from tensorboard import data

from python_newclass.dictionary import json_data


def jsonSave(student):
    with open("../json1.json", "w", encoding="utf-8") as file:
        json.dump(student, file, ensure_ascii=False)
    print("json저장")


def jsonLoad(jsonfilename):
    with open("../json1.json", "r", encoding="utf-8") as file:
        jsonfilename = json.load(file)
    print(json.dumps(jsonfilename, ensure_ascii=False))
    return jsonfilename


def save(student):
    with open("../data.pkl", "wb") as file:
        pi.dump(student, file) # 인코더
        print("파일이 정상적으로 저장 되었습니다.")


# 1번 전화번호 출력 2. 칸마다 자르기 3.  자른공간에 '-'넣기
def insert(student):
    name = input("이름 입력: ")
    if (name not in student) == True:
       address = input("주소를 입력하세요 : ")
       age = int(input("나이를 입력하세요 : "))
       phone = input("휴대번호를 입력하세요 : ")
       print(phone.__sizeof__())
       if(phone.__sizeof__())  == 49:
           phone = input("휴대번호를 반드시 입력해주세요 : ")
       elif (49 < phone.__sizeof__() < 60 or phone.__sizeof__() >= 61):
           print("잘못된 번호형식입니다.")
           phone = input("다시 입력해주세요 : ")
       elif(phone.__sizeof__()) == 60:
           print("정보가 등록되었습니다.")
    else:
        print("학생이 존재합니다.")
        return insert(student)

    student[name] = [address, age, phone]
    person = student[name]

    return student

    # pass


def search(student):
    search_name = input("검색할 친구의 이름을 입력해주세요. ")

    if(search_name in student) == True:
        print("해당 이름이 없습니다.")
        VieHeadLine()

        print('|', f'{search_name:^8}', end='|')

        for data in student.get(search_name):
            print(f'{data:^15}', end='|')
        print()
        ViewFootLine()
    else:
        print("해당 이름이 없습니다.")
        return search(student)

    return student


    # pass


def VieHeadLine():
    print("============================")
    print('|   이름     |     주소        |나이            | ')


def ViewFootLine():
    print("============================")


def view(student):
    print("========================================================")
    print('|   이름     |     주소        |    나이        |     휴대폰 번호 |')
    for key, value in student.items():
        print("|", f'{key:^7}', '|', end='')
        # 번호 먼저 추가해주고
        dataformat = "{}-{}-{}".format(value[2][0:3], value[2][3:7], value[2][7:11])
        value.append(dataformat)
        # 기존 리스트 삭제
        del value[2]
        
        for data in value:
            print(f'{data:^15}', end='|')
        print()

    print("=========================================================")
    # pass


def update(student):
    update_name = input("수정할 친구의 이름을 입력해주세요.")
    if(update_name in student) == True:
        address = input("수정 할 주소를 입력하세요 : ")
        age = int(input("수정 할 나이를 입력하세요 : "))

        student[update_name] = [address, age]
        person = student[update_name]

    else:
        print("해당 이름이 없습니다. ")
        return update(student)
    # pass

    view(student)


def delete(student):
    delete_name = input("삭제할 학생의 이름을 입력하세요. ")
    if(delete_name in student) == True:

        student.pop(delete_name)
        print("{}님이 삭제되었습니다. ".format(delete_name))
        return student
        # pass


def loadData():
    import os.path
    isFile = os.path.isfile('../data.pkl')
    if isFile == False:
        with open("../data.pkl", "wb") as file:
            print("파일을 생성 했습니다. ")
    else:
        with open("../data.pkl", "rb+") as file:
            student = pi.load(file)
    return student


def menumain():
    print()
    print("1. 등록 2. 목록 3. 수정 4. 삭제 5. 검색 6. 저장 7.json으로저장 8. json으로 로드  9. 종료")
    print()
    print()
    print()
    print()
    print()


def main():
    menumain()
    student = loadData()  # 디코더
    # student = dict({'김상건': ['달서구', 30]})
    while True:
        select = int(input("1. 등록 2. 목록 3. 수정 4. 삭제 5. 검색 6. 저장 7. Json으로 저장 8. json으로 로드  9. 종료 \n"))
        if select == 1:
            student == insert(student)
            view(student)
            print(student)
        elif select == 2:
            student == view(student)
        elif select == 3:
            student == update(student)
        elif select == 4:
            view(student)
            student == delete(student)
        elif select == 5:
            student == search(student)
        elif select == 6:
            student == save(student)
            break
        elif select == 7:
            student == jsonSave(student)
        elif select == 8:
            student == jsonLoad(json_data)
        else:
            break


if __name__ == "__main__":
    main()