# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록
# solution 함수를 완성해주세요.

def solution(numbers):
    #answer는 비어있는 list(배열)
    answer = list()# [= 얘랑 같음 anwser = ()]빈 리스트
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            # numbers[i]는 첫 번째 선택한 숫자
            # numbers[j]는 두 번째 선택한 숫자
            두수의합 = numbers[i] + numbers[j]
            answer.append(두수의합)
    #set(집합) 처리를 하면서 중복제거와 오름차순 정렬을 깔끔하게 해결
    return list(set(answer))

def main():
    numbers = [5, 0, 2, 7]
    print(solution(numbers))

if __name__ == "__main__":
    main()